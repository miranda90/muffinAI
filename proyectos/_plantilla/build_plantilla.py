"""New pages: python3 tools/build.py proyectos/<cliente>/build_<pagina>.py --check.
No writes at import time. Replace content, profile and source evidence before delivery.
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
from mfn import pad
from recipes import hero
OUTPUT = "salida.json"
PROFILE = {"editor": "visual", "artifact_kind": "page", "root_font_px": 16,
           "fonts": [], "media_domains": [], "dependencies": {}, "global_styles": []}
SOURCE = {"kind": "manual", "reference": "Ejemplo de plantilla; sustituir por el diseño real"}
TOKENS = {"primary": "#000000", "max_width": "1728px"}
EXCEPTIONS = []  # {code, path, reason}; structural errors cannot be suppressed.


def build(context):
    section = hero("Titular", spacing=pad({"top":"5rem", "bottom":"5rem"},
                                          mobile={"top":"2rem", "bottom":"2rem"}),
                   max_width=context.tokens.get("max_width", TOKENS["max_width"]))
    context.bind("hero", section, evidence="inferred", responsive={"mobile":"Una columna, padding 2rem"})
    return [section]


if __name__ == "__main__":
    from build import main
    sys.exit(main([str(Path(__file__).resolve()), *sys.argv[1:]]))
