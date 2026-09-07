# -*- coding: utf-8 -*-
"""Genera el JSON BeBuilder de la página 'Productos → Maderas → Aglomerado'
(Maderas Vázquez, Figma quZT4q6SeoX1SKC6fmg2Yu, nodo 1032:288).

Salida: maderas-vazquez-aglomerado.json

Reglas del proyecto: contenedor interior a 1728px (`width_switcher: "custom"` +
`css_advanced_max_width`), padding lateral del diseño (120px = 7.5rem en las bandas de
producto, 64px = 4rem en hero y pre-footer). Header y footer del Figma son instancias
(plantillas de theme aparte); el pre-footer sí va en la página.

Decisiones de mapeo (lo que el bloque ES, no cómo se ve):
  - Chips "Estándar / Hidrófugo / Ignífugo" → 3 `button` inline con ancla a la sección
    (`custom_id` estandar/hidrofugo/ignifugo).
  - Bandas apiladas con esquinas superiores redondeadas y sombra → sección con
    `border-radius` 64px arriba, `box-shadow` y `margin-top` -60px sobre la anterior.
  - Tabla "Dimensiones disponibles" → una fila = un wrap anidado (`item_is_wrap`) con dos
    `plain_text` 1/2; cabecera azul, filas alternas, radio en primera/última.
  - Pareja de fotos → wrap `grid` 2 columnas con gap 16px + 2 `image` con radio 42px.
  - Tarjetas oscuras "stock permanente" / "atención técnica" → `icon_box_2` (icono en
    círculo blanco + título + texto) dentro de un wrap anidado con fondo.
  - Tarjeta blanca "Contáctanos" (foto + título + texto + enlace) → `promo_box`.
  - Certificaciones → 3 wraps anidados 1/3 con `image` (caja blanca) + etiqueta.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- tokens (Figma)
PRIMARY      = "#3B4FB0"   # primary
PRIMARY_DARK = "#1F2230"   # primary-dark
BLACK        = "#323232"   # black
DARKGRAY     = "#5C5851"   # dark-gray
MEDIUMGRAY   = "#E3E5E8"   # medium-gray
LIGHTGRAY    = "#F4F3F0"   # light-gray
ACCENT_BG    = "#EFF0F0"   # accent-background
WHITE        = "#FDFDFC"   # white
SHADOW       = "0px 0px 64px 0px rgba(51,80,153,0.08)"
MEDIA        = "https://maderasvazquez.com/wp-content/uploads/2026/08/"
MAXW         = "1728px"

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
# icon_box_2
S_IB_WRAP   = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper"
S_IB_ICON   = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper i"
S_IB_DESC   = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc"
# promo_box
S_PB_PHOTO  = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .promo_box_wrapper .photo_wrapper"
S_PB_TITLE  = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .promo_box_wrapper .desc_wrapper .title"
S_PB_DESC   = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .promo_box_wrapper .desc_wrapper .desc"
S_PB_BTN    = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .promo_box_wrapper .desc_wrapper .button"
S_PB_BTN_H  = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .promo_box_wrapper .desc_wrapper .button:hover"

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


def box(d, t=None, m=None):
    """padding/margin uniforme en los cuatro lados."""
    return pad({"top": d, "right": d, "bottom": d, "left": d},
               {"top": t, "right": t, "bottom": t, "left": t} if t else None,
               {"top": m, "right": m, "bottom": m, "left": m} if m else None)


def mb(desktop, mobile=None):
    return css(S_ITEM_IN, "margin", pad({"bottom": desktop}, None,
                                        {"bottom": mobile} if mobile else None))


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


def btn(title, link, bg, fg, extra=None):
    """Botón píldora del diseño: 16px semibold uppercase, padding 16/24, radio 200px."""
    attr = {
        "title": title,
        "link": link,
        "button_style": "",
        "background_switcher": "default",
        "css_button_color": css(S_BUTTON, "color", fg),
        "css_button_background_color": css(S_BUTTON, "background-color", bg),
        "css_button_border_radius": css(S_BUTTON, "border-radius",
                                        {"desktop": "200px 200px 200px 200px"}),
        "css_button_padding": css(S_BUTTON, "padding",
                                  pad({"top": "1rem", "right": "1.5rem",
                                       "bottom": "1rem", "left": "1.5rem"},
                                      None,
                                      {"top": "0.875rem", "right": "1.25rem",
                                       "bottom": "0.875rem", "left": "1.25rem"})),
        "css_button_typography": typo(S_BUTTON,
                                      {"font-size": "16px", "line-height": "1.2",
                                       "font-weight": "600", "text-transform": "uppercase"},
                                      None,
                                      {"font-size": "15px", "line-height": "1.2",
                                       "font-weight": "600", "text-transform": "uppercase"}),
    }
    if extra:
        attr.update(extra)
    return attr


def chip(title, link, active=False):
    """Chip de ancla del hero (40px alto, radio 200, 14px semibold)."""
    attr = {
        "title": title,
        "link": link,
        "button_style": "",
        "width_switcher": "inline",
        "background_switcher": "default",
        "css_button_color": css(S_BUTTON, "color", PRIMARY if active else WHITE),
        "css_button_background_color": css(S_BUTTON, "background-color",
                                           WHITE if active else "rgba(0,0,0,0)"),
        "css_button_border_style": css(S_BUTTON, "border-style", "solid"),
        "css_button_border_color": css(S_BUTTON, "border-color", MEDIUMGRAY),
        "css_button_border_width": css(S_BUTTON, "border-width", {"desktop": "1px 1px 1px 1px"}),
        "css_button_border_radius": css(S_BUTTON, "border-radius",
                                        {"desktop": "200px 200px 200px 200px"}),
        "css_button_padding": css(S_BUTTON, "padding",
                                  pad({"top": "0.5rem", "right": "1.5rem",
                                       "bottom": "0.5rem", "left": "1.5rem"})),
        "css_button_typography": typo(S_BUTTON,
                                      {"font-size": "14px", "line-height": "1.4",
                                       "font-weight": "600"},
                                      None,
                                      {"font-size": "13px", "line-height": "1.4",
                                       "font-weight": "600"}),
        "css_button_color_hover": css(S_BUTTON + ":hover", "color", PRIMARY),
        "background_switcher_hover": "default",
        "css_button_background_hover": css(S_BUTTON + ":hover, " + S_BUTTON + ":before",
                                           "background", WHITE),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   pad({"right": "0.75rem", "bottom": "0.75rem"})),
    }
    return attr


# tipografías del diseño (Nunito; la familia se fija en Theme Options) ----------
def t_h1_bold(sel):
    return typo(sel,
                {"font-size": "64px", "line-height": "1.2", "letter-spacing": "-1.28px",
                 "font-weight": "700"},
                {"font-size": "52px", "line-height": "1.2", "letter-spacing": "-1px",
                 "font-weight": "700"},
                {"font-size": "40px", "line-height": "1.2", "letter-spacing": "-0.8px",
                 "font-weight": "700"})


def t_h1_medium(sel):
    return typo(sel,
                {"font-size": "64px", "line-height": "1", "letter-spacing": "-1.28px",
                 "font-weight": "500"},
                {"font-size": "52px", "line-height": "1.05", "letter-spacing": "-1px",
                 "font-weight": "500"},
                {"font-size": "40px", "line-height": "1.1", "letter-spacing": "-0.8px",
                 "font-weight": "500"})


def t_h2(sel):
    return typo(sel,
                {"font-size": "42px", "line-height": "1.2", "font-weight": "600"},
                {"font-size": "36px", "line-height": "1.2", "font-weight": "600"},
                {"font-size": "30px", "line-height": "1.2", "font-weight": "600"})


def t_h4(sel):
    return typo(sel,
                {"font-size": "20px", "line-height": "1.3", "letter-spacing": "-0.4px",
                 "font-weight": "700"},
                None,
                {"font-size": "18px", "line-height": "1.3", "letter-spacing": "-0.36px",
                 "font-weight": "700"})


def t_plarge(sel):
    return typo(sel,
                {"font-size": "20px", "line-height": "1.4", "font-weight": "500"},
                None,
                {"font-size": "17px", "line-height": "1.4", "font-weight": "500"})


def t_plarge_bold(sel):
    return typo(sel,
                {"font-size": "22px", "line-height": "1.4", "font-weight": "700"},
                None,
                {"font-size": "19px", "line-height": "1.4", "font-weight": "700"})


def t_pmedium(sel, weight="400"):
    return typo(sel,
                {"font-size": "16px", "line-height": "1.4", "font-weight": weight},
                None,
                {"font-size": "15px", "line-height": "1.4", "font-weight": weight})


def t_th(sel):
    return typo(sel,
                {"font-size": "15px", "line-height": "22px", "font-weight": "700",
                 "text-transform": "uppercase"},
                None,
                {"font-size": "13px", "line-height": "20px", "font-weight": "700",
                 "text-transform": "uppercase"})


def t_td(sel):
    return typo(sel,
                {"font-size": "14px", "line-height": "1.4", "font-weight": "400"},
                None,
                {"font-size": "13px", "line-height": "1.4", "font-weight": "400"})


def t_link(sel):
    return typo(sel,
                {"font-size": "13px", "line-height": "20px", "font-weight": "400"},
                None,
                {"font-size": "13px", "line-height": "20px", "font-weight": "400"})


# ================================================================ 1. HERO
# Nodo 1032:290: 1052px, imagen de fondo + overlay (degradado vertical a negro 0.6 sobre
# velo negro 0.4), padding lateral 64px, contenido desde 250px. Fila titular/intro+chips,
# después bloque "Composición" (línea superior, 400px, contenido pegado abajo).
HERO_INTRO = (
    "Panel derivado de la madera, compuesto por partículas de madera unidas con resinas "
    "sintéticas y prensadas a alta presión. Disponible en diferentes espesores y formatos "
    "para carpintería, construcción e industria."
)
COMPOSICION = (
    "El tablero aglomerado se fabrica a partir de partículas de madera (virutas, serrín) que "
    "se mezclan con resinas sintéticas y se prensan bajo calor y presión. El resultado es un "
    "panel homogéneo, estable y económico, ideal para mobiliario, revestimientos y "
    "aplicaciones de interior donde se requiere un soporte plano y uniforme."
)
HERO_OVERLAY = ("linear-gradient(180deg, rgba(0,0,0,0) 47%, rgba(0,0,0,0.6) 75%), "
                "linear-gradient(90deg, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0.4) 100%)")

hero = section(
    sec_base(
        # bottom = 120px del diseño + 60px que la siguiente banda monta encima
        pad({"top": "15.625rem", "right": "4rem", "bottom": "11.25rem", "left": "4rem"},
            {"top": "10rem", "right": "2.5rem", "bottom": "8rem", "left": "2.5rem"},
            {"top": "8rem", "right": "1.25rem", "bottom": "6.5rem", "left": "1.25rem"}),
        {
            "background_switcher": "default",
            "css_advanced_background_color": css(S_SECTION, "background-color", PRIMARY_DARK),
            "css_advanced_background_image": css(S_SECTION, "background-image",
                                                 {"desktop": MEDIA + "hero-aglomerado.jpg"}),
            "css_advanced_background_size": css(S_SECTION, "background-size", {"desktop": "cover"}),
            "css_advanced_background_position": css(S_SECTION, "background-position",
                                                    {"desktop": "center"}),
            "css_advanced_background_repeat": css(S_SECTION, "background-repeat",
                                                  {"desktop": "no-repeat"}),
            "background_overlay_switcher": "gradient",
            "css_advanced_overlay_gradient": css(S_SECT_OVER, "gradient", {
                "type": "linear", "angle": "180",
                "color": "rgba(0,0,0,0)", "location": "47",
                "color2": "rgba(0,0,0,0.6)", "location2": "75",
                "string": HERO_OVERLAY,
            }),
        }),
    [
        wrap(
            {},
            [
                item("heading", {
                    "title": "Aglomerado",
                    "header_tag": "h1",
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": t_h1_bold(S_TITLE),
                    "css_advanced_margin": mb("0", "1.5rem"),
                }, title="Hero — titular"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Hero — titular"),
        wrap(
            {},
            [
                item("plain_text", {
                    "content": HERO_INTRO,
                    "css_descdesca_color": css(S_DESC_C, "color", ACCENT_BG),
                    "css_desc_typography": t_plarge(S_DESC),
                    "css_advanced_margin": mb("1.5rem", "1.25rem"),
                }, title="Hero — intro"),
                item("button", chip("Estándar", "#estandar", active=True),
                     title="Hero — chip Estándar"),
                item("button", chip("Hidrófugo", "#hidrofugo"), title="Hero — chip Hidrófugo"),
                item("button", chip("Ignífugo", "#ignifugo"), title="Hero — chip Ignífugo"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Hero — intro y chips"),
        wrap(
            {
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"top": "3.375rem"}, None, {"top": "2rem"})),
                "css_advanced_border_style": css(S_WRAP_IN, "border-style", "solid"),
                "css_advanced_border_color": css(S_WRAP_IN, "border-color", "rgba(255,255,255,0.8)"),
                "css_advanced_border_width": css(S_WRAP_IN, "border-width",
                                                 {"desktop": "1px 0px 0px 0px"}),
                "css_advanced_min_height": css(S_WRAP_IN, "min-height",
                                               {"desktop": "400px", "tablet": "300px",
                                                "mobile": "auto"}),
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"top": "3rem"}, None, {"top": "2rem"})),
                "css_advanced_align_content": css(S_WRAP_IN, "align-content", {"desktop": "flex-end"}),
                "css_advanced_justify_content": css(S_WRAP_IN, "justify-content",
                                                    {"desktop": "center"}),
            },
            [
                item("heading", {
                    "title": "Composición",
                    "header_tag": "h2",
                    "css_txt_align": css(S_TITLE, "text-align", {"desktop": "center"}),
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": t_h1_medium(S_TITLE),
                    "css_advanced_margin": mb("4rem", "2rem"),
                }, title="Hero — Composición"),
                item("plain_text", {
                    "content": COMPOSICION,
                    "width_switcher": "custom",
                    "css_advanced_flex": css(S_ITEM, "width",
                                             {"desktop": "692px", "tablet": "80%", "mobile": "100%"}),
                    "css_desc_text_align": css(S_DESC, "text-align", {"desktop": "center"}),
                    "css_descdesca_color": css(S_DESC_C, "color", ACCENT_BG),
                    "css_desc_typography": t_plarge(S_DESC),
                    "css_advanced_margin": mb("0"),
                }, title="Hero — Composición texto"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Hero — Composición"),
    ],
    title="Hero — Aglomerado")


# ================================================================ 2-4. BANDAS DE PRODUCTO
def table_row(c1, c2, kind):
    """Fila de la tabla de dimensiones. kind: 'th' | 'odd' | 'even' | 'last-odd' | 'last-even'."""
    attr = {
        "background_switcher": "default",
        "css_advanced_padding": css(S_WRAP_IN, "padding",
                                    pad({"top": "1rem", "right": "1.25rem",
                                         "bottom": "1rem", "left": "1.25rem"},
                                        None,
                                        {"top": "0.75rem", "right": "0.875rem",
                                         "bottom": "0.75rem", "left": "0.875rem"})),
    }
    if kind == "th":
        attr["css_advanced_background_color"] = css(S_WRAP_IN, "background-color", PRIMARY)
        attr["css_advanced_border_radius"] = css(S_WRAP_IN, "border-radius",
                                                 {"desktop": "12px 12px 0px 0px"})
        color, tfn = WHITE, t_th
    else:
        bg = WHITE if kind.endswith("odd") else LIGHTGRAY
        attr["css_advanced_background_color"] = css(S_WRAP_IN, "background-color", bg)
        attr["css_advanced_border_style"] = css(S_WRAP_IN, "border-style", "solid")
        attr["css_advanced_border_color"] = css(S_WRAP_IN, "border-color", MEDIUMGRAY)
        attr["css_advanced_border_width"] = css(S_WRAP_IN, "border-width",
                                                {"desktop": "0px 1px 1px 1px"})
        if kind.startswith("last"):
            attr["css_advanced_border_radius"] = css(S_WRAP_IN, "border-radius",
                                                     {"desktop": "0px 0px 12px 12px"})
        color, tfn = DARKGRAY, t_td
    cells = []
    for txt in (c1, c2):
        cells.append(item("plain_text", {
            "content": txt,
            "css_descdesca_color": css(S_DESC_C, "color", color),
            "css_desc_typography": tfn(S_DESC),
            "css_advanced_margin": mb("0"),
        }, size="1/2", tablet="1/2", mobile="1/2", title="Celda"))
    return nested(attr, cells, size="1/1", tablet="1/1", mobile="1/1",
                  title="Tabla — " + ("cabecera" if kind == "th" else "fila"))


def photos_wrap(files, side):
    """Pareja de fotos 3:4 con radio 42px: wrap grid 2 columnas, gap 16px."""
    attr = {
        "grid": "grid",
        "grid_columns_switcher": "",
        "css_grid_columns": css(S_WRAP_GRID, "grid-template-columns",
                                {"desktop": "repeat(2, 1fr)", "tablet": "repeat(2, 1fr)",
                                 "mobile": "repeat(2, 1fr)"}),
        "css_grid_columns_gap": css(S_WRAP_GRID, "column-gap", {"desktop": "16px", "mobile": "12px"}),
        "css_grid_rows_gap": css(S_WRAP_GRID, "row-gap", {"desktop": "16px", "mobile": "12px"}),
        "css_advanced_padding": css(S_WRAP_IN, "padding",
                                    pad({"right" if side == "left" else "left": "2rem"},
                                        {"right" if side == "left" else "left": "1rem"},
                                        {"bottom": "2rem"})),
    }
    items = []
    for i, f in enumerate(files):
        items.append(item("image", {
            "src": MEDIA + f,
            "size": "full",
            "alt": "",
            "hover": "disable",
            "image_height": "custom",
            "image_height_style": "",
            "css_image_cover_height": css(S_IMGCOVER, "height",
                                          {"desktop": "380px", "tablet": "300px", "mobile": "220px"}),
            "css_image_border_radius": css(S_IMGFRAME, "border-radius",
                                           {"desktop": "42px 42px 42px 42px",
                                            "mobile": "24px 24px 24px 24px"}),
            "css_advanced_margin": mb("0"),
        }, size="1/1", tablet="1/1", mobile="1/1", title="Foto %d" % (i + 1)))
    return wrap(attr, items, size="2/5", tablet="1/2", mobile="1/1", title="Fotos")


def text_wrap(name, desc, rows, side):
    items = [
        item("heading", {
            "title": name,
            "header_tag": "h2",
            "css_color": css(S_TITLE_C, "color", PRIMARY_DARK),
            "css_typography": t_h2(S_TITLE),
            "css_advanced_margin": mb("0.75rem"),
        }, title=name + " — título"),
        item("plain_text", {
            "content": desc,
            "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
            "css_desc_typography": t_plarge(S_DESC),
            "css_advanced_margin": mb("1.5rem"),
        }, title=name + " — descripción"),
        item("heading", {
            "title": "Dimensiones disponibles",
            "header_tag": "h3",
            "css_color": css(S_TITLE_C, "color", PRIMARY_DARK),
            "css_typography": t_h4(S_TITLE),
            "css_advanced_margin": mb("0.75rem"),
        }, title=name + " — subtítulo tabla"),
        table_row("Medidas (mm)", "Espesores (mm)", "th"),
    ]
    for i, (m, e) in enumerate(rows):
        kind = "odd" if i % 2 == 0 else "even"
        if i == len(rows) - 1:
            kind = "last-" + kind
        items.append(table_row(m, e, kind))
    items.append(item("plain_text", {
        "content": '<a href="/contacto/">Otras opciones y medidas, consultar →</a>',
        "css_descdesca_color": css(S_DESC_C, "color", PRIMARY),
        "css_desc_typography": t_link(S_DESC),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   pad({"top": "0.75rem", "bottom": "0"})),
    }, title=name + " — enlace consultar"))
    attr = {
        "css_advanced_padding": css(S_WRAP_IN, "padding",
                                    pad({"left" if side == "right" else "right": "2rem"},
                                        {"left" if side == "right" else "right": "1rem"},
                                        {"bottom": "0"})),
    }
    return wrap(attr, items, size="3/5", tablet="1/2", mobile="1/1", title=name + " — texto")


def product_section(slug, name, desc, rows, photos, bg, photos_side):
    """Banda apilada: esquinas superiores 64px, sombra, monta 60px sobre la anterior."""
    attr = sec_base(
        pad({"top": "7.5rem", "right": "7.5rem", "bottom": "7.5rem", "left": "7.5rem"},
            {"top": "4rem", "right": "2.5rem", "bottom": "4rem", "left": "2.5rem"},
            {"top": "3rem", "right": "1.25rem", "bottom": "3rem", "left": "1.25rem"}),
        {
            "custom_id": slug,
            "background_switcher": "default",
            "css_advanced_background_color": css(S_SECTION, "background-color", bg),
            "css_advanced_margin": css(S_SECTION, "margin",
                                       pad({"top": "-3.75rem"}, None, {"top": "-2.5rem"})),
            "css_advanced_border_radius": css(S_SECTION, "border-radius",
                                              {"desktop": "64px 64px 0px 0px",
                                               "mobile": "32px 32px 0px 0px"}),
            "css_advanced_box_shadow": css(S_SECTION, "box-shadow", {"desktop": SHADOW}),
            "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "center"}),
        })
    p = photos_wrap(photos, photos_side)
    t = text_wrap(name, desc, rows, "right" if photos_side == "left" else "left")
    wraps = [p, t] if photos_side == "left" else [t, p]
    return section(attr, wraps, title="Aglomerado — " + name)


estandar = product_section(
    "estandar", "Estándar",
    "El aglomerado estándar es la opción más versátil y económica. Fabricado con partículas "
    "de madera de densidad media, ofrece una superficie lisa y uniforme apta para laminado, "
    "chapado o pintura. Uso recomendado en ambientes secos de interior.",
    [("2440 × 1220", "10, 16, 19 y 30"), ("2850 × 2100", "30 y 40")],
    ["aglomerado-estandar-1.png", "aglomerado-estandar-2.png"],
    WHITE, "left")

hidrofugo = product_section(
    "hidrofugo", "Hidrófugo",
    "Tablero fabricado con resinas especiales de melamina-urea-formaldehído que aumentan su "
    "resistencia a la humedad. Identificable por su color verdoso característico. Indicado "
    "para cocinas, baños y zonas con humedad ambiental moderada.",
    [("2440 × 1220", "16, 19 y 22"), ("2850 × 2100", "19 y 22")],
    ["aglomerado-hidrofugo-1.png", "aglomerado-hidrofugo-2.png"],
    LIGHTGRAY, "right")

ignifugo = product_section(
    "ignifugo", "Ignífugo",
    "Tablero con tratamiento retardante del fuego que cumple la clasificación B-s2,d0 según "
    "norma UNE-EN 13501-1. Incorpora sales ignífugas en su composición que retrasan la "
    "propagación de la llama. Obligatorio en edificios de pública concurrencia y según "
    "normativa CTE.",
    [("2440 × 1220", "16, 19 y 22")],
    ["aglomerado-ignifugo-1.png", "aglomerado-ignifugo-2.png"],
    WHITE, "left")


# ================================================================ 5. PRE-FOOTER
# Nodo 312:1079: fondo accent, padding 120/64. Izquierda tarjeta azul 700px (radio 42,
# padding 64) con certificaciones; derecha dos tarjetas oscuras + tarjeta blanca de contacto.
CERTS = [
    ("cert-pefc.png", "01", "PEFC™"),
    ("cert-iso-9001.png", "02", "ISO 9001"),
    ("cert-fsc.png", "03", "FSC ®"),
]


def cert_cell(file, num, label):
    return nested(
        {
            "css_advanced_margin": css(S_WRAP_IN, "margin",
                                       pad({"bottom": "2.625rem"}, None, {"bottom": "1.5rem"})),
        },
        [
            item("image", {
                "src": MEDIA + file,
                "size": "full",
                "alt": label,
                "hover": "disable",
                "image_height": "custom",
                "image_height_style": "fit",
                "css_image_cover_height": css(S_IMGCOVER, "height",
                                              {"desktop": "116px", "mobile": "96px"}),
                "css_image_text_align": css(S_ITEM_IN, "text-align", {"desktop": "center"}),
                "height_switcher": "custom",
                "css_advanced_height": css(S_ITEM_IN, "height", {"desktop": "164px", "mobile": "140px"}),
                "background_switcher": "default",
                "css_advanced_background_color": css(S_ITEM_IN, "background-color", WHITE),
                "css_advanced_border_radius": css(S_ITEM_IN, "border-radius",
                                                  {"desktop": "24px 24px 24px 24px"}),
                "css_advanced_padding": css(S_ITEM_IN, "padding", box("1.5rem", None, "1.25rem")),
                "css_advanced_margin": mb("1.5rem", "1rem"),
            }, title="Certificación — logo " + label),
            item("plain_text", {
                "content": num,
                "width_switcher": "inline",
                "css_descdesca_color": css(S_DESC_C, "color", LIGHTGRAY),
                "css_desc_typography": t_pmedium(S_DESC),
                "css_advanced_margin": css(S_ITEM_IN, "margin",
                                           pad({"right": "0.5rem", "bottom": "0"})),
            }, title="Certificación — número"),
            item("heading", {
                "title": label,
                "header_tag": "p",
                "width_switcher": "inline",
                "css_color": css(S_TITLE_C, "color", WHITE),
                "css_typography": t_plarge_bold(S_TITLE),
                "css_advanced_margin": mb("0"),
            }, title="Certificación — nombre"),
        ],
        size="1/3", tablet="1/3", mobile="1/1", title="Certificación " + label)


def dark_card(icon, title, content):
    return nested(
        {
            "background_switcher": "default",
            "css_advanced_background_color": css(S_WRAP_IN, "background-color", PRIMARY_DARK),
            "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                              {"desktop": "42px 42px 42px 42px",
                                               "mobile": "24px 24px 24px 24px"}),
            "css_advanced_padding": css(S_WRAP_IN, "padding", box("2.625rem", None, "1.5rem")),
            "css_advanced_margin": css(S_WRAP_IN, "margin",
                                       pad({"bottom": "2.625rem"}, None, {"bottom": "1.5rem"})),
            "height_switcher": "custom",
            "css_advanced_height": css(S_WRAP_IN, "height", {"desktop": "100%"}),
        },
        [
            item("icon_box_2", {
                "title": title,
                "title_tag": "h3",
                "content": content,
                "icon": icon,
                "icon_position": "top",
                "icon_align": "start",
                "hover": "",
                "css_icon_box_icon_wrapper_width": css(S_IB_WRAP, "width", {"desktop": "70px", "mobile": "60px"}),
                "css_icon_box_icon_wrapper_height": css(S_IB_WRAP, "height", {"desktop": "70px", "mobile": "60px"}),
                "background_switcher": "default",
                "css_icon_box_icon_wrapper_bg_color": css(S_IB_WRAP, "background-color", WHITE),
                "css_icon_box_icon_wrapper_border_radius": css(S_IB_WRAP, "border-radius",
                                                               {"desktop": "100px 100px 100px 100px"}),
                "css_icon_box_icon_wrapper_i_font_size": css(S_IB_ICON, "font-size", {"desktop": "32px", "mobile": "28px"}),
                "css_icon_box_icon_wrapper_icon_color": css(S_IB_ICON, "color", PRIMARY_DARK),
                "css_icon_box_icon_wrapper_margin": css(S_IB_WRAP, "margin",
                                                        pad({"bottom": "4rem"}, None, {"bottom": "2rem"})),
                "css_icon_box_title_color": css(S_TITLE, "color", WHITE),
                "css_icon_box_title_typography": t_plarge_bold(S_TITLE),
                "css_icon_box_title_margin": css(S_TITLE, "margin", pad({"bottom": "1rem"})),
                "css_icon_box_desc_color": css(S_IB_DESC, "color", MEDIUMGRAY),
                "css_icon_box_desc_typography": t_pmedium(S_IB_DESC),
                "css_icon_box_desc_margin": css(S_IB_DESC, "margin", pad({"bottom": "0"})),
                "css_advanced_margin": mb("0"),
            }, title=title),
        ],
        size="1/2", tablet="1/2", mobile="1/1", title="Tarjeta — " + title)


contact_card = nested(
    {
        "background_switcher": "default",
        "css_advanced_background_color": css(S_WRAP_IN, "background-color", WHITE),
        "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                          {"desktop": "42px 42px 42px 42px",
                                           "mobile": "24px 24px 24px 24px"}),
        "css_advanced_box_shadow": css(S_WRAP_IN, "box-shadow", {"desktop": SHADOW}),
        "css_advanced_padding": css(S_WRAP_IN, "padding", box("2.625rem", None, "1.5rem")),
    },
    [
        item("promo_box", {
            "image": MEDIA + "prefooter-contacto.jpg",
            "title": "Contáctanos y ponnos a prueba en la realización de tu proyecto",
            "title_tag": "h3",
            "content": ("Nos gustan los retos y encontrar nuevas oportunidades para innovar con "
                        "nuestro trabajo. Estamos en constante aprendizaje y mejora, y podemos "
                        "demostrarlo. Te estamos esperando."),
            "btn_text": "Contactar →",
            "btn_link": "/contacto/",
            "position": "left",
            "border": "0",
            "css_promo_box_wrapperphoto_wrapper_border_radius": css(
                S_PB_PHOTO, "border-radius", {"desktop": "16px 16px 16px 16px"}),
            "css_promo_box_desc_title_color": css(S_PB_TITLE, "color", BLACK),
            "css_promo_box_desc_title_typography": t_plarge_bold(S_PB_TITLE),
            "css_promo_box_desc_title_margin": css(S_PB_TITLE, "margin", pad({"bottom": "1rem"})),
            "css_promo_box_desc_desc_color": css(S_PB_DESC, "color", DARKGRAY),
            "css_promo_box_desc_desc_typography": t_pmedium(S_PB_DESC),
            "css_promo_box_desc_desc_margin": css(S_PB_DESC, "margin", pad({"bottom": "1.5rem"})),
            "background_switcher": "default",
            "css_promo_box_desc_button_background_color": css(S_PB_BTN, "background-color",
                                                              "rgba(0,0,0,0)"),
            "css_promo_box_desc_button_color": css(S_PB_BTN, "color", BLACK),
            "css_promo_box_desc_button_padding": css(S_PB_BTN, "padding", box("0")),
            "css_promo_box_desc_button_typography": typo(
                S_PB_BTN,
                {"font-size": "16px", "line-height": "1.2", "font-weight": "600",
                 "text-transform": "uppercase"},
                None,
                {"font-size": "15px", "line-height": "1.2", "font-weight": "600",
                 "text-transform": "uppercase"}),
            "css_promo_box_desc_button_color_hover": css(S_PB_BTN_H, "color", PRIMARY),
            "background_switcher_hover": "default",
            "css_promo_box_desc_button_background_hover": css(
                S_PB_BTN_H + ", " + S_PB_BTN + ":before", "background", "rgba(0,0,0,0)"),
            "css_advanced_margin": mb("0"),
        }, title="Contáctanos"),
    ],
    size="1/1", tablet="1/1", mobile="1/1", title="Tarjeta — Contáctanos")

prefooter = section(
    sec_base(
        pad({"top": "7.5rem", "right": "4rem", "bottom": "7.5rem", "left": "4rem"},
            {"top": "4rem", "right": "2.5rem", "bottom": "4rem", "left": "2.5rem"},
            {"top": "3rem", "right": "1.25rem", "bottom": "3rem", "left": "1.25rem"}),
        {
            "background_switcher": "default",
            "css_advanced_background_color": css(S_SECTION, "background-color", ACCENT_BG),
            "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "stretch"}),
        }),
    [
        wrap(
            {
                "background_switcher": "default",
                "css_advanced_background_color": css(S_WRAP_IN, "background-color", PRIMARY),
                "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                                  {"desktop": "42px 42px 42px 42px",
                                                   "mobile": "24px 24px 24px 24px"}),
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            box("4rem", "2.5rem", "1.5rem")),
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "0"}, {"bottom": "2.5rem"},
                                               {"bottom": "1.5rem"})),
                "height_switcher": "custom",
                "css_advanced_height": css(S_WRAP_IN, "height", {"desktop": "100%"}),
            },
            [
                item("heading", {
                    "title": "Sostenibilidad garantizada con certificaciones oficiales",
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": t_h2(S_TITLE),
                    "css_advanced_margin": mb("3.25rem", "2rem"),
                }, title="Certificaciones — titular"),
            ] + [cert_cell(*c) for c in CERTS] + [
                item("plain_text", {
                    "content": ("Nuestros procesos y productos cuentan con certificaciones "
                                "oficiales que garantizan calidad, sostenibilidad y cumplimiento "
                                "de las normativas más exigentes del sector."),
                    "css_descdesca_color": css(S_DESC_C, "color", MEDIUMGRAY),
                    "css_desc_typography": t_pmedium(S_DESC),
                    "css_advanced_margin": mb("3.25rem", "2rem"),
                }, title="Certificaciones — texto"),
                item("button", btn("Nuestra política sostenible", "/sostenibilidad/",
                                   ACCENT_BG, PRIMARY_DARK, {
                    "css_advanced_margin": mb("0"),
                }), title="Certificaciones — botón"),
            ],
            size="2/5", tablet="1/1", mobile="1/1", title="Pre-footer — certificaciones"),
        wrap(
            {
                "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "stretch"}),
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"left": "1.5rem"}, {"left": "0"}, {"left": "0"})),
            },
            [
                dark_card("fas fa-box",
                          "Gama de stock permanente",
                          "Estamos siempre preparados para cubrir las necesidades de nuestros "
                          "clientes, y nos adaptamos a diferentes situaciones."),
                dark_card("fas fa-headset",
                          "Atención técnica especializada",
                          "Nuestro equipo de profesionales está siempre preparado para resolver "
                          "dudas y dar soluciones."),
                contact_card,
            ],
            size="3/5", tablet="1/1", mobile="1/1", title="Pre-footer — servicios y contacto"),
    ],
    title="Pre-footer — Certificaciones y contacto")


# ================================================================ salida
data = [hero, estandar, hidrofugo, ignifugo, prefooter]

with open(HERE / "maderas-vazquez-aglomerado.json", "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)


def count_items(items):
    n = 0
    for it in items:
        n += 1
        if it.get("item_is_wrap"):
            n += count_items(it["items"])
    return n


print("secciones:", len(data))
print("wraps:", sum(len(s["wraps"]) for s in data))
print("items:", sum(count_items(w["items"]) for s in data for w in s["wraps"]))
