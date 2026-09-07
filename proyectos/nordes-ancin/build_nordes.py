# -*- coding: utf-8 -*-
"""Genera el JSON BeBuilder de 'Listado de proyectos' (Nordes Ancin, Figma 2572:15432)."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- tokens
PRIMARY   = "#001689"
BLACK     = "#1F1F1F"
DARKGRAY  = "#6B6B6B"   # neutrals/dark-gray
WHITE     = "#FCFCFC"
OFFWHITE  = "#F1F1EE"
GRAYLABEL = "#A3A3A3"
TITLEDARK = "#2C2926"   # text-dark
MEDIA     = "https://nordesancin.com/wp-content/uploads/2026/07/"

# selectores base
S_SECTION   = ".mcb-section-mfnuidelement"
S_SECT_WRAP = ".mcb-section-mfnuidelement .section_wrapper"
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

def _no_zero(side_vals):
    """PHP `empty()` descarta "0": el helper no emitiria la regla y quedaria el
    margen por defecto del theme (`class-mfn-helper.php:198` y `:406`)."""
    return {k: ("0px" if v in ("0", 0) else v) for k, v in side_vals.items()}

def pad(desktop, tablet=None, mobile=None):
    # Regla del proyecto: todo espaciado lleva valor mobile. Cuando el diseno no
    # pide un valor distinto (p. ej. "bottom": 0), se replica el de desktop.
    val = {"desktop": _no_zero(desktop)}
    if tablet:
        val["tablet"] = _no_zero(tablet)
    val["mobile"] = _no_zero(mobile) if mobile else _no_zero(desktop)
    return val

# ================================================================ 1. HERO
hero = section(
    {
        "width_switcher": "full",
        "height_switcher": "custom",
        "background_switcher": "default",
        "background_overlay_switcher": "default",
        "css_advanced_height": css(S_SECTION, "height",
                                   {"desktop": "600px", "tablet": "520px", "mobile": "460px"}),
        "css_advanced_background_image": css(S_SECTION, "background-image",
                                             {"desktop": MEDIA + "hero-listado-proyectos.jpg"}),
        "css_advanced_background_size": css(S_SECTION, "background-size", {"desktop": "cover"}),
        "css_advanced_background_position": css(S_SECTION, "background-position", {"desktop": "center"}),
        "css_advanced_background_repeat": css(S_SECTION, "background-repeat", {"desktop": "no-repeat"}),
        "css_advanced_background_overlay_background_color":
            css(S_SECT_OVER, "background-color", "rgba(0,0,0,0.4)"),
        "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "flex-end"}),
        "css_advanced_padding": css(S_SECTION, "padding",
                                    pad({"top": "10rem", "bottom": "4rem"},
                                        {"top": "8rem", "bottom": "3rem"},
                                        {"top": "7rem", "bottom": "2.5rem"})),
    },
    [
        wrap({}, [
            item("heading", {
                "title": "Proyectos destacados de instalaciones técnicas para cada sector",
                "header_tag": "h1",
                "css_color": css(S_TITLE_C, "color", WHITE),
                "css_typography": typo(S_TITLE,
                    {"font-size": "64px", "line-height": "1.1", "letter-spacing": "-3.2px", "font-weight": "500"},
                    {"font-size": "48px", "line-height": "1.1", "letter-spacing": "-2px", "font-weight": "500"},
                    {"font-size": "34px", "line-height": "1.15", "letter-spacing": "-1.2px", "font-weight": "500"}),
                "css_advanced_margin": css(S_ITEM_IN, "margin",
                                           pad({"bottom": "0"}, None, {"bottom": "1.5rem"})),
            })
        ], size="1/2", tablet="1/2", mobile="1/1", title="Hero title"),
        wrap({}, [
            item("plain_text", {
                "content": ("Contamos con una amplia experiencia en el desarrollo de proyectos para "
                            "diferentes sectores. Cada proyecto refleja nuestro compromiso con la calidad, "
                            "la eficiencia y la adaptación a las necesidades específicas de cada cliente."),
                "css_descdesca_color": css(S_DESC_C, "color", OFFWHITE),
                "css_desc_typography": typo(S_DESC,
                    {"font-size": "22px", "line-height": "1.6"},
                    None,
                    {"font-size": "17px", "line-height": "1.6"}),
            })
        ], size="1/2", tablet="1/2", mobile="1/1", title="Hero text"),
    ],
    title="Hero — Listado de proyectos")

# ================================================================ 2. GRID (query loop)
# CON wrap anidado, obligatorio. La tarjeta de un query loop de WRAP va dentro de
# un `item_is_wrap: 1`, nunca como items directos del wrap del loop.
#
# Medido en el servidor (post 715, 2026-07-29): importada la version con 5 items
# directos y guardada una vez en el VB, la BD queda con el wrap del loop conteniendo
# UN wrap anidado VACIO -> 53 items importados, 49 guardados. El VB envuelve los
# `div.column` de la iteracion en un contenedor (scripts.js:7364) y al reconstruir
# el arbol prepareForm.items() (scripts.js:2317-2323, cascada de selectores
# .children) resuelve ese contenedor como nested wrap y sus hijos se pierden.
# Sin nodos no hay CSS: por eso el boton salia sin fondo y la imagen sin altura.
#
# El export real del propio VB usa siempre esta forma:
# examples/example2/home.json -> wrap query -> item_is_wrap:1 -> image+button+heading.
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
        # superpuesta a la imagen, como en Figma (24px desde la esquina)
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
        "css_image_cover_height": css(
            ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame.mfn-coverimg .image_wrapper img",
            "height", {"desktop": "360px", "tablet": "320px", "mobile": "260px"}),
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
        "css_typography": typo(S_TITLE,
            {"font-size": "36px", "line-height": "1.24", "letter-spacing": "-0.72px", "font-weight": "500"},
            {"font-size": "30px", "line-height": "1.24", "letter-spacing": "-0.6px", "font-weight": "500"},
            {"font-size": "26px", "line-height": "1.24", "letter-spacing": "-0.5px", "font-weight": "500"}),
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
        "css_desc_typography": typo(S_DESC,
            {"font-size": "18px", "line-height": "1.6"},
            None,
            {"font-size": "16px", "line-height": "1.6"}),
        "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
    }, title="Project location"),
]

grid = section(
    {
        "width_switcher": "",
        "css_advanced_padding": css(S_SECTION, "padding",
                                    pad({"top": "4rem", "bottom": "7.5rem"},
                                        {"top": "3rem", "bottom": "5rem"},
                                        {"top": "2.5rem", "bottom": "3rem"})),
    },
    [
        wrap(
            {
                "type": "query",
                "query_type": "posts",
                "query_post_type": "portfolio",
                "query_post_orderby": "menu_order",
                "query_post_order": "ASC",
                "query_post_per_page": "12",
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
            title="Grid proyectos"),
    ],
    title="Grid de proyectos")

# ================================================================ 3. HIGHLIGHT
highlight = section(
    {
        "width_switcher": "full",
        "height_switcher": "custom",
        "background_switcher": "default",
        "css_advanced_height": css(S_SECTION, "height",
                                   {"desktop": "1117px", "tablet": "760px", "mobile": "560px"}),
        "css_advanced_background_image": css(S_SECTION, "background-image",
                                             {"desktop": MEDIA + "highlight-proyectos.jpg"}),
        "css_advanced_background_size": css(S_SECTION, "background-size", {"desktop": "cover"}),
        "css_advanced_background_position": css(S_SECTION, "background-position", {"desktop": "center"}),
        "css_advanced_background_repeat": css(S_SECTION, "background-repeat", {"desktop": "no-repeat"}),
        "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "flex-end"}),
        "css_advanced_padding": css(S_SECTION, "padding",
                                    pad({"top": "4rem", "bottom": "4rem"},
                                        None,
                                        {"top": "2rem", "bottom": "2rem"})),
    },
    [
        wrap(
            {
                "background_switcher": "default",
                "css_advanced_background_color": css(S_WRAP_IN, "background-color", "rgba(31,31,31,0.72)"),
                "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                                  {"desktop": "12px 12px 12px 12px"}),
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"top": "2.5rem", "right": "2.5rem",
                                                 "bottom": "2.5rem", "left": "2.5rem"},
                                                None,
                                                {"top": "1.5rem", "right": "1.5rem",
                                                 "bottom": "1.5rem", "left": "1.5rem"})),
            },
            [
                item("heading", {
                    "title": "Conoce lo que podemos hacer por tu proyecto",
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": typo(S_TITLE,
                        {"font-size": "40px", "line-height": "1.2", "letter-spacing": "-1.6px", "font-weight": "500"},
                        None,
                        {"font-size": "28px", "line-height": "1.2", "letter-spacing": "-1px", "font-weight": "500"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }),
                item("plain_text", {
                    "content": ("Ofrecemos servicios integrales y a medida para todo tipo de sectores, "
                                "adaptándonos a las necesidades de cada cliente."),
                    "css_descdesca_color": css(S_DESC_C, "color", OFFWHITE),
                    "css_desc_typography": typo(S_DESC,
                        {"font-size": "18px", "line-height": "1.6"},
                        None,
                        {"font-size": "16px", "line-height": "1.6"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "2rem"}, None, {"bottom": "1.5rem"})),
                }),
                item("button", {
                    "title": "Nuestros servicios",
                    "link": "/servicios/",
                    "background_switcher": "default",
                    "icon": "icon-right-thin",
                    "icon_position": "right",
                    "full_width": "1",
                    "css_button_color": css(S_BUTTON, "color", BLACK),
                    "css_button_icon_color": css(S_BUTTON + " i", "color", BLACK),
                    "css_button_background_color": css(S_BUTTON, "background-color", WHITE),
                    "css_button_border_radius": css(S_BUTTON, "border-radius",
                                                    {"desktop": "8px 8px 8px 8px"}),
                    "css_button_padding": css(S_BUTTON, "padding",
                                              pad({"top": "1rem", "right": "1.5rem",
                                                   "bottom": "1rem", "left": "1.5rem"})),
                    "css_button_typography": typo(S_BUTTON,
                        {"font-size": "18px", "line-height": "1.4"},
                        None,
                        {"font-size": "16px", "line-height": "1.4"}),
                }),
            ],
            size="1/3", tablet="1/2", mobile="1/1", title="Highlight card"),
    ],
    title="Highlight")

# ================================================================ 4. SECTORES
SECTORES = [
    ("Industrial y alimentario",
     "Climatización y frío industrial para el sector industrial y alimentario",
     "Desarrollamos instalaciones para entornos industriales y alimentarios, integrando climatización, "
     "frío industrial, ventilación y electricidad para garantizar eficiencia, fiabilidad y continuidad "
     "en los procesos productivos.",
     "sector-industrial-alimentario.jpg"),
    ("Logístico",
     "Soluciones de climatización y frío industrial para el sector logístico",
     "Desarrollamos instalaciones para plataformas logísticas, centros de distribución y espacios de "
     "almacenamiento, garantizando eficiencia, fiabilidad y continuidad operativa.",
     "sector-logistico.jpg"),
    ("Edificación corporativa",
     "Instalaciones térmicas y eléctricas para oficinas y edificios corporativos",
     "Diseñamos, ejecutamos y mantenemos instalaciones para oficinas, sedes empresariales y edificios "
     "corporativos, mejorando el confort interior y optimizando el rendimiento energético.",
     "sector-edificacion-corporativa.jpg"),
    ("Comercial y retail",
     "Instalaciones para comercio, retail y espacios comerciales",
     "Creamos soluciones técnicas para tiendas, locales comerciales y grandes superficies, combinando "
     "confort, eficiencia energética y sistemas adaptados al uso diario de cada espacio.",
     "sector-comercial-retail.jpg"),
    ("Hotelero",
     "Sistemas eficientes de climatización y ACS para hoteles",
     "Desarrollamos instalaciones para hoteles y alojamientos turísticos, garantizando confort, eficiencia "
     "energética, disponibilidad de agua caliente y un funcionamiento fiable durante todo el año.",
     "sector-hotelero.jpg"),
    ("Sanitario y farmacéutico",
     "Control ambiental para espacios sanitarios y farmacéuticos",
     "Ejecutamos instalaciones para hospitales, clínicas, laboratorios y espacios farmacéuticos, "
     "priorizando el control ambiental, la calidad del aire, la eficiencia y la seguridad operativa.",
     "sector-sanitario-farmaceutico.jpg"),
    ("Deportivo y ocio",
     "Climatización y eficiencia para centros deportivos y de ocio",
     "Diseñamos instalaciones de climatización, ventilación, calefacción, ACS y electricidad para "
     "espacios deportivos y de ocio, priorizando el confort de los usuarios y la eficiencia del edificio.",
     "sector-deportivo-ocio.jpg"),
    ("Aeronáutico",
     "Soluciones técnicas para instalaciones aeronáuticas y aeroportuarias",
     "Desarrollamos soluciones para aeropuertos e instalaciones aeronáuticas, preparadas para grandes "
     "superficies, altos niveles de ocupación y entornos que requieren máxima fiabilidad y continuidad "
     "operativa.",
     "sector-aeronautico.jpg"),
    ("Cultural e institucional",
     "Confort y eficiencia en edificios culturales e institucionales",
     "Diseñamos instalaciones para edificios culturales, administrativos e institucionales, combinando "
     "confort, eficiencia y flexibilidad para responder a los distintos usos, niveles de ocupación y "
     "necesidades de cada espacio.",
     "sector-cultural-institucional.jpg"),
]

sector_wraps = []
for eyebrow, titulo, desc, img in SECTORES:
    sector_wraps.append(wrap(
        {
            "css_advanced_padding": css(S_WRAP_IN, "padding",
                                        pad({"right": "4rem"}, {"right": "2rem"}, {"right": "0"})),
            "css_advanced_margin": css(S_WRAP_IN, "margin",
                                       pad({"bottom": "4rem"}, {"bottom": "3rem"}, {"bottom": "1.5rem"})),
        },
        [
            item("plain_text", {
                "content": eyebrow.upper(),
                "css_descdesca_color": css(S_DESC_C, "color", PRIMARY),
                "css_desc_typography": typo(S_DESC,
                    {"font-size": "16px", "line-height": "1.25", "text-transform": "uppercase", "font-weight": "500"},
                    None,
                    {"font-size": "14px", "line-height": "1.25", "text-transform": "uppercase", "font-weight": "500"}),
                "css_advanced_margin": css(S_ITEM_IN, "margin",
                                           pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
            }, title="Sector eyebrow"),
            item("heading", {
                "title": titulo,
                "header_tag": "h2",
                "css_color": css(S_TITLE_C, "color", BLACK),
                "css_typography": typo(S_TITLE,
                    {"font-size": "48px", "line-height": "1.2", "letter-spacing": "-1.92px", "font-weight": "500"},
                    {"font-size": "38px", "line-height": "1.2", "letter-spacing": "-1.4px", "font-weight": "500"},
                    {"font-size": "30px", "line-height": "1.2", "letter-spacing": "-1px", "font-weight": "500"}),
                "css_advanced_margin": css(S_ITEM_IN, "margin",
                                           pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
            }, title="Sector title"),
            item("plain_text", {
                "content": desc,
                "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                "css_desc_typography": typo(S_DESC,
                    {"font-size": "18px", "line-height": "1.6"},
                    None,
                    {"font-size": "16px", "line-height": "1.6"}),
                "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
            }, title="Sector description"),
        ],
        size="1/2", tablet="1/2", mobile="1/1", title="Sector text — " + eyebrow))

    sector_wraps.append(wrap(
        {
            "css_advanced_margin": css(S_WRAP_IN, "margin",
                                       pad({"bottom": "4rem"}, {"bottom": "3rem"}, {"bottom": "3rem"})),
        },
        [
            item("image", {
                "src": MEDIA + img,
                "stretch": "1",
                "alt": titulo,
                "css_image_border_radius": css(S_IMGFRAME, "border-radius",
                                               {"desktop": "12px 12px 12px 12px"}),
                "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
            }, title="Sector image")
        ],
        size="1/2", tablet="1/2", mobile="1/1", title="Sector image — " + eyebrow))

sectores = section(
    {
        "width_switcher": "",
        "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "center"}),
        "css_advanced_padding": css(S_SECTION, "padding",
                                    pad({"top": "7.5rem", "bottom": "3.5rem"},
                                        {"top": "5rem", "bottom": "2rem"},
                                        {"top": "3rem", "bottom": "1rem"})),
    },
    sector_wraps,
    title="Sectores")

# ================================================================ 5. CONTACTO
contacto = section(
    {
        "width_switcher": "",
        "background_switcher": "default",
        "css_advanced_background_color": css(S_SECTION, "background-color", OFFWHITE),
        "css_advanced_padding": css(S_SECTION, "padding",
                                    pad({"top": "7.5rem", "bottom": "7.5rem"},
                                        {"top": "5rem", "bottom": "5rem"},
                                        {"top": "3rem", "bottom": "3rem"})),
    },
    [
        wrap(
            {
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"right": "4rem"}, {"right": "2rem"}, {"right": "0"})),
            },
            [
                item("heading", {
                    "title": "¿Tienes un proyecto en mente? Te escuchamos",
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", TITLEDARK),
                    "css_typography": typo(S_TITLE,
                        {"font-size": "48px", "line-height": "1.2", "letter-spacing": "-1.92px", "font-weight": "500"},
                        {"font-size": "38px", "line-height": "1.2", "letter-spacing": "-1.4px", "font-weight": "500"},
                        {"font-size": "30px", "line-height": "1.2", "letter-spacing": "-1px", "font-weight": "500"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }, title="Contact title"),
                item("plain_text", {
                    "content": ("Cuéntanos qué necesitas y nuestro equipo técnico te ayudará "
                                "a definir la mejor solución para tu instalación."),
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": typo(S_DESC,
                        {"font-size": "18px", "line-height": "1.6"},
                        None,
                        {"font-size": "16px", "line-height": "1.6"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "4rem"}, None, {"bottom": "2rem"})),
                }, title="Contact description"),
                item("plain_text", {
                    "content": "CONTACTO",
                    "css_descdesca_color": css(S_DESC_C, "color", GRAYLABEL),
                    "css_desc_typography": typo(S_DESC,
                        {"font-size": "18px", "line-height": "1.6", "text-transform": "uppercase"},
                        None,
                        {"font-size": "15px", "line-height": "1.6", "text-transform": "uppercase"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "2rem"}, None, {"bottom": "1rem"})),
                }, title="Contact label"),
                item("plain_text", {
                    "content": "Polígono Espíritu Santo, c/ Monier 9-11, parcelas 36-38, 15650 Cambre",
                    "css_descdesca_color": css(S_DESC_C, "color", TITLEDARK),
                    "css_desc_typography": typo(S_DESC,
                        {"font-size": "18px", "line-height": "1.6"},
                        None,
                        {"font-size": "16px", "line-height": "1.6"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }, title="Contact address"),
                item("plain_text", {
                    "content": "<a href=\"tel:+34981138338\">+34 981 138 338</a>",
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": typo(S_DESC,
                        {"font-size": "18px", "line-height": "1.6"},
                        None,
                        {"font-size": "16px", "line-height": "1.6"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }, title="Contact phone"),
                item("plain_text", {
                    "content": "<a href=\"mailto:info@nordesancin.com\">info@nordesancin.com</a>",
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": typo(S_DESC,
                        {"font-size": "18px", "line-height": "1.6"},
                        None,
                        {"font-size": "16px", "line-height": "1.6"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Contact email"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Contacto intro"),
        wrap(
            {
                "background_switcher": "default",
                "css_advanced_background_color": css(S_WRAP_IN, "background-color", WHITE),
                "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                                  {"desktop": "12px 12px 12px 12px"}),
                "css_advanced_box_shadow": css(S_WRAP_IN, "box-shadow",
                                               "0 4px 24px rgba(0,15,92,0.05)"),
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
                    "css_color": css(S_TITLE_C, "color", TITLEDARK),
                    "css_typography": typo(S_TITLE,
                        {"font-size": "32px", "line-height": "1.2", "letter-spacing": "-1px", "font-weight": "500"},
                        None,
                        {"font-size": "24px", "line-height": "1.2", "letter-spacing": "-0.6px", "font-weight": "500"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "0.75rem"}, None, {"bottom": "0.5rem"})),
                }, title="Form title"),
                item("plain_text", {
                    "content": "Respondemos a empresas en menos de 24 horas laborables.",
                    "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                    "css_desc_typography": typo(S_DESC,
                        {"font-size": "16px", "line-height": "1.6"},
                        None,
                        {"font-size": "15px", "line-height": "1.6"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "2rem"}, None, {"bottom": "1.5rem"})),
                }, title="Form description"),
                item("cf7", {
                    "form": "",
                    "css_formformlabel_color": css(
                        ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form,"
                        ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form label",
                        "color", TITLEDARK),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Formulario"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Formulario"),
    ],
    title="Contacto — Formulario proyectos")

# ================================================================ salida
data = [hero, grid, highlight, sectores, contacto]

import sys
out = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "nordes-ancin-listado-proyectos.json"
with open(out, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)
print("secciones:", len(data))
print("wraps:", sum(len(s["wraps"]) for s in data))
