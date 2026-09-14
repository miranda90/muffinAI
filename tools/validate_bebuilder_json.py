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
import copy
from functools import lru_cache
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from contracts import inspect_tree, strict_loads, read_json, atomic_json, MAX_BYTES
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
    r"^(#(?:[0-9a-f]{3}|[0-9a-f]{4}|[0-9a-f]{6}|[0-9a-f]{8})"
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
POLICY_CODES = {"E020", "E021", "E022", "E023", "E024", "W002", "W061", "W062", "W050", "W051"}
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
        if not isinstance(data, dict) or not isinstance(data.get("items"), dict) or not data["items"]:
            raise ValueError("Catálogo inválido: items debe ser un objeto no vacío.")
        for key in ("section", "wrap", "advanced"):
            if not isinstance(data.get(key), (list, dict)):
                raise ValueError("Catálogo inválido: falta " + key)
        self.raw = data
        self.aliases = {k: x["type"] for k, x in data["items"].items()
                        if isinstance(x, dict) and x.get("type", k) != k}
        self.item_types = set(data["items"]) - set(self.aliases)
        for alias in self.aliases:
            self.canonical(alias)
        if "render_types" in data and set(data["render_types"]) != self.item_types:
            raise ValueError("El catálogo no coincide con los métodos de render declarados")
        self.inline_shortcodes = set(data.get("inline_shortcodes", {}).keys())
        self.animations = set(data.get("animations", {}).keys())

        self.section = self._index(data.get("section", []))
        self.wrap = self._index(data.get("wrap", []))
        self.advanced = self._index(data.get("advanced", []))

        self.items = {}
        for itype, spec in data.get("items", {}).items():
            if not isinstance(spec, dict): raise ValueError("Definición de item inválida: " + itype)
            idx = self._index(spec.get("attr", []))
            for fid, defs in self.advanced.items():
                idx.setdefault(fid, []).extend(defs)
            self.items[itype] = idx

        # Catálogo global: usado solo para decidir si una clave es "desconocida
        # en este tipo" o "inexistente en todo el theme".
        self.controllers = {}
        for scope_key, index in [("section", self.section), ("wrap", self.wrap), (None, self.advanced), *self.items.items()]:
            mapping = {}
            for key, definitions in index.items():
                for definition in definitions:
                    mapping.setdefault(definition.get("attr_id", key), key)
            self.controllers[scope_key] = mapping

        self.all_ids = set(self.section) | set(self.wrap) | set(self.advanced)
        for idx in self.items.values():
            self.all_ids |= set(idx)

    def canonical(self, itype):
        seen = set()
        while itype in self.aliases:
            if itype in seen:
                raise ValueError("Ciclo de alias: " + itype)
            seen.add(itype)
            itype = self.aliases[itype]
        if itype not in self.item_types:
            raise ValueError("Tipo sin definición canónica: " + str(itype))
        return itype

    def index_for(self, scope, itype=None):
        return self.section if scope == "section" else self.wrap if scope == "wrap" else self.items.get(itype, self.advanced)

    def field(self, scope, itype, key, selector=None):
        defs = self.defs_for(scope, itype, key)
        styled = [d for d in defs if d.get("selector") and d.get("style")]
        if selector is not None:
            styled = [d for d in styled if d["selector"] == selector]
        signatures = {(d["selector"], d["style"], d.get("type"), d.get("version")) for d in styled}
        if len(signatures) != 1:
            raise ValueError("Campo ausente o ambiguo: %s/%s/%s" % (scope, itype, key))
        return styled[0]

    @staticmethod
    def _walk(fields, out):
        """Aplana definiciones, incluidas las anidadas en options/param/form."""
        if isinstance(fields, dict):
            fields = list(fields.values())
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
        defaults = dict(ignore=set(), fix=False, origin="generated", editor="visual", strict=False,
                        exceptions=[], manifest=None, profile=None)
        defaults.update(vars(opts))
        self.o = SimpleNamespace(**defaults)
        self.suppressed = []
        self.issues = []
        self.stats = Counter()
        self.uids = defaultdict(list)
        self.fixes = []
        self.fixed = False

    # -- registro ---------------------------------------------------------- #

    def add(self, level, code, path, msg, hint=""):
        if self.o.origin == "export" and code in POLICY_CODES:
            level = INFO
        issue = Issue(level, code, path, msg, hint)
        if code in self.o.ignore:
            self.suppressed.append(issue)
            return
        for exception in self.o.exceptions:
            if exception.get("code") == code and exception.get("path") == path and exception.get("reason", "").strip():
                if level != ERROR or code in POLICY_CODES:
                    self.suppressed.append(issue)
                    return
        self.issues.append(issue)

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
        try:
            if not getattr(self.o, "checked", False): inspect_tree(doc)
        except ValueError as exc:
            self.err("E000", "$", str(exc))
            return doc
        self.reserved_uids = set()
        stack = [doc]
        while stack:
            value = stack.pop()
            if isinstance(value, dict):
                if isinstance(value.get("uid"), str):
                    self.reserved_uids.add(value["uid"])
                stack.extend(value.values())
            elif isinstance(value, list):
                stack.extend(value)
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

        if attr is not None:
            self.query_post_type(node, attr, path)
        if "items" in node and "wraps" not in node:
            if self.o.origin == "generated":
                self.err("E015", path, "Generar wraps explícitos; la estructura legacy no se entrega.")
            elif isinstance(node["items"], list):
                for i, it in enumerate(node["items"]):
                    self.item(it, "%s.items[%d]" % (path, i))
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
            self.container(node, attr, path)

        items = node.get("items")
        if items is None:
            self.info("I005", path, "Wrap sin `items` (columna vacía).")
        elif not isinstance(items, list):
            self.err("E005", path + ".items", "`items` debe ser un array.")
        else:
            self.queryloop_card(node, attr, items, path, nested)
            for i, it in enumerate(items):
                self.item(it, "%s.items[%d]" % (path, i))

    def queryloop_card(self, node, attr, items, path, nested):
        """Un query loop de WRAP debe contener la tarjeta en UN wrap anidado."""
        if nested or not isinstance(attr, dict):
            return
        if str(attr.get("type", "")) != "query":
            return
        direct = [it for it in items
                  if isinstance(it, dict) and not it.get("item_is_wrap")]
        # Un único item directo sí lo exporta el propio VB (examples/example1/about-us.json
        # $[1].wraps[4]: query loop en slider con un solo `image`). La pérdida medida se da
        # al agrupar varios: ahí el contenedor de iteración se confunde con un nested wrap.
        if len(items) <= 1:
            return
        self.err("E016", path + ".items",
                 "Query loop de wrap con %d items directos: la tarjeta debe ir dentro de "
                 "UN wrap anidado (`item_is_wrap: 1`) o el primer guardado en el VB "
                 "los borra." % len(direct),
                 "Medido en servidor (2026-07-29): importados 53 items con 5 directos en el "
                 "loop, guardados 49 — el wrap del loop quedó con un wrap anidado VACÍO. "
                 "prepareForm.items() (scripts.js:2317-2323) resuelve el contenedor de "
                 "iteración (scripts.js:7364) como nested wrap y pierde los hijos. Sin nodos "
                 "no hay CSS: colores y alturas desaparecen. La forma que el VB exporta es "
                 "wrap query → item_is_wrap:1 → items (examples/example2/home.json).")

    def container(self, node, attr, path):
        self.query_post_type(node, attr, path)
        if "grid" in node:
            self.err("E017", path + ".grid", "grid pertenece a attr, no a la raíz del wrap.")
        for key in ("css_grid_columns", "css_grid_columns_custom", "css_grid_columns_gap", "css_grid_rows_gap"):
            if key in attr and attr.get("grid") != "grid":
                self.warn("W065", path + ".attr." + key, "Campo grid sin attr.grid: grid; no se aplica.")

    # -- query loop: CPTs desactivables ------------------------------------ #

    # Theme Options > Post types permite desactivar estos CPT. Al desactivarlos,
    # functions.php:118-146 deja de hacer `require_once` de su clase, pero los
    # posts siguen en la BD con ese `post_type` y el Visual Builder instancia la
    # clase sin `class_exists()` (visual-builder-class.php:52 y :638).
    MFN_DISABLEABLE_CPT = {
        "portfolio": "Mfn_Post_Type_Portfolio",
        "client": "Mfn_Post_Type_Client",
        "offer": "Mfn_Post_Type_Offer",
        "slide": "Mfn_Post_Type_Slide",
        "testimonial": "Mfn_Post_Type_Testimonial",
        "layout": "Mfn_Post_Type_Layout",
        "template": "Mfn_Post_Type_Template",
    }

    def query_post_type(self, node, attr, path):
        if str(node.get("type", "") or attr.get("type", "")) != "query":
            return
        if str(attr.get("query_type", "")) != "posts":
            return
        cpt = str(attr.get("query_post_type", "") or "")
        if cpt in self.MFN_DISABLEABLE_CPT:
            self.warn("W063", "%s.attr.query_post_type" % path,
                      "El query loop consume el CPT `%s`, que Theme Options puede desactivar." % cpt,
                      "Si está desactivado en el destino: (1) el loop no devuelve nada, y (2) editar "
                      "cualquier post de ese tipo en el Visual Builder provoca un fatal 500 en "
                      "admin-ajax — `new %s()` sin `class_exists()` en visual-builder-class.php:52. "
                      "Comprobar Theme Options > Post types antes de importar (trampa 15)."
                      % self.MFN_DISABLEABLE_CPT[cpt])

    # -- item -------------------------------------------------------------- #

    def item(self, node, path, depth=0):
        if not isinstance(node, dict):
            self.err("E003", path, "El item no es un objeto (es %s)." % type(node).__name__)
            return

        is_wrap = node.get("item_is_wrap") in (1, "1", True, "true")

        if is_wrap:
            self.stats["nested_wraps"] += 1
            if self.o.fix and type(node.get("item_is_wrap")) is not int:
                node["item_is_wrap"] = 1
                self.fix(path, "item_is_wrap normalizado a 1")
            report_nested = self.warn if self.o.editor == "classic" else self.info
            report_nested("W005", path,
                      "`item_is_wrap` (wrap anidado): válido en el Visual Builder, "
                      "pero desactiva BeBuilder Blocks Classic y genera warnings en el builder clásico.",
                      "admin.php:1637-1646 / :833. Evitarlo si la página debe editarse fuera del VB.")
            if depth >= 1:
                self.err("E014", path,
                         "Wrap anidado dentro de otro wrap anidado (nivel %d). El theme solo "
                         "recorre UN nivel de `item_is_wrap`." % (depth + 1),
                         "unique_ID_reset (helper.php:246-282) no regenera los uid más abajo; "
                         "loadExistedElements (visual-builder-class.php:1005) descarta del formulario "
                         "todo hijo sin `type`; MfnLocalCssCompability::nested_wrap "
                         "(local-css-compability.php:365-371) llama a nested_item() sin volver a "
                         "comprobar `item_is_wrap`. Aplanar a un solo nivel.")
            if node.get("type"):
                self.err("E011", path + ".type",
                         "Un wrap anidado (`item_is_wrap: 1`) no debe llevar `type` (tiene \"%s\")."
                         % node.get("type"))
            if not isinstance(node.get("items"), list):
                self.err("E012", path, "`item_is_wrap: 1` sin array `items`.")
            self.node_identity(node, path, "wrap")
            self.sizes(node, path, SIZES, required=True, kind="item")
            attr = self.attr(node, path, "wrap", None)
            if attr is not None:
                self.container(node, attr, path)
            if not isinstance(node.get("items"), list):
                return
            if depth >= 1:
                return
            for i, it in enumerate(node["items"]):
                self.item(it, "%s.items[%d]" % (path, i), depth + 1)
            return

        self.stats["items"] += 1
        itype = node.get("type")

        if not itype:
            self.err("E009", path,
                     "Item sin `type` y sin `item_is_wrap: 1`: el front lo descarta (front.php:2606).")
            itype = None
        elif not isinstance(itype, str):
            self.err("E010", path + ".type", "`type` debe ser string (es %s)." % type(itype).__name__)
            itype = None
        elif itype in self.s.aliases:
            canonical = self.s.canonical(itype)
            self.err("E018", path + ".type", "Alias %s no renderizable; generar type: %s." % (itype, canonical))
            itype = UNKNOWN_TYPE
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
                candidate, suffix = self.gen_uid(path), 0
                while candidate in self.reserved_uids:
                    suffix += 1
                    candidate = self.gen_uid(path + ":" + str(suffix))
                node["uid"] = candidate
                self.reserved_uids.add(candidate)
                self.uids[candidate].append(path)
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

        identity = kind
        spec = {}
        if kind == "item" and isinstance(node.get("type"), str) and node["type"] in self.s.item_types:
            identity = node["type"]
            spec = self.s.raw["items"][identity]
        for key, default in (("icon", spec.get("icon", identity)), ("jsclass", identity),
                             ("title", spec.get("title", identity.replace("_", " ").title()))):
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
        elif not isinstance(size, str) or size not in allowed:
            self.err("E008", path + ".size",
                     "`size: %r` inválido." % size,
                     "Válidos: %s%s." % (", ".join(sorted(SIZES)),
                                         " y \"divider\" (solo wrap)" if kind == "wrap" else ""))

        for key in ("tablet_size", "mobile_size", "laptop_size"):
            val = node.get(key)
            if val is None:
                if key in ("tablet_size", "mobile_size"):
                    if self.o.fix and isinstance(size, str) and size in allowed:
                        node[key] = size if key == "tablet_size" else "1/1"
                        self.fix(path, "%s=\"%s\" añadido" % (key, node[key]))
                    else:
                        self.warn("W002", path,
                                  "Sin `%s` (fallback implícito: %s): el responsive debe ser "
                                  "explícito." % (key, "= size" if key == "tablet_size" else '"1/1"'),
                                  "Regla 5 del proyecto (05-reglas-y-trampas.md §1). "
                                  "`--fix` lo añade automáticamente.")
            elif not isinstance(val, str) or val not in allowed:
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
                if isinstance(value, dict) and any(k in value for k in ("selector", "style", "val")):
                    self.css_field(key, value, [], {}, kpath)
                continue

            self.value(key, value, defs, kpath, scope, itype)

        self.consistency(attr, apath, scope, itype)
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
        matching = [d for d in styled if isinstance(value, dict) and
                    d["selector"] == value.get("selector") and d["style"] == value.get("style")]
        primary = matching[0] if matching else styled[0] if styled else defs[0]

        if isinstance(value, dict) and ("selector" in value or "style" in value or "val" in value):
            self.css_field(key, value, defs, primary, kpath)
            return

        if styled:
            if value not in (None, "", {}, []):
                declared = self.declared_options(styled)
                if self.o.origin == "export" and isinstance(value, str) and value in declared:
                    # El VB exporta el select sin tocar como string plano (su `std`): no genera
                    # CSS y el theme aplica su propio valor por defecto. En generación sigue
                    # siendo error porque el objeto css_* es la única forma de emitir la regla.
                    self.info("I034", kpath, "Select de estilo exportado como valor plano (default del VB); no genera CSS.")
                else:
                    self.err("E034", kpath, "Campo CSS sin objeto selector/style/val; no genera CSS.")
            return

        if isinstance(value, (list, dict)):
            self.structured_content(value, primary, kpath)
            return
        if value is not None and not isinstance(value, str):
            self.warn("W066", kpath, "Campo de contenido debe ser string o estructura declarada.")

        if isinstance(value, str):
            self.string_content(value, kpath)
            enum_checked = self.options(value, defs, kpath, key)
            self.special_plain(key, value, kpath, enum_checked)

    def structured_content(self, value, definition, path):
        if definition.get("type") == "tabs" and not isinstance(value, list):
            self.err("E038", path, "Un repetidor tabs requiere un array de objetos.")
            return
        if definition.get("type") == "tabs" and any(not isinstance(x, dict) for x in value):
            self.err("E038", path, "Cada fila tabs debe ser un objeto.")
        stack = [(value, path)]
        while stack:
            obj, here = stack.pop()
            if isinstance(obj, str):
                self.string_content(obj, here)
            elif isinstance(obj, dict):
                if any(k in obj for k in ("selector", "style", "val")) and "selector" in obj:
                    self.css_field("nested", obj, [], {}, here)
                else:
                    stack.extend((v, here + "." + k) for k, v in obj.items())
            elif isinstance(obj, list):
                stack.extend((v, "%s[%d]" % (here, i)) for i, v in enumerate(obj))

    @staticmethod
    def zero_values(val, path):
        """Rutas de `val` cuyo valor es "0"/0 — descartado por `empty()` en el helper."""
        if val in ("0", 0):
            return [path]
        if isinstance(val, dict):
            out = []
            for k, v in val.items():
                out.extend(Validator.zero_values(v, "%s.%s" % (path, k)))
            return out
        return []

    def css_field(self, key, value, defs, primary, kpath):
        selector = value.get("selector")
        style = value.get("style")
        val = value.get("val")
        if not isinstance(selector, str) or not isinstance(style, str):
            self.err("E030", kpath, "selector y style deben ser strings no vacíos.")
            return
        if not style or not re.fullmatch(r"(?:--)?[a-zA-Z_][a-zA-Z0-9_-]*", style):
            self.err("E030", kpath + ".style", "Propiedad CSS vacía o inválida.")
            return
        if isinstance(val, (list, bool)):
            self.err("E039", kpath + ".val", "Valor CSS debe ser string, número o mapa de dispositivos.")
            return

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
        # Se comprueba también dentro de `val` (breakpoints y lados de un dimensions):
        # `mfnLocalStyle` recibe cada lado por separado y devuelve array() si es "0".
        emitted = value.get("val")
        if any(kind in style for kind in ("transform", "gradient", "filter")):
            def strings_only(obj):
                if not isinstance(obj, dict): return obj
                return {k: strings_only(v) for k, v in obj.items() if k in DEVICE_SET or k == "string"}
            emitted = strings_only(emitted)
        for zpath in self.zero_values(emitted, kpath + ".val"):
            self.warn("W039", zpath,
                      "valor \"0\": PHP `empty()` lo trata como vacío y NO genera CSS "
                      "(queda el valor por defecto del theme).",
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

            if any("mfnuidelement" not in part for part in selector.split(",")):
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
                          "(difieren solo espacios o la notación de pseudoclases).")

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
        if isinstance(v, (list, bool)):
            self.err("E039", path, "Hoja CSS de tipo inválido.")
            return

        # ---- dimensions: las dos gramáticas incompatibles (trampa 14)
        if ftype == "dimensions":
            separated = fdef.get("version") == "separated-fields"
            if isinstance(v, dict):
                if not separated:
                    recognized = set(v) <= (SIDES | {"top-left", "top-right", "bottom-right", "bottom-left"})
                    complete = set(v) == SIDES or (style == "border-radius" and set(v) == {"top-left", "top-right", "bottom-right", "bottom-left"})
                    if self.o.fix and recognized and complete and all(isinstance(x, (str, int, float)) and not isinstance(x, bool) for x in v.values()):
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
                            if not isinstance(sv, (str, int, float)) or isinstance(sv, bool):
                                self.err("E039", path + "." + side, "Dimensión debe ser escalar.")
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
            if not isinstance(v.get("string"), str) or not v["string"]:
                self.err("E036", path,
                         "`%s` sin subclave `string` (o vacía): el helper descarta el resto "
                         "de subclaves y no emite nada." % key,
                         "Ej.: {\"type\":\"linear\",...,"
                         "\"string\":\"linear-gradient(180deg,#000 0%,#fff 100%)\"}")
            elif ftype == "transform" or style == "transform":
                serial = v["string"]
                if not isinstance(serial, str) or not re.fullmatch(r"\s*-?(?:\d+(?:\.\d*)?|\.\d+)(?:\s*,\s*-?(?:\d+(?:\.\d*)?|\.\d+)){6}\s*", serial):
                    self.err("E040", path, "Transform string requiere siete números CSV (a,b,c,d,tx,ty,rotate), sin matrix().")
                else:
                    keys = ("scaleX", "skewY", "skewX", "scaleY", "translateX", "translateY", "rotate")
                    for key2, number in zip(keys, serial.split(",")):
                        try:
                            consistent = key2 in v and float(v[key2]) == float(number)
                        except (ValueError, TypeError):
                            consistent = False
                        if not consistent:
                            self.err("E040", path + "." + key2, "Parámetro editable ausente o incoherente con string.")
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
                    if not isinstance(v2, (str, int, float)) or isinstance(v2, bool):
                        self.err("E039", path + "." + k2, "Propiedad tipográfica debe ser escalar.")
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
        if isinstance(v, dict):
            self.err("E039", path, "Este campo CSS requiere un valor escalar, no subpropiedades.")
            return
        if isinstance(v, (int, float)):
            self.unit(str(v), style, path)
        if isinstance(v, str):
            self.options(v, [fdef], path, key)
            if style:
                self.unit(v, style, path)
            if re.search(r"[;{}]", v) and style not in ("--mfn-custom", None):
                self.warn("W047", path, "El valor contiene `;` o `{}`: puede romper la regla CSS generada.")

    # -- utilidades de valor ------------------------------------------------ #

    def declared_options(self, defs):
        """Claves de enum estático declaradas por un campo select/switch (sin listas dinámicas)."""
        keys = set()
        for d in defs:
            opts = d.get("options")
            if not isinstance(opts, dict) or d.get("type") not in ("switch", "select", "radio_img"):
                continue
            if any(x is not None for x in (d.get("php_options"), d.get("themeoptions"), d.get("dynamic_data"))):
                continue
            if any(isinstance(x, dict) for x in opts.values()):
                continue
            keys.update(map(str, opts.keys()))
        return keys

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

    def consistency(self, attr, apath, scope, itype=None):
        index = self.s.index_for(scope, itype)
        controllers = self.s.controllers.get(scope if scope != "item" else itype, {})
        def evaluate(condition):
            if isinstance(condition, dict) and "id" in condition:
                key = controllers.get(condition["id"])
                if key is None:
                    return None
                if key not in attr:
                    return None
                expected, actual = condition.get("val"), attr[key]
                op = condition.get("opt", "is")
                if op == "is": return actual == expected
                if op == "isnt": return actual != expected
                return None
            if isinstance(condition, (list, dict)):
                parts = list(condition.values()) if isinstance(condition, dict) else condition
                operator = parts[0] if parts and isinstance(parts[0], str) else "AND"
                values = [evaluate(x) for x in parts if isinstance(x, (dict, list))]
                if not values: return None
                if operator == "OR":
                    return True if True in values else None if None in values else False
                return False if False in values else None if None in values else True
            return None
        for key, value in attr.items():
            if value in (None, "", {}, []): continue
            if key == "css_advanced_background_color" and attr.get("background_switcher") == "video":
                continue  # color de respaldo del vídeo: el panel lo oculta pero el helper lo emite (trampa 25, tests/php)
            defs = index.get(key, [])
            if isinstance(value, dict) and value.get("selector"):
                defs = [d for d in defs if d.get("selector") == value["selector"]] or defs
            conditions = [d.get("condition") for d in defs]
            if not conditions or any(not c for c in conditions): continue
            states = [evaluate(c) for c in conditions]
            if True in states: continue
            if None in states:
                self.warn("W050", apath + "." + key, "Condición del panel no resuelta; declarar sus controles explícitos.")
            else:
                self.warn("W051", apath + "." + key, "Campo oculto por sus condiciones del catálogo; comprobar intención.")

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
        # Conservatively preserve all combinators and internal whitespace.
        return (sel or "").strip().replace("|", ":")

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
        return strict_loads(text), None
    except json.JSONDecodeError as e:
        lines = text.splitlines()
        ctx = lines[e.lineno - 1] if 0 < e.lineno <= len(lines) else ""
        pointer = " " * max(e.colno - 1, 0) + "^"
        return None, ("%s: JSON no parseable — %s (línea %d, columna %d)\n    %s\n    %s"
                      % (source, e.msg, e.lineno, e.colno, ctx[:200], pointer[:200]))
    except (ValueError, RecursionError) as e:
        return None, "%s: %s" % (source, e)


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


@lru_cache(maxsize=4)
def _cached_schema(path, mtime, size):
    return Schema(read_json(path))


def load_schema(path=None):
    path = Path(find_schema(path))
    stat = path.stat()
    return _cached_schema(str(path.resolve()), stat.st_mtime_ns, stat.st_size)


def validate(document, schema=None, *, origin="generated", editor="visual", strict=False,
             fix=False, ignore=(), exceptions=(), manifest=None, profile=None):
    """Pure public API: never changes the caller's document or writes files."""
    inspect_tree(document)
    if origin not in ("generated", "export") or editor not in ("visual", "classic"):
        raise ValueError("Perfil de validación desconocido.")
    if not isinstance(exceptions, (list, tuple)) or any(
        not isinstance(x, dict) or not all(isinstance(x.get(k), str) and x[k].strip()
                                          for k in ("code", "path", "reason")) for x in exceptions):
        raise ValueError("Excepciones requieren code, path y reason no vacíos.")
    schema = schema or load_schema()
    opts = SimpleNamespace(origin=origin, editor=editor, strict=strict, fix=fix,
                           ignore=set(ignore), exceptions=list(exceptions), manifest=manifest, profile=profile, checked=True)
    working = copy.deepcopy(document)
    v = Validator(schema, opts)
    v.run(working)
    fixes = list(v.fixes)
    if fix:
        apply_deep_fixes(working, schema, v)
        opts.fix = False
        v = Validator(schema, opts)
        v.run(working)
    from project_checks import check_project
    check_project(working, v)
    counts = Counter(i.level for i in v.issues)
    structural = [i for i in v.issues + v.suppressed if i.level == ERROR and i.code not in POLICY_CODES]
    exit_code = 1 if counts[ERROR] or structural else 2 if strict and counts[WARN] else 0
    return {
        "valid": counts[ERROR] == 0 and not structural,
        "structurally_valid": not structural,
        "accepted": exit_code == 0,
        "exit_code": exit_code,
        "origin": origin, "editor": editor,
        "counts": {level: counts[level] for level in (ERROR, WARN, INFO)},
        "stats": {k: c for k, c in v.stats.items() if not k.startswith("type_")},
        "types": {k[5:]: c for k, c in v.stats.items() if k.startswith("type_")},
        "fixes": fixes, "issues": [i.as_dict() for i in v.issues],
        "suppressed": [i.as_dict() for i in v.suppressed],
        "document": working,
    }


def main(argv=None):
    p = argparse.ArgumentParser(description="Valida BeBuilder sin modificar el original.")
    p.add_argument("file", help="JSON de entrada o - para stdin")
    p.add_argument("--schema")
    p.add_argument("--json", action="store_true", dest="as_json")
    p.add_argument("--level", choices=[ERROR, WARN, INFO], default=INFO)
    p.add_argument("--strict", action="store_true")
    p.add_argument("--origin", choices=["generated", "export"], default="generated")
    p.add_argument("--editor", choices=["visual", "classic"], default="visual")
    p.add_argument("--manifest")
    p.add_argument("--profile")
    p.add_argument("--exceptions", help="Array JSON de {code,path,reason}")
    p.add_argument("--ignore", default="")
    p.add_argument("--max-issues", type=int, default=200)
    p.add_argument("--max-per-code", type=int, default=5)
    p.add_argument("--fix", action="store_true")
    p.add_argument("-o", "--output")
    p.add_argument("--indent", type=int, default=2)
    p.add_argument("--no-hints", action="store_true")
    p.add_argument("--no-color", action="store_true")
    opts = p.parse_args(argv)
    try:
        if opts.output and not opts.fix:
            raise ValueError("--output requiere --fix.")
        if min(opts.max_issues, opts.max_per_code, opts.indent) < 0:
            raise ValueError("Límites e indentación deben ser no negativos.")
        if opts.output and opts.file != "-" and Path(opts.output).resolve() == Path(opts.file).resolve():
            raise ValueError("La salida debe ser distinta del original.")
        schema_path = find_schema(opts.schema)
        if not schema_path:
            raise ValueError("No se encuentra el catálogo.")
        schema = load_schema(schema_path)
        document = strict_loads(sys.stdin.read(MAX_BYTES + 1)) if opts.file == "-" else read_json(opts.file)
        result = validate(document, schema, origin=opts.origin, editor=opts.editor, strict=opts.strict,
                          fix=opts.fix, ignore=[x.strip().upper() for x in opts.ignore.split(",") if x.strip()],
                          exceptions=read_json(opts.exceptions) if opts.exceptions else [],
                          manifest=read_json(opts.manifest) if opts.manifest else None,
                          profile=read_json(opts.profile) if opts.profile else None)
        result["source"] = opts.file
        # A rejected repair remains reviewable on stdout, but never replaces a file.
        if opts.output and result["accepted"]:
            atomic_json(opts.output, result["document"], opts.indent or None)
        if opts.as_json:
            if not opts.fix: result.pop("document")
            print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
        else:
            issues = [Issue(i["level"], i["code"], i["path"], i["message"], i.get("hint", "")) for i in result["issues"]]
            with redirect_stdout(sys.stderr if opts.fix else sys.stdout):
                render(issues, Counter(result["stats"]), opts, opts.file)
                print("Aceptado: %s (exit %d)" % (result["accepted"], result["exit_code"]))
            if opts.fix and not opts.output:
                print(json.dumps(result["document"], ensure_ascii=False, indent=opts.indent or None, allow_nan=False))
        return result["exit_code"]
    except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError) as exc:
        error = {"valid": False, "structurally_valid": False, "accepted": False,
                 "exit_code": 3, "parse_error": str(exc), "issues": []}
        if opts.as_json: print(json.dumps(error, ensure_ascii=False))
        else: print(str(exc), file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
