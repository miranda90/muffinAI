#!/usr/bin/env python3
"""Genera las fichas .md de builder-elements/ y _elements.json a partir de fields-dump.json.

Uso:
    php extract.php            # genera fields-dump.json (ejecuta el PHP real con stubs WP)
    python3 generate_fichas.py # regenera todas las fichas .md y _elements.json
"""
import json
import argparse
import tempfile
from pathlib import Path
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)  # builder-elements/
DUMP = os.path.join(HERE, "fields-dump.json")

STRUCTURAL = {"html", "header", "subheader", "info", "helper", "preview"}


def esc(s):
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def fmt_options(opts):
    if not isinstance(opts, dict):
        return ""
    parts = []
    for k, v in opts.items():
        label = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
        key = '`""`' if k == "" else f"`{k}`"
        parts.append(f"{key} {esc(label)}")
    return " · ".join(parts)


def fmt_condition(cond):
    if not cond:
        return ""
    if isinstance(cond, list) or (isinstance(cond, dict) and "0" in cond):
        # forma compuesta ['AND', {...}, {...}] (json puede convertir a dict indexado)
        items = list(cond.values()) if isinstance(cond, dict) else cond
        op = items[0] if isinstance(items[0], str) else "AND"
        subs = [fmt_condition(c) for c in items if isinstance(c, dict)]
        return f" {op} ".join(s for s in subs if s)
    if isinstance(cond, dict) and "id" in cond:
        return f"`{cond.get('id')}` {cond.get('opt', 'is')} `{cond.get('val', '')}`"
    return ""


def field_value_format(f):
    """Describe el formato de valor esperado en el JSON para este campo."""
    t = f.get("type", "")
    respons = bool(f.get("responsive"))
    if "selector" in f and "style" in f:
        style = f.get("style", "")
        if t == "dimensions":
            # Dos formatos incompatibles, discriminados por la clave `version`:
            #  - version == "separated-fields" (solo margin/padding): objeto por lado.
            #  - sin `version` (border-width, border-radius): shorthand CSS en un
            #    string separado por espacios. forms/fields/dimensions.js:9 hace
            #    value.split(' ') y solo acepta string; con objeto los 4 inputs
            #    salen vacíos y el hidden guarda "[object Object]".
            if f.get("version") == "separated-fields":
                inner = '{"top": "...", "right": "...", "bottom": "...", "left": "..."}'
            elif "border-radius" in style:
                inner = '"8px 8px 8px 8px"'
            else:
                inner = '"1px 1px 1px 1px"'
        elif t == "typography_vb":
            inner = '{"font-size": "...", "line-height": "...", "font-weight": "...", ...}'
        elif t == "gradient":
            inner = '{..., "string": "linear-gradient(...)"} — solo string se emite'
        elif t == "transform":
            inner = '{"scaleX":1,"skewY":0,"skewX":0,"scaleY":1,"translateX":0,"translateY":0,"rotate":0,"string":"1,0,0,1,0,0,0"}'
        elif t in ("css_filters", "backdrop_filter"):
            inner = '{..., "string": "blur(...) ..."} — solo string se emite'
        else:
            inner = '"valor"'
        dev = f'{{"desktop": {inner}, "tablet": ..., "mobile": ...}}' if respons else inner
        return (
            f'Objeto CSS: `{{"selector": "{f["selector"]}", "style": "{style}", "val": {dev}}}`'
        )
    if t == "switch" and f.get("version") == "multiple":
        return 'String de tokens separados por espacio, con espacio inicial (ej. `" hide-mobile hide-tablet"`)'
    if t == "pills":
        return 'String de clases separadas por espacio (ej. `"clase-a clase-b"`)'
    if t == "checkbox":
        return '`"1"` activo / `""` inactivo'
    if t == "upload_multi":
        return 'IDs de adjuntos separados por coma (ej. `"12,45,88"`)'
    if t == "tabs":
        return "Array de objetos (formato propio del campo tabs)"
    if t == "sliderbar":
        p = f.get("param") or {}
        unit = p.get("unit", "") if isinstance(p, dict) else ""
        return f'Número como string{" + `" + unit + "`" if unit else ""}'
    return "String"


def render_fields(attrs, level=3):
    """Render de la lista plana de campos, agrupando por headers."""
    lines = []
    h = "#" * level
    for f in attrs:
        if not isinstance(f, dict):
            continue
        t = f.get("type", "")
        fid = f.get("id")
        if t in STRUCTURAL or not fid:
            if t in ("header", "subheader") and f.get("title"):
                lines.append(f"\n{h} {esc(f['title'])}\n")
            continue
        deprecated = "mfn-deprecated" in str(f.get("class", ""))
        dep = " ⚠️ **DEPRECATED — no usar en JSON nuevo**" if deprecated else ""
        lines.append(f"- **`{fid}`** ({t}){dep} — {esc(f.get('title', ''))}")
        if f.get("desc"):
            lines.append(f"  - {esc(f['desc'])}")
        vf = field_value_format(f)
        lines.append(f"  - Valor: {vf}")
        if f.get("type") == "dimensions" and f.get("version") != "separated-fields":
            order = (
                "top-left top-right bottom-right bottom-left"
                if "border-radius" in str(f.get("style", ""))
                else "top right bottom left"
            )
            lines.append(
                f"  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`{order}`), "
                "**nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)"
            )
        if f.get("options"):
            lines.append(f"  - Opciones: {fmt_options(f['options'])}")
        if "std" in f and f["std"] not in (None, ""):
            std = f["std"] if isinstance(f["std"], str) else json.dumps(f["std"], ensure_ascii=False)
            lines.append(f"  - Default: `{esc(std)}`")
        if f.get("condition"):
            c = fmt_condition(f["condition"])
            if c:
                lines.append(f"  - Visible si: {c}")
        if f.get("responsive"):
            lines.append("  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)")
    return lines


def example_json(eid, item):
    # Concrete editable content, no theme placeholder URLs or implicit demo video.
    attr = {}
    fields = {f.get("id"): f for f in item.get("attr", []) if isinstance(f, dict)}
    if "title" in fields: attr["title"] = "Título de ejemplo"
    elif "content" in fields: attr["content"] = "Contenido de ejemplo"
    if eid == "heading": attr["header_tag"] = "h2"
    if eid == "video": attr["video"] = ""
    if eid == "counter": attr.update(number="100", icon="", image="")
    return json.dumps({"type": eid, "uid": "itm000001", "icon": item.get("icon", eid),
                       "jsclass": eid, "title": item.get("title", eid), "size": "1/1",
                       "tablet_size": "1/1", "mobile_size": "1/1", "attr": attr},
                      indent=2, ensure_ascii=False)


def ficha_item(eid, item, inline=None):
    real_type = item.get("type", eid)
    lines = [f"# `{eid}` — {esc(item.get('title', eid))}", ""]
    lines.append(f"- **Categoría:** {item.get('cat', '—')}")
    lines.append(
        f"- **Size por defecto:** {item.get('size', '—')} · tablet {item.get('tablet_size', '—')}"
        f" · mobile {item.get('mobile_size', '—')} · tablet_resized {item.get('tablet_resized', '—')}"
    )
    if real_type != eid:
        lines.append(f"- **Alias de:** [`{real_type}`]({real_type}.md) — usa los campos de ese elemento.")
        lines.append("")
        lines.append(
            f"Este elemento es un alias de plantilla (`type` interno: `{real_type}`). "
            f"No define campos propios: consulta la ficha de [`{real_type}`]({real_type}.md)."
        )
    else:
        attrs = item.get("attr") or item.get("fields") or []
        n = sum(1 for f in attrs if isinstance(f, dict) and f.get("id") and f.get("type") not in STRUCTURAL)
        lines.append(f"- **Campos propios:** {n}")
        lines.append("")
        lines.append("## Campos")
        lines.extend(render_fields(attrs))
        lines.append("")
        lines.append("## Ejemplo mínimo")
        lines.append("")
        lines.append("```json")
        lines.append(example_json(eid, item))
        lines.append("```")
    if inline:
        lines.append("")
        lines.append("## Variante shortcode inline (para `content` de column/plain_text/visual)")
        lines.append("")
        lines.append(
            "⚠️ Definición DISTINTA al elemento del builder — solo para el shortcode dentro de texto:"
        )
        lines.extend(render_fields(inline.get("attr", []), level=4))
    lines.append("")
    lines.append("---")
    lines.append(
        "Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes,"
        " posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md)."
    )
    lines.append(
        "Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`."
        " Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`."
    )
    lines.append("")
    lines.append("*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*")
    return "\n".join(lines)


def ficha_inline_only(eid, item):
    lines = [f"# `{eid}` — {esc(item.get('title', eid))} (shortcode inline)", ""]
    lines.append(
        "Shortcode **inline** para usar dentro de `content` (column, plain_text, visual)."
        " NO es un item del builder: no lleva `type`/`size`/`uid`."
    )
    lines.append("")
    lines.append("## Campos")
    lines.extend(render_fields(item.get("attr", [])))
    lines.append("")
    lines.append("*Generado desde `class-mfn-builder-fields.php` (`get_inline_shortcode()`) — no editar a mano.*")
    return "\n".join(lines)


def ficha_shared(name, title, intro, attrs):
    lines = [f"# {title}", "", intro, ""]
    lines.extend(render_fields(attrs))
    lines.append("")
    lines.append("*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*")
    return "\n".join(lines)


def generated_files(d):
    items, inline = d["items"], d["inline_shortcodes"]
    output = {eid + ".md": ficha_item(eid, item, inline.get(eid)) for eid, item in items.items()}
    output.update({eid + ".md": ficha_inline_only(eid, item) for eid, item in inline.items() if eid not in items})
    for name, title, intro, fields in (
        ("_advanced", "Pestaña Advanced (común a TODOS los items)", "Campos comunes.", d["advanced"]),
        ("_section", "Campos de SECCIÓN", "Campos de attr de sección.", d["section"]),
        ("_wrap", "Campos de WRAP", "Campos de attr de wrap.", d["wrap"]),
    ):
        output[name + ".md"] = ficha_shared(name, title, intro, fields)
    output["_elements.json"] = json.dumps(d, indent=1, ensure_ascii=False)
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dump", default=DUMP)
    parser.add_argument("--out", default=OUT)
    parser.add_argument("--check", action="store_true")
    opts = parser.parse_args()
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
    from contracts import read_json
    from validate_bebuilder_json import Schema
    data = read_json(opts.dump)
    schema = Schema(data)
    render_types = set(data.get("render_types", schema.item_types))
    if render_types != schema.item_types:
        raise ValueError("El catálogo canónico no coincide con los métodos de render")
    output = generated_files(data)
    dest = Path(opts.out)
    if opts.check:
        changed = [name for name, text in output.items() if not (dest/name).is_file() or (dest/name).read_text() != text]
        if changed: print("Fichas desactualizadas: " + ", ".join(changed))
        return int(bool(changed))
    dest.mkdir(parents=True, exist_ok=True)
    # Prepare the complete generation before replacing anything. Publish the catalog last.
    with tempfile.TemporaryDirectory(prefix=".catalog-", dir=dest.parent) as stage:
        stage = Path(stage)
        for name, text in output.items():
            if Path(name).name != name: raise ValueError("Nombre de ficha inválido")
            (stage/name).write_text(text, encoding="utf-8")
        for name in output: os.replace(stage/name, dest/name)
    print("Generados %d ficheros; %d tipos, %d alias" % (len(output), len(schema.item_types), len(schema.aliases)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
