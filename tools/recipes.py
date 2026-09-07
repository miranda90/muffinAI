"""Native patterns for new builds. Content and tokens always come from the design."""
from mfn import item, wrap, nested, section, sec_base, pad, style_field, m0


def heading(text, *, tag="h2", typography=None):
    attr = {"title": text, "header_tag": tag, "css_advanced_margin": m0()}
    if typography:
        attr["css_typography"] = style_field("item", "css_typography", typography, itype="heading")
    return item("heading", attr)


def button(text, link, *, background, color, spacing=None):
    attr = {"title": text, "link": link, "background_switcher": "default", "css_advanced_margin": m0()}
    for key, val in (("css_button_background_color", background), ("css_button_color", color)):
        attr[key] = style_field("item", key, val, itype="button")
    if spacing: attr["css_button_padding"] = style_field("item", "css_button_padding", spacing, itype="button")
    return item("button", attr)


def image(src, *, alt="", cover_height=None):
    attr = {"src": src, "alt": alt, "size": "full", "css_advanced_margin": m0()}
    if cover_height:
        attr["image_height"] = "custom"
        attr["css_image_cover_height"] = style_field("item", "css_image_cover_height", cover_height, itype="image")
    return item("image", attr)


def video(mp4, poster, *, autoplay=False, controls=True, loop=False, muted=False):
    return item("video", {"video": "", "mp4": mp4, "placeholder": poster,
                          "html5_parameters": ";".join(("a" if autoplay else "", "c" if controls else "",
                                                       "l" if loop else "", "m" if muted else "", "i"))})


def counter(number, title, *, prefix="", suffix="", separator=""):
    if type(number) is not int:
        raise ValueError("counter solo para enteros; preservar otros formatos con texto")
    if separator not in ("", "comma", "space"):
        raise ValueError("Separador no soportado; no cambiar el formato del diseño")
    return item("counter", {"number": str(number), "title": title, "prefix": prefix, "label": suffix,
                            "thousands_separator": separator, "icon": "", "image": ""})


def card(items, *, background=None, spacing=None, equal_height=False, cta_bottom=False):
    attr = {}
    if background is not None:
        attr["background_switcher"] = "default"
        attr["css_advanced_background_color"] = style_field("wrap", "css_advanced_background_color", background)
    if spacing: attr["css_advanced_padding"] = style_field("wrap", "css_advanced_padding", spacing)
    if equal_height:
        attr["height_switcher"] = "custom"
        attr["css_advanced_height"] = style_field("wrap", "css_advanced_height", {"desktop": "100%"})
    if cta_bottom:
        attr["grid"] = ""
        attr["css_advanced_align_content"] = style_field("wrap", "css_advanced_align_content", {"desktop": "space-between"})
    return nested(attr, items)


def grid(cells, *, columns=3, tablet=2, mobile=1, gap="1.5rem"):
    if any(type(x) is not int or not 1 <= x <= 6 for x in (columns, tablet, mobile)):
        raise ValueError("Grid admite 1–6 columnas; usar campo custom para otra retícula")
    cols = lambda x: "1fr" if x == 1 else "repeat(%d, 1fr)" % x
    attr = {"grid": "grid", "grid_columns_switcher": ""}
    attr["css_grid_columns"] = style_field("wrap", "css_grid_columns", {
        "desktop": cols(columns), "tablet": cols(tablet), "mobile": cols(mobile)})
    for key in ("css_grid_columns_gap", "css_grid_rows_gap"):
        attr[key] = style_field("wrap", key, {"desktop": gap, "mobile": gap})
    return wrap(attr, cells)


def band(wraps, *, spacing, max_width=None, title="Section"):
    return section(sec_base(spacing, maxw=max_width), wraps, title=title)


def hero(title, *, spacing, max_width=None, typography=None, actions=()):
    return band([wrap({}, [heading(title, tag="h1", typography=typography), *actions])],
                spacing=spacing, max_width=max_width, title="Hero")


def split(left, right, *, spacing, max_width=None):
    return band([wrap({}, left, size="1/2"), wrap({}, right, size="1/2")],
                spacing=spacing, max_width=max_width, title="Texto e imagen")


def cta(title, actions, *, spacing, max_width=None):
    return band([wrap({}, [heading(title), *actions])], spacing=spacing, max_width=max_width, title="CTA")
