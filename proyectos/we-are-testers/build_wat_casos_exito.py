# -*- coding: utf-8 -*-
"""Genera el JSON BeBuilder de la página 'Casos de éxito' (We Are Testers, Figma 4375:3952).

Solo el contenido de página: el header y el footer del diseño son plantillas globales de BeTheme
y no se incluyen aquí.

Regla de proyecto: contenedor interior a 1728px (`width_switcher: "custom"` +
`css_advanced_max_width` sobre `.section_wrapper`) y padding lateral según el diseño
(36px en el hero, 64px en la sección de casos, 80/120px en CTA y clientes).

Assets esperados en MEDIA (ver assets/we-are-testers/):
  hero-foto.png, hero-fondo.jpg, caso-eroski.png, caso-unicaja.png, caso-azti.png,
  caso-europcar.png, cta-fondo.jpg, eyebrow-cuadrado.svg
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- tokens (Figma)
PRIMARY    = "#7F41F5"   # primary
BRAND_DARK = "#5717CF"   # background/bg-brand, text/text-fg-brand
NEUTRAL1   = "#221C3D"   # neutrals/neutral-1 (titulares)
HEADING    = "#101828"   # text/text-heading
BODY       = "#4A5565"   # text/text-body
NEUTRAL4   = "#C5C7C8"   # neutrals/neutral-4 (borde pills)
NEUTRAL5   = "#F4F7F9"   # neutrals/neutral-5
DIVIDER    = "#E5E7EB"
WHITE      = "#FFFFFF"
BLACK      = "#000000"
MEDIA      = "https://wearetesters.com/wp-content/uploads/2026/08/"

MAXW = "1728px"

# selectores base
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
S_BC        = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .breadcrumbs"
S_CLI_WRAP  = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider_ul li .client_wrapper"

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
    """PHP `empty()` descarta "0": se escribe "0px" para que el helper emita la regla."""
    return {k: ("0px" if v in ("0", 0) else v) for k, v in side_vals.items()}


def pad(desktop, tablet=None, mobile=None):
    """Todo espaciado lleva valor mobile; si el diseño no pide otro, replica desktop."""
    val = {"desktop": _no_zero(desktop)}
    if tablet:
        val["tablet"] = _no_zero(tablet)
    val["mobile"] = _no_zero(mobile) if mobile else _no_zero(desktop)
    return val


def m0(bottom="0", mobile_bottom=None):
    """Margen del item: anula el default del theme (12px laterales, 40px abajo)."""
    return css(S_ITEM_IN, "margin",
               pad({"top": "0", "right": "0", "bottom": bottom, "left": "0"}, None,
                   {"top": "0", "right": "0", "bottom": mobile_bottom or bottom, "left": "0"}))


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
    """Contenedor interior a 1728px + padding del diseño."""
    attr = {
        "width_switcher": "custom",
        "css_advanced_max_width": css(S_SECT_MAXW, "max-width", MAXW),
        "css_advanced_padding": css(S_SECTION, "padding", pad_val),
    }
    if extra:
        attr.update(extra)
    return attr


def sec_bg(color, image=None):
    attr = {
        "background_switcher": "default",
        "css_advanced_background_color": css(S_SECTION, "background-color", color),
    }
    if image:
        attr.update({
            "css_advanced_background_image": css(S_SECTION, "background-image",
                                                 {"desktop": MEDIA + image}),
            "css_advanced_background_size": css(S_SECTION, "background-size", {"desktop": "cover"}),
            "css_advanced_background_position": css(S_SECTION, "background-position",
                                                    {"desktop": "center"}),
            "css_advanced_background_repeat": css(S_SECTION, "background-repeat",
                                                  {"desktop": "no-repeat"}),
        })
    return attr


def wrap_bg(color, image=None):
    attr = {
        "background_switcher": "default",
        "css_advanced_background_color": css(S_WRAP_IN, "background-color", color),
    }
    if image:
        attr.update({
            "css_advanced_background_image": css(S_WRAP_IN, "background-image",
                                                 {"desktop": MEDIA + image}),
            "css_advanced_background_size": css(S_WRAP_IN, "background-size", {"desktop": "cover"}),
            "css_advanced_background_position": css(S_WRAP_IN, "background-position",
                                                    {"desktop": "center"}),
            "css_advanced_background_repeat": css(S_WRAP_IN, "background-repeat",
                                                  {"desktop": "no-repeat"}),
        })
    return attr


def btn(title, link, bg, fg, icon_color=None, extra=None):
    """Button_prim del diseño: icono flecha a la izquierda, texto 18px, sin radio.
    El diseño usa una flecha diagonal (↗); BeTheme no la trae de serie, se usa `icon-right-thin`
    (para la diagonal exacta, pack propio: docs/bebuilder/07-iconos.md §9)."""
    attr = {
        "title": title,
        "link": link,
        "icon": "icon-right-thin",
        "icon_position": "left",
        "button_style": "",
        "background_switcher": "default",
        "css_button_color": css(S_BUTTON, "color", fg),
        "css_button_icon_color": css(S_BUTTON + " i", "color", icon_color or fg),
        "css_button_background_color": css(S_BUTTON, "background-color", bg),
        "css_button_border_radius": css(S_BUTTON, "border-radius",
                                        {"desktop": "0px 0px 0px 0px"}),
        "css_button_gap": css(S_BUTTON, "gap", {"desktop": "16px", "mobile": "12px"}),
        "css_button_icon_size": css(S_BUTTON + " .button_icon", "font-size",
                                    {"desktop": "20px", "mobile": "18px"}),
        "css_button_padding": css(S_BUTTON, "padding",
                                  pad({"top": "0.625rem", "right": "1.5rem",
                                       "bottom": "0.625rem", "left": "0.75rem"},
                                      None,
                                      {"top": "0.625rem", "right": "1.25rem",
                                       "bottom": "0.625rem", "left": "0.75rem"})),
        "css_button_typography": typo(S_BUTTON,
                                      {"font-size": "18px", "line-height": "1.4",
                                       "font-weight": "400"},
                                      None,
                                      {"font-size": "16px", "line-height": "1.4",
                                       "font-weight": "400"}),
        "css_advanced_margin": m0(),
    }
    if extra:
        attr.update(extra)
    return attr


def pill(text):
    """Etiqueta de servicio (COMUNIDADES ONLINE…): button sin enlace, outline gris, radio total.
    `width_switcher: inline` para que varias queden en fila."""
    return item("button", {
        "title": text,
        "link": "",
        "icon": "",
        "button_style": "",
        "width_switcher": "inline",
        "background_switcher": "default",
        "css_button_color": css(S_BUTTON, "color", BLACK),
        "css_button_background_color": css(S_BUTTON, "background-color", "transparent"),
        "css_button_border_style": css(S_BUTTON, "border-style", "solid"),
        "css_button_border_width": css(S_BUTTON, "border-width", {"desktop": "1px 1px 1px 1px"}),
        "css_button_border_color": css(S_BUTTON, "border-color", NEUTRAL4),
        "css_button_border_radius": css(S_BUTTON, "border-radius",
                                        {"desktop": "2000px 2000px 2000px 2000px"}),
        "css_button_padding": css(S_BUTTON, "padding",
                                  pad({"top": "0.375rem", "right": "0.75rem",
                                       "bottom": "0.375rem", "left": "0.75rem"})),
        "css_button_typography": typo(S_BUTTON,
                                      {"font-size": "12px", "line-height": "1.3",
                                       "font-weight": "500", "text-transform": "uppercase"},
                                      None,
                                      {"font-size": "11px", "line-height": "1.3",
                                       "font-weight": "500", "text-transform": "uppercase"}),
        "css_button_background_hover": css(S_BUTTON + ":hover, " + S_BUTTON + ":before",
                                           "background", NEUTRAL5),
        "css_button_color_hover": css(S_BUTTON + ":hover", "color", BLACK),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   pad({"top": "0", "right": "0.75rem", "bottom": "0", "left": "0"})),
    }, size="1/4", tablet="1/4", mobile="1/2", title="Etiqueta — " + text)


# tipografías del diseño ------------------------------------------------
def t_h2(sel):        # h2 · Figtree SemiBold 68 / 1 / -1.36px
    return typo(sel,
                {"font-size": "68px", "line-height": "1", "letter-spacing": "-1.36px",
                 "font-weight": "600"},
                {"font-size": "48px", "line-height": "1.05", "letter-spacing": "-1px",
                 "font-weight": "600"},
                {"font-size": "36px", "line-height": "1.1", "letter-spacing": "-0.7px",
                 "font-weight": "600"})


def t_h60(sel):       # text-6xl/font-semibold · 60 / 1.5
    return typo(sel,
                {"font-size": "60px", "line-height": "1.2", "font-weight": "600"},
                {"font-size": "44px", "line-height": "1.2", "font-weight": "600"},
                {"font-size": "34px", "line-height": "1.2", "font-weight": "600"})


def t_h30(sel):       # text-3xl/font-semibold · 30 / 1.5
    return typo(sel,
                {"font-size": "30px", "line-height": "1.5", "font-weight": "600"},
                None,
                {"font-size": "22px", "line-height": "1.4", "font-weight": "600"})


def t_eyebrow(sel):   # h2_02 · 24 / 1.1 / -0.48px uppercase
    return typo(sel,
                {"font-size": "24px", "line-height": "1.1", "letter-spacing": "-0.48px",
                 "font-weight": "600", "text-transform": "uppercase"},
                None,
                {"font-size": "18px", "line-height": "1.1", "letter-spacing": "-0.36px",
                 "font-weight": "600", "text-transform": "uppercase"})


def t_p24(sel):       # text-2xl/font-normal
    return typo(sel,
                {"font-size": "24px", "line-height": "1.5", "font-weight": "400"},
                None,
                {"font-size": "18px", "line-height": "1.5", "font-weight": "400"})


def t_p20(sel):       # text-xl/font-normal
    return typo(sel,
                {"font-size": "20px", "line-height": "1.5", "font-weight": "400"},
                None,
                {"font-size": "17px", "line-height": "1.5", "font-weight": "400"})


def t_p18(sel):       # text-lg/font-normal
    return typo(sel,
                {"font-size": "18px", "line-height": "1.5", "font-weight": "400"},
                None,
                {"font-size": "16px", "line-height": "1.5", "font-weight": "400"})


# eyebrow: cuadrado morado 10px + texto 24px uppercase --------------------
def eyebrow(text, center=False):
    attr = {
        "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "center"}),
        "css_advanced_margin": css(S_WRAP_IN, "margin",
                                   pad({"bottom": "2rem"}, None, {"bottom": "1.25rem"})),
    }
    if center:
        attr["css_advanced_justify_content"] = css(S_WRAP_IN, "justify-content",
                                                   {"desktop": "center"})
    return wrap(attr, [
        item("image", {
            "src": MEDIA + "eyebrow-cuadrado.svg",
            "alt": "",
            "width_switcher": "inline",
            "hover": "disable",
            "css_image_frame_width": css(S_IMGFRAME, "width", {"desktop": "10px"}),
            "css_advanced_margin": css(S_ITEM_IN, "margin",
                                       pad({"top": "0", "right": "1.125rem", "bottom": "0", "left": "0"},
                                           None,
                                           {"top": "0", "right": "0.75rem", "bottom": "0", "left": "0"})),
        }, size="1/6", tablet="1/6", mobile="1/6", title="Eyebrow — cuadrado"),
        item("heading", {
            "title": text,
            "header_tag": "p",
            "width_switcher": "inline",
            "css_color": css(S_TITLE_C, "color", NEUTRAL1),
            "css_typography": t_eyebrow(S_TITLE),
            "css_advanced_margin": m0(),
        }, size="5/6", tablet="5/6", mobile="5/6", title="Eyebrow — texto"),
    ], title="Eyebrow — " + text)


# ================================================================ 1. HERO
hero = section(
    sec_base(
        pad({"top": "0", "right": "2.25rem", "bottom": "0", "left": "2.25rem"},
            {"top": "0", "right": "1.5rem", "bottom": "0", "left": "1.5rem"},
            {"top": "0", "right": "1rem", "bottom": "0", "left": "1rem"}),
        dict(sec_bg(PRIMARY, "hero-fondo.jpg"), **{
            "height_switcher": "custom",
            "css_advanced_height": css(S_SECTION, "height",
                                       {"desktop": "900px", "tablet": "auto", "mobile": "auto"}),
            "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "stretch"}),
        })),
    [
        # Columna texto: breadcrumb arriba, titular+texto+botón abajo (space-between)
        wrap(
            {
                "height_switcher": "custom",
                "css_advanced_height": css(S_WRAP_IN, "height",
                                           {"desktop": "100%", "tablet": "auto", "mobile": "auto"}),
                "css_advanced_align_content": css(S_WRAP_IN, "align-content",
                                                  {"desktop": "space-between"}),
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"top": "3rem", "right": "3rem",
                                                 "bottom": "3rem", "left": "3rem"},
                                                {"top": "8rem", "right": "1rem",
                                                 "bottom": "2.5rem", "left": "1rem"},
                                                {"top": "7rem", "right": "0",
                                                 "bottom": "2rem", "left": "0"})),
            },
            [
                item("breadcrumbs", {
                    "separator": "/",
                    "breadcrumb_home": "1",
                    "css_breadcrumbs_typography": typo(S_BC,
                                                       {"font-size": "14px", "line-height": "1.5",
                                                        "font-weight": "600"},
                                                       None,
                                                       {"font-size": "13px", "line-height": "1.5",
                                                        "font-weight": "600"}),
                    "css_breadcrumbs_gap": css(S_BC, "gap", {"desktop": "10px"}),
                    "css_breadcrumbsli_color": css(S_BC + " li", "color", WHITE),
                    "css_breadcrumbslia_color": css(S_BC + " li a", "color", WHITE),
                    "css_breadcrumbslia_color_hover": css(S_BC + " li:hover a", "color", NEUTRAL5),
                    "css_breadcrumbsli-breadcrumbs-separator_color": css(
                        S_BC + " li .mfn-breadcrumbs-separator", "color", "rgba(255,255,255,0.6)"),
                    "css_advanced_margin": m0("0", "2rem"),
                }, title="Hero — breadcrumb"),
                item("heading", {
                    "title": "Investigación que se convierte en decisiones",
                    "header_tag": "h1",
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": t_h2(S_TITLE),
                    "css_advanced_margin": m0("2.25rem", "1.5rem"),
                }, title="Hero — titular"),
                item("plain_text", {
                    "content": ("Descubre cómo ayudamos a empresas de diferentes sectores a comprender "
                                "mejor a sus consumidores y usuarios y convertir los insights en mejores "
                                "decisiones de negocio."),
                    "css_descdesca_color": css(S_DESC_C, "color", NEUTRAL5),
                    "css_desc_typography": t_p24(S_DESC),
                    "css_advanced_margin": m0("4rem", "2rem"),
                }, title="Hero — descripción"),
                item("button", btn("Cuéntanos tu reto", "/contacto/", WHITE, BRAND_DARK, extra={
                    "width_switcher": "inline",
                }), size="1/2", tablet="1/2", mobile="1/1", title="Hero — botón"),
            ],
            size="1/2", tablet="1/1", mobile="1/1", title="Hero — texto"),
        # Columna imagen: panel morado con formas + foto recortada
        wrap(
            {
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"top": "3rem", "right": "3rem",
                                                 "bottom": "3rem", "left": "0"},
                                                {"top": "0", "right": "1rem",
                                                 "bottom": "2.5rem", "left": "1rem"},
                                                {"top": "0", "right": "0",
                                                 "bottom": "2rem", "left": "0"})),
                "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "center"}),
            },
            [
                nested(
                    dict(wrap_bg(PRIMARY, "hero-fondo.jpg"), **{
                        "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "flex-end"}),
                    }),
                    [
                        item("image", {
                            "src": MEDIA + "hero-foto.png",
                            "alt": "Equipo de We are testers analizando resultados con un cliente",
                            "stretch": "1",
                            "hover": "disable",
                            "image_height": "custom",
                            "image_height_style": "",
                            "css_image_cover_height": css(S_IMGCOVER, "height",
                                                          {"desktop": "805px", "tablet": "560px",
                                                           "mobile": "420px"}),
                            "css_advanced_margin": m0(),
                        }, title="Hero — foto"),
                    ],
                    title="Hero — panel imagen"),
            ],
            size="1/2", tablet="1/1", mobile="1/1", title="Hero — imagen"),
    ],
    title="Hero — Casos de éxito")

# ================================================================ 2. CASOS DE ÉXITO
CASOS = [
    # (cliente, titular, texto, etiquetas, imagen, link, imagen a la izquierda)
    ("Eroski",
     "Cocrear con consumidores un nuevo modelo de tienda",
     "A través de una comunidad online, Eroski pudo profundizar en las necesidades y expectativas "
     "de sus clientes para identificar las claves de una experiencia de compra ideal y orientar la "
     "definición de un nuevo modelo de tienda.",
     ["Comunidades online"], "caso-eroski.png", "/casos-de-exito/eroski/", False),
    ("Unicaja Banco",
     "Validar un nuevo producto digital antes de su lanzamiento",
     "Liberbank Digital, actualmente integrado en Unicaja Banco, confió en We are testers para "
     "validar el lanzamiento de una nueva tarjeta dirigida a un público específico, analizando su "
     "funcionamiento, la experiencia de contratación, el diseño y la sensibilidad al precio.",
     ["Investigación cuantitativa", "UX Research"], "caso-unicaja.png",
     "/casos-de-exito/unicaja-banco/", True),
    ("Azti",
     "Incorporar la voz del consumidor al desarrollo de nuevos productos",
     "AZTI incorporó la perspectiva de consumidores de diferentes países para explorar sus "
     "percepciones, hábitos y necesidades y obtener insights que orientaran el desarrollo de nuevos "
     "productos reducidos en azúcar.",
     ["Comunidades online", "Investigación cualitativa"], "caso-azti.png",
     "/casos-de-exito/azti/", False),
    ("Europcar",
     "Integrar la voz del cliente en la estrategia de negocio",
     "A través de diferentes estudios cuantitativos y de UX Research, Europcar pudo validar "
     "decisiones de negocio, comprender mejor a sus clientes y optimizar la experiencia de "
     "contratación online.",
     ["Investigación cuantitativa", "UX Research"], "caso-europcar.png",
     "/casos-de-exito/europcar/", True),
]


def caso_row(cliente, titular, texto, tags, imagen, link, img_left, last=False):
    """Fila 608px: texto 765px + imagen 739px, alternando lado. En mobile la imagen va siempre
    arriba (`css_advanced_order`), el DOM alterna como el diseño."""
    texto_items = [
        item("heading", {
            "title": cliente,
            "header_tag": "h2",
            "css_color": css(S_TITLE_C, "color", NEUTRAL1),
            "css_typography": t_h2(S_TITLE),
            "css_advanced_margin": m0("1rem", "0.75rem"),
        }, title=cliente + " — cliente"),
        item("heading", {
            "title": titular,
            "header_tag": "h3",
            "css_color": css(S_TITLE_C, "color", BRAND_DARK),
            "css_typography": t_h30(S_TITLE),
            "css_advanced_margin": m0("1rem", "0.75rem"),
        }, title=cliente + " — titular"),
        item("plain_text", {
            "content": texto,
            "css_descdesca_color": css(S_DESC_C, "color", BODY),
            "css_desc_typography": t_p18(S_DESC),
            "css_advanced_margin": m0("1.5rem", "1.25rem"),
        }, title=cliente + " — texto"),
    ]
    texto_items += [pill(t) for t in tags]
    texto_items.append(
        item("button", btn("Leer más", link, "transparent", NEUTRAL1, icon_color=PRIMARY, extra={
            "width_switcher": "inline",
            "css_button_padding": css(S_BUTTON, "padding",
                                      pad({"top": "0.25rem", "right": "0", "bottom": "0", "left": "0"})),
            "css_button_color_hover": css(S_BUTTON + ":hover", "color", BRAND_DARK),
            "css_button_background_hover": css(S_BUTTON + ":hover, " + S_BUTTON + ":before",
                                               "background", "transparent"),
            "css_advanced_margin": css(S_ITEM_IN, "margin",
                                       pad({"top": "1.75rem", "right": "0", "bottom": "0", "left": "0"},
                                           None,
                                           {"top": "1.25rem", "right": "0", "bottom": "0", "left": "0"})),
        }), size="1/2", tablet="1/2", mobile="1/1", title=cliente + " — leer más"))

    texto = nested(
        {
            "css_advanced_padding": css(S_WRAP_IN, "padding",
                                        pad({"top": "0", "right": "2rem" if not img_left else "0",
                                             "bottom": "0", "left": "0" if not img_left else "2rem"},
                                            None,
                                            {"top": "0", "right": "0", "bottom": "0", "left": "0"})),
            "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "flex-start"}),
            "css_advanced_order": css(S_WRAP, "order", {"desktop": "2" if img_left else "1",
                                                        "mobile": "2"}),
        },
        texto_items,
        size="1/2", tablet="1/2", mobile="1/1", title=cliente + " — texto")

    imagen_item = item("image", {
        "src": MEDIA + imagen,
        "alt": "Caso de éxito " + cliente,
        "stretch": "1",
        "hover": "disable",
        "link": link,
        "css_advanced_margin": m0("0", "1.5rem"),
        "css_advanced_order": css(S_ITEM, "order", {"desktop": "1" if img_left else "2",
                                                    "mobile": "1"}),
    }, size="1/2", tablet="1/2", mobile="1/1", title=cliente + " — imagen")

    children = [imagen_item, texto] if img_left else [texto, imagen_item]

    attr = {
        "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "center"}),
        "css_advanced_padding": css(S_WRAP_IN, "padding",
                                    pad({"top": "4rem", "right": "1rem", "bottom": "4rem", "left": "1rem"},
                                        {"top": "3rem", "right": "0", "bottom": "3rem", "left": "0"},
                                        {"top": "2.5rem", "right": "0", "bottom": "2.5rem", "left": "0"})),
    }
    if not last:
        attr.update({
            "css_advanced_border_style": css(S_WRAP_IN, "border-style", "solid"),
            "css_advanced_border_width": css(S_WRAP_IN, "border-width", {"desktop": "0px 0px 1px 0px"}),
            "css_advanced_border_color": css(S_WRAP_IN, "border-color", DIVIDER),
        })
    return wrap(attr, children, title="Caso — " + cliente)


casos = section(
    dict(sec_base(
        pad({"top": "7.5rem", "right": "4rem", "bottom": "0", "left": "4rem"},
            {"top": "5rem", "right": "2rem", "bottom": "0", "left": "2rem"},
            {"top": "4rem", "right": "1rem", "bottom": "0", "left": "1rem"})),
         **sec_bg(WHITE)),
    [
        eyebrow("Casos de éxito"),
        wrap(
            {"css_advanced_margin": css(S_WRAP_IN, "margin",
                                        pad({"bottom": "5rem"}, {"bottom": "3rem"}, {"bottom": "2rem"}))},
            [
                item("heading", {
                    "title": "Historias de clientes<br>que confían en We are testers",
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", NEUTRAL1),
                    "css_typography": t_h2(S_TITLE),
                    "css_advanced_margin": m0(),
                }, title="Casos — titular"),
            ],
            title="Casos — titular"),
    ] + [caso_row(*c, last=(i == len(CASOS) - 1)) for i, c in enumerate(CASOS)],
    title="Casos de éxito")

# ================================================================ 3. CLIENTES (logos)
clientes = section(
    dict(sec_base(
        pad({"top": "7.5rem", "right": "0", "bottom": "7.5rem", "left": "0"},
            {"top": "5rem", "right": "0", "bottom": "5rem", "left": "0"},
            {"top": "4rem", "right": "0", "bottom": "4rem", "left": "0"}),
        ),
         **sec_bg(WHITE)),
    [
        eyebrow("Clientes", center=True),
        wrap(
            {"css_advanced_margin": css(S_WRAP_IN, "margin",
                                        pad({"bottom": "3rem"}, None, {"bottom": "2rem"}))},
            [
                item("heading", {
                    "title": "Ya confían en nosotros",
                    "header_tag": "h2",
                    "css_txt_align": css(S_TITLE, "text-align", {"desktop": "center"}),
                    "css_color": css(S_TITLE_C, "color", HEADING),
                    "css_typography": t_h60(S_TITLE),
                    "css_advanced_margin": m0(),
                }, title="Clientes — titular"),
            ],
            title="Clientes — titular"),
        wrap(
            {"css_advanced_margin": css(S_WRAP_IN, "margin",
                                        pad({"bottom": "3rem"}, None, {"bottom": "2rem"}))},
            [
                # Logos desde el CPT Client (Theme Options → Post types → Clients activo)
                item("clients_slider", {
                    "title": "",
                    "title_tag": "span",
                    "orderby": "menu_order",
                    "order": "ASC",
                    "per_slide": "8",
                    "scroll": "1",
                    "navigation": "content",
                    "background_switcher": "default",
                    "css_clients_slider_ulliclient_wrapper_height": css(S_CLI_WRAP, "height", "89px"),
                    "css_clients_slider_ulliclient_wrapper_padding": css(
                        S_CLI_WRAP, "padding",
                        pad({"top": "1.5rem", "right": "1.5rem", "bottom": "1.5rem", "left": "1.5rem"},
                            None,
                            {"top": "1rem", "right": "1rem", "bottom": "1rem", "left": "1rem"})),
                    "css_clients_slider_ulliclient_wrapper_background_color": css(
                        S_CLI_WRAP, "background-color", NEUTRAL5),
                    "css_clients_slider_ulliclient_wrapper_background_color_hover": css(
                        S_CLI_WRAP + ":hover", "background-color", "#E9EDF1"),
                    "css_advanced_margin": m0(),
                }, title="Clientes — logos"),
            ],
            title="Clientes — logos"),
        wrap(
            {"css_advanced_justify_content": css(S_WRAP_IN, "justify-content", {"desktop": "center"})},
            [
                item("button", btn("Ver casos de éxito", "/casos-de-exito/", BRAND_DARK, WHITE, extra={
                    "width_switcher": "inline",
                    "css_button_background_hover": css(S_BUTTON + ":hover, " + S_BUTTON + ":before",
                                                       "background", PRIMARY),
                    "css_button_color_hover": css(S_BUTTON + ":hover", "color", WHITE),
                }), size="1/3", tablet="1/2", mobile="1/1", title="Clientes — botón"),
            ],
            title="Clientes — botón"),
    ],
    title="Clientes")

# ================================================================ 4. CTA
cta = section(
    dict(sec_base(
        pad({"top": "7.5rem", "right": "5rem", "bottom": "7.5rem", "left": "5rem"},
            {"top": "5rem", "right": "2rem", "bottom": "5rem", "left": "2rem"},
            {"top": "4rem", "right": "1rem", "bottom": "4rem", "left": "1rem"})),
         **sec_bg(PRIMARY, "cta-fondo.jpg")),
    [
        wrap(
            {
                "css_advanced_justify_content": css(S_WRAP_IN, "justify-content", {"desktop": "center"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "2rem"}, None, {"bottom": "1.5rem"})),
            },
            [
                item("heading", {
                    "title": "Más conocimiento para tus próximos retos",
                    "header_tag": "h2",
                    "css_txt_align": css(S_TITLE, "text-align", {"desktop": "center"}),
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": t_h2(S_TITLE),
                    "css_advanced_margin": m0("1.5rem", "1rem"),
                }, size="1/2", tablet="2/3", mobile="1/1", title="CTA — titular"),
                item("plain_text", {
                    "content": ("Profundiza en las tendencias y comportamientos que están transformando "
                                "los mercados a través de nuestros informes."),
                    "css_desc_text_align": css(S_DESC, "text-align", {"desktop": "center"}),
                    "css_descdesca_color": css(S_DESC_C, "color", WHITE),
                    "css_desc_typography": t_p20(S_DESC),
                    "css_advanced_margin": m0(),
                }, size="2/5", tablet="2/3", mobile="1/1", title="CTA — texto"),
            ],
            title="CTA — texto"),
        wrap(
            {"css_advanced_justify_content": css(S_WRAP_IN, "justify-content", {"desktop": "center"})},
            [
                item("button", btn("Ver informes", "/recursos/informes/", WHITE, BRAND_DARK, extra={
                    "width_switcher": "inline",
                    "css_button_background_hover": css(S_BUTTON + ":hover, " + S_BUTTON + ":before",
                                                       "background", NEUTRAL5),
                    "css_button_color_hover": css(S_BUTTON + ":hover", "color", BRAND_DARK),
                }), size="1/3", tablet="1/2", mobile="1/1", title="CTA — botón"),
            ],
            title="CTA — botón"),
    ],
    title="CTA — Informes")

# ================================================================ salida
page = [hero, casos, clientes, cta]

if __name__ == "__main__":
    out = HERE / "we-are-testers-casos-de-exito.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(page, fh, ensure_ascii=False, indent=2)
    print("OK ->", out, "| secciones:", len(page))
