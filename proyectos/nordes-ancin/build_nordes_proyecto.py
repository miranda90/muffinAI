# -*- coding: utf-8 -*-
"""Genera el JSON BeBuilder de la 'Ficha de proyecto' (Nordés Ancín, Figma 2819:227).

Salida: nordes-ancin-proyecto.json (contenido literal del diseño: proyecto ITER).

Mismas reglas de proyecto que la portada: contenedor interior a 1728px
(`width_switcher: "custom"` + `css_advanced_max_width`) y padding lateral 36px = 2.25rem.
Header, footer y menú lateral son plantillas aparte (build_nordes_header.py /
build_nordes_footer.py); la banda CTA final sí va en la página, como en la portada.

Decisiones de mapeo (lo que el bloque ES, no cómo se ve):
  - Migas "Inicio > Proyectos > Iter"  → `breadcrumbs` (nativo, se genera solo).
  - Fila de datos (cliente/ubicación/período/sector) → wrap grid 4 columnas con un
    subwrap por celda y divisor por `border-left`.
  - Galería de 6 fotos con flechas y paginación → `slider` (Slides CPT, categoría
    "iter"). Requiere Slides activo en Theme Options → Post types y 6 slides creadas.
  - "Otros proyectos" → query loop de `portfolio` (3 tarjetas, misma tarjeta que el
    listado).
  - Formulario → `cf7` (igual que el listado).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- tokens
PRIMARY   = "#001689"
BLACK     = "#1F1F1F"
TEXTDARK  = "#222223"   # neutrals/neutral-1
NEUTRAL2  = "#464648"
DARKGRAY  = "#6B6B6B"
GRAYLABEL = "#A3A3A3"
WHITE     = "#FCFCFC"
OFFWHITE  = "#F1F1EE"
DIVIDER   = "rgba(252,252,252,0.24)"
MEDIA     = "https://nordesancin.com/wp-content/uploads/2026/07/"

MAXW      = "1728px"

# selectores base
S_SECTION   = ".mcb-section-mfnuidelement"
S_SECT_WRAP = ".mcb-section-mfnuidelement .section_wrapper"
S_SECT_MAXW = ".mcb-section-mfnuidelement.custom-width .section_wrapper"
S_SECT_OVER = ".mcb-section-mfnuidelement .mcb-background-overlay"
S_WRAP      = ".mcb-section .mcb-wrap-mfnuidelement"
S_WRAP_IN   = ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner"
S_WRAP_GRID = ".mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement .mcb-wrap-inner"
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
S_BREAD     = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .breadcrumbs"
S_SLIDER_IMG = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider.default "
                ".content_slider_ul .slick-list,.mcb-section .mcb-wrap .mcb-item-mfnuidelement "
                ".content_slider:not(.default) .content_slider_ul li img")
S_SLIDER_BTN = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button"

_n = [0]


def uid(prefix):
    _n[0] += 1
    return "{}{:06d}".format(prefix, _n[0])


def css(selector, style, val):
    return {"selector": selector, "style": style, "val": val}


def typo(sel, desktop, tablet=None, mobile=None):
    val = {"desktop": desktop}
    if tablet:
        val["tablet"] = tablet
    if mobile:
        val["mobile"] = mobile
    return css(sel, "typography", val)


def _no_zero(side_vals):
    """PHP `empty()` descarta "0": se escribe "0px" (class-mfn-helper.php:198, :406)."""
    return {k: ("0px" if v in ("0", 0) else v) for k, v in side_vals.items()}


def pad(desktop, tablet=None, mobile=None):
    """Todo espaciado lleva valor mobile; si el diseño no pide otro, replica desktop."""
    val = {"desktop": _no_zero(desktop)}
    if tablet:
        val["tablet"] = _no_zero(tablet)
    val["mobile"] = _no_zero(mobile) if mobile else _no_zero(desktop)
    return val


def section(attr, wraps, title="Section"):
    return {"uid": uid("sec"), "icon": "section", "jsclass": "section",
            "title": title, "ver": "default", "attr": attr, "wraps": wraps}


def wrap(attr, items, size="1/1", tablet=None, mobile="1/1", title="Wrap"):
    return {"uid": uid("wrp"), "icon": "wrap", "jsclass": "wrap", "title": title,
            "size": size, "tablet_size": tablet or size, "mobile_size": mobile,
            "attr": attr, "items": items}


def nested(attr, items, size="1/1", tablet=None, mobile="1/1", title="Wrap"):
    return {"uid": uid("itm"), "icon": "wrap", "jsclass": "wrap", "title": title,
            "item_is_wrap": 1,
            "size": size, "tablet_size": tablet or size, "mobile_size": mobile,
            "attr": attr, "items": items}


def item(itype, attr, size="1/1", tablet=None, mobile="1/1", title=None, icon=None):
    return {"uid": uid("itm"), "type": itype, "jsclass": itype,
            "title": title or itype.replace("_", " ").title(), "icon": icon or itype,
            "size": size, "tablet_size": tablet or size, "mobile_size": mobile,
            "attr": attr}


# ---------------------------------------------------------------- mixins
def sec_base(pad_val, extra=None):
    """Contenedor interior a 1728px + padding lateral 36px."""
    attr = {
        "width_switcher": "custom",
        "css_advanced_max_width": css(S_SECT_MAXW, "max-width", MAXW),
        "css_advanced_padding": css(S_SECTION, "padding", pad_val),
    }
    if extra:
        attr.update(extra)
    return attr


def sec_bg_image(filename, extra=None):
    attr = {
        "background_switcher": "default",
        "css_advanced_background_image": css(S_SECTION, "background-image",
                                             {"desktop": MEDIA + filename}),
        "css_advanced_background_size": css(S_SECTION, "background-size", {"desktop": "cover"}),
        "css_advanced_background_position": css(S_SECTION, "background-position",
                                                {"desktop": "center"}),
        "css_advanced_background_repeat": css(S_SECTION, "background-repeat",
                                              {"desktop": "no-repeat"}),
    }
    if extra:
        attr.update(extra)
    return attr


def wrap_width(desktop, tablet=None, mobile="100%"):
    return {
        "width_switcher": "custom",
        "css_advanced_flex": css(S_WRAP, "width",
                                 {"desktop": desktop,
                                  "tablet": tablet or desktop,
                                  "mobile": mobile}),
    }


def btn(title, link, bg, fg, extra=None, full=False):
    attr = {
        "title": title,
        "link": link,
        "icon": "icon-right-thin",
        "icon_position": "right",
        "button_style": "",
        "background_switcher": "default",
        "css_button_color": css(S_BUTTON, "color", fg),
        "css_button_icon_color": css(S_BUTTON + " i", "color", fg),
        "css_button_background_color": css(S_BUTTON, "background-color", bg),
        "css_button_border_radius": css(S_BUTTON, "border-radius",
                                        {"desktop": "8px 8px 8px 8px"}),
        "css_button_padding": css(S_BUTTON, "padding",
                                  pad({"top": "1rem", "right": "1.5rem",
                                       "bottom": "1rem", "left": "1.5rem"},
                                      None,
                                      {"top": "0.875rem", "right": "1.25rem",
                                       "bottom": "0.875rem", "left": "1.25rem"})),
        "css_button_typography": typo(S_BUTTON,
                                      {"font-size": "20px", "line-height": "1.4",
                                       "letter-spacing": "-0.8px", "font-weight": "400"},
                                      None,
                                      {"font-size": "17px", "line-height": "1.4",
                                       "letter-spacing": "-0.6px", "font-weight": "400"}),
    }
    if full:
        attr["full_width"] = "1"
    if extra:
        attr.update(extra)
    return attr


# tipografías del diseño ------------------------------------------------
def t_h1(sel):
    return typo(sel,
                {"font-size": "64px", "line-height": "1.1",
                 "letter-spacing": "-3.2px", "font-weight": "500"},
                {"font-size": "48px", "line-height": "1.1",
                 "letter-spacing": "-2.4px", "font-weight": "500"},
                {"font-size": "34px", "line-height": "1.15",
                 "letter-spacing": "-1.2px", "font-weight": "500"})


def t_h2(sel):
    return typo(sel,
                {"font-size": "48px", "line-height": "1.2",
                 "letter-spacing": "-1.92px", "font-weight": "500"},
                {"font-size": "38px", "line-height": "1.2",
                 "letter-spacing": "-1.4px", "font-weight": "500"},
                {"font-size": "30px", "line-height": "1.2",
                 "letter-spacing": "-1px", "font-weight": "500"})


def t_h3(sel):
    return typo(sel,
                {"font-size": "36px", "line-height": "1.24",
                 "letter-spacing": "-0.72px", "font-weight": "500"},
                {"font-size": "30px", "line-height": "1.24",
                 "letter-spacing": "-0.6px", "font-weight": "500"},
                {"font-size": "26px", "line-height": "1.24",
                 "letter-spacing": "-0.5px", "font-weight": "500"})


def t_h5(sel):
    """h5 del diseño: font-titles Roman 24 / 1.2."""
    return typo(sel,
                {"font-size": "24px", "line-height": "1.2", "font-weight": "400"},
                None,
                {"font-size": "20px", "line-height": "1.2", "font-weight": "400"})


def t_intro(sel):
    """h-project-intro: font-titles Heavy 92 / 1.1 / -5.52px."""
    return typo(sel,
                {"font-size": "92px", "line-height": "1.1",
                 "letter-spacing": "-5.52px", "font-weight": "800"},
                {"font-size": "64px", "line-height": "1.1",
                 "letter-spacing": "-3.5px", "font-weight": "800"},
                {"font-size": "40px", "line-height": "1.1",
                 "letter-spacing": "-2px", "font-weight": "800"})


def t_pxl(sel):
    return typo(sel,
                {"font-size": "22px", "line-height": "1.6"},
                None,
                {"font-size": "18px", "line-height": "1.6"})


def t_pl(sel):
    """p-L: font-titles Roman 20 / 1.4 / -0.4px (se usa en heading tag p)."""
    return typo(sel,
                {"font-size": "20px", "line-height": "1.4",
                 "letter-spacing": "-0.4px", "font-weight": "400"},
                None,
                {"font-size": "17px", "line-height": "1.4",
                 "letter-spacing": "-0.3px", "font-weight": "400"})


def t_pm(sel, weight="400"):
    return typo(sel,
                {"font-size": "18px", "line-height": "1.6", "font-weight": weight},
                None,
                {"font-size": "16px", "line-height": "1.6", "font-weight": weight})


def t_ps(sel):
    return typo(sel,
                {"font-size": "13.3px", "line-height": "1.6"},
                None,
                {"font-size": "13px", "line-height": "1.6"})


def t_caps(sel):
    return typo(sel,
                {"font-size": "18px", "line-height": "1.6", "text-transform": "uppercase"},
                None,
                {"font-size": "15px", "line-height": "1.6", "text-transform": "uppercase"})


# ================================================================ 1. HERO
# Nodo 2819:967: 1117px, imagen + overlay rgba(4,4,4,0.36), contenido abajo,
# padding 36px; bloque titular 967px; 64px hasta la fila de datos.
DATOS = [
    ("Cliente final", "ITER Organization<br>Fusion for Energy"),
    ("Ubicación", "Cadarache<br>Provenza, Francia"),
    ("Período de ejecución", "2013 – 2016"),
    ("Sector", "Industrial y Alimentario"),
]


def dato_cell(label, value, first=False):
    """Celda de la fila de datos: etiqueta p-S + valor h5 (font-titles, tag p).
    Divisor vertical entre celdas por border-left (Line 4 del diseño)."""
    attr = {
        "css_advanced_padding": css(S_WRAP_IN, "padding",
                                    pad({"top": "2.25rem", "right": "2.25rem",
                                         "bottom": "2.25rem", "left": "2.25rem"},
                                        {"top": "1.5rem", "right": "1.5rem",
                                         "bottom": "1.5rem", "left": "1.5rem"},
                                        {"top": "1.25rem", "right": "1.25rem",
                                         "bottom": "1.25rem", "left": "1.25rem"})),
        "height_switcher": "custom",
        "css_advanced_height": css(S_WRAP_IN, "height", {"desktop": "100%"}),
    }
    if not first:
        attr.update({
            "css_advanced_border_style": css(S_WRAP_IN, "border-style", "solid"),
            "css_advanced_border_color": css(S_WRAP_IN, "border-color", DIVIDER),
            "css_advanced_border_width": css(S_WRAP_IN, "border-width",
                                             {"desktop": "0px 0px 0px 1px",
                                              "tablet": "0px 0px 0px 1px",
                                              "mobile": "1px 0px 0px 0px"}),
        })
    return nested(attr, [
        item("plain_text", {
            "content": label,
            "css_descdesca_color": css(S_DESC_C, "color", OFFWHITE),
            "css_desc_typography": t_ps(S_DESC),
            "css_advanced_margin": css(S_ITEM_IN, "margin",
                                       pad({"bottom": "1rem"}, None, {"bottom": "0.5rem"})),
        }, title="Dato — etiqueta"),
        item("heading", {
            "title": value,
            "header_tag": "p",
            "css_color": css(S_TITLE_C, "color", WHITE),
            "css_typography": t_h5(S_TITLE),
            "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
        }, title="Dato — valor"),
    ], size="1/1", tablet="1/1", mobile="1/1", title="Dato — " + label)


hero = section(
    sec_base(
        pad({"top": "2.25rem", "right": "2.25rem", "bottom": "2.25rem", "left": "2.25rem"},
            {"top": "8rem", "right": "2rem", "bottom": "2.5rem", "left": "2rem"},
            {"top": "7rem", "right": "1.25rem", "bottom": "2rem", "left": "1.25rem"}),
        dict(sec_bg_image("hero-proyecto-iter.jpg"), **{
            "height_switcher": "custom",
            "css_advanced_height": css(S_SECTION, "height",
                                       {"desktop": "1117px", "tablet": "880px", "mobile": "auto"}),
            "background_overlay_switcher": "default",
            "css_advanced_background_overlay_background_color":
                css(S_SECT_OVER, "background-color", "rgba(4,4,4,0.36)"),
            "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "flex-end"}),
        })),
    [
        # Titular en fila propia (wrap 1/1); los 967px del diseño salen del size del
        # item (3/5 de 1656 ≈ 994px), no de un ancho custom del wrap (trampa 22).
        wrap(
            {
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "4rem"}, {"bottom": "3rem"},
                                               {"bottom": "2rem"})),
            },
            [
                item("breadcrumbs", {
                    "separator": "→",
                    "breadcrumb_home": "1",
                    "css_breadcrumbs_typography": typo(S_BREAD,
                        {"font-size": "16px", "line-height": "1", "letter-spacing": "-0.64px"},
                        None,
                        {"font-size": "14px", "line-height": "1", "letter-spacing": "-0.4px"}),
                    "css_breadcrumbs_gap": css(S_BREAD, "gap", {"desktop": "8px"}),
                    "css_breadcrumbsli_color": css(S_BREAD + " li", "color", WHITE),
                    "css_breadcrumbslia_color": css(S_BREAD + " li a", "color", WHITE),
                    "css_breadcrumbslia_color_hover": css(S_BREAD + " li:hover a", "color", OFFWHITE),
                    "css_breadcrumbsli-breadcrumbs-separator_color":
                        css(S_BREAD + " li .mfn-breadcrumbs-separator", "color", WHITE),
                    "css_breadcrumbsli-breadcrumbs-separator_font_size":
                        css(S_BREAD + " li .mfn-breadcrumbs-separator", "font-size",
                            {"desktop": "13px", "mobile": "12px"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "2.25rem"}, None, {"bottom": "1.5rem"})),
                }, title="Hero — migas"),
                item("heading", {
                    "title": "Ejecución de instalaciones para ITER: un sol en miniatura en Cadarache",
                    "header_tag": "h1",
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": t_h1(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, size="3/5", tablet="4/5", mobile="1/1", title="Hero — titular"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Hero — titular"),
        # Fila de datos: grid de 4 celdas sobre fondo primary, radio 12px.
        wrap(
            {
                "grid": "grid",
                "grid_columns_switcher": "",
                "css_grid_columns": css(S_WRAP_GRID, "grid-template-columns",
                                        {"desktop": "repeat(4, 1fr)",
                                         "tablet": "repeat(2, 1fr)",
                                         "mobile": "1fr"}),
                "css_grid_columns_gap": css(S_WRAP_GRID, "column-gap", {"desktop": "0px"}),
                "css_grid_rows_gap": css(S_WRAP_GRID, "row-gap", {"desktop": "0px"}),
                "background_switcher": "default",
                "css_advanced_background_color": css(S_WRAP_IN, "background-color", PRIMARY),
                "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                                  {"desktop": "12px 12px 12px 12px"}),
            },
            [dato_cell(l, v, first=(i == 0)) for i, (l, v) in enumerate(DATOS)],
            size="1/1", tablet="1/1", mobile="1/1", title="Hero — fila de datos"),
    ],
    title="Hero — Ficha de proyecto")

# ================================================================ 2. EL RETO
RETO_IZQ = (
    "<p>Un tokamak de 23.000 toneladas y 60 metros de altura, diseñado para alcanzar "
    "temperaturas de hasta 150 millones de grados, exige una ejecución sin margen para el "
    "error. En Cadarache, <strong>Nordés Ancín trabajó en cuatro de los 39 edificios del "
    "complejo ITER</strong>, coordinándose con siete agencias internacionales, bajo "
    "protocolos de obra nuclear y mientras la obra civil continuaba avanzando.</p>"
)
RETO_IZQ_2 = (
    "<p>La estrategia fue anticipar en oficina todo lo posible. Las instalaciones se "
    "modelaron sobre el modelo federado del complejo para resolver interferencias antes de "
    "llegar a obra, y colectores y tramos de conducto se prefabricaron en Cambre para reducir "
    "el tiempo de montaje en Cadarache. Un equipo propio permaneció desplazado durante toda "
    "la ejecución, con jefe de obra permanente y una <strong>trazabilidad documental "
    "exhaustiva de pruebas, protocolos y mediciones.</strong></p>"
)
RETO_DER = (
    "<p>El alcance incluyó climatización y tratamiento de aire, ventilación y extracción, "
    "calefacción y ACS, fontanería y saneamiento, distribución eléctrica, cuadros eléctricos "
    "y de control, protección contra incendios, además de la puesta en marcha y las pruebas "
    "finales.</p>"
    "<p><strong>Los cuatro edificios se entregaron dentro del calendario previsto</strong>, "
    "sin mover una sola fecha. La prefabricación redujo semanas de trabajo en plataforma y la "
    "documentación fue aceptada sin devoluciones. Además, la experiencia permitió consolidar "
    "un método de planificación y trazabilidad documental que Nordés Ancín aplica desde "
    "entonces en el resto de sus obras.</p>"
)

reto = section(
    sec_base(
        pad({"top": "7.5rem", "right": "2.25rem", "bottom": "7.5rem", "left": "2.25rem"},
            {"top": "5rem", "right": "2rem", "bottom": "5rem", "left": "2rem"},
            {"top": "3.5rem", "right": "1.25rem", "bottom": "3.5rem", "left": "1.25rem"}),
        {
            "background_switcher": "default",
            "css_advanced_background_color": css(S_SECTION, "background-color", WHITE),
        }),
    [
        wrap(
            {
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "4rem"}, {"bottom": "3rem"},
                                               {"bottom": "2rem"})),
            },
            [
                item("heading", {
                    "title": ("Un reto de ingeniería, coordinación y precisión "
                              "a escala internacional"),
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", BLACK),
                    "css_typography": t_intro(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, size="3/5", tablet="5/6", mobile="1/1", title="Reto — titular"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Reto — cabecera"),
        wrap(
            {
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"right": "2rem"}, {"right": "1rem"}, {"right": "0"})),
            },
            [
                item("plain_text", {
                    "content": RETO_IZQ,
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": t_pxl(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "2.25rem"}, None, {"bottom": "1.5rem"})),
                }, title="Reto — párrafo destacado"),
                item("plain_text", {
                    "content": RETO_IZQ_2,
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": t_pm(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "0"}, None, {"bottom": "1.5rem"})),
                }, title="Reto — estrategia"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Reto — columna izquierda"),
        wrap(
            {
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"left": "2rem"}, {"left": "1rem"}, {"left": "0"})),
            },
            [
                item("plain_text", {
                    "content": RETO_DER,
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": t_pm(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "2.25rem"}, None, {"bottom": "1.5rem"})),
                }, title="Reto — alcance y resultado"),
                item("button", btn("Ver vídeo del montaje",
                                   "https://www.youtube.com/watch?v=XXXXXXXXXXX",
                                   PRIMARY, WHITE, {
                    "target": "lightbox",
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }), title="Reto — botón vídeo"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Reto — columna derecha"),
    ],
    title="El reto")

# ================================================================ 3. GALERÍA
# Nodo 2819:338: 920px, radio 12px, overlay 0.24, controles (1…6 + flechas) en tarjeta
# translúcida. Elemento nativo más cercano: `slider` (Slides CPT). La paginación
# numérica no existe en el theme: se entregan flechas + dots estilizados.
galeria = section(
    sec_base(
        pad({"top": "0", "right": "2.25rem", "bottom": "0", "left": "2.25rem"},
            {"top": "0", "right": "2rem", "bottom": "0", "left": "2rem"},
            {"top": "0", "right": "1.25rem", "bottom": "0", "left": "1.25rem"}),
        {
            "background_switcher": "default",
            "css_advanced_background_color": css(S_SECTION, "background-color", WHITE),
        }),
    [
        wrap(
            {
                "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                                  {"desktop": "12px 12px 12px 12px"}),
            },
            [
                item("slider", {
                    "category": "iter",
                    "orderby": "menu_order",
                    "order": "ASC",
                    "style": "flat",
                    "title_tag": "h3",
                    "navigation": "",
                    "css_image_border_radius": css(S_SLIDER_IMG, "border-radius",
                                                   {"desktop": "12px 12px 12px 12px"}),
                    "css_content_slider_ulbutton_fontsize": css(
                        S_SLIDER_BTN, "--mfn-slider-arrow-size",
                        {"desktop": "29px", "mobile": "22px"}),
                    "css_content_slider_ulbutton_border_style": css(
                        S_SLIDER_BTN, "border-style", "none"),
                    "css_content_slider_ulbutton_border_radius": css(
                        S_SLIDER_BTN, "border-radius", {"desktop": "12px 12px 12px 12px"}),
                    "css_content_slider_ulbutton_color": css(S_SLIDER_BTN + " i", "color", WHITE),
                    "background_switcher": "default",
                    "css_content_slider_ulbutton_background_color": css(
                        S_SLIDER_BTN, "background-color", "rgba(31,31,31,0.12)"),
                    "css_content_slider_ulbutton_color_hover": css(
                        S_SLIDER_BTN + ":hover i", "color", WHITE),
                    "background_switcher_hover": "default",
                    "css_content_slider_ulbutton_background_hover": css(
                        S_SLIDER_BTN + ":hover, " + S_SLIDER_BTN + ":before",
                        "background", PRIMARY),
                    "css_dots_bg": css(
                        ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination a,"
                        ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination a:after",
                        "background-color", GRAYLABEL),
                    "css_dots_bg_active": css(
                        ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination .slick-active a,"
                        ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination .slick-active a:after",
                        "background-color", WHITE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Galería — slider"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Galería"),
    ],
    title="Galería del proyecto")

# ================================================================ 4. OTROS PROYECTOS
# Misma tarjeta que el listado (build_nordes.py): wrap anidado dentro del loop.
CARD_ITEMS = [
    item("plain_text", {
        "content": "{categories}",
        "width_switcher": "inline",
        "css_descdesca_color": css(S_DESC_C, "color", WHITE),
        "css_desc_typography": typo(S_DESC,
            {"font-size": "20px", "line-height": "1.4", "letter-spacing": "-0.8px"},
            None,
            {"font-size": "15px", "line-height": "1.4", "letter-spacing": "-0.4px"}),
        "background_switcher": "default",
        "css_advanced_background_color": css(S_ITEM_IN, "background-color", "rgba(31,31,31,0.72)"),
        "css_advanced_backdrop_filter": css(S_ITEM_IN, "backdrop-filter",
                                            {"desktop": {"blur": "60", "string": "blur(60px)"}}),
        "css_advanced_border_radius": css(S_ITEM_IN, "border-radius",
                                          {"desktop": "2000px 2000px 2000px 2000px"}),
        "css_advanced_padding": css(S_ITEM_IN, "padding",
                                    pad({"top": "0.75rem", "right": "1.25rem",
                                         "bottom": "0.75rem", "left": "1.25rem"},
                                        None,
                                        {"top": "0.5rem", "right": "0.875rem",
                                         "bottom": "0.5rem", "left": "0.875rem"})),
        "css_advanced_position": css(S_ITEM, "position", {"desktop": "absolute"}),
        "css_advanced_top": css(S_ITEM, "top", {"desktop": "1.5rem", "mobile": "1rem"}),
        "css_advanced_left": css(S_ITEM, "left", {"desktop": "1.5rem", "mobile": "1rem"}),
        "css_advanced_z_index": css(S_ITEM, "z-index", "2"),
    }, title="Sector tag"),
    item("image", {
        "src": "{featured_image}",
        "stretch": "1",
        "alt": "{title}",
        "link": "{permalink}",
        "image_height": "custom",
        "image_height_style": "",
        "css_image_cover_height": css(S_IMGCOVER, "height",
                                      {"desktop": "360px", "tablet": "320px", "mobile": "260px"}),
        "css_image_border_radius": css(S_IMGFRAME, "border-radius",
                                       {"desktop": "12px 12px 12px 12px"}),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   pad({"bottom": "1rem"}, None, {"bottom": "0.75rem"})),
    }, title="Project image"),
    item("heading", {
        "title": "{title}",
        "header_tag": "h3",
        "link": "{permalink}",
        "css_color": css(S_TITLE_C, "color", BLACK),
        "css_typography": t_h3(S_TITLE),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   pad({"bottom": "0.5rem"}, None, {"bottom": "0.375rem"})),
    }, size="4/5", tablet="4/5", mobile="4/5", title="Project title"),
    item("button", {
        "title": "",
        "link": "{permalink}",
        "link_title": "Ver proyecto",
        "icon": "icon-right-thin",
        "icon_position": "right",
        "button_style": "",
        "background_switcher": "default",
        "css_button_color": css(S_BUTTON, "color", WHITE),
        "css_button_icon_color": css(S_BUTTON + " i", "color", WHITE),
        "css_button_background_color": css(S_BUTTON, "background-color", PRIMARY),
        "css_button_border_radius": css(S_BUTTON, "border-radius",
                                        {"desktop": "8px 8px 8px 8px"}),
        "css_button_padding": css(S_BUTTON, "padding",
                                  pad({"top": "0.5rem", "right": "1rem",
                                       "bottom": "0.5rem", "left": "1rem"})),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   {"desktop": {"left": "auto"}, "mobile": {"left": "auto"}}),
    }, size="1/5", tablet="1/5", mobile="1/5", title="Project link"),
    item("plain_text", {
        "content": "{postmeta:ubicacion}",
        "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
        "css_desc_typography": t_pm(S_DESC),
        "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
    }, title="Project location"),
]

otros = section(
    sec_base(
        pad({"top": "7.5rem", "right": "2.25rem", "bottom": "7.5rem", "left": "2.25rem"},
            {"top": "5rem", "right": "2rem", "bottom": "5rem", "left": "2rem"},
            {"top": "3.5rem", "right": "1.25rem", "bottom": "3.5rem", "left": "1.25rem"}),
        {
            "background_switcher": "default",
            "css_advanced_background_color": css(S_SECTION, "background-color", WHITE),
        }),
    [
        wrap(
            dict(wrap_width("650px", "60%"), **{
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "4rem"}, None, {"bottom": "1.5rem"})),
            }),
            [
                item("heading", {
                    "title": "Otros proyectos que resolvimos desde Nordés ancín",
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", BLACK),
                    "css_typography": t_h2(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Otros proyectos — titular"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Otros proyectos — cabecera"),
        wrap(
            {
                "css_advanced_align_self": css(S_WRAP, "align-self", {"desktop": "flex-end"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "4rem"}, None, {"bottom": "2.5rem"})),
            },
            [
                item("button", btn("Todos los proyectos", "/proyectos/", PRIMARY, WHITE, {
                    "css__text_align": css(S_ITEM, "text-align",
                                           {"desktop": "right", "mobile": "left"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }), title="Otros proyectos — botón"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Otros proyectos — acción"),
        wrap(
            {
                "type": "query",
                "query_type": "posts",
                "query_post_type": "portfolio",
                "query_post_orderby": "rand",
                "query_post_order": "DESC",
                "query_post_per_page": "3",
                "query_display": "",
                "grid": "grid",
                "grid_columns_switcher": "",
                "css_grid_columns": css(S_WRAP_GRID, "grid-template-columns",
                                        {"desktop": "repeat(3, 1fr)",
                                         "tablet": "repeat(2, 1fr)",
                                         "mobile": "1fr"}),
                "css_grid_columns_gap": css(S_WRAP_GRID, "column-gap",
                                            {"desktop": "4rem", "tablet": "2rem", "mobile": "0px"}),
                "css_grid_rows_gap": css(S_WRAP_GRID, "row-gap",
                                         {"desktop": "4rem", "tablet": "3rem", "mobile": "2.5rem"}),
            },
            [nested({"css_advanced_position": css(S_WRAP_IN, "position", "relative")},
                    CARD_ITEMS, size="1/1", tablet="1/1", mobile="1/1",
                    title="Tarjeta proyecto")],
            size="1/1", tablet="1/1", mobile="1/1", title="Otros proyectos — listado"),
    ],
    title="Otros proyectos")

# ================================================================ 5. CONTACTO
LEGAL = (
    "Los datos personales facilitados voluntariamente por usted, a través del presente "
    "formulario web serán tratados, por Nordés Ancín, S.A., con su consentimiento, con la "
    "finalidad de atender su solicitud, consulta, queja o sugerencia, sin que se produzca "
    "comunicaciones o cesiones de datos y conservados durante los plazos necesarios para "
    "atender su solicitud. Puede usted ejercer los derechos de acceso, rectificación o "
    "supresión de sus datos, dirigiéndose a lopd@nordesancin.com, para más información al "
    "respecto, puede consultar nuestra <a href=\"/politica-de-privacidad/\">Política de "
    "Privacidad</a>."
)

contacto = section(
    sec_base(
        pad({"top": "7.5rem", "right": "2.25rem", "bottom": "7.5rem", "left": "2.25rem"},
            {"top": "5rem", "right": "2rem", "bottom": "5rem", "left": "2rem"},
            {"top": "3rem", "right": "1.25rem", "bottom": "3rem", "left": "1.25rem"}),
        {
            "background_switcher": "default",
            "css_advanced_background_color": css(S_SECTION, "background-color", OFFWHITE),
            "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "center"}),
        }),
    [
        wrap(
            {
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"right": "7.5rem"}, {"right": "3rem"}, {"right": "0"})),
            },
            [
                item("heading", {
                    "title": "¿Tienes un proyecto en mente? Te escuchamos",
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", TEXTDARK),
                    "css_typography": t_h2(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }, title="Contacto — titular"),
                item("heading", {
                    "title": ("Cuéntanos qué necesitas y nuestro equipo técnico te ayudará "
                              "a definir la mejor solución para tu instalación."),
                    "header_tag": "p",
                    "css_color": css(S_TITLE_C, "color", NEUTRAL2),
                    "css_typography": t_pl(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "4rem"}, None, {"bottom": "2rem"})),
                }, size="5/6", tablet="1/1", mobile="1/1", title="Contacto — descripción"),
                item("plain_text", {
                    "content": "CONTACTO",
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": t_caps(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "2.25rem"}, None, {"bottom": "1rem"})),
                }, title="Contacto — etiqueta"),
                item("heading", {
                    "title": "Polígono Espíritu Santo, c/ Monier 9-11, parcelas 36-38, 15650 Cambre",
                    "header_tag": "p",
                    "css_color": css(S_TITLE_C, "color", BLACK),
                    "css_typography": t_pl(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }, size="3/5", tablet="1/1", mobile="1/1", title="Contacto — dirección"),
                item("plain_text", {
                    "content": "<a href=\"tel:+34981138338\">+34 981 138 338</a>",
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": t_pm(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }, title="Contacto — teléfono"),
                item("plain_text", {
                    "content": "<a href=\"mailto:info@nordesancin.com\">info@nordesancin.com</a>",
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": t_pm(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Contacto — email"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Contacto — intro"),
        wrap(
            {
                "background_switcher": "default",
                "css_advanced_background_color": css(S_WRAP_IN, "background-color", WHITE),
                "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                                  {"desktop": "16px 16px 16px 16px"}),
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"top": "2.25rem", "right": "2.25rem",
                                                 "bottom": "2.25rem", "left": "2.25rem"},
                                                None,
                                                {"top": "1.5rem", "right": "1.25rem",
                                                 "bottom": "1.5rem", "left": "1.25rem"})),
            },
            [
                item("heading", {
                    "title": "Escríbenos",
                    "header_tag": "h3",
                    "css_color": css(S_TITLE_C, "color", TEXTDARK),
                    "css_typography": t_h3(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1rem"}, None, {"bottom": "0.5rem"})),
                }, title="Formulario — título"),
                item("heading", {
                    "title": "Respondemos a empresas en menos de 24 horas laborables.",
                    "header_tag": "p",
                    "css_color": css(S_TITLE_C, "color", DARKGRAY),
                    "css_typography": t_pl(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "2.25rem"}, None, {"bottom": "1.5rem"})),
                }, title="Formulario — descripción"),
                item("cf7", {
                    "form": "",
                    "css_formformlabel_color": css(
                        ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form,"
                        ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form label",
                        "color", NEUTRAL2),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "2.25rem"}, None, {"bottom": "1.5rem"})),
                }, title="Formulario"),
                item("plain_text", {
                    "content": LEGAL,
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": t_ps(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Formulario — texto legal"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Contacto — formulario"),
    ],
    title="Contacto — Formulario proyectos")

# ================================================================ 6. CTA
cta = section(
    sec_base(
        pad({"top": "7.5rem", "right": "2.25rem", "bottom": "7.5rem", "left": "2.25rem"},
            {"top": "5rem", "right": "2rem", "bottom": "5rem", "left": "2rem"},
            {"top": "4rem", "right": "1.25rem", "bottom": "4rem", "left": "1.25rem"}),
        dict(sec_bg_image("cta-portada.jpg"), **{
            "height_switcher": "custom",
            "css_advanced_height": css(S_SECTION, "height",
                                       {"desktop": "960px", "tablet": "700px", "mobile": "auto"}),
            "background_overlay_switcher": "default",
            "css_advanced_background_overlay_background_color":
                css(S_SECT_OVER, "background-color", "rgba(0,22,137,0.55)"),
            "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "center"}),
            "css_advanced_justify_content": css(S_SECT_WRAP, "justify-content",
                                                {"desktop": "center"}),
        })),
    [
        wrap(
            wrap_width("904px", "80%"),
            [
                item("heading", {
                    "title": "Preparemos una solución a medida",
                    "header_tag": "h2",
                    "css_txt_align": css(S_TITLE, "text-align", {"desktop": "center"}),
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": typo(S_TITLE,
                                           {"font-size": "120px", "line-height": "1.1",
                                            "letter-spacing": "-7.2px", "font-weight": "400"},
                                           {"font-size": "72px", "line-height": "1.1",
                                            "letter-spacing": "-4.32px", "font-weight": "400"},
                                           {"font-size": "40px", "line-height": "1.15",
                                            "letter-spacing": "-2.4px", "font-weight": "400"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "4rem"}, None, {"bottom": "2rem"})),
                }, title="CTA — titular"),
                item("button", btn("Ponte en contacto", "/contacto/", WHITE, BLACK, {
                    "css__text_align": css(S_ITEM, "text-align", {"desktop": "center"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }), title="CTA — botón"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="CTA — contenido"),
    ],
    title="CTA — Preparemos una solución a medida")

# ================================================================ salida
data = [hero, reto, galeria, otros, contacto, cta]

with open(HERE / "nordes-ancin-proyecto.json", "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("secciones:", len(data))
print("wraps:", sum(len(s["wraps"]) for s in data))
