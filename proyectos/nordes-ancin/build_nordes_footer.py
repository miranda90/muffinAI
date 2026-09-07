# -*- coding: utf-8 -*-
"""Genera el JSON BeBuilder del footer (Figma 2572:6421) — Nordés Ancín.

Salida:
  nordes-ancin-footer.json  → plantilla tipo **Footer**

El nodo de Figma se llama "Call to Action and Footer": la banda CTA superior
("Preparemos una solución a medida") ya está maquetada como sección de la
portada (`build_nordes_portada.py`), así que aquí solo va el footer propiamente
dicho: tarjeta de certificaciones, tarjeta principal y barra de copyright.
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
DARKGRAY  = "#6B6B6B"
LINE      = "rgba(31,31,31,0.12)"
MEDIA     = "https://nordesancin.com/wp-content/uploads/2026/07/"

MAXW      = "1728px"

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
S_TITLE     = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title"
S_TITLE_C   = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title,"
               ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title a")
S_DESC      = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc"
S_DESC_C    = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc,"
               ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc a")
S_BUTTON    = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button"
S_IMGFRAME  = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame"

# selectores del elemento footer_menu (class-mfn-builder-fields.php)
S_FMENU_A   = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul a"
S_FMENU_AH  = ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul a:hover"
S_FMENU_UL  = (".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner "
               "ul.mfn-footer-menu-style-vertical")

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


def item_width(desktop, tablet=None, mobile=None):
    return {
        "width_switcher": "custom",
        "css_advanced_flex": css(S_ITEM, "width",
                                 {"desktop": desktop,
                                  "tablet": tablet or desktop,
                                  "mobile": mobile or tablet or desktop}),
    }


# tipografías del diseño ------------------------------------------------
def t_h4(sel):
    """h4: 28 / 1.2 / -1.12px."""
    return typo(sel,
                {"font-size": "28px", "line-height": "1.2",
                 "letter-spacing": "-1.12px", "font-weight": "400"},
                {"font-size": "26px", "line-height": "1.2",
                 "letter-spacing": "-1.04px", "font-weight": "400"},
                {"font-size": "24px", "line-height": "1.2",
                 "letter-spacing": "-0.96px", "font-weight": "400"})


def t_btn(sel):
    """a-btn: 20 / 1.4 / -0.8px."""
    return typo(sel,
                {"font-size": "20px", "line-height": "1.4", "letter-spacing": "-0.8px"},
                None,
                {"font-size": "18px", "line-height": "1.4", "letter-spacing": "-0.72px"})


def t_pm(sel):
    """p-M: 18 / 1.6."""
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


def t_caps(sel):
    """p-S en mayúsculas: etiquetas CONTACTO / MENÚ / LEGAL."""
    return typo(sel,
                {"font-size": "13.3px", "line-height": "1.6",
                 "letter-spacing": "0.5px", "text-transform": "uppercase"},
                None,
                {"font-size": "13px", "line-height": "1.6",
                 "letter-spacing": "0.5px", "text-transform": "uppercase"})


def label(text, title):
    """Etiqueta gris en mayúsculas de cada columna del footer."""
    return item("plain_text", {
        "content": text,
        "css_descdesca_color": css(S_DESC_C, "color", GRAYLABEL),
        "css_desc_typography": t_caps(S_DESC),
        "css_advanced_margin": css(S_ITEM_IN, "margin",
                                   pad({"bottom": "2.25rem"}, None, {"bottom": "1.5rem"})),
    }, title=title)


def columna_menu(texto_label, borde, title):
    """Columna de enlaces (MENÚ / LEGAL). El borde izquierdo es la línea
    vertical que separa contacto de los menús; en tablet y móvil las columnas
    se apilan, así que ahí desaparece."""
    attr = {
        "css_advanced_padding": css(S_WRAP_IN, "padding",
                                    pad({"left": "4rem" if borde else "2.25rem"},
                                        {"left": "0px"},
                                        {"left": "0px"})),
        "css_advanced_margin": css(S_WRAP_IN, "margin",
                                   pad({"bottom": "0"}, None, {"bottom": "2.25rem"})),
    }
    if borde:
        attr.update({
            # `border_style_wrap` es solo el attr_id de la condición del VB; el
            # atributo que se guarda es `css_advanced_border_style`.
            "css_advanced_border_style": css(S_WRAP_IN, "border-style", "solid"),
            "css_advanced_border_color": css(S_WRAP_IN, "border-color", LINE),
            "css_advanced_border_width": css(S_WRAP_IN, "border-width",
                                             {"desktop": "0px 0px 0px 1px",
                                              "tablet": "0px 0px 0px 0px",
                                              "mobile": "0px 0px 0px 0px"}),
        })
    return nested(attr, [
        label(texto_label, title="Etiqueta — " + texto_label),
        item("footer_menu", {
            "menu_display": "",
            "menu_style": "vertical",
            "css_mcb-column-innerul-footer-menu--vertical_text_align":
                css(S_FMENU_UL, "text-align", {"desktop": "left"}),
            "css_ula_typography": t_pm(S_FMENU_A),
            "css_ula_color": css(S_FMENU_A, "color", BLACK),
            "css_ula_color_hover": css(S_FMENU_AH, "color", PRIMARY),
            "css_ula_padding": css(S_FMENU_A, "padding",
                                   pad({"top": "0", "right": "0",
                                        "bottom": "0.5rem", "left": "0"})),
            "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
        }, title="Menú — " + texto_label),
    ], size="1/5", tablet="1/2", mobile="1/1", title=title)


REDES = [
    ("icono-instagram.svg", "Instagram", "https://www.instagram.com/"),
    ("icono-linkedin.svg", "LinkedIn", "https://www.linkedin.com/"),
    ("icono-facebook.svg", "Facebook", "https://www.facebook.com/"),
]


def red_social(archivo, alt, url):
    """Celda del grid: item directo, sin wrap anidado."""
    return item("image", {
        "src": MEDIA + archivo,
        "stretch": "0",
        "alt": alt,
        "link": url,
        "target": "1",
        "lazy_load": "",
        "css_image_frame_width": css(S_IMGFRAME, "width",
                                     {"desktop": "24px", "mobile": "24px"}),
        "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
    }, title="Red social — " + alt)


# ================================================================ FOOTER
footer = section(
    {
        "width_switcher": "custom",
        "css_advanced_max_width": css(S_SECT_MAXW, "max-width", MAXW),
        "background_switcher": "default",
        "css_advanced_background_color": css(S_SECTION, "background-color", PRIMARY),
        "css_advanced_padding": css(S_SECTION, "padding",
                                    pad({"top": "0", "right": "2.25rem",
                                         "bottom": "2.25rem", "left": "2.25rem"},
                                        {"top": "0", "right": "1.5rem",
                                         "bottom": "1.5rem", "left": "1.5rem"},
                                        {"top": "0", "right": "1.25rem",
                                         "bottom": "1.25rem", "left": "1.25rem"})),
    },
    [
        # --- tarjeta de certificaciones -------------------------------
        wrap(
            {
                "background_switcher": "default",
                "css_advanced_background_color": css(S_WRAP_IN, "background-color", OFFWHITE),
                "css_advanced_border_radius": css(S_WRAP_IN, "border-radius",
                                                  {"desktop": "12px 12px 12px 12px"}),
                "css_advanced_padding": css(S_WRAP_IN, "padding",
                                            pad({"top": "1.75rem", "right": "2.25rem",
                                                 "bottom": "1.75rem", "left": "2.25rem"},
                                                None,
                                                {"top": "1.5rem", "right": "1.5rem",
                                                 "bottom": "1.5rem", "left": "1.5rem"})),
                "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "center"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin", pad({"bottom": "1rem"})),
            },
            [
                nested(
                    {"css_advanced_margin": css(S_WRAP_IN, "margin",
                                                pad({"bottom": "0"}, None, {"bottom": "2rem"}))},
                    [
                        item("heading", dict(item_width("280px", "280px", "100%"), **{
                            "title": "Certificaciones que marcan la diferencia",
                            "header_tag": "h4",
                            "css_color": css(S_TITLE_C, "color", BLACK),
                            "css_typography": t_h4(S_TITLE),
                            "css_txt_align": css(S_TITLE, "text-align", {"desktop": "left"}),
                            "css_advanced_margin": css(S_ITEM_IN, "margin",
                                                       pad({"bottom": "1rem"})),
                        }), title="Título — Certificaciones"),
                        item("button", {
                            "title": "Nuestras certificaciones",
                            "link": "/certificaciones/",
                            "icon": "icon-right-thin",
                            "icon_position": "right",
                            "button_style": "",
                            "background_switcher": "default",
                            "css_button_color": css(S_BUTTON, "color", WHITE),
                            "css_button_icon_color": css(S_BUTTON + " i", "color", WHITE),
                            "css_button_background_color": css(S_BUTTON, "background-color",
                                                               PRIMARY),
                            "css_button_border_radius": css(S_BUTTON, "border-radius",
                                                            {"desktop": "8px 8px 8px 8px"}),
                            "css_button_padding": css(S_BUTTON, "padding",
                                                      pad({"top": "0.875rem", "right": "1.5rem",
                                                           "bottom": "0.875rem", "left": "1.5rem"},
                                                          None,
                                                          {"top": "0.75rem", "right": "1.25rem",
                                                           "bottom": "0.75rem", "left": "1.25rem"})),
                            "css_button_typography": t_btn(S_BUTTON),
                            "css__text_align": css(S_ITEM, "text-align", {"desktop": "left"}),
                            "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                        }, title="Botón — Nuestras certificaciones"),
                    ],
                    size="1/2", tablet="1/1", mobile="1/1", title="Certificaciones — texto"),

                nested(
                    {
                        "css_advanced_justify_content": css(S_WRAP_IN, "justify-content",
                                                            {"desktop": "flex-end",
                                                             "mobile": "flex-start"}),
                        "css_advanced_margin": css(S_WRAP_IN, "margin", pad({"bottom": "0"})),
                    },
                    [
                        item("image", dict(item_width("338px", "300px", "260px"), **{
                            "src": MEDIA + "sello-bureau-veritas.png",
                            "stretch": "0",
                            "alt": "Certificación Bureau Veritas ISO 9001, ISO 14001, ISO 45001",
                            "lazy_load": "",
                            "css_image_frame_width": css(S_IMGFRAME, "width",
                                                         {"desktop": "338px",
                                                          "tablet": "300px",
                                                          "mobile": "260px"}),
                            "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                        }), title="Sello Bureau Veritas"),
                    ],
                    size="1/2", tablet="1/1", mobile="1/1", title="Certificaciones — sello"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Footer — certificaciones"),

        # --- tarjeta principal ----------------------------------------
        wrap(
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
                "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "stretch"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin", pad({"bottom": "2.25rem"})),
            },
            [
                # contacto + logotipo
                nested(
                    {"css_advanced_margin": css(S_WRAP_IN, "margin",
                                                pad({"bottom": "0"}, None, {"bottom": "2.25rem"}))},
                    [
                        label("Contacto", title="Etiqueta — Contacto"),
                        item("plain_text", {
                            "content": ("Polígono Espíritu Santo<br />c/ Monier 9-11, "
                                        "parcelas 36-38<br />15650 Cambre"),
                            "css_descdesca_color": css(S_DESC_C, "color", BLACK),
                            "css_desc_typography": t_pm(S_DESC),
                            "css_advanced_margin": css(S_ITEM_IN, "margin",
                                                       pad({"bottom": "1.5rem"})),
                        }, title="Dirección"),
                        item("plain_text", {
                            "content": '<a href="tel:+34981138338">+34 981 138 338</a>',
                            "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                            "css_desc_typography": t_ps(S_DESC),
                            "css_advanced_margin": css(S_ITEM_IN, "margin",
                                                       pad({"bottom": "1.5rem"})),
                        }, title="Teléfono"),
                        item("plain_text", {
                            "content": '<a href="mailto:info@nordesancin.com">info@nordesancin.com</a>',
                            "css_descdesca_color": css(S_DESC_C, "color", DARKGRAY),
                            "css_desc_typography": t_ps(S_DESC),
                            "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                        }, title="Email"),
                        item("footer_logo", dict(item_width("316px", "280px", "240px"), **{
                            "image": MEDIA + "logo-nordes-ancin-color.svg",
                            "link": "/",
                            "css_advanced_margin": css(S_ITEM_IN, "margin",
                                                       pad({"top": "8.5rem", "bottom": "0"},
                                                           {"top": "4rem", "bottom": "0"},
                                                           {"top": "3rem", "bottom": "0"})),
                        }), title="Logotipo"),
                    ],
                    size="3/5", tablet="1/1", mobile="1/1", title="Footer — contacto"),

                columna_menu("Menú", True, "Footer — menú"),
                columna_menu("Legal", False, "Footer — legal"),
            ],
            size="1/1", tablet="1/1", mobile="1/1", title="Footer — bloque principal"),

        # --- barra inferior: copyright --------------------------------
        wrap(
            {
                "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "center"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin",
                                           pad({"bottom": "0"}, None, {"bottom": "1.5rem"})),
            },
            [
                item("plain_text", {
                    "content": "Copyright © Nordés Ancín. Todos los derechos reservados.",
                    "css_descdesca_color": css(S_DESC_C, "color", WHITE),
                    "css_desc_typography": t_ps(S_DESC),
                    "css_advanced_margin": css(S_ITEM_IN, "margin", pad({"bottom": "0"})),
                }, title="Copyright"),
            ],
            size="1/2", tablet="1/2", mobile="1/1", title="Footer — copyright"),

        # --- barra inferior: redes ------------------------------------
        wrap(
            {
                "grid": "grid",
                "grid_columns_switcher": "custom",
                "css_grid_columns_custom": css(S_WRAP_GRIDC, "grid-template-columns",
                                               {"desktop": "repeat(3, 24px)",
                                                "mobile": "repeat(3, 24px)"}),
                "css_grid_columns_gap": css(S_WRAP_GRID, "column-gap", {"desktop": "1rem"}),
                "css_grid_rows_gap": css(S_WRAP_GRID, "row-gap", {"desktop": "0px"}),
                "css_advanced_justify_content": css(S_WRAP_IN, "justify-content",
                                                    {"desktop": "flex-end",
                                                     "mobile": "flex-start"}),
                "css_advanced_align_items": css(S_WRAP_IN, "align-items", {"desktop": "center"}),
                "css_advanced_margin": css(S_WRAP_IN, "margin", pad({"bottom": "0"})),
            },
            [red_social(*r) for r in REDES],
            size="1/2", tablet="1/2", mobile="1/1", title="Footer — redes sociales"),
    ],
    title="Footer — Nordés Ancín")


with open(HERE / "nordes-ancin-footer.json", "w", encoding="utf-8") as fh:
    json.dump([footer], fh, ensure_ascii=False, indent=2)

print("footer: 1 sección")
