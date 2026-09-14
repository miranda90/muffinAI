"""Campos de un elemento en una línea cada uno (sustituye a leer la ficha entera).

    python3 tools/fields.py button                # campos propios del tipo
    python3 tools/fields.py button --grep border  # filtrar por regex (id, style, título)
    python3 tools/fields.py wrap | section        # campos de wrap / sección
    python3 tools/fields.py --advanced            # pestaña Advanced (común a todos los items)
    python3 tools/fields.py --types               # tipos renderizables y alias

Los nombres sirven tal cual (o sin prefijo css_/css_advanced_) como kwargs de
el()/wr()/nw()/sec() en tools/mfn.py.
"""
import argparse
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_bebuilder_json import load_schema

SHORT = [(".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "item"),
         (".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "wrap-inner"),
         (".mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement .mcb-wrap-inner", "wrap-grid"),
         (".mcb-section .mcb-wrap-mfnuidelement", "wrap"),
         (".mcb-section-mfnuidelement.custom-width .section_wrapper", "section.custom .section_wrapper"),
         (".mcb-section-mfnuidelement", "section")]


def condition(value):
    if isinstance(value, dict):
        return "%s %s %r" % (value.get("id"), value.get("opt", "is"), value.get("val"))
    if isinstance(value, list):
        parts = [condition(x) for x in value if isinstance(x, (dict, list))]
        return (" %s " % (value[0] if value and isinstance(value[0], str) else "AND")).join(parts)
    return ""


def line(definition):
    kind = definition.get("type") or "?"
    if definition.get("version") == "separated-fields":
        kind += "/sides"
    bits = [definition["id"], kind]
    if definition.get("responsive"):
        bits.append("rwd")
    param = definition.get("param") if isinstance(definition.get("param"), dict) else {}
    if definition.get("default_unit") or param.get("unit"):
        bits.append("unit=" + (definition.get("default_unit") or param["unit"]))
    options = definition.get("options")
    if isinstance(options, dict) and all(not isinstance(v, dict) for v in options.values()):
        bits.append("opts=" + "|".join(repr(k) if k == "" else str(k) for k in options))
    if definition.get("std") not in (None, "", [], {}) and not isinstance(definition.get("std"), (dict, list)):
        bits.append("std=%r" % definition["std"])
    if definition.get("condition"):
        bits.append("if " + condition(definition["condition"]))
    if definition.get("style"):
        selector = definition.get("selector", "")
        for long, short in SHORT:
            selector = selector.replace(long, short)
        bits.append("-> %s @ %s" % (definition["style"], selector))
    return "  ".join(bits)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("scope", nargs="?", help="tipo de item, wrap o section")
    parser.add_argument("--grep", help="regex sobre id, style o título")
    parser.add_argument("--advanced", action="store_true", help="pestaña Advanced común")
    parser.add_argument("--types", action="store_true", help="listar tipos y alias")
    opts = parser.parse_args(argv)
    schema = load_schema()
    if opts.types:
        for itype in sorted(schema.item_types):
            spec = schema.raw["items"][itype]
            aliases = sorted(a for a, t in schema.aliases.items() if t == itype)
            print("%-28s %s%s" % (itype, spec.get("title", ""), "  (alias: %s)" % ", ".join(aliases) if aliases else ""))
        return 0
    if opts.advanced:
        index, header = schema.advanced, "advanced (todos los items)"
    elif opts.scope in ("wrap", "section"):
        index, header = schema.index_for(opts.scope), opts.scope
    elif opts.scope:
        itype = schema.canonical(opts.scope)
        own = set(schema._index(schema.raw["items"][itype].get("attr", [])))
        index = {k: v for k, v in schema.items[itype].items() if k in own}
        header = "%s (+ advanced: --advanced)" % itype
    else:
        parser.error("indica un tipo, wrap, section, --advanced o --types")
    pattern = re.compile(opts.grep, re.I) if opts.grep else None
    print("# " + header)
    for key, definitions in index.items():
        seen = set()
        for definition in definitions:
            text = line(definition)
            if text in seen or (pattern and not pattern.search(text + " " + str(definition.get("title", "")))):
                continue
            seen.add(text)
            print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
