# -*- coding: utf-8 -*-
"""Núcleo compartido para scripts build_*.py de BeBuilder.

Extraído de los helpers que se repetían idénticos en los siete scripts del taller
(nordes, maderas, wat). Los scripts existentes NO lo usan (quedan congelados tal
cual generaron sus páginas); los nuevos arrancan de proyectos/_plantilla/.

Uso desde proyectos/<cliente>/build_x.py:

    import sys
    from pathlib import Path
    HERE = Path(__file__).resolve().parent
    sys.path.insert(0, str(HERE.parents[1] / "tools"))
    from mfn import *  # o import explícito

Los tokens del proyecto (colores, MEDIA, MAXW) se definen en cada script:
son del diseño, no del theme.
"""

__all__ = [
    "S_SECTION", "S_SECT_WRAP", "S_SECT_MAXW", "S_WRAP", "S_WRAP_IN",
    "S_ITEM", "S_ITEM_IN", "S_TITLE", "S_TITLE_C", "S_DESC", "S_DESC_C",
    "S_BUTTON", "S_IMGFRAME", "S_IMGCOVER",
    "uid", "uid_reset", "css", "typo", "pad", "m0",
    "section", "wrap", "nested", "item", "sec_base",
    "load_manifest", "media",
]

import json
from copy import deepcopy
from contextvars import ContextVar
from dataclasses import dataclass, field as dataclass_field
from functools import lru_cache, wraps as functools_wraps
from contracts import read_json, validate_manifest, BREAKPOINTS
from pathlib import Path

# ---------------------------------------------------------------- selectores base
# Placeholders del CSS pipeline (docs/bebuilder/02): mfnuidelement se sustituye
# por el uid del nodo al generar post-{ID}.css.
S_SECTION   = ".mcb-section-mfnuidelement"
S_SECT_WRAP = ".mcb-section-mfnuidelement .section_wrapper"
S_SECT_MAXW = ".mcb-section-mfnuidelement.custom-width .section_wrapper"
S_WRAP      = ".mcb-section .mcb-wrap-mfnuidelement"
S_WRAP_IN   = ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner"
S_ITEM      = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement"
S_ITEM_IN   = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner"
S_TITLE     = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title"
S_TITLE_C   = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title,"
               ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title a")
S_DESC      = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc"
S_DESC_C    = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc,"
               ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc a")
S_BUTTON    = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button"
S_IMGFRAME  = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame"
S_IMGCOVER  = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement "
               ".image_frame.mfn-coverimg .image_wrapper img")

# ---------------------------------------------------------------- constructores
_n = [0]
_active = ContextVar("muffin_build_context", default=None)


def uid(prefix):
    """uid secuencial determinista (el import del VB los regenera igualmente)."""
    context = _active.get()
    if context is not None:
        return context.next_uid(prefix)
    _n[0] += 1
    return "{}{:06d}".format(prefix, _n[0])


def uid_reset():
    _n[0] = 0


def css(selector, style, val):
    if not isinstance(selector, str) or not selector or not isinstance(style, str) or not style:
        raise ValueError("selector/style deben ser strings no vacíos")
    return {"selector": selector, "style": style, "val": normalize_zero(deepcopy(val), style)}


def typo(sel, desktop, tablet=None, mobile=None):
    val = {"desktop": desktop}
    if tablet is not None:
        val["tablet"] = tablet
    val["mobile"] = deepcopy(desktop if mobile is None else mobile)
    return css(sel, "typography", val)


def _no_zero(side_vals):
    """PHP `empty()` descarta "0": se escribe "0px" para que el helper emita la regla."""
    return {k: ("0px" if v in ("0", 0) else v) for k, v in side_vals.items()}


def pad(desktop, tablet=None, mobile=None):
    """Todo espaciado lleva valor mobile; si el diseño no pide otro, replica desktop."""
    val = {"desktop": _no_zero(desktop)}
    if tablet is not None:
        val["tablet"] = _no_zero(tablet)
    val["mobile"] = _no_zero(desktop if mobile is None else mobile)
    return val


def m0(bottom="0", mobile_bottom=None):
    """Margen del item: anula el default del theme (12px laterales, 40px abajo)."""
    return css(S_ITEM_IN, "margin",
               pad({"top": "0", "right": "0", "bottom": bottom, "left": "0"}, None,
                   {"top": "0", "right": "0", "bottom": bottom if mobile_bottom is None else mobile_bottom, "left": "0"}))


def section(attr, wraps, title="Section", ver="default"):
    return {"uid": uid("sec"), "icon": "section", "jsclass": "section",
            "title": title, "ver": ver, "attr": attr, "wraps": wraps}


def wrap(attr, items, size="1/1", tablet=None, mobile="1/1", title="Wrap"):
    return {"uid": uid("wrp"), "icon": "wrap", "jsclass": "wrap", "title": title,
            "size": size, "tablet_size": tablet or size, "mobile_size": mobile,
            "attr": attr, "items": items}


def nested(attr, items, size="1/1", tablet=None, mobile="1/1", title="Wrap"):
    """Wrap anidado (item_is_wrap). Un solo nivel: trampa 16."""
    return {"uid": uid("itm"), "icon": "wrap", "jsclass": "wrap", "title": title,
            "item_is_wrap": 1,
            "size": size, "tablet_size": tablet or size, "mobile_size": mobile,
            "attr": attr, "items": items}


def item(itype, attr, size="1/1", tablet=None, mobile="1/1", title=None, icon=None):
    return {"uid": uid("itm"), "type": itype, "jsclass": itype,
            "title": title or itype.replace("_", " ").title(), "icon": icon or itype,
            "size": size, "tablet_size": tablet or size, "mobile_size": mobile,
            "attr": attr}


def load_manifest(path):
    """assets/manifest.json → {nombre: {"id", "url", ...}} (doc 09 §3.3).

    Devuelve {} si no existe todavía, para que el script arranque antes de subir
    los medios; media() avisará entonces de cada fichero que falte.
    """
    path = Path(path)
    if not path.exists():
        return {}
    return validate_manifest(read_json(path), root=path.parent)


def media(manifest, name):
    """URL#ID del medio, formato del export real del VB (doc 09 §4).

    Con #ID el theme sirve la imagen por wp_get_attachment_image (srcset, alt,
    dimensiones); sin él cae a <img> crudo. KeyError = medio no subido: se sube,
    no se inventa la URL.
    """
    validate_manifest(manifest)
    try:
        m = manifest[name]
    except KeyError:
        raise KeyError("medio '{}' no está en assets/manifest.json: subirlo antes "
                       "(docs/bebuilder/09-medios-imagenes-video.md)".format(name))
    return "{}#{}".format(m["url"], m["id"])


def sec_base(pad_val, maxw=None, extra=None):
    """Sección con padding del diseño y, si se pasa maxw, contenedor interior custom."""
    attr = {"css_advanced_padding": css(S_SECTION, "padding", pad_val)}
    if maxw is not None:
        attr["width_switcher"] = "custom"
        attr["css_advanced_max_width"] = css(S_SECT_MAXW, "max-width", maxw)
    else:
        attr["width_switcher"] = "full"
    if extra:
        attr.update(extra)
    return attr


def catalog():
    """One catalog per process; maintenance commands use fresh processes."""
    from validate_bebuilder_json import load_schema
    return load_schema()


def normalize_zero(value, style):
    if isinstance(value, dict):
        return {key: normalize_zero(val, key if style == "typography" and key not in
                                    ("desktop", "laptop", "tablet", "mobile") else style)
                for key, val in value.items()}
    if isinstance(value, bool):
        raise ValueError("Booleano no es un valor CSS")
    if value in (0, "0"):
        from validate_bebuilder_json import STYLES_NEED_UNIT
        return "0px" if style in STYLES_NEED_UNIT else "+0" if style in ("z-index", "order") else "0.0"
    return value


def style_field(scope, key, value, *, itype=None, selector=None):
    schema = catalog()
    if itype is not None: itype = schema.canonical(itype)
    definition = schema.field(scope, itype, key, selector)
    return css(definition["selector"], definition["style"], value)


def transform(*, scale_x=1, scale_y=1, skew_x=0, skew_y=0, x=0, y=0, rotate=0):
    """BeBuilder stores seven CSV numbers, not a CSS matrix() string."""
    import math
    values = (scale_x, skew_y, skew_x, scale_y, x, y, rotate)
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in values):
        raise ValueError("Transform requiere siete números finitos")
    result = dict(zip(("scaleX", "skewY", "skewX", "scaleY", "translateX", "translateY", "rotate"), values))
    result["string"] = ",".join(format(v, ".12g") for v in values)
    return result


def px_to_rem(value, root_px):
    if root_px <= 0: raise ValueError("La raíz tipográfica debe ser positiva")
    return "%grem" % (value / root_px)


@dataclass
class BuildContext:
    profile: dict = dataclass_field(default_factory=dict)
    manifest: dict = dataclass_field(default_factory=dict)
    tokens: dict = dataclass_field(default_factory=dict)
    design: dict = dataclass_field(default_factory=lambda: {"source": {}, "blocks": []})
    exceptions: list = dataclass_field(default_factory=list)
    _counter: int = 0
    _token: object = None

    def __enter__(self):
        if self._token is not None: raise ValueError("Contexto ya activo")
        self._counter = 0
        self._token = _active.set(self)
        return self

    def __exit__(self, *exc):
        _active.reset(self._token)
        self._token = None

    def next_uid(self, prefix):
        self._counter += 1
        return "%s%06d" % (prefix, self._counter)

    def bind(self, block_id, nodes, *, evidence="measured", responsive=None, exception=None):
        """Sidecar correspondence, never serialized inside BeBuilder attr."""
        if evidence not in ("measured", "inferred", "pending"):
            raise ValueError("evidence debe ser measured/inferred/pending")
        existing = next((x for x in self.design["blocks"] if x["id"] == block_id), None)
        if existing and existing.get("uids"):
            raise ValueError("Bloque de diseño ya asignado: " + block_id)
        if isinstance(nodes, dict): nodes = [nodes]
        record = {"id": block_id, "uids": [x["uid"] for x in nodes], "evidence": evidence,
                  "responsive": responsive or {}, "exception": exception}
        if existing is not None:
            existing.update(record)
        else:
            self.design["blocks"].append(record)
        return nodes

    def media(self, name):
        return media(self.manifest, name)

    def style(self, scope, key, value, *, itype=None, selector=None):
        return style_field(scope, key, value, itype=itype, selector=selector)


def _checked_constructor(function):
    @functools_wraps(function)
    def build(*args, **kwargs):
        from validate_bebuilder_json import SIZES, SIZES_WRAP
        node = function(*args, **kwargs)
        if not isinstance(node["attr"], dict): raise ValueError("attr debe ser objeto")
        if "wraps" in node:
            if not isinstance(node["wraps"], list): raise ValueError("wraps debe ser array")
        else:
            allowed = SIZES_WRAP if node.get("jsclass") == "wrap" and not node.get("item_is_wrap") else SIZES
            for key in ("size", "tablet_size", "mobile_size"):
                if not isinstance(node[key], str) or node[key] not in allowed:
                    raise ValueError("%s inválido: %r" % (key, node[key]))
        if "items" in node and not isinstance(node["items"], list): raise ValueError("items debe ser array")
        if node.get("item_is_wrap") and any(isinstance(x, dict) and x.get("item_is_wrap") for x in node["items"]):
            raise ValueError("Solo se admite un nivel de nested wrap")
        if "type" in node:
            schema = catalog()
            original = node["type"]
            canonical = schema.canonical(original)
            node["type"] = node["jsclass"] = canonical
            if original != canonical:
                spec = schema.raw["items"][original]
                node["icon"] = spec.get("icon", canonical)
                node["title"] = spec.get("title", node["title"])
        return deepcopy(node)
    return build


section = _checked_constructor(section)
wrap = _checked_constructor(wrap)
nested = _checked_constructor(nested)
item = _checked_constructor(item)

__all__ += ["BuildContext", "catalog", "style_field", "transform", "px_to_rem", "BREAKPOINTS"]
