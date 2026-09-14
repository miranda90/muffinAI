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


# ---------------------------------------------------------------- API compacta
# Cada kwarg es un campo del catálogo (con o sin prefijo css_/css_advanced_).
# Selector y style salen del catálogo; el valor se normaliza según el tipo del
# campo; los switchers que condicionan el campo (background_switcher, grid,
# image_height, full_width, width/height_switcher…) se declaran solos.
_DEVICES = ("desktop", "laptop", "tablet", "mobile")
_RE_PX = __import__("re").compile(r"^(-?\d*\.?\d+)px$")
_RE_TOKEN = __import__("re").compile(r"[^\s(]+\([^)]*\)|\S+")
_PASS_TYPES = {"color", "gradient", "transform", "box_shadow", "backdrop_filter", "text_shadow"}


def _root_px():
    context = _active.get()
    root = context.profile.get("root_font_px") if context is not None else None
    return root or 16


def _rem(value):
    """px → rem (regla 6). Números = px. Otras unidades y palabras pasan tal cual."""
    if isinstance(value, bool):
        raise ValueError("Booleano no es un espaciado")
    if isinstance(value, (int, float)):
        value = "%gpx" % value
    if isinstance(value, str):
        match = _RE_PX.match(value.strip())
        if match:
            n = float(match.group(1))
            return "0" if n == 0 else "%grem" % round(n / _root_px(), 4)
    return value


def _sides(value):
    """'16px 0' | 16 | (t, r, b, l) | {'top':…} → dict de lados en orden CSS."""
    if isinstance(value, dict):
        return dict(value)
    if isinstance(value, (int, float)):
        value = (value,)
    elif isinstance(value, str):
        value = _RE_TOKEN.findall(value)  # calc(100% - 2rem) es un solo valor
    parts = list(value)
    if len(parts) == 1:
        parts = parts * 4
    elif len(parts) == 2:
        parts = [parts[0], parts[1], parts[0], parts[1]]
    elif len(parts) == 3:
        parts = [parts[0], parts[1], parts[2], parts[1]]
    elif len(parts) != 4:
        raise ValueError("Espaciado con %d valores; se admiten 1-4" % len(parts))
    return dict(zip(("top", "right", "bottom", "left"), parts))


def _devices(value):
    if isinstance(value, dict) and value and set(value) <= set(_DEVICES):
        return deepcopy(value)
    return {"desktop": value}


def _with_mobile(devices):
    """Regla 5: mobile replica desktop si falta. Sin desktop (solo laptop/tablet) se respeta tal cual."""
    if "desktop" in devices:
        devices.setdefault("mobile", deepcopy(devices["desktop"]))
    return devices


def _unit(value, unit):
    return "%g%s" % (value, unit) if isinstance(value, (int, float)) and not isinstance(value, bool) and unit else value


def _norm(definition, value):
    style, ftype = definition.get("style"), definition.get("type")
    if ftype == "dimensions" and definition.get("version") == "separated-fields":
        out = {d: _no_zero({k: _rem(x) for k, x in _sides(v).items()}) for d, v in _devices(value).items()}
        return _with_mobile(out)
    if ftype == "dimensions":  # border-width / border-radius: string shorthand (trampa 14)
        return {d: " ".join(str(_unit(x, "px")) for x in _sides(v).values())
                for d, v in _devices(value).items()}
    if ftype == "typography_vb" or style == "typography":
        return _with_mobile(_devices(value))
    if ftype in _PASS_TYPES or not definition.get("responsive"):
        return value
    param = definition.get("param") if isinstance(definition.get("param"), dict) else {}
    unit = definition.get("default_unit") or param.get("unit")
    out = {d: _unit(v, unit) for d, v in _devices(value).items()}
    return _with_mobile(out) if style == "font-size" else out


def _conditions(definition):
    condition = definition.get("condition")
    if isinstance(condition, dict):
        return [condition]
    if isinstance(condition, list) and (not condition or condition[0] == "AND" or isinstance(condition[0], dict)):
        return [c for c in condition if isinstance(c, dict)]
    return []


def A(scope, itype=None, **fields):
    """attr de sección/wrap/item a partir de kwargs con nombres del catálogo."""
    import difflib
    schema = catalog()
    if scope == "item":
        itype = schema.canonical(itype)
        index, controllers = schema.items[itype], schema.controllers.get(itype, {})
    elif scope in ("section", "wrap"):
        index, controllers = schema.index_for(scope), schema.controllers.get(scope, {})
    else:
        raise ValueError("scope debe ser section/wrap/item")
    from validate_bebuilder_json import LEGACY_SECTION, LEGACY_WRAP, LEGACY_ITEM
    legacy = {"section": LEGACY_SECTION, "wrap": LEGACY_WRAP, "item": LEGACY_ITEM}[scope]
    attr, pending = {}, []
    for key, value in fields.items():
        candidates = [c for c in (key, "css_" + key, "css_advanced_" + key, "css__" + key) if c in index]
        # Campos legacy planos (wrap.padding, section.background_color…) no tapan al css_*.
        resolved = next((c for c in candidates if any(d.get("selector") and d.get("style") for d in index[c])),
                        candidates[0] if candidates else None)
        if resolved in legacy:  # padding/align/bg_color… sin variante css_*: el front los vuelca como style inline
            raise ValueError("Campo legacy '%s' (%s): usar el css_* equivalente (python3 tools/fields.py %s)"
                             % (key, scope, itype or scope))
        if resolved is None:
            near = difflib.get_close_matches(key, [k.replace("css_advanced_", "").replace("css_", "") for k in index], 3, 0.6)
            raise ValueError("Campo '%s' no existe en %s%s; parecidos: %s" % (key, scope, "/" + itype if itype else "", ", ".join(near) or "ninguno"))
        definitions = index[resolved]
        styled = [d for d in definitions if d.get("selector") and d.get("style")]
        if styled:
            signatures = {(d["selector"], d["style"]) for d in styled}
            if len(signatures) != 1:
                raise ValueError("Campo ambiguo '%s': usar style_field() con selector explícito" % resolved)
            definition = styled[0]
            prebuilt = isinstance(value, dict) and {"selector", "style", "val"} <= set(value)
            attr[resolved] = value if prebuilt else css(definition["selector"], definition["style"], _norm(definition, value))
        else:  # campo de contenido/switch: el theme guarda strings ("1", "120")
            attr[resolved] = str(value) if isinstance(value, (int, float)) and not isinstance(value, bool) else value
        if value not in (None, "", {}, []):
            pending.extend(_conditions(d) for d in definitions)
    for conditions in pending:  # switchers del panel: trampa 19 y afines
        for condition in conditions:
            if condition.get("opt", "is") != "is" or "val" not in condition:
                continue  # "isnt"/OR no fijan un valor concreto: el validador (W050) lo señala
            controller = controllers.get(condition["id"], condition["id"])
            attr.setdefault(controller, condition["val"])
    return attr


def _cols(cols):
    """"1/2" | ("1/2",) → desktop=tablet, mobile 1/1; ("1/3", "1/2") → mobile 1/1; tres → tal cual."""
    cols = (cols,) if isinstance(cols, str) else tuple(cols)
    if len(cols) == 1:
        cols = (cols[0], cols[0])
    if len(cols) == 2:
        cols = cols + ("1/1",)
    if len(cols) != 3:
        raise ValueError("cols admite 1-3 tamaños: %r" % (cols,))
    return cols


# `name=` es el título del nodo en el panel del VB. No se llama `label`/`title` porque esos son
# campos de contenido (counter.label, heading.title) y taparlos perdería datos en silencio.
def el(itype, *, cols="1/1", name=None, **fields):
    """Item: el("heading", title="Hola", header_tag="h1", color="#fff", margin=0)."""
    size, tablet, mobile = _cols(cols)
    return item(itype, A("item", itype, **fields), size, tablet, mobile, title=name)


def wr(*items, cols="1/1", name="Wrap", **fields):
    """Wrap con items posicionales: wr(el(...), el(...), cols="1/2", padding=(0, 16))."""
    size, tablet, mobile = _cols(cols)
    return wrap(A("wrap", **fields), list(items), size, tablet, mobile, title=name)


def nw(*items, cols="1/1", name="Wrap", **fields):
    """Wrap anidado (tarjeta de grid o de query loop). Un solo nivel: trampa 16."""
    size, tablet, mobile = _cols(cols)
    return nested(A("wrap", **fields), list(items), size, tablet, mobile, title=name)


def sec(*wraps, name="Section", **fields):
    """Sección: sec(wr(...), padding=(80, 0), max_width="1728px", background_color="#111")."""
    attr = A("section", **fields)
    attr.setdefault("width_switcher", "full")
    return section(attr, list(wraps), title=name)


def bg(image, size="cover", position="center", repeat="no-repeat"):
    """Fondo de imagen para sec()/wr()/nw(): sec(..., **bg(context.media("hero")))."""
    return {"background_image": {"desktop": image}, "background_size": size,
            "background_position": position, "background_repeat": repeat}


def video_bg(mp4, *, fallback, overlay=None, opacity=None, dots=False):
    """Vídeo de fondo de sección (trampa 25): sec(..., **video_bg(context.media("hero"), fallback="#111",
    overlay="#000", opacity=0.4)). `fallback` es el color mientras carga; opacity 0-1; dots oculta la trama."""
    fields = {"background_switcher": "video", "bg_video_mp4": mp4, "bg_video_dots": "" if dots else "hide",
              "background_color": fallback}
    if overlay is not None:
        fields["background_overlay_background_color"] = overlay
    if opacity is not None:
        fields["background_overlay_opacity"] = opacity
    return fields


__all__ += ["A", "el", "wr", "nw", "sec", "bg", "video_bg"]
