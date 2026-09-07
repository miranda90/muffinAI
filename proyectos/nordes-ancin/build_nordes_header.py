# -*- coding: utf-8 -*-
"""Genera el JSON BeBuilder del header (Figma 2572:6423) y del menú lateral que
abre la hamburguesa (Figma 2587:16054) — Nordés Ancín.

Salidas:
  nordes-ancin-header.json    → plantilla tipo **Header**
  nordes-ancin-sidemenu.json  → plantilla tipo **Sidebar menu** (Betheme "sidemenu")

La hamburguesa es visible en las tres resoluciones; el menú horizontal solo en
desktop/laptop (`visibility: " hide-tablet hide-mobile"`).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- tokens
PRIMARY   = "#001689"
BLACK     = "#1F1F1F"
WHITE     = "#FCFCFC"
OFFWHITE  = "#F1F1EE"
GRAYLABEL = "#A3A3A3"
GLASS     = "rgba(31,31,31,0.12)"
LINE      = "rgba(252,252,252,0.24)"
MEDIA     = "https://nordesancin.com/wp-content/uploads/2026/07/"

MAXW      = "1728px"

# term_id del nav_menu "Main Menu" en el dev. Betheme exige un id numérico:
# si va vacío, el header pinta los placeholders "Item 1 / Item 2 / Item 3".
MENU_PRINCIPAL = "6"

# selectores base -------------------------------------------------------
S_SECTION   = ".mcb-section-mfnuidelement"
S_SECT_WRAP = ".mcb-section-mfnuidelement .section_wrapper"
S_SECT_MAXW = ".mcb-section-mfnuidelement.custom-width .section_wrapper"
S_WRAP      = ".mcb-section .mcb-wrap-mfnuidelement"
S_WRAP_IN   = ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner"
S_WRAP_GRID = ".mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement .mcb-wrap-inner"
S_WRAP_GRIDC = (".mcb-section .mcb-wrap-grid.mcb-wrap-grid-col-custom.mcb-wrap-mfnuidelement "
                ".mcb-wrap-inner")
S_ITEM      = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement"
S_ITEM_IN   = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner"
S_DESC      = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc"
S_DESC_C    = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc,"
               ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc a")
S_BUTTON    = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button"
S_IMGFRAME  = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame"

# selectores propios de los elementos de header (copiados de
# class-mfn-builder-fields.php vía builder-elements/_elements.json)
S_LOGO_WRAP = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .logo-wrapper"
S_HMENU     = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu"
S_HMENU_LI  = S_HMENU + " > li.mfn-menu-li"
S_HMENU_A   = S_HMENU_LI + " > a.mfn-menu-link"
S_HMENU_AH  = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu "
               "> li.mfn-menu-li:hover > a.mfn-menu-link")
S_BURGER    = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu-burger"
S_BURGER_I  = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper i"
S_BURGER_IW = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper"
S_WPML_A    = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-language-switcher ul li a"
S_WPML_ARR  = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement "
               ".mfn-language-switcher-dropdown.mfn-language-switcher-dropdown-icon ul li a "
               ".mfn-arrow-icon")
S_SIDE_A    = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu "
               "li a.mfn-menu-link")
S_SIDE_AH   = S_SIDE_A + ":hover"
S_SIDE_LI   = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li"
S_SIDE_SUBI = S_SIDE_LI + " .outer-menu-sub i"

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
    """PHP `empty()` descarta "0" y el helper no emite la regla: se escribe "0px"."""
    return {k: ("0px" if v in ("0", 0) else v) for k, v in side_vals.items()}


def pad(desktop, tablet=None, mobile=None):
    val = {"desktop": _no_zero(desktop)}
    if tablet:
        val["tablet"] = _no_zero(tablet)
    val["mobile"] = _no_zero(mobile) if mobile else _no_zero(desktop)
    return val


def section(attr, wraps, title="Section", ver="default"):
    return {"uid": uid("sec"), "icon": "section", "jsclass": "section",
            "title": title, "ver": ver, "attr": attr, "wraps": wraps}


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


def wrap_width(desktop, tablet=None, mobile="100%"):
    return {
        "width_switcher": "custom",
        "css_advanced_flex": css(S_WRAP, "width",
                                 {"desktop": desktop,
                                  "tablet": tablet or desktop,
                                  "mobile": mobile}),
    }


def item_width(desktop, tablet=None, mobile=None):
    return {
        "width_switcher": "custom",
        "css_advanced_flex": css(S_ITEM, "width",
                                 {"desktop": desktop,
                                  "tablet": tablet or desktop,
                                  "mobile": mobile or tablet or desktop}),
    }


# tipografías del diseño ------------------------------------------------
def t_nav(sel):
    """a-nav: 16 / 1 / -0.64px."""
    return typo(sel,
                {"font-size": "16px", "line-height": "1",
                 "letter-spacing": "-0.64px", "font-weight": "400"},
                None,
                {"font-size": "15px", "line-height": "1",
                 "letter-spacing": "-0.6px", "font-weight": "400"})


def t_h3(sel):
    return typo(sel,
                {"font-size": "36px", "line-height": "1.24",
                 "letter-spacing": "-0.72px", "font-weight": "500"},
                {"font-size": "32px", "line-height": "1.24",
                 "letter-spacing": "-0.64px", "font-weight": "500"},
                {"font-size": "28px", "line-height": "1.24",
                 "letter-spacing": "-0.56px", "font-weight": "500"})


def t_pl(sel):
    """p-L: 20 / 1.4 / -0.4px."""
    return typo(sel,
                {"font-size": "20px", "line-height": "1.4", "letter-spacing": "-0.4px"},
                None,
                {"font-size": "18px", "line-height": "1.4", "letter-spacing": "-0.36px"})


def t_pm(sel):
    return typo(sel,
                {"font-size": "18px", "line-height": "1.6"},
                None,
                {"font-size": "16px", "line-height": "1.6"})


def t_ps(sel):
    """p-S: 13.3 / 1.6."""
    return typo(sel,
                {"font-size": "13.3px", "line-height": "1.6"},
                None,
                {"font-size": "13px", "line-height": "1.6"})


def label(text, bottom="2.25rem", bottom_mobile="1.5rem", title="Etiqueta"):
    """Etiqueta gris en mayúsculas del panel lateral (MENÚ / CONTACTO / REDES)."""
    return item("plain_text", {
        "content": text,
        "css_descdesca_color": css(S_DESC_C, "color", GRAYLABEL),
        "css_desc_typography": typo(S_DESC,
                                    {"font-size": "18px", "line-height": "1.6",
                                     "text-transform": "uppercase"},
                                    None,
                                    {"font-size": "16px", "line-height": "1.6",
                                     "text-transform": "uppercase"}),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   pad({"bottom": bottom}, None, {"bottom": bottom_mobile})),
    }, title=title)


# ================================================================ HEADER
# Sección única del template de header. `ver: "default"`; si más adelante se
# quiere una versión sticky distinta, se añade otra sección con
# `ver: "header-sticky"` (front.php:448-450).
header = section(
    {
        "width_switcher": "custom",
        "css_advanced_max_width": css(S_SECT_MAXW, "max-width", MAXW),
        "css_advanced_padding": css(S_SECTION, "padding",
                                    pad({"top": "2.25rem", "right": "2.25rem",
                                         "bottom": "2.25rem", "left": "2.25rem"},
                                        {"top": "1.5rem", "right": "1.5rem",
                                         "bottom": "1.5rem", "left": "1.5rem"},
                                        {"top": "1rem", "right": "1.25rem",
                                         "bottom": "1rem", "left": "1.25rem"})),
        "css_advanced_align_items": css(S_SECT_WRAP, "align-items", {"desktop": "center"}),
        "css_advanced_justify_content": css(S_SECT_WRAP, "justify-content",
                                            {"desktop": "space-between"}),
    },
    [
        # --- logo -----------------------------------------------------
        wrap(
            {
                "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "center"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin", pad({"bottom": "0"})),
            },
            [
                item("header_logo", dict(item_width("228px", "200px", "160px"), **{
                    "image": MEDIA + "logo-nordes-ancin-blanco.svg",
                    "link": "/",
                    "css_logo_align": css(S_LOGO_WRAP, "align-items", {"desktop": "center"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }), title="Logotipo"),
            ],
            size="1/4", tablet="1/3", mobile="1/2", title="Header — logo"),

        # --- bloque derecho: píldora + botón --------------------------
        wrap(
            {
                "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "center"}),
                "css_advanced_justify_content": css(S_WRAP_IN, "justify-content",
                                                    {"desktop": "flex-end"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin", pad({"bottom": "0"})),
            },
            [
                # píldora translúcida (bg-blur-1 del diseño)
                nested(
                    dict(wrap_width("668px", "auto", "auto"), **{
                        "background_switcher": "default",
                        "css_advanced_background_color": css(S_WRAP_IN, "background-color", GLASS),
                        "css_backdrop_filter": css(S_WRAP_IN, "backdrop-filter",
                                                   {"desktop": {"blur": "60",
                                                                "string": "blur(60px)"}}),
                        "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                                          {"desktop": "12px 12px 12px 12px"}),
                        "css_advanced_padding": css(S_WRAP_IN, "padding",
                                                    pad({"top": "0.5rem", "right": "0.5rem",
                                                         "bottom": "0.5rem", "left": "1rem"},
                                                        None,
                                                        {"top": "0.375rem", "right": "0.375rem",
                                                         "bottom": "0.375rem", "left": "0.5rem"})),
                        "css_advanced_align_items": css(S_WRAP_IN, "align-items",
                                                        {"desktop": "center"}),
                        "css_advanced_justify_content": css(S_WRAP_IN, "justify-content",
                                                            {"desktop": "space-between",
                                                             "tablet": "flex-end"}),
                        "css_advanced_margin": css(S_WRAP_IN, "margin",
                                                   pad({"right": "0.5rem", "bottom": "0"})),
                    }),
                    [
                        # menú horizontal: solo desktop/laptop, la navegación de
                        # tablet y móvil la cubre la hamburguesa
                        item("header_menu", {
                            "menu_display": MENU_PRINCIPAL,
                            "visibility": " hide-tablet hide-mobile",
                            "submenu_display": "hover",
                            "submenu_icon_display": "on",
                            "submenu_icon": "fas fa-angle-down",
                            "submenu_animation": "fade-up",
                            "css_header_menu_justify": css(S_HMENU, "justify-content",
                                                           {"desktop": "flex-start"}),
                            "css_menu-li_header_menu_gap": css(S_HMENU_LI,
                                                               "--mfn-header-menu-gap",
                                                               {"desktop": "24px"}),
                            "css_menu-link_padding": css(S_HMENU_A, "padding",
                                                         pad({"top": "0", "right": "0",
                                                              "bottom": "0", "left": "0"})),
                            "css_menu-link_typography": t_nav(S_HMENU_A),
                            "css_menu-link_color": css(S_HMENU_A, "color", WHITE),
                            "css_menu-link_color_hover": css(S_HMENU_AH, "color", OFFWHITE),
                            "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                        }, size="2/3", tablet="1/1", mobile="1/1", title="Menú principal"),

                        # selector de idioma (WPML)
                        item("header_language_switcher", {
                            "style": "dropdown",
                            "flags": "0",
                            "background_switcher": "default",
                            "dropdown_icon": "1",
                            "dropdown_icon_html": "fas fa-angle-down",
                            "css_language-switcherullia_background_color":
                                css(S_WPML_A, "background-color", OFFWHITE),
                            "css_language-switcherullia_color": css(S_WPML_A, "color", BLACK),
                            "css_language-switcherullia_typography": t_ps(S_WPML_A),
                            "css_language-switcherullia_border_radius":
                                css(S_WPML_A, "border-radius", {"desktop": "8px 8px 8px 8px"}),
                            "css_language-switcherullia_padding":
                                css(S_WPML_A, "padding",
                                    pad({"top": "0.75rem", "right": "0.75rem",
                                         "bottom": "0.75rem", "left": "0.75rem"})),
                            "css_language-switcher-dropdown-icon-ul-li-a-arrow-icon_arrow_size":
                                css(S_WPML_ARR, "--mfn-wpml-arrow-size", {"desktop": "12px"}),
                            "css_advanced_margin": css(S_ITEM_IN, "margin",
                                                       pad({"right": "0.5rem", "bottom": "0"})),
                        }, size="1/6", tablet="1/2", mobile="1/2", title="Idioma (WPML)"),

                        # hamburguesa: visible en todas las resoluciones
                        item("header_burger", {
                            "icon": "fas fa-bars",
                            "link_title": "Abrir menú",
                            "background_switcher": "default",
                            "sidebar_type": "0",
                            "menu_display": MENU_PRINCIPAL,
                            "menu_pos": "right",
                            "css_menu-burger_background_color": css(S_BURGER, "background-color",
                                                                    BLACK),
                            "css_menu-burger_border_radius": css(S_BURGER, "border-radius",
                                                                 {"desktop": "8px 8px 8px 8px"}),
                            "css_menu-burger_padding": css(S_BURGER, "padding",
                                                           pad({"top": "0.75rem", "right": "1rem",
                                                                "bottom": "0.75rem",
                                                                "left": "1rem"})),
                            "css_icon-wrapperi_color": css(S_BURGER_I, "color", WHITE),
                            "css_icon-boxicon_icon_size": css(S_BURGER_IW,
                                                              "--mfn-header-menu-icon-size",
                                                              {"desktop": "19.2px"}),
                            "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                        }, size="1/6", tablet="1/2", mobile="1/2", title="Hamburguesa"),
                    ],
                    size="3/4", tablet="3/4", mobile="1/2", title="Header — píldora nav"),

                # botón CTA
                item("button", {
                    "title": "Contáctanos",
                    "link": "/contacto/",
                    "icon": "icon-right-thin",
                    "icon_position": "right",
                    "button_style": "",
                    "background_switcher": "default",
                    "css_button_color": css(S_BUTTON, "color", WHITE),
                    "css_button_icon_color": css(S_BUTTON + " i", "color", WHITE),
                    "css_button_background_color": css(S_BUTTON, "background-color", PRIMARY),
                    "css_button_border_radius": css(S_BUTTON, "border-radius",
                                                    {"desktop": "12px 12px 12px 12px"}),
                    "css_button_padding": css(S_BUTTON, "padding",
                                              pad({"top": "0.5rem", "right": "1rem",
                                                   "bottom": "0.5rem", "left": "1rem"},
                                                  None,
                                                  {"top": "0.5rem", "right": "0.75rem",
                                                   "bottom": "0.5rem", "left": "0.75rem"})),
                    "css_button_typography": t_nav(S_BUTTON),
                    "css__text_align": css(S_ITEM, "text-align", {"desktop": "right"}),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, size="1/4", tablet="1/4", mobile="1/2", title="Botón — Contáctanos"),
            ],
            size="3/4", tablet="2/3", mobile="1/2", title="Header — navegación"),
    ],
    title="Header — Nordés Ancín")


# ================================================================ SIDEMENU
# Contenido del panel azul. El fondo (#001689), el ancho (700px), el padding,
# la posición (derecha) y el botón de cerrar son ajustes de la plantilla
# (`set_sidemenu_fields`, post meta), no del JSON.
REDES = [
    ("icono-instagram.svg", "Instagram", "https://www.instagram.com/"),
    ("icono-linkedin.svg", "LinkedIn", "https://www.linkedin.com/"),
    ("icono-facebook.svg", "Facebook", "https://www.facebook.com/"),
]


def red_social(archivo, alt, url):
    """Cada icono es una celda del grid: items directos, sin wrap anidado
    (E016 solo afecta a los query loops)."""
    return item("image", {
        "src": MEDIA + archivo,
        "stretch": "0",
        "alt": alt,
        "link": url,
        "target": "1",
        "lazy_load": "",
        "css_image_frame_width": css(S_IMGFRAME, "width",
                                     {"desktop": "28.8px", "mobile": "24px"}),
        "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
    }, size="1/1", tablet="1/1", mobile="1/1", title="Red social — " + alt)


sidemenu = section(
    {
        "width_switcher": "full",
        "css_advanced_padding": css(S_SECTION, "padding",
                                    pad({"top": "0px", "right": "0px",
                                         "bottom": "0px", "left": "0px"})),
    },
    [
        # --- menú -----------------------------------------------------
        wrap(
            {"css_advanced_margin": css(S_WRAP_IN, "margin",
                                        pad({"bottom": "4rem"}, None, {"bottom": "2.5rem"}))},
            [
                label("Menú", title="Etiqueta — Menú"),
                item("sidemenu_menu", {
                    "tabs": [{"title": "Menú lateral", "menu": MENU_PRINCIPAL}],
                    "submenu": "on",
                    "submenu_on": "toggled",
                    "submenu_icon_display": "on",
                    "submenu_icon": "fas fa-angle-down",
                    "css_ul-sidemenu-menulia-menu-link_padding":
                        css(S_SIDE_A, "padding", pad({"top": "0", "right": "0",
                                                      "bottom": "0", "left": "0"})),
                    "css_ul-sidemenu-menulia-menu-link_margin":
                        css(S_SIDE_A, "margin",
                            pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                    "css_sidemenu-menulia-menu-link_typography": t_h3(S_SIDE_A),
                    "css_ul-sidemenu-menulia-menu-link_color": css(S_SIDE_A, "color", WHITE),
                    "css_ul-sidemenu-menu-link_color_hover": css(S_SIDE_AH, "color", OFFWHITE),
                    "css_sidemenu-menuli_sidemenu_submenu_icon_size":
                        css(S_SIDE_LI, "--mfn-sidemenu-submenu-icon-size", {"desktop": "19.2px"}),
                    "css_sidemenu-menuliouter-menu-subi_color": css(S_SIDE_SUBI, "color", WHITE),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Menú lateral"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Panel — menú"),

        # --- separador ------------------------------------------------
        wrap(
            {"css_advanced_margin": css(S_WRAP_IN, "margin",
                                        pad({"bottom": "4rem"}, None, {"bottom": "2.5rem"}))},
            [
                item("divider", {
                    "height": "1",
                    "style": "default",
                    "line": "default",
                    "color": LINE,
                    "themecolor": "0",
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Separador"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Panel — separador"),

        # --- contacto -------------------------------------------------
        wrap(
            {"css_advanced_margin": css(S_WRAP_IN, "margin",
                                        pad({"bottom": "7.5rem"}, None, {"bottom": "3rem"}))},
            [
                label("Contacto", title="Etiqueta — Contacto"),
                item("plain_text", {
                    "content": ("Polígono Espíritu Santo, c/ Monier 9-11, parcelas 36-38, "
                                "15650 Cambre"),
                    "css_descdesca_color": css(S_DESC_C, "color", WHITE),
                    "css_desc_typography": t_pl(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }, title="Dirección"),
                item("plain_text", {
                    "content": '<a href="tel:+34981138338">+34 981 138 338</a>',
                    "css_descdesca_color": css(S_DESC_C, "color", OFFWHITE),
                    "css_desc_typography": t_pm(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin",
                                               pad({"bottom": "1.5rem"}, None, {"bottom": "1rem"})),
                }, title="Teléfono"),
                item("plain_text", {
                    "content": '<a href="mailto:info@nordesancin.com">info@nordesancin.com</a>',
                    "css_descdesca_color": css(S_DESC_C, "color", OFFWHITE),
                    "css_desc_typography": t_pm(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Email"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Panel — contacto"),

        # --- redes sociales -------------------------------------------
        wrap(
            {"css_advanced_margin": css(S_WRAP_IN, "margin", pad({"bottom": "0"}))},
            [
                label("Redes sociales", bottom="2.25rem", bottom_mobile="1.5rem",
                      title="Etiqueta — Redes sociales"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Panel — redes (etiqueta)"),
        # los iconos van en grid: es el único modo de fijar el hueco de 19.2px
        # del diseño (los wraps hermanos solo tienen el gutter del theme)
        wrap(
            {
                "grid": "grid",
                "grid_columns_switcher": "custom",
                "css_grid_columns_custom": css(S_WRAP_GRIDC, "grid-template-columns",
                                               {"desktop": "repeat(3, 28.8px)",
                                                "mobile": "repeat(3, 24px)"}),
                "css_grid_columns_gap": css(S_WRAP_GRID, "column-gap",
                                            {"desktop": "1.2rem", "mobile": "1rem"}),
                "css_grid_rows_gap": css(S_WRAP_GRID, "row-gap", {"desktop": "0px"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin", pad({"bottom": "0"})),
            },
            [red_social(*r) for r in REDES],
            size="1/1", tablet="1/1", mobile="1/1", title="Panel — redes sociales"),
    ],
    title="Menú lateral — Nordés Ancín")


# ================================================================ salida
with open(HERE / "nordes-ancin-header.json", "w", encoding="utf-8") as fh:
    json.dump([header], fh, ensure_ascii=False, indent=2)

with open(HERE / "nordes-ancin-sidemenu.json", "w", encoding="utf-8") as fh:
    json.dump([sidemenu], fh, ensure_ascii=False, indent=2)

print("header: 1 sección · sidemenu: 1 sección")
