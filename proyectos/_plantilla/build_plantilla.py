"""Plantilla de página nueva. Copiar a proyectos/<cliente>/build_<pagina>.py y ejecutar:

    python3 tools/build.py proyectos/<cliente>/build_<pagina>.py --check   # construir y validar
    python3 tools/build.py proyectos/<cliente>/build_<pagina>.py           # publicar JSON + informe

Cada kwarg de el()/wr()/nw()/sec() es un campo del catálogo (python3 tools/fields.py <tipo>),
con o sin prefijo css_/css_advanced_. Selector, style, rem, valor mobile y switchers salen solos.
Sin escrituras al importar: build(context) devuelve la página y tools/build.py la entrega.
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
from mfn import el, wr, nw, sec, bg

OUTPUT = "salida.json"
PROFILE = {"editor": "visual", "artifact_kind": "page", "root_font_px": 16,
           "fonts": [], "media_domains": [], "dependencies": {}, "global_styles": []}
SOURCE = {"kind": "manual", "reference": "Ejemplo de plantilla; sustituir por el diseño real"}
# Tokens del diseño (Figma): colores, contenedor y roles tipográficos con su valor mobile.
TOKENS = {"primary": "#7F41F5", "dark": "#221C3D", "body": "#4A5565", "light": "#F4F7F9", "white": "#FFFFFF",
          "max_width": "1728px"}
T = {  # rol → typography (desktop, mobile); tablet opcional
    "h1": {"desktop": {"font-size": "68px", "line-height": "1", "font-weight": "600"},
           "mobile": {"font-size": "36px", "line-height": "1.1", "font-weight": "600"}},
    "h2": {"desktop": {"font-size": "48px", "line-height": "1.1", "font-weight": "600"},
           "mobile": {"font-size": "30px", "line-height": "1.2", "font-weight": "600"}},
    "h3": {"desktop": {"font-size": "24px", "line-height": "1.3", "font-weight": "600"},
           "mobile": {"font-size": "20px", "line-height": "1.3", "font-weight": "600"}},
    "p": {"desktop": {"font-size": "20px", "line-height": "1.5"}, "mobile": {"font-size": "17px", "line-height": "1.5"}},
}
EXCEPTIONS = []  # {code, path, reason}; los errores estructurales no se pueden suprimir.

# Estilo compartido de botón: un dict de kwargs que se reutiliza con **BTN.
BTN = dict(button_background_color=TOKENS["primary"], button_color=TOKENS["white"], button_border_radius=0,
           button_padding=(12, 28), button_typography={"desktop": {"font-size": "18px", "font-weight": "500"},
                                                       "mobile": {"font-size": "16px", "font-weight": "500"}},
           margin=0)


def card(title, text, link, image_src=None):
    """Tarjeta de grid: nested wrap con fondo, alto 100% y botón abajo (trampa 21)."""
    image = [el("image", src=image_src, alt=title, image_cover_height=240, margin=(0, 0, 24, 0))] if image_src else []
    return nw(*image,
              el("heading", title=title, header_tag="h3", color=TOKENS["dark"], typography=T["h3"], margin=(0, 0, 12, 0)),
              el("plain_text", content=text, descdesca_color=TOKENS["body"], desc_typography=T["p"], margin=(0, 0, 24, 0)),
              el("button", title="Ver más", link=link, **BTN),
              background_color=TOKENS["white"], padding=32, height="100%", align_content="space-between",
              label="Tarjeta — " + title)


def build(context):
    M = context.tokens.get("max_width", TOKENS["max_width"])
    # Medios: siempre desde assets/manifest.json → URL#ID (context.media("hero")). El validador
    # rechaza URLs fuera del manifest (E072): sin medios subidos, la plantilla los omite.
    img = context.media("hero") if "hero" in context.manifest else None

    hero = sec(
        wr(el("heading", title="Titular del hero", header_tag="h1", color=TOKENS["white"], typography=T["h1"], margin=(0, 0, 24, 0)),
           el("plain_text", content="Texto de apoyo del hero.", descdesca_color=TOKENS["white"], desc_typography=T["p"], margin=(0, 0, 40, 0)),
           el("button", title="Empezar", link="/contacto/", **BTN, cols=("1/3", "1/2")),
           cols=("2/3", "1/1")),
        padding=(160, 36, 120, 36), max_width=M, background_color=TOKENS["dark"], **(bg(img) if img else {}), label="Hero")
    context.bind("hero", hero, evidence="inferred", responsive={"mobile": "Una columna; padding 160→ver TOKENS"})

    cards = sec(
        wr(el("heading", title="Lo que hacemos", header_tag="h2", color=TOKENS["dark"], typography=T["h2"], margin=(0, 0, 48, 0))),
        wr(card("Servicio uno", "Descripción breve.", "/servicios/uno/", img),
           card("Servicio dos", "Descripción breve.", "/servicios/dos/", img),
           card("Servicio tres", "Descripción breve.", "/servicios/tres/", img),
           grid_columns={"desktop": "repeat(3, 1fr)", "tablet": "repeat(2, 1fr)", "mobile": "1fr"},
           grid_columns_gap="2rem", grid_rows_gap="2rem"),
        padding=(120, 64), max_width=M, background_color=TOKENS["light"], label="Servicios")
    context.bind("servicios", cards, evidence="inferred", responsive={"tablet": "2 columnas", "mobile": "1 columna"})

    cta = sec(
        wr(el("heading", title="¿Hablamos?", header_tag="h2", color=TOKENS["white"], typography=T["h2"], txt_align="center", margin=(0, 0, 32, 0)),
           el("button", title="Contactar", link="/contacto/", **BTN, cols=("1/4", "1/2")),
           justify_content="center"),
        padding=(96, 36), max_width=M, background_color=TOKENS["primary"], label="CTA")
    context.bind("cta", cta, evidence="inferred", responsive={"mobile": "Botón a media anchura"})
    return [hero, cards, cta]


if __name__ == "__main__":
    from build import main
    sys.exit(main([str(Path(__file__).resolve()), *sys.argv[1:]]))
