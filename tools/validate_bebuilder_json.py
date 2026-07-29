#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador de JSON para BeBuilder (BeTheme / Muffin Builder).

Fuente de verdad: builder-elements/_elements.json (volcado del PHP real del theme,
generado por builder-elements/_generator/extract.php). Reglas derivadas de
docs/bebuilder/01..06 y del código de betheme/.

Uso:
    python3 tools/validate_bebuilder_json.py pagina.json
    python3 tools/validate_bebuilder_json.py pagina.json --json
    python3 tools/validate_bebuilder_json.py pagina.json --fix -o pagina.fixed.json
    cat pagina.json | python3 tools/validate_bebuilder_json.py -

Códigos de salida:
    0 = sin errores (ni warnings si se usa --strict)
    1 = errores
    2 = solo warnings, con --strict
    3 = fallo de uso / JSON no parseable / schema no encontrado
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

# --------------------------------------------------------------------------- #
# Constantes derivadas del theme
# --------------------------------------------------------------------------- #

# front.php:37-51 — cualquier otro valor produce warnings PHP + layout roto
SIZES = {
    "1/6", "1/5", "1/4", "1/3", "2/5", "1/2",
    "3/5", "2/3", "3/4", "4/5", "5/6", "1/1",
}
SIZES_WRAP = SIZES | {"divider"}

# class-mfn-helper.php:505-565
DEVICES = ("desktop", "laptop", "tablet", "mobile")
DEVICE_SET = set(DEVICES)

# dimensions con version "separated-fields"
SIDES = {"top", "right", "bottom", "left"}

# 02-css-pipeline.md §5 — estos estilos SOLO emiten la subclave "string"
STRING_ONLY_TYPES = {"gradient", "transform", "css_filters", "backdrop_filter"}

# 02-css-pipeline.md §7 — atributos legacy que vuelcan style="" inline
LEGACY_SECTION = {
    "padding_top", "padding_bottom", "padding_horizontal",
    "bg_color", "bg_image", "bg_position", "bg_size", "custom_css",
}
LEGACY_WRAP = {
    "padding", "bg_color", "bg_image", "bg_position", "bg_size",
    "move_up", "style", "custom_css",
}
LEGACY_ITEM = {
    "custom_css", "align", "margin_bottom", "padding",
    "column_bg", "bg_image", "bg_position", "bg_size",
}

# front.php:2638-2640 — basura de runtime del Visual Builder
RUNTIME_ATTRS = {"vb", "vb_postid", "rwd"}

# 05-reglas-y-trampas.md §1.3 / class-mfn-helper.php:305
TYPOGRAPHY_KEYS = {
    "font-family", "font-size", "line-height", "font-weight", "letter-spacing",
    "text-transform", "font-style", "text-decoration", "color", "word-spacing",
    "font-variant", "text-align",
}

# 03-atributos-comunes.md §1
VISIBILITY_TOKENS = {"hide-desktop", "hide-laptop", "hide-tablet", "hide-mobile"}

# helper.php:197-224 genera 9 chars ([0-9a-f] openssl / [0-9a-z] fallback);
# el Visual Builder (JS) emite algunos de 8. Se acepta el rango observado.
RE_UID = re.compile(r"^[0-9a-z]{6,12}$")

# Claves attr dinámicas: el catálogo no las lista porque dependen de taxonomías/CPT
RE_DYNAMIC_ATTR = re.compile(
    r"^(query_terms_(includes|excludes)_|query_post_type_|query_taxonomy_|mfn_)"
)

# Valores que llevan dynamic data: no validables contra options
RE_DYNAMIC_VALUE = re.compile(r"\{[a-z0-9_\-|: ]+\}", re.I)

RE_INLINE_STYLE = re.compile(r"""\bstyle\s*=\s*["']""", re.I)
RE_STYLE_TAG = re.compile(r"<\s*style[\s>]|<\s*link[^>]+stylesheet", re.I)
RE_SHORTCODE = re.compile(r"\[([a-z0-9_]+)[\s\]/]", re.I)

RE_COLOR = re.compile(
    r"^(#[0-9a-f]{3,8}"
    r"|rgba?\([^)]*\)"
    r"|hsla?\([^)]*\)"
    r"|var\(--[^)]*\)"
    r"|color-mix\([^)]*\)"
    r"|transparent|currentcolor|inherit|initial|unset|none)$",
    re.I,
)
CSS_NAMED_COLORS = {
    "black", "white", "red", "green", "blue", "yellow", "orange", "purple",
    "gray", "grey", "silver", "maroon", "olive", "lime", "aqua", "teal",
    "navy", "fuchsia", "pink", "brown", "gold", "beige", "ivory", "cyan",
    "magenta", "violet", "indigo", "coral", "salmon", "khaki", "tan",
}

# Valor numérico que necesita unidad (heurística sobre el style CSS emitido)
STYLES_NEED_UNIT = {
    "width", "height", "min-width", "min-height", "max-width", "max-height",
    "top", "right", "bottom", "left", "font-size", "letter-spacing",
    "column-gap", "row-gap", "gap", "border-width", "border-radius",
    "padding", "margin", "text-indent",
}
STYLES_UNITLESS_OK = {"line-height", "z-index", "order", "opacity", "flex-grow", "flex-shrink"}

RE_NUMERIC = re.compile(r"^-?\d+(\.\d+)?$")

# --- Reglas del proyecto (05-reglas-y-trampas.md §1, reglas 5 y 6) ---------- #

# Regla 6: márgenes y paddings en rem
SPACING_STYLES = {"padding", "margin"}
RE_BAD_SPACING_UNIT = re.compile(r"^-?\d*\.?\d+\s*(px|pt|em|ex|ch|cm|mm|in|pc)$", re.I)

# Regla 5: estilos que deben declarar valor `mobile` además de `desktop`
RESPONSIVE_REQUIRED_STYLES = {"padding", "margin", "typography", "font-size"}

# Coherencia switcher -> subcampo (03-atributos-comunes.md §4)
SWITCHER_RULES = [
    # (campo dependiente, switcher, valor requerido, ámbitos)
    ("css_advanced_flex", "width_switcher", {"custom"}, {"section", "wrap", "item"}),
    ("css_advanced_height", "height_switcher", {"custom", "full-screen"}, {"section", "wrap", "item"}),
    ("css_advanced_gradient", "background_switcher", {"gradient"}, {"section", "wrap", "item"}),
    ("css_advanced_overlay_gradient", "background_overlay_switcher", {"gradient"}, {"section", "wrap"}),
    ("css_grid_columns_custom", "grid_columns_switcher", {"custom"}, {"wrap"}),
]


# --------------------------------------------------------------------------- #
# Modelo de incidencias
# --------------------------------------------------------------------------- #

# Centinela: el `type` del item no existe, así que su catálogo de attr es desconocido
UNKNOWN_TYPE = "\x00unknown"

ERROR, WARN, INFO = "error", "warning", "info"
LEVEL_ORDER = {ERROR: 0, WARN: 1, INFO: 2}


class Issue:
    __slots__ = ("level", "code", "path", "msg", "hint")

    def __init__(self, level, code, path, msg, hint=""):
        self.level = level
        self.code = code
        self.path = path
        self.msg = msg
        self.hint = hint

    def as_dict(self):
        d = {"level": self.level, "code": self.code, "path": self.path, "message": self.msg}
        if self.hint:
            d["hint"] = self.hint
        return d


# --------------------------------------------------------------------------- #
# Catálogo de campos (schema)
# --------------------------------------------------------------------------- #

class Schema:
    """Índice de definiciones de campo extraídas de _elements.json."""

    def __init__(self, data):
        self.raw = data
        self.item_types = set(data.get("items", {}).keys())
        self.inline_shortcodes = set(data.get("inline_shortcodes", {}).keys())
        self.animations = set(data.get("animations", {}).keys())

        self.section = self._index(data.get("section", []))
        self.wrap = self._index(data.get("wrap", []))
        self.advanced = self._index(data.get("advanced", []))

        self.items = {}
        for itype, spec in data.get("items", {}).items():
            idx = self._index(spec.get("attr", []))
            for fid, defs in self.advanced.items():
                idx.setdefault(fid, []).extend(defs)
            self.items[itype] = idx

        # Catálogo global: usado solo para decidir si una clave es "desconocida
        # en este tipo" o "inexistente en todo el theme".
        self.all_ids = set(self.section) | set(self.wrap) | set(self.advanced)
        for idx in self.items.values():
            self.all_ids |= set(idx)

    @staticmethod
    def _walk(fields, out):
        """Aplana definiciones, incluidas las anidadas en options/param/form."""
        if isinstance(fields, dict):
            fields = fields.values()
        if not isinstance(fields, (list, tuple)):
            return
        for f in fields:
            if not isinstance(f, dict):
                continue
            if f.get("id"):
                out.append(f)
            for nested_key in ("options", "param", "form", "fields", "attr"):
                nested = f.get(nested_key)
                if isinstance(nested, (list, dict)):
                    # options de tipo {clave: "Etiqueta"} no son campos
                    values = nested.values() if isinstance(nested, dict) else nested
                    if any(isinstance(v, dict) for v in values):
                        Schema._walk(nested, out)

    def _index(self, fields):
        flat = []
        self._walk(fields, flat)
        idx = defaultdict(list)
        for f in flat:
            idx[f["id"]].append(f)
        return dict(idx)

    def defs_for(self, scope, itype, key):
        if scope == "section":
            return self.section.get(key, [])
        if scope == "wrap":
            return self.wrap.get(key, [])
        idx = self.items.get(itype) or {}
        return idx.get(key) or self.advanced.get(key, [])


# --------------------------------------------------------------------------- #
# Validador
# --------------------------------------------------------------------------- #

class Validator:
    def __init__(self, schema, opts):
        self.s = schema
        self.o = opts
        self.issues = []
        self.stats = Counter()
        self.uids = defaultdict(list)
        self.fixes = []
        self.fixed = False

    # -- registro ---------------------------------------------------------- #

    def add(self, level, code, path, msg, hint=""):
        if code in self.o.ignore:
            return
        self.issues.append(Issue(level, code, path, msg, hint))

    def err(self, *a, **k):
        self.add(ERROR, *a, **k)

    def warn(self, *a, **k):
        self.add(WARN, *a, **k)

    def info(self, *a, **k):
        self.add(INFO, *a, **k)

    def fix(self, path, what):
        self.fixes.append("%s — %s" % (path, what))
        self.fixed = True

    # -- entrada ----------------------------------------------------------- #

    def run(self, doc):
        if not isinstance(doc, list):
            self.err("E001", "$", "La raíz no es un array de secciones (es %s)."
                     % type(doc).__name__,
                     "BeBuilder espera SIEMPRE un array: [ {sección}, ... ].")
            return doc
        if not doc:
            self.err("E002", "$", "Array raíz vacío.",
                     "Guardar con secciones vacías ejecuta delete_post_meta('mfn-page-items') "
                     "y BORRA el contenido de la página (visual-builder.php:385).")
            return doc

        for i, section in enumerate(doc):
            self.section(section, "$[%d]" % i)

        self.check_uid_collisions()
        return doc

    # -- sección ----------------------------------------------------------- #

    def section(self, node, path):
        if not isinstance(node, dict):
            self.err("E003", path, "La sección no es un objeto (es %s)." % type(node).__name__)
            return
        self.stats["sections"] += 1

        self.node_identity(node, path, "section")

        if "items" in node and "wraps" not in node:
            self.warn("W001", path, "Sección con `items` en vez de `wraps` (formato legacy).",
                      "visual-builder-class.php:951 lo autoconvierte, pero genera JSON no canónico.")

        wraps = node.get("wraps")
        if wraps is None:
            if node.get("mfn_global_section_id") or node.get("global_sections"):
                self.info("I004", path, "Sección global sin `wraps` (contenido resuelto por ID).")
            elif "items" not in node:
                self.err("E004", path, "Sección sin `wraps`: se renderiza vacía.")
        elif not isinstance(wraps, list):
            self.err("E005", path + ".wraps", "`wraps` debe ser un array.")
            wraps = None

        attr = self.attr(node, path, "section", None)

        if attr is not None and "width_switcher" not in attr:
            self.info("I050", path + ".attr",
                      "Sección sin `width_switcher` explícito.",
                      'Checklist del proyecto: escribir "full" | "" | "custom".')

        if wraps:
            for i, w in enumerate(wraps):
                self.wrap(w, "%s.wraps[%d]" % (path, i))

    # -- wrap -------------------------------------------------------------- #

    def wrap(self, node, path, nested=False):
        if not isinstance(node, dict):
            self.err("E003", path, "El wrap no es un objeto (es %s)." % type(node).__name__)
            return
        self.stats["wraps"] += 1

        self.node_identity(node, path, "wrap")
        self.sizes(node, path, SIZES_WRAP, required=True, kind="wrap")

        attr = self.attr(node, path, "wrap", None)

        if attr is not None:
            grid = str(node.get("grid", "") or attr.get("grid", ""))
            for key in ("css_grid_columns", "css_grid_columns_custom", "css_grid_columns_gap"):
                if key in attr and grid != "grid":
                    self.info("I053", "%s.attr.%s" % (path, key),
                              "`%s` sin `grid: \"grid\"` en el wrap: la regla se genera pero no "
                              "aplica (el selector exige `.mcb-wrap-grid`)." % key)
                    break

        items = node.get("items")
        if items is None:
            self.info("I005", path, "Wrap sin `items` (columna vacía).")
        elif not isinstance(items, list):
            self.err("E005", path + ".items", "`items` debe ser un array.")
        else:
            for i, it in enumerate(items):
                self.item(it, "%s.items[%d]" % (path, i))

    # -- item -------------------------------------------------------------- #

    def item(self, node, path):
        if not isinstance(node, dict):
            self.err("E003", path, "El item no es un objeto (es %s)." % type(node).__name__)
            return

        is_wrap = str(node.get("item_is_wrap", "")) in ("1", "true")

        if is_wrap:
            self.stats["nested_wraps"] += 1
            self.warn("W005", path,
                      "`item_is_wrap` (wrap anidado): válido en el Visual Builder, "
                      "pero desactiva BeBuilder Blocks Classic y genera warnings en el builder clásico.",
                      "admin.php:1637-1646 / :833. Evitarlo si la página debe editarse fuera del VB.")
            if node.get("type"):
                self.err("E011", path + ".type",
                         "Un wrap anidado (`item_is_wrap: 1`) no debe llevar `type` (tiene \"%s\")."
                         % node.get("type"))
            if not isinstance(node.get("items"), list):
                self.err("E012", path, "`item_is_wrap: 1` sin array `items`.")
            self.node_identity(node, path, "wrap")
            self.sizes(node, path, SIZES, required=True, kind="item")
            self.attr(node, path, "wrap", None)
            for i, it in enumerate(node.get("items") or []):
                self.item(it, "%s.items[%d]" % (path, i))
            return

        self.stats["items"] += 1
        itype = node.get("type")

        if not itype:
            self.err("E009", path,
                     "Item sin `type` y sin `item_is_wrap: 1`: el front lo descarta (front.php:2606).")
        elif not isinstance(itype, str):
            self.err("E010", path + ".type", "`type` debe ser string (es %s)." % type(itype).__name__)
            itype = None
        elif itype not in self.s.item_types:
            near = self.suggest(itype, self.s.item_types)
            self.err("E010", path + ".type",
                     "`type: \"%s\"` no existe: el item se ignora EN SILENCIO (front.php:2608)." % itype,
                     ("¿Querías \"%s\"?" % near) if near else
                     "Tipos válidos: builder-elements/_elements.json → items (149).")
            self.stats["type_" + str(itype)] += 1
            itype = UNKNOWN_TYPE  # evita una cascada de W058 sobre un catálogo equivocado
        else:
            self.stats["type_" + itype] += 1

        self.node_identity(node, path, "item")
        self.sizes(node, path, SIZES, required=True, kind="item")

        attr = self.attr(node, path, "item", itype)

        if itype == "heading" and attr is not None:
            if not attr.get("title") and (attr.get("content") or attr.get("tag")):
                self.err("E055", path + ".attr",
                         "El item `heading` usa `title` + `header_tag`; `content`/`tag` son del "
                         "shortcode inline. Mezclarlos deja el título vacío.")
            elif not attr.get("title"):
                self.warn("W055", path + ".attr", "Item `heading` sin `attr.title`.")

    # -- identidad / sizes -------------------------------------------------- #

    def node_identity(self, node, path, kind):
        uid = node.get("uid")
        if uid is None:
            if self.o.fix:
                node["uid"] = self.gen_uid(path)
                self.fix(path, "uid generado (%s)" % node["uid"])
            else:
                self.info("I001", path, "Sin `uid` (el import lo regenera igualmente).")
        elif not isinstance(uid, str) or not RE_UID.match(uid):
            self.warn("W003", path + ".uid",
                      "`uid` fuera de formato (%r): se esperan 9 caracteres [0-9a-z]." % uid,
                      "helper.php:197-224. Se regenera al importar, pero rompe el CSS local "
                      "si se escribe el meta directamente.")
        else:
            self.uids[uid].append(path)

        for key, default in (("icon", kind), ("jsclass", kind), ("title", kind.capitalize())):
            if key not in node:
                if self.o.fix:
                    node[key] = default
                    self.fix(path, "%s=\"%s\" añadido (paridad Visual Builder)" % (key, default))
                else:
                    self.info("I003", path,
                              "Sin `%s` (opcional; lo regenera el VB al abrir la página)." % key)
                    break

    def sizes(self, node, path, allowed, required, kind):
        size = node.get("size")
        if size is None:
            if required:
                self.err("E00%d" % (6 if kind == "wrap" else 7), path,
                         "%s sin `size`: NO se renderiza, sin ningún aviso." % kind.capitalize(),
                         "front.php:1625 (wrap) / :2614 (item). Causa nº1 de \"importé y no sale nada\".")
        elif size not in allowed:
            self.err("E008", path + ".size",
                     "`size: %r` inválido." % size,
                     "Válidos: %s%s." % (", ".join(sorted(SIZES)),
                                         " y \"divider\" (solo wrap)" if kind == "wrap" else ""))

        for key in ("tablet_size", "mobile_size", "laptop_size"):
            val = node.get(key)
            if val is None:
                if key in ("tablet_size", "mobile_size"):
                    if self.o.fix and size in allowed:
                        node[key] = size if key == "tablet_size" else "1/1"
                        self.fix(path, "%s=\"%s\" añadido" % (key, node[key]))
                    else:
                        self.warn("W002", path,
                                  "Sin `%s` (fallback implícito: %s): el responsive debe ser "
                                  "explícito." % (key, "= size" if key == "tablet_size" else '"1/1"'),
                                  "Regla 5 del proyecto (05-reglas-y-trampas.md §1). "
                                  "`--fix` lo añade automáticamente.")
            elif val not in allowed:
                self.err("E008", "%s.%s" % (path, key), "`%s: %r` inválido." % (key, val))

    def check_uid_collisions(self):
        for uid, paths in self.uids.items():
            if len(paths) > 1:
                self.warn("W004", paths[1],
                          "`uid` duplicado \"%s\" (también en %s)." % (uid, paths[0]),
                          "El import los regenera, pero con escritura directa del meta "
                          "el CSS local de un bloque pisa al del otro.")

    # -- attr --------------------------------------------------------------- #

    def attr(self, node, path, scope, itype):
        attr = node.get("attr")
        if attr is None:
            self.info("I006", path, "Sin `attr` (fallback `[]`: el bloque no tendrá estilos).")
            return None
        if not isinstance(attr, dict):
            self.err("E013", path + ".attr", "`attr` debe ser un objeto (es %s)." % type(attr).__name__)
            return None

        apath = path + ".attr"
        legacy = {"section": LEGACY_SECTION, "wrap": LEGACY_WRAP, "item": LEGACY_ITEM}[scope]

        for key in list(attr.keys()):
            value = attr[key]
            kpath = "%s.%s" % (apath, key)

            if key in RUNTIME_ATTRS:
                if self.o.fix:
                    del attr[key]
                    self.fix(kpath, "atributo de runtime del VB eliminado")
                else:
                    self.err("E020", kpath,
                             "Atributo de runtime del Visual Builder (`%s`): no debe exportarse." % key,
                             "`vb_postid` altera la resolución de dynamic data (front.php:2638-2640).")
                continue

            if key == "custom_css":
                self.err("E022", kpath, "`custom_css` inyecta CSS crudo: prohibido en JSON generado.",
                         "Trasladarlo a campos `css_*` específicos (docs/bebuilder/02 §7).")
                continue

            if key in legacy:
                if value in (None, "", 0, "0", {}, []):
                    self.info("I021", kpath,
                              "Atributo legacy `%s` vacío: inerte, pero conviene no exportarlo." % key)
                    if self.o.fix:
                        del attr[key]
                        self.fix(kpath, "atributo legacy vacío eliminado")
                else:
                    self.err("E021", kpath,
                             "Atributo legacy `%s` (%s) con valor %r: el front lo vuelca como "
                             "style=\"\" inline." % (key, scope, value),
                             self.legacy_hint(key))
                continue

            if key == "class":
                if self.o.fix:
                    merged = " ".join(x for x in [str(attr.get("classes", "")), str(value)] if x).strip()
                    attr["classes"] = merged
                    del attr[key]
                    self.fix(kpath, "`class` migrado a `classes` (\"%s\")" % merged)
                else:
                    self.warn("W020", kpath, "`class` está deprecado: usar `classes` (pestaña Advanced).")
                continue

            defs = self.s.defs_for(scope, itype, key)
            if not defs:
                if itype is UNKNOWN_TYPE:
                    continue  # ya se reportó E010; el catálogo de este item no existe
                if not RE_DYNAMIC_ATTR.match(key):
                    known = key in self.s.all_ids
                    self.warn("W058", kpath,
                              "`%s` no está declarado %s: shortcode_atts() lo descarta en silencio." % (
                                  key,
                                  "para el item `%s`" % itype if known and itype else "en el catálogo del theme"),
                              "" if known else "Posible typo. Catálogo: builder-elements/_elements.json.")
                continue

            self.value(key, value, defs, kpath, scope, itype)

        self.consistency(attr, apath, scope)
        return attr

    @staticmethod
    def legacy_hint(key):
        table = {
            "padding_top": "→ css_advanced_padding sobre .mcb-section-mfnuidelement",
            "padding_bottom": "→ css_advanced_padding sobre .mcb-section-mfnuidelement",
            "padding_horizontal": "→ css_advanced_padding sobre .mcb-section-mfnuidelement",
            "padding": "→ css_advanced_padding sobre .mcb-wrap-inner / .mcb-column-inner",
            "bg_color": "→ css_advanced_background_color",
            "bg_image": "→ css_advanced_background_image",
            "bg_position": "→ css_advanced_background_position",
            "bg_size": "→ css_advanced_background_size",
            "style": "→ campos css_* específicos",
            "align": "→ css_txt_align / css_advanced_*",
            "margin_bottom": "→ css_advanced_margin",
            "column_bg": "→ css_advanced_background_color",
            "move_up": "→ css_advanced_margin (top negativo)",
        }
        return table.get(key, "Equivalencias en docs/bebuilder/02-css-pipeline.md §7.")

    # -- valores ------------------------------------------------------------ #

    def value(self, key, value, defs, kpath, scope, itype):
        # Un id puede tener varias definiciones (advanced + propia del elemento).
        # Se valida contra la primera que declare selector/style, si la hay.
        styled = [d for d in defs if d.get("selector") and d.get("style")]
        primary = styled[0] if styled else defs[0]

        if isinstance(value, dict) and ("selector" in value or "style" in value or "val" in value):
            self.css_field(key, value, defs, primary, kpath)
            return

        if styled and isinstance(value, dict):
            # Campo de estilo exportado como valor plano responsive: no genera CSS
            self.info("I030", kpath,
                      "`%s` sin `selector`/`style`: no genera CSS (class-mfn-helper.php:195-198)." % key)
            return

        if isinstance(value, str):
            self.string_content(value, kpath)
            enum_checked = self.options(value, defs, kpath, key)
            self.special_plain(key, value, kpath, enum_checked)

    def css_field(self, key, value, defs, primary, kpath):
        selector = value.get("selector")
        style = value.get("style")
        val = value.get("val")

        # class-mfn-helper.php:198 — `if (empty(selector) || empty(val)) continue;`
        # `style` NO se comprueba: si falta, se emite ":valor;" (CSS corrupto).
        blank = [k for k in ("selector", "val") if not value.get(k)]
        if blank:
            self.warn("W030", kpath,
                      "Campo de estilo con %s vacío: NO genera CSS." % " y ".join(blank),
                      "class-mfn-helper.php:198 salta el atributo si `selector` o `val` están vacíos.")
        elif not style:
            self.err("E030", kpath,
                     "`selector` y `val` presentes pero `style` vacío: el helper emite "
                     "\":valor;\" y corrompe la regla CSS del bloque.",
                     "class-mfn-helper.php:198 no valida `style`; el fallo aparece en el CSS final.")

        # PHP empty(): "0" y 0 se consideran vacíos y el atributo se descarta.
        if value.get("val") in ("0", 0):
            self.warn("W039", kpath + ".val",
                      "`val` = %r: PHP `empty()` lo trata como vacío y NO genera CSS."
                      % value.get("val"),
                      "Usar \"0px\" / \"0%\" en su lugar (class-mfn-helper.php:198 y :406).")

        if not selector:
            return

        if isinstance(selector, str):
            expected = {d.get("selector") for d in defs if d.get("selector")}
            norm = {self.norm_selector(e) for e in expected}
            exact = selector in expected
            equivalent = exact or self.norm_selector(selector) in norm

            if re.search(r"[{};]", selector):
                self.err("E032", kpath + ".selector",
                         "El selector contiene `{`, `}` o `;`: rompe el CSS generado.")

            if not exact:
                # El propio theme declara `:hover` literal en algunos selectores;
                # solo es un fallo si el campo NO lo declara así.
                declares_colon = any(":" in e for e in expected)
                if re.search(r":[a-z\-]{3,}", selector) and "|" not in selector and not declares_colon:
                    if self.o.fix:
                        value["selector"] = re.sub(r":(?=[a-z\-]{3,})", "|", selector)
                        self.fix(kpath + ".selector", "pseudo-clase `:` → `|`")
                        selector = value["selector"]
                    else:
                        self.err("E031", kpath + ".selector",
                                 "Pseudo-clase escrita con `:` (%s): el helper espera `|`." % selector,
                                 "class-mfn-helper.php:404-428 sustituye `|` por `:`. "
                                 "Escribir `|hover`, `|before`.")

            if "mfnuidelement" not in selector:
                self.warn("W031", kpath + ".selector",
                          "El selector no contiene `mfnuidelement`: el estilo se aplicará a TODA la página.",
                          "Selectores base por nivel en docs/bebuilder/02-css-pipeline.md §3.")

            if expected and not equivalent:
                self.warn("W032", kpath + ".selector",
                          "Selector distinto del declarado en el theme para `%s`." % key,
                          "En el JSON: %s\n          Esperado:   %s"
                          % (selector, " | ".join(sorted(expected))))
            elif expected and equivalent and not exact:
                self.info("I032", kpath + ".selector",
                          "Selector equivalente pero no idéntico al del theme "
                          "(difiere el combinador `>` o los espacios).")

        if isinstance(style, str):
            expected = {d.get("style") for d in defs if d.get("style")}
            if expected and style not in expected:
                self.warn("W033", kpath + ".style",
                          "`style: \"%s\"` distinto del declarado en el theme (%s)."
                          % (style, ", ".join(sorted(expected))))

        if val in (None, "", {}, []):
            return

        self.val(key, val, primary, style, kpath + ".val")
        self.responsive_coverage(key, val, style, kpath + ".val")

    def responsive_coverage(self, key, val, style, vpath):
        """Regla 5 del proyecto: espaciados y tipografías necesitan valor `mobile`."""
        if style not in RESPONSIVE_REQUIRED_STYLES or not isinstance(val, dict):
            return
        devices = set(val.keys()) & DEVICE_SET
        if not devices or "mobile" in devices:
            return
        self.warn("W062", vpath,
                  "`%s` sin valor `mobile` (solo %s): el JSON debe contemplar el responsive."
                  % (key, ", ".join(sorted(devices))),
                  "Regla 5 del proyecto (05-reglas-y-trampas.md §1). En móvil el valor de "
                  "desktop suele ser excesivo; añadir la clave \"mobile\" al `val`.")

    def val(self, key, val, fdef, style, vpath):
        responsive = bool(fdef.get("responsive"))
        ftype = fdef.get("type")

        if isinstance(val, dict):
            first = set(val.keys())
            devices = first & DEVICE_SET
            others = first - DEVICE_SET
            # Sub-propiedades legítimas a primer nivel según el tipo de campo
            subprops = self.subprops_for(fdef, ftype)
            stray = others - subprops

            if responsive and stray and not devices:
                self.warn("W037", vpath,
                          "`val` con claves no-dispositivo (%s) en un campo responsive: se emiten "
                          "como sub-propiedades SOLO en desktop." % ", ".join(sorted(stray)),
                          "Envolver en {\"desktop\": {...}}. Dispositivos: desktop/laptop/tablet/mobile.")
            elif responsive and stray and devices:
                self.err("E037", vpath,
                          "`val` mezcla dispositivos (%s) con claves sueltas no reconocidas (%s)."
                          % (", ".join(sorted(devices)), ", ".join(sorted(stray))))
            elif responsive and others and not devices:
                self.info("I038", vpath,
                          "`val` sin claves de dispositivo: las sub-propiedades (%s) se emiten "
                          "SOLO en desktop." % ", ".join(sorted(others)),
                          "Si el valor debe aplicar en todos los tamaños, envolver en "
                          "{\"desktop\": {...}} (la cascada hace el resto).")
            elif others and devices:
                self.info("I037", vpath,
                          "Propiedades a primer nivel (%s) junto a dispositivos: se aplican solo "
                          "en desktop (formato habitual del VB para campos no responsive)."
                          % ", ".join(sorted(others & subprops)))
            # Nota: el motor despacha por clave de dispositivo SIEMPRE
            # (class-mfn-helper.php:240-290), aunque el campo no sea `responsive`
            # en el panel: usar desktop/laptop/tablet/mobile nunca es un fallo.

            if devices:
                for dev in sorted(devices):
                    self.leaf(key, val[dev], fdef, style, "%s.%s" % (vpath, dev), ftype)
                loose = {k: v for k, v in val.items() if k in subprops}
                if loose:
                    self.leaf(key, loose, fdef, style, vpath, ftype)
            else:
                self.leaf(key, val, fdef, style, vpath, ftype)
        else:
            self.leaf(key, val, fdef, style, vpath, ftype)

    @staticmethod
    def subprops_for(fdef, ftype):
        if ftype == "typography_vb" or fdef.get("style") == "typography":
            return TYPOGRAPHY_KEYS
        if ftype == "dimensions" and fdef.get("version") == "separated-fields":
            return SIDES
        if ftype in STRING_ONLY_TYPES:
            return {"string", "type", "angle", "color", "location", "color2", "location2",
                    "blur", "brightness", "contrast", "grayscale", "hue-rotate",
                    "invert", "opacity", "saturate", "sepia",
                    "translateX", "translateY", "rotate", "scaleX", "scaleY",
                    "skewX", "skewY", "perspective"}
        return set()

    def leaf(self, key, v, fdef, style, path, ftype):
        if v in (None, "", {}, []):
            return

        # ---- dimensions: las dos gramáticas incompatibles (trampa 14)
        if ftype == "dimensions":
            separated = fdef.get("version") == "separated-fields"
            if isinstance(v, dict):
                if not separated:
                    if self.o.fix:
                        shorthand = self.dims_to_shorthand(v, style)
                        self.replace_leaf(path, shorthand)
                        self.fix(path, "objeto → shorthand \"%s\"" % shorthand)
                    else:
                        self.err("E035", path,
                                 "`%s` es un `dimensions` SIN `version`: exige string shorthand, no objeto." % key,
                                 "El helper emite `%s-top` (propiedad inexistente → borde/radio invisible) y el "
                                 "panel del VB guarda \"[object Object]\". Formato: \"1px 1px 1px 1px\" "
                                 "(%s). Trampa 14." % (
                                     style or "border-width",
                                     "top-left top-right bottom-right bottom-left"
                                     if style == "border-radius" else "top right bottom left"))
                else:
                    unknown = set(v.keys()) - SIDES
                    if unknown:
                        self.warn("W044", path,
                                  "Lados desconocidos en `%s`: %s (válidos: top, right, bottom, left)."
                                  % (key, ", ".join(sorted(unknown))))
                    for side, sv in v.items():
                        if side in SIDES:
                            self.unit(sv, style, "%s.%s" % (path, side))
                            self.rem_unit(key, sv, style, "%s.%s" % (path, side))
            elif isinstance(v, str):
                if separated:
                    self.info("I035", path,
                              "`%s` (separated-fields) con string: válido, se emite como shorthand." % key)
                else:
                    parts = v.split()
                    if len(parts) not in (1, 2, 3, 4):
                        self.warn("W045", path, "Shorthand de %d valores en `%s`." % (len(parts), key))
                for p in v.split():
                    self.unit(p, style, path)
                    self.rem_unit(key, p, style, path)
            return

        # ---- gradient / transform / filter: el helper descarta toda subclave != "string"
        # (class-mfn-helper.php:229-232 y :250-253, coincidencia por substring en `style`)
        if isinstance(v, dict) and (
                ftype in STRING_ONLY_TYPES
                or any(t in (style or "") for t in ("gradient", "transform", "filter"))):
            if not v.get("string"):
                self.err("E036", path,
                         "`%s` sin subclave `string` (o vacía): el helper descarta el resto "
                         "de subclaves y no emite nada." % key,
                         "Ej.: {\"type\":\"linear\",...,"
                         "\"string\":\"linear-gradient(180deg,#000 0%,#fff 100%)\"}")
            return

        # ---- typography
        if ftype == "typography_vb" or style == "typography":
            if isinstance(v, dict):
                unknown = set(v.keys()) - TYPOGRAPHY_KEYS
                if unknown:
                    self.warn("W041", path,
                              "Propiedades tipográficas no reconocidas: %s." % ", ".join(sorted(unknown)),
                              "Válidas: %s." % ", ".join(sorted(TYPOGRAPHY_KEYS)))
                for k2, v2 in v.items():
                    if k2 == "color" and isinstance(v2, str):
                        self.color(v2, "%s.%s" % (path, k2))
                    elif k2 in ("font-size", "letter-spacing", "word-spacing") and isinstance(v2, str):
                        self.unit(v2, k2, "%s.%s" % (path, k2))
            else:
                self.warn("W041", path, "`typography` debe ser un objeto de propiedades CSS.")
            return

        # ---- color
        if ftype == "color" or (style or "").endswith("color"):
            if isinstance(v, str):
                self.color(v, path)
            return

        # ---- box-shadow / text-shadow
        if ftype in ("box_shadow", "text_shadow"):
            if not isinstance(v, str):
                self.warn("W046", path, "`%s` debe ser un string CSS." % key)
            return

        # ---- opciones cerradas responsive
        if isinstance(v, str):
            self.options(v, [fdef], path, key)
            if style:
                self.unit(v, style, path)
            if re.search(r"[;{}]", v) and style not in ("--mfn-custom", None):
                self.warn("W047", path, "El valor contiene `;` o `{}`: puede romper la regla CSS generada.")

    # -- utilidades de valor ------------------------------------------------ #

    def options(self, v, defs, path, key):
        """Valida contra el enum del campo. Devuelve True si el campo tenía enum."""
        all_valid = set()
        checked = False

        for d in defs:
            opts = d.get("options")
            if not opts or d.get("php_options") or d.get("themeoptions") \
                    or d.get("mfn_taxonomies") or d.get("js_options") or d.get("dynamic_data"):
                return checked
            if d.get("type") not in ("switch", "select", "radio_img", "multiselect"):
                return checked
            if isinstance(opts, dict):
                if any(isinstance(x, dict) for x in opts.values()):
                    return  # options con subcampos (tabs): no es un enum
                valid = set(map(str, opts.keys()))
            elif isinstance(opts, list):
                if any(isinstance(x, dict) for x in opts):
                    return checked
                valid = set(str(i) for i in range(len(opts)))
            else:
                return checked

            checked = True
            all_valid |= valid
            if d.get("std") is not None:
                all_valid.add(str(d["std"]))

            # switch `version: "multiple"` y multiselect: valor = varios tokens
            if d.get("type") == "multiselect" or d.get("version") == "multiple":
                tokens = [t for t in re.split(r"[\s,]+", v) if t]
                bad = [t for t in tokens if t not in valid]
                if not bad:
                    return checked
                continue
            if v in valid or RE_DYNAMIC_VALUE.search(v):
                return checked

        if checked and v != "" and v not in all_valid:
            near = self.suggest(v, all_valid)
            self.warn("W040", path,
                      "`%s: \"%s\"` no está entre las opciones declaradas del campo." % (key, v),
                      ("¿\"%s\"? " % near if near else "") +
                      "Opciones: %s." % ", ".join(sorted(x or '""' for x in all_valid)))
        return checked

    def rem_unit(self, key, v, style, path):
        """Regla 6 del proyecto: márgenes y paddings en rem."""
        if style not in SPACING_STYLES or not isinstance(v, str):
            return
        v = v.strip()
        if not v or not RE_BAD_SPACING_UNIT.match(v):
            return
        if re.match(r"^-?0+(\.0+)?\s*[a-z%]*$", v, re.I):
            return  # el cero no necesita unidad
        unit = RE_BAD_SPACING_UNIT.match(v).group(1).lower()
        hint = ""
        try:
            n = float(re.sub(r"[a-z]+$", "", v, flags=re.I))
            if unit == "px":
                hint = "Equivale a %grem con la raíz en 16px." % round(n / 16.0, 4)
            elif unit == "em":
                hint = "Con la tipografía por defecto equivale a %grem." % round(n, 4)
        except ValueError:
            pass
        self.warn("W061", path,
                  "`%s` en `%s` (%s): los márgenes y paddings van en `rem`."
                  % (v, key, unit),
                  (hint + " " if hint else "") +
                  "Regla 6 del proyecto (05-reglas-y-trampas.md §1). Admitidos además: "
                  "0, auto, %, unidades de viewport y calc()/var().")

    def color(self, v, path):
        v = v.strip()
        if not v or RE_COLOR.match(v) or v.lower() in CSS_NAMED_COLORS or RE_DYNAMIC_VALUE.search(v):
            return
        self.warn("W042", path, "Color no reconocido: %r." % v,
                  "Formatos: #rrggbb(aa), rgb()/rgba(), hsl(), var(--x), transparent.")

    def unit(self, v, style, path):
        if not isinstance(v, str):
            return
        v = v.strip()
        if not v or style in STYLES_UNITLESS_OK or RE_DYNAMIC_VALUE.search(v):
            return
        base = (style or "").split("-")[0]
        if style in STYLES_NEED_UNIT or base in ("padding", "margin", "border"):
            if RE_NUMERIC.match(v) and v not in ("0", "0.0"):
                self.warn("W043", path,
                          "Valor numérico sin unidad (%r) para `%s`: el navegador descarta la declaración."
                          % (v, style))

    def string_content(self, v, path):
        if RE_INLINE_STYLE.search(v):
            self.err("E023", path, "HTML con `style=\"\"` inline: prohibido por la regla del proyecto.",
                     "Trasladar a campos `css_*` (docs/bebuilder/02 §7).")
        if RE_STYLE_TAG.search(v):
            self.err("E024", path, "El contenido incluye `<style>` o un `<link rel=stylesheet>`.")
        for sc in set(m.group(1) for m in RE_SHORTCODE.finditer(v)):
            if sc in self.s.inline_shortcodes or sc in self.s.item_types:
                continue
            if sc in ("vc_row", "et_pb_section"):
                self.warn("W060", path, "Shortcode de otro page builder: `[%s]`." % sc)
            elif len(sc) > 2 and "_" in sc or sc in ("gallery", "embed", "caption"):
                continue  # shortcodes de WP/plugins: no verificables
            else:
                self.info("I060", path, "Shortcode no reconocido en el catálogo: `[%s]`." % sc)

    def special_plain(self, key, v, path, enum_checked=False):
        if key == "animate":
            if v and v not in self.s.animations and not enum_checked:
                self.warn("W056", path, "Animación desconocida: %r." % v,
                          "Válidas: %s." % ", ".join(sorted(x for x in self.s.animations if x)))
        elif key == "visibility":
            tokens = [t for t in v.split(" ") if t]
            bad = [t for t in tokens if t not in VISIBILITY_TOKENS]
            if bad:
                self.warn("W057", path, "Tokens de visibilidad desconocidos: %s." % ", ".join(bad),
                          "Válidos: %s." % ", ".join(sorted(VISIBILITY_TOKENS)))
            if tokens and not v.startswith(" "):
                self.info("I057", path,
                          "`visibility` se exporta con espacio inicial (\" hide-mobile\").")
        elif key == "custom_id":
            if v and not re.match(r"^[A-Za-z][\w:.\-]*$", v):
                self.warn("W059", path, "`custom_id` no es un id HTML válido: %r." % v)

    def consistency(self, attr, apath, scope):
        for field, switcher, required, scopes in SWITCHER_RULES:
            if scope not in scopes or field not in attr:
                continue
            current = attr.get(switcher)
            if current is None:
                self.warn("W050", "%s.%s" % (apath, field),
                          "`%s` presente sin `%s` explícito." % (field, switcher),
                          "Escribir `\"%s\": \"%s\"` o el panel del VB no mostrará el control."
                          % (switcher, sorted(required)[0]))
            elif str(current) not in required:
                self.warn("W051", "%s.%s" % (apath, field),
                          "`%s` requiere `%s` en %s (actual: %r)."
                          % (field, switcher, "/".join(sorted(required)), current))

    # -- fix helpers -------------------------------------------------------- #

    def replace_leaf(self, path, newval):
        """Marcador: la sustitución real la hace fix_tree() sobre el nodo."""
        self._pending = getattr(self, "_pending", {})
        self._pending[path] = newval

    @staticmethod
    def dims_to_shorthand(obj, style):
        if style == "border-radius":
            order = ("top", "right", "bottom", "left")  # tl tr br bl mapeados por posición
            keys = ("top-left", "top-right", "bottom-right", "bottom-left")
            vals = [str(obj.get(k) or obj.get(o) or "0") for k, o in zip(keys, order)]
        else:
            vals = [str(obj.get(k) or "0") for k in ("top", "right", "bottom", "left")]
        vals = [v if v not in ("", "None") else "0" for v in vals]
        return " ".join(vals)

    @staticmethod
    def norm_selector(sel):
        """Normaliza combinadores y espacios para comparar selectores equivalentes."""
        return re.sub(r"\s*>\s*", " ", re.sub(r"\s+", " ", sel or "")).strip()

    @staticmethod
    def gen_uid(seed):
        return hashlib.sha1(seed.encode("utf-8")).hexdigest()[:9]

    @staticmethod
    def suggest(word, candidates):
        import difflib
        m = difflib.get_close_matches(str(word), [str(c) for c in candidates], n=1, cutoff=0.75)
        return m[0] if m else ""


# --------------------------------------------------------------------------- #
# Fixer estructural (segunda pasada, aplica cambios de árbol)
# --------------------------------------------------------------------------- #

def apply_deep_fixes(doc, schema, validator):
    """Aplica los fixes que requieren reescribir hojas de `val` (dimensions)."""
    pending = getattr(validator, "_pending", {})
    if not pending:
        return
    for path, newval in pending.items():
        set_by_path(doc, path, newval)


def set_by_path(doc, path, value):
    tokens = re.findall(r"\[(\d+)\]|\.([^.\[]+)", path[1:] if path.startswith("$") else path)
    node = doc
    keys = [int(a) if a else b for a, b in tokens]
    for k in keys[:-1]:
        node = node[k]
    node[keys[-1]] = value


# --------------------------------------------------------------------------- #
# Carga y salida
# --------------------------------------------------------------------------- #

def find_schema(explicit):
    if explicit:
        return explicit
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (
        os.path.join(here, "..", "builder-elements", "_elements.json"),
        os.path.join(os.getcwd(), "builder-elements", "_elements.json"),
    ):
        cand = os.path.normpath(cand)
        if os.path.isfile(cand):
            return cand
    return None


def load_json(text, source):
    try:
        return json.loads(text), None
    except json.JSONDecodeError as e:
        lines = text.splitlines()
        ctx = lines[e.lineno - 1] if 0 < e.lineno <= len(lines) else ""
        pointer = " " * max(e.colno - 1, 0) + "^"
        return None, ("%s: JSON no parseable — %s (línea %d, columna %d)\n    %s\n    %s"
                      % (source, e.msg, e.lineno, e.colno, ctx[:200], pointer[:200]))


COLORS = {ERROR: "\033[31m", WARN: "\033[33m", INFO: "\033[36m", "ok": "\033[32m", "off": "\033[0m",
          "dim": "\033[2m", "bold": "\033[1m"}
ICON = {ERROR: "ERROR  ", WARN: "WARN   ", INFO: "INFO   "}


def render(issues, stats, opts, source):
    use_color = sys.stdout.isatty() and not opts.no_color

    def c(key, text):
        return "%s%s%s" % (COLORS[key], text, COLORS["off"]) if use_color else text

    order = {ERROR: 0, WARN: 1, INFO: 2}
    issues = sorted(issues, key=lambda i: (order[i.level], i.path))

    counts = Counter(i.level for i in issues)
    per_code = Counter(i.code for i in issues)
    shown = 0
    seen_code = Counter()
    out = []
    for i in issues:
        if LEVEL_ORDER[i.level] > LEVEL_ORDER[opts.level]:
            continue
        seen_code[i.code] += 1
        if opts.max_per_code and seen_code[i.code] > opts.max_per_code:
            if seen_code[i.code] == opts.max_per_code + 1:
                out.append(c("dim", "        … y %d casos más de %s (--max-per-code 0 para verlos)."
                             % (per_code[i.code] - opts.max_per_code, i.code)))
            continue
        shown += 1
        if opts.max_issues and shown > opts.max_issues:
            out.append(c("dim", "  … %d incidencias más (usa --max-issues 0)."
                         % (len(issues) - shown + 1)))
            break
        out.append("%s %s %s" % (c(i.level, ICON[i.level]), c("dim", i.code), c("bold", i.path)))
        out.append("        %s" % i.msg)
        if i.hint and not opts.no_hints:
            out.append(c("dim", "        ↳ %s" % i.hint))

    header = "%s  —  %d secciones, %d wraps, %d items, %d wraps anidados" % (
        source, stats["sections"], stats["wraps"], stats["items"], stats["nested_wraps"])
    print(c("bold", header))
    print("")
    if out:
        print("\n".join(out))
        print("")

    if per_code:
        level_of, sample = {}, {}
        for i in issues:
            level_of.setdefault(i.code, i.level)
            sample.setdefault(i.code, i.msg)
        print(c("bold", "Resumen por código"))
        for code, n in sorted(per_code.items(),
                              key=lambda kv: (LEVEL_ORDER[level_of[kv[0]]], -kv[1])):
            if LEVEL_ORDER[level_of[code]] > LEVEL_ORDER[opts.level]:
                continue
            text = re.sub(r"\s+", " ", sample[code])
            print("  %s %-5s ×%-4d %s" % (
                c(level_of[code], ICON[level_of[code]].strip()[0]), code, n,
                text[:88] + ("…" if len(text) > 88 else "")))
        print("")

    verdict = "%d errores · %d warnings · %d infos" % (
        counts[ERROR], counts[WARN], counts[INFO])
    if counts[ERROR]:
        print(c(ERROR, "RECHAZADO — " + verdict))
        print(c(ERROR, "No importar: el JSON se degradará en silencio o romperá el render."))
    elif counts[WARN]:
        print(c(WARN, "VÁLIDO CON AVISOS — " + verdict))
    else:
        print(c("ok", "VÁLIDO — " + verdict))


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Validador de JSON BeBuilder (BeTheme / Muffin Builder).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Fuente de verdad: builder-elements/_elements.json + docs/bebuilder/.")
    p.add_argument("file", help="Fichero JSON a validar ('-' para stdin).")
    p.add_argument("--schema", help="Ruta a _elements.json (autodetectada por defecto).")
    p.add_argument("--json", action="store_true", dest="as_json",
                   help="Salida en JSON (para CI o para que la consuma un agente).")
    p.add_argument("--level", choices=[ERROR, WARN, INFO], default=INFO,
                   help="Nivel mínimo a mostrar (por defecto: info).")
    p.add_argument("--strict", action="store_true",
                   help="Salir con código 2 si hay warnings.")
    p.add_argument("--ignore", default="",
                   help="Códigos a silenciar, separados por coma (ej. W058,I003).")
    p.add_argument("--max-issues", type=int, default=200,
                   help="Máximo de incidencias impresas (0 = sin límite).")
    p.add_argument("--max-per-code", type=int, default=5,
                   help="Máximo de repeticiones impresas por código (0 = sin límite).")
    p.add_argument("--fix", action="store_true",
                   help="Corrige automáticamente lo mecánico y escribe el resultado.")
    p.add_argument("-o", "--output", help="Fichero de salida para --fix (por defecto: stdout).")
    p.add_argument("--indent", type=int, default=2, help="Indentación del JSON corregido.")
    p.add_argument("--no-hints", action="store_true", help="Oculta la línea de pista/evidencia.")
    p.add_argument("--no-color", action="store_true")
    opts = p.parse_args(argv)
    opts.ignore = set(x.strip().upper() for x in opts.ignore.split(",") if x.strip())

    schema_path = find_schema(opts.schema)
    if not schema_path:
        sys.stderr.write("No se encuentra builder-elements/_elements.json. "
                         "Usa --schema RUTA.\n")
        return 3
    with open(schema_path, "r", encoding="utf-8") as fh:
        schema = Schema(json.load(fh))

    if opts.file == "-":
        text, source = sys.stdin.read(), "<stdin>"
    else:
        if not os.path.isfile(opts.file):
            sys.stderr.write("No existe el fichero: %s\n" % opts.file)
            return 3
        with open(opts.file, "r", encoding="utf-8-sig") as fh:
            text = fh.read()
        source = opts.file

    doc, parse_err = load_json(text, source)
    if parse_err:
        if opts.as_json:
            print(json.dumps({"valid": False, "parse_error": parse_err, "issues": []},
                             ensure_ascii=False, indent=2))
        else:
            sys.stderr.write(parse_err + "\n")
        return 3

    v = Validator(schema, opts)
    v.run(doc)
    if opts.fix:
        apply_deep_fixes(doc, schema, v)

    counts = Counter(i.level for i in v.issues)

    if opts.as_json:
        print(json.dumps({
            "source": source,
            "valid": counts[ERROR] == 0,
            "counts": {"error": counts[ERROR], "warning": counts[WARN], "info": counts[INFO]},
            "stats": {k: c for k, c in v.stats.items() if not k.startswith("type_")},
            "types": {k[5:]: c for k, c in v.stats.items() if k.startswith("type_")},
            "fixes": v.fixes,
            "issues": [i.as_dict() for i in v.issues
                       if LEVEL_ORDER[i.level] <= LEVEL_ORDER[opts.level]],
        }, ensure_ascii=False, indent=2))
    else:
        render(v.issues, v.stats, opts, source)
        if opts.fix:
            sys.stderr.write("\n%d correcciones aplicadas.\n" % len(v.fixes))
            for f in v.fixes[:50]:
                sys.stderr.write("  · %s\n" % f)

    if opts.fix:
        payload = json.dumps(doc, ensure_ascii=False,
                             indent=opts.indent if opts.indent > 0 else None)
        if opts.output:
            with open(opts.output, "w", encoding="utf-8") as fh:
                fh.write(payload + "\n")
            sys.stderr.write("Escrito: %s\n" % opts.output)
        else:
            print(payload)

    if counts[ERROR]:
        return 1
    if opts.strict and counts[WARN]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
