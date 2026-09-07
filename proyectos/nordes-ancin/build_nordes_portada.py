# -*- coding: utf-8 -*-
"""Genera el JSON BeBuilder de la 'Portada' (Nordés Ancín, Figma 2572:6297).

Regla de proyecto: el contenedor interior de toda sección tiene max-width 1728px
(`width_switcher: "custom"` + `css_advanced_max_width` sobre `.section_wrapper`)
y padding lateral de 36px = 2.25rem, igual que el diseño (1728 - 36*2 = 1656).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- tokens
PRIMARY   = "#001689"
BLACK     = "#1F1F1F"
TEXTDARK  = "#2C2926"
DARKGRAY  = "#6B6B6B"
WHITE     = "#FCFCFC"
OFFWHITE  = "#F1F1EE"
EMPLEOTXT = "#F3F4EE"
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
    """PHP `empty()` descarta "0": el helper no emitiría la regla y quedaría el margen
    por defecto del theme (`class-mfn-helper.php:198` y `:406`). Se escribe "0px"."""
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


def glass_card(padding=("2.25rem", "1.5rem"), extra=None):
    """Tarjeta translúcida con desenfoque (bg-blur-1 del diseño)."""
    d, m = padding
    attr = {
        "background_switcher": "default",
        "css_advanced_background_color": css(S_WRAP_IN, "background-color",
                                             "rgba(31,31,31,0.12)"),
        "css_backdrop_filter": css(S_WRAP_IN, "backdrop-filter",
                                   {"desktop": {"blur": "60", "string": "blur(60px)"}}),
        "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                          {"desktop": "12px 12px 12px 12px"}),
        "css_advanced_padding": css(S_WRAP_IN, "padding",
                                    pad({"top": d, "right": d, "bottom": d, "left": d},
                                        None,
                                        {"top": m, "right": m, "bottom": m, "left": m})),
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


def t_h4(sel):
    return typo(sel,
                {"font-size": "28px", "line-height": "1.2",
                 "letter-spacing": "-1.12px", "font-weight": "400"},
                None,
                {"font-size": "22px", "line-height": "1.2",
                 "letter-spacing": "-0.8px", "font-weight": "400"})


def t_pxl(sel):
    return typo(sel,
                {"font-size": "22px", "line-height": "1.6"},
                None,
                {"font-size": "18px", "line-height": "1.6"})


def t_pm(sel, weight="400"):
    return typo(sel,
                {"font-size": "18px", "line-height": "1.6", "font-weight": weight},
                None,
                {"font-size": "16px", "line-height": "1.6", "font-weight": weight})


def t_caps(sel):
    return typo(sel,
                {"font-size": "16px", "line-height": "1.4", "text-transform": "uppercase"},
                None,
                {"font-size": "14px", "line-height": "1.4", "text-transform": "uppercase"})


# ================================================================ 1. HERO
hero = section(
    sec_base(
        pad({"top": "2.25rem", "right": "2.25rem", "bottom": "2.25rem", "left": "2.25rem"},
            {"top": "8rem", "right": "2rem", "bottom": "2.5rem", "left": "2rem"},
            {"top": "7rem", "right": "1.25rem", "bottom": "2rem", "left": "1.25rem"}),
        dict(sec_bg_image("hero-portada.jpg"), **{
            "height_switcher": "custom",
            "css_advanced_height": css(S_SECTION, "height",
                                       {"desktop": "1117px", "tablet": "880px", "mobile": "auto"}),
            "css_advanced_align_items": css(S_SECT_WRAP, "align-items",
                                            {"desktop": "flex-end"}),
            "css_advanced_justify_content": css(S_SECT_WRAP, "justify-content",
                                                {"desktop": "space-between"}),
        })),
    [
        # El titular ocupa fila propia (wrap 1/1); el ancho de 650px del diseño se
        # consigue con el `size` del propio item, no con un width fijo del wrap:
        # así el resto de wraps no sube a esta fila al hacer flex-wrap.
        wrap(
            {
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "7.5rem"},
                                               {"bottom": "4rem"},
                                               {"bottom": "3rem"})),
            },
            [
                item("heading", {
                    "title": "Diseño, ejecución y mantenimiento de proyectos integrales de instalaciones",
                    "header_tag": "h1",
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": t_h1(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, size="2/5", tablet="1/2", mobile="1/1", title="Hero title"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Hero — titular"),
        wrap(
            dict(glass_card(("1.5rem", "1.25rem")), **dict(
                wrap_width("500px", "420px"),
                **{"css_advanced_align_self": css(S_WRAP, "align-self", {"desktop": "flex-end"}),
                   "css_advanced_margin": css(S_WRAP_IN, "margin",
                                              pad({"bottom": "0"}, None, {"bottom": "1.5rem"}))})),
            [
                item("heading", {
                    "title": "Diseño e ingeniería",
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": t_h4(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "0.5rem"})),
                }, title="Servicio destacado — título"),
                item("plain_text", {
                    "content": ("Desarrollo de proyectos técnicos adaptados a cada cliente, "
                                "combinando innovación, eficiencia y precisión."),
                    "css_descdesca_color": css(S_DESC_C, "color", OFFWHITE),
                    "css_desc_typography": t_pm(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1.25rem"})),
                }, title="Servicio destacado — texto"),
                item("button", btn("Saber más", "/servicios/diseno-e-ingenieria/", WHITE, BLACK, {
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }), size="1/2", tablet="1/2", mobile="1/1", title="Servicio destacado — botón"),
            ],
            size="1/3", tablet="1/2", mobile="1/1", title="Hero — tarjeta servicio"),
        wrap(
            dict(wrap_width("564px", "480px"), **{
                "css_advanced_align_self": css(S_WRAP, "align-self", {"desktop": "flex-end"}),
            }),
            [
                item("plain_text", {
                    "content": ("En Nordés Ancín desarrollamos soluciones de ingeniería y montaje en "
                                "climatización, ventilación, frío industrial, fontanería, saneamiento, "
                                "protección contra incendios, evacuación de humos, electricidad y "
                                "cuadros eléctricos y de control."),
                    "css_descdesca_color": css(S_DESC_C, "color", WHITE),
                    "css_desc_typography": t_pxl(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Hero — descripción"),
            ],
            size="1/3", tablet="1/2", mobile="1/1", title="Hero — texto"),
    ],
    title="Hero — Portada")

# ================================================================ 2. VALUE PROP
# (prefijo, número, sufijo, separador de miles, descripción)
STATS = [
    ("+", "1000", "", "space", "Profesionales en plantilla"),
    ("", "600", "", "", "Clientes en activo"),
    ("+", "8000", "", "space", "Proyectos anuales"),
    ("", "98", "%", "", "Clientes recurrentes"),
]

# selectores del counter
S_CNT       = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .counter"
S_CNT_NUMW  = S_CNT + " .number-wrapper"
S_CNT_NUM   = S_CNT_NUMW + " .number"
S_CNT_PRE   = S_CNT_NUMW + " .prefix"
S_CNT_POST  = S_CNT_NUMW + " .postfix"
S_CNT_TITLE = S_CNT + " .title"


def t_cifra(sel):
    return typo(sel,
                {"font-size": "48px", "line-height": "1.2", "font-weight": "400"},
                None,
                {"font-size": "36px", "line-height": "1.2", "font-weight": "400"})


def stat_wrap(prefix, number, postfix, separator, label):
    """Cifra animada con `counter`: anima de 0 a `number` al entrar en viewport
    (`scripts.js:1425-1465`). `icon` e `image` vacíos o se pinta el `icon-lamp` por defecto."""
    return wrap(
        dict(wrap_width("180px", "180px", "50%"), **{
            "css_advanced_margin": css(S_WRAP_IN, "margin",
                                       pad({"left": "2rem", "right": "2rem", "bottom": "0"},
                                           {"left": "1.25rem", "right": "1.25rem", "bottom": "0"},
                                           {"left": "0", "right": "0", "bottom": "2rem"})),
        }),
        [
            item("counter", {
                "icon": "",
                "image": "",
                "prefix": prefix,
                "number": number,
                "label": postfix,
                "thousands_separator": separator,
                "duration": "1500",
                "type": "vertical",
                "title": label,
                "title_tag": "p",
                "css_counter_text_align": css(S_CNT, "text-align", {"desktop": "center"}),
                "css_counternumber-wrappernumber_color": css(S_CNT_NUM, "color", TEXTDARK),
                "css_counternumber-wrappernumber_typography": t_cifra(S_CNT_NUM),
                "css_counternumber-wrapperprefix_color": css(S_CNT_PRE, "color", TEXTDARK),
                "css_counternumber-wrapperprefix_typography": t_cifra(S_CNT_PRE),
                "css_counternumber-wrapperpostfix_color": css(S_CNT_POST, "color", TEXTDARK),
                "css_counternumber-wrapperpostfix_typography": t_cifra(S_CNT_POST),
                "css_counternumber-wrapper_margin": css(S_CNT_NUMW, "margin",
                                                        pad({"bottom": "1.5rem"}, None,
                                                            {"bottom": "0.75rem"})),
                "css_countertitle_color": css(S_CNT_TITLE, "color", DARKGRAY),
                "css_countertitle_typography": t_caps(S_CNT_TITLE),
                "css_countertitle_margin": css(S_CNT_TITLE, "margin", pad({"bottom": "0"})),
                "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
            }, title="Cifra — " + label),
        ],
        size="1/4", tablet="1/4", mobile="1/2", title="Cifra — " + label)


value_prop = section(
    sec_base(
        pad({"top": "7.5rem", "right": "2.25rem", "bottom": "7.5rem", "left": "2.25rem"},
            {"top": "5rem", "right": "2rem", "bottom": "5rem", "left": "2rem"},
            {"top": "3.5rem", "right": "1.25rem", "bottom": "3.5rem", "left": "1.25rem"}),
        {
            "background_switcher": "default",
            "css_advanced_background_color": css(S_SECTION, "background-color", WHITE),
            "css_advanced_justify_content": css(S_SECT_WRAP, "justify-content",
                                                {"desktop": "center"}),
        }),
    [
        wrap(
            {
                "css_advanced_justify_content": css(S_WRAP_IN, "justify-content",
                                                    {"desktop": "center"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "4rem"}, None, {"bottom": "2.5rem"})),
            },
            [
                item("heading", {
                    "title": ("Soluciones técnicas integrales para instalaciones eficientes, seguras "
                              "y duraderas, con ingeniería propia, equipo especializado y "
                              "acompañamiento en todas las fases del proyecto."),
                    "header_tag": "h2",
                    "css_txt_align": css(S_TITLE, "text-align", {"desktop": "center"}),
                    "css_color": css(S_TITLE_C, "color", BLACK),
                    "css_typography": typo(S_TITLE,
                                           {"font-size": "42px", "line-height": "1.2",
                                            "letter-spacing": "-1.68px", "font-weight": "400"},
                                           {"font-size": "34px", "line-height": "1.2",
                                            "letter-spacing": "-1.2px", "font-weight": "400"},
                                           {"font-size": "26px", "line-height": "1.25",
                                            "letter-spacing": "-0.8px", "font-weight": "400"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, size="2/3", tablet="5/6", mobile="1/1", title="Value prop — titular"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Value prop — texto"),
    ] + [stat_wrap(*s) for s in STATS] + [
        wrap(
            {
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"top": "4rem"}, None, {"top": "1.5rem"})),
            },
            [
                item("button", btn("Conoce Nordés Ancín", "/empresa/", PRIMARY, WHITE, {
                    "css__text_align": css(S_ITEM, "text-align", {"desktop": "center"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }), title="Value prop — botón"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Value prop — acción"),
    ],
    title="Value proposition")

# ================================================================ 3. PROYECTO DESTACADO
proyecto = section(
    sec_base(
        pad({"top": "2.25rem", "right": "2.25rem", "bottom": "2.25rem", "left": "2.25rem"},
            {"top": "2rem", "right": "2rem", "bottom": "2rem", "left": "2rem"},
            {"top": "2rem", "right": "1.25rem", "bottom": "2rem", "left": "1.25rem"}),
        dict(sec_bg_image("proyecto-destacado-ikea.jpg"), **{
            "height_switcher": "custom",
            "css_advanced_height": css(S_SECTION, "height",
                                       {"desktop": "1117px", "tablet": "880px", "mobile": "auto"}),
            "background_overlay_switcher": "default",
            "css_advanced_background_overlay_background_color":
                css(S_SECT_OVER, "background-color", "rgba(31,31,31,0.24)"),
            "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "flex-end"}),
        })),
    [
        wrap(
            dict(glass_card(), **dict(
                wrap_width("500px", "440px"),
                **{"css_advanced_min_height": css(S_WRAP_IN, "min-height",
                                                  {"desktop": "680px", "tablet": "560px",
                                                   "mobile": "auto"})})),
            [
                item("plain_text", {
                    "content": "Proyectos retail",
                    "css_descdesca_color": css(S_DESC_C, "color", WHITE),
                    "css_desc_typography": t_caps(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "2.5rem"}, None, {"bottom": "1.5rem"})),
                }, title="Proyecto — categoría"),
                item("image", {
                    "src": MEDIA + "logo-ikea-blanco.svg",
                    "stretch": "0",
                    "alt": "IKEA",
                    "lazy_load": "",
                    "css_image_frame_width": css(S_IMGFRAME, "width",
                                                 {"desktop": "186px", "mobile": "140px"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "7.5rem"},
                                                   {"bottom": "4rem"},
                                                   {"bottom": "2.5rem"})),
                }, title="Proyecto — logo cliente"),
                item("heading", {
                    "title": "Instalación de climatización en local comercial",
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": t_h3(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }, title="Proyecto — título"),
                item("plain_text", {
                    "content": ("Instalación de climatización. Ventilación de Garajes. Detección de CO. "
                                "Sistema de control centralizado. Producción de ACS mediante un campo de "
                                "paneles solares y calderas de apoyo."),
                    "css_descdesca_color": css(S_DESC_C, "color", WHITE),
                    "css_desc_typography": t_pm(S_DESC, weight="700"),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "4rem"}, None, {"bottom": "2rem"})),
                }, title="Proyecto — descripción"),
                item("button", btn("Proyectos destacados", "/proyectos/", WHITE, BLACK, {
                    "css_button_justify_content": css(
                        ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button.button_full_width",
                        "justify-content", {"desktop": "center"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, full=True), title="Proyecto — botón"),
            ],
            size="1/3", tablet="1/2", mobile="1/1", title="Proyecto destacado — tarjeta"),
    ],
    title="Proyecto destacado")

# ================================================================ 4. SERVICIOS
SERVICIOS = [
    ("icono-diseno-ingenieria.svg", "Diseño e ingeniería",
     "Desarrollo de proyectos técnicos adaptados a cada cliente, combinando innovación, "
     "eficiencia y precisión.", "/servicios/diseno-e-ingenieria/"),
    ("icono-ejecucion-instalaciones.svg", "Ejecución de instalaciones",
     "Ejecución integral de instalaciones con equipo propio altamente especializado.",
     "/servicios/ejecucion-de-instalaciones/"),
    ("icono-cuadros-electricos.svg", "Cuadros eléctricos y de control",
     "Diseño, montaje y puesta en marcha de cuadros eléctricos y de control adaptados a las "
     "necesidades de cada instalación.", "/servicios/cuadros-electricos-y-de-control/"),
    ("icono-mantenimiento-postventa.svg", "Mantenimiento y postventa",
     "Servicios de mantenimiento orientados a garantizar la continuidad y eficiencia de las "
     "instalaciones.", "/servicios/mantenimiento-y-postventa/"),
]


def servicio_wrap(icono, titulo, texto, link):
    """Tarjeta = wrap anidado (celda del grid). El grid del wrap padre pone los gaps
    exactos del diseño (36px) y estira todas las celdas a la misma altura; `height: 100%`
    hace que el fondo blanco de la tarjeta llene la celda."""
    return nested(
        {
            "background_switcher": "default",
            "css_advanced_background_color": css(S_WRAP_IN, "background-color", WHITE),
            "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                              {"desktop": "12px 12px 12px 12px"}),
            "css_advanced_padding": css(S_WRAP_IN, "padding",
                                        pad({"top": "2.25rem", "right": "2.25rem",
                                             "bottom": "2.25rem", "left": "2.25rem"},
                                            None,
                                            {"top": "1.5rem", "right": "1.5rem",
                                             "bottom": "1.5rem", "left": "1.5rem"})),
            "height_switcher": "custom",
            "css_advanced_height": css(S_WRAP_IN, "height", {"desktop": "100%"}),
            "css_advanced_align_content": css(S_WRAP_IN, "align-content",
                                              {"desktop": "space-between"}),
        },
        [
            item("image", {
                "src": MEDIA + icono,
                "stretch": "0",
                "alt": titulo,
                "lazy_load": "",
                "css_image_frame_width": css(S_IMGFRAME, "width",
                                             {"desktop": "77px", "mobile": "60px"}),
                "css_advanced_margin": css(S_ITEM_IN, "margin",
                                           pad({"bottom": "2.25rem"}, None, {"bottom": "1.5rem"})),
            }, title="Servicio — icono"),
            item("heading", {
                "title": titulo,
                "header_tag": "h3",
                "link": link,
                "css_color": css(S_TITLE_C, "color", BLACK),
                "css_typography": t_h3(S_TITLE),
                "css_advanced_margin": css(S_ITEM_IN, "margin",
                                           pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
            }, title="Servicio — título"),
            item("plain_text", {
                "content": texto,
                "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                "css_desc_typography": t_pm(S_DESC),
                "css_advanced_margin": css(S_ITEM_IN, "margin",
                                           pad({"bottom": "2.25rem"}, None, {"bottom": "1.5rem"})),
            }, title="Servicio — descripción"),
            item("button", btn("Saber más", link, PRIMARY, WHITE, {
                "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
            }), size="1/2", tablet="1/2", mobile="1/1", title="Servicio — botón"),
        ],
        size="1/1", tablet="1/1", mobile="1/1", title="Servicio — " + titulo)


servicios = section(
    sec_base(
        pad({"top": "7.5rem", "right": "2.25rem", "bottom": "7.5rem", "left": "2.25rem"},
            {"top": "5rem", "right": "2rem", "bottom": "5rem", "left": "2rem"},
            {"top": "3.5rem", "right": "1.25rem", "bottom": "3.5rem", "left": "1.25rem"}),
        {
            "background_switcher": "default",
            "css_advanced_background_color": css(S_SECTION, "background-color", OFFWHITE),
        }),
    [
        wrap(
            dict(wrap_width("650px", "60%"), **{
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "4rem"}, None, {"bottom": "1.5rem"})),
            }),
            [
                item("heading", {
                    "title": "Descubre nuestros servicios integrales en instalaciones",
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", BLACK),
                    "css_typography": t_h2(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Servicios — titular"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Servicios — cabecera"),
        wrap(
            {
                "css_advanced_align_self": css(S_WRAP, "align-self", {"desktop": "flex-end"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "4rem"}, None, {"bottom": "2.5rem"})),
            },
            [
                item("button", btn("Todos los servicios", "/servicios/", PRIMARY, WHITE, {
                    "css__text_align": css(S_ITEM, "text-align",
                                           {"desktop": "right", "mobile": "left"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }), title="Servicios — botón"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Servicios — acción"),
        wrap(
            {
                "grid": "grid",
                "grid_columns_switcher": "",
                "css_grid_columns": css(S_WRAP_GRID, "grid-template-columns",
                                        {"desktop": "repeat(4, 1fr)",
                                         "tablet": "repeat(2, 1fr)",
                                         "mobile": "1fr"}),
                "css_grid_columns_gap": css(S_WRAP_GRID, "column-gap",
                                            {"desktop": "2.25rem", "tablet": "2rem", "mobile": "0px"}),
                "css_grid_rows_gap": css(S_WRAP_GRID, "row-gap",
                                         {"desktop": "2.25rem", "tablet": "2rem", "mobile": "1.5rem"}),
            },
            [servicio_wrap(*s) for s in SERVICIOS],
            size="1/1", tablet="1/1", mobile="1/1", title="Servicios — tarjetas"),
    ],
    title="Servicios")

# ================================================================ 5. EMPLEO
empleo = section(
    sec_base(
        pad({"top": "2.25rem", "right": "2.25rem", "bottom": "2.25rem", "left": "2.25rem"},
            {"top": "2rem", "right": "2rem", "bottom": "2rem", "left": "2rem"},
            {"top": "2rem", "right": "1.25rem", "bottom": "2rem", "left": "1.25rem"}),
        dict(sec_bg_image("empleo-portada.jpg"), **{
            "height_switcher": "custom",
            "css_advanced_height": css(S_SECTION, "height",
                                       {"desktop": "1117px", "tablet": "820px", "mobile": "auto"}),
            "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "flex-end"}),
        })),
    [
        wrap(
            dict(glass_card(), **wrap_width("500px", "440px")),
            [
                item("heading", {
                    "title": ("Únete a Nordés Ancín y desarrolla tu carrera en un entorno técnico "
                              "y comprometido."),
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", WHITE),
                    "css_typography": t_h3(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }, title="Empleo — titular"),
                item("plain_text", {
                    "content": ("Apostamos por un entorno donde aprender, aportar y construir "
                                "soluciones eficientes junto a un equipo técnico comprometido."),
                    "css_descdesca_color": css(S_DESC_C, "color", EMPLEOTXT),
                    "css_desc_typography": typo(S_DESC,
                                                {"font-size": "16px", "line-height": "1.4"},
                                                None,
                                                {"font-size": "15px", "line-height": "1.5"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "4rem"}, None, {"bottom": "2rem"})),
                }, title="Empleo — texto"),
                item("button", btn("Trabaja con nosotros", "/empleo/", WHITE, BLACK, {
                    "css_button_justify_content": css(
                        ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button.button_full_width",
                        "justify-content", {"desktop": "center"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, full=True), title="Empleo — botón"),
            ],
            size="1/3", tablet="1/2", mobile="1/1", title="Empleo — tarjeta"),
    ],
    title="Empleo")

# ================================================================ 6. ACTUALIDAD (query loop)
# Tarjeta del loop DENTRO de un wrap anidado (item_is_wrap: 1). Nunca items sueltos:
# el primer guardado del VB los borraría (regla E016 del validador).
NOTICIA_ITEMS = [
    item("image", {
        "src": "{featured_image}",
        "stretch": "1",
        "alt": "{title}",
        "link": "{permalink}",
        "lazy_load": "",
        "image_height": "custom",
        "image_height_style": "",
        "css_image_cover_height": css(S_IMGCOVER, "height",
                                      {"desktop": "249px", "tablet": "220px", "mobile": "200px"}),
        "css_image_border_radius": css(S_IMGFRAME, "border-radius",
                                       {"desktop": "12px 12px 12px 12px"}),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   pad({"bottom": "1rem"}, None, {"bottom": "0.75rem"})),
    }, title="Noticia — imagen"),
    item("plain_text", {
        "content": "{date}",
        "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
        "css_desc_typography": t_pm(S_DESC),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   pad({"bottom": "0.5rem"}, None, {"bottom": "0.375rem"})),
    }, title="Noticia — fecha"),
    item("heading", {
        "title": "{title}",
        "header_tag": "h3",
        "link": "{permalink}",
        "css_color": css(S_TITLE_C, "color", BLACK),
        "css_typography": typo(S_TITLE,
                               {"font-size": "22px", "line-height": "1.6", "font-weight": "400"},
                               None,
                               {"font-size": "19px", "line-height": "1.5", "font-weight": "400"}),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
    }, title="Noticia — título"),
    item("button", btn("Leer más", "{permalink}", PRIMARY, WHITE, {
        "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
    }), size="1/2", tablet="1/2", mobile="1/1", title="Noticia — botón"),
]

actualidad = section(
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
                    "title": "Actualidad, proyectos y novedades de Nordés Ancín",
                    "header_tag": "h2",
                    "css_color": css(S_TITLE_C, "color", BLACK),
                    "css_typography": t_h2(S_TITLE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Actualidad — titular"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Actualidad — cabecera"),
        wrap(
            {
                "css_advanced_align_self": css(S_WRAP, "align-self", {"desktop": "flex-end"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "4rem"}, None, {"bottom": "2.5rem"})),
            },
            [
                item("button", btn("Todas las noticias", "/actualidad/", PRIMARY, WHITE, {
                    "css__text_align": css(S_ITEM, "text-align",
                                           {"desktop": "right", "mobile": "left"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }), title="Actualidad — botón"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Actualidad — acción"),
        wrap(
            {
                "type": "query",
                "query_type": "posts",
                "query_post_type": "post",
                "query_post_orderby": "date",
                "query_post_order": "DESC",
                "query_post_per_page": "4",
                "query_display": "",
                "grid": "grid",
                "grid_columns_switcher": "",
                "css_grid_columns": css(S_WRAP_GRID, "grid-template-columns",
                                        {"desktop": "repeat(4, 1fr)",
                                         "tablet": "repeat(2, 1fr)",
                                         "mobile": "1fr"}),
                "css_grid_columns_gap": css(S_WRAP_GRID, "column-gap",
                                            {"desktop": "2.25rem", "tablet": "2rem", "mobile": "0px"}),
                "css_grid_rows_gap": css(S_WRAP_GRID, "row-gap",
                                         {"desktop": "3rem", "tablet": "2.5rem", "mobile": "2.5rem"}),
            },
            [nested({}, NOTICIA_ITEMS, size="1/1", tablet="1/1", mobile="1/1",
                    title="Tarjeta noticia")],
            size="1/1", tablet="1/1", mobile="1/1", title="Actualidad — listado"),
    ],
    title="Actualidad")

# ================================================================ 7. CTA
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
data = [hero, value_prop, proyecto, servicios, empleo, actualidad, cta]

with open(HERE / "nordes-ancin-portada.json", "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("secciones:", len(data))
