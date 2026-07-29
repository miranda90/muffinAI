# `heading` — Heading

- **Categoría:** typography
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 16

## Campos
- **`title`** (textarea) — Title
  - Valor: String
  - Default: `This is the heading`
- **`header_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h2`

### Link

- **`link`** (text) — Link
  - Valor: String
- **`target`** (select) — Target
  - Valor: String
  - Opciones: `0` Default \| _self · `1` New tab or window \| _blank · `lightbox` Lightbox (image or embed video)
- **`link_title`** (text) — Link title
  - Valor: String
- **`onclick`** (text) — Onclick
  - Valor: String

### Heading

- **`css_txt_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .title a", "style": "color", "val": "valor"}`
- **`css_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title:hover,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .title a:hover", "style": "color", "val": "valor"}`
- **`css_text_shadow`** (text_shadow) — Text shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "text-shadow", "val": "valor"}`
- **`css_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_line_clamp`** (text) — Line clamp
  - Limit the number of lines to
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "-webkit-line-clamp", "val": "valor"}`

### Mask shape

- **`css_bg_img`** (upload) — Background image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "background-image", "val": "valor"}`
- **`css_bg_img_pos`** (select) — Background position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "background-position", "val": "valor"}`
  - Opciones: `""` Default · `center center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center
- **`css_stroke_width`** (select) — Text stroke width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "-webkit-text-stroke-width", "val": "valor"}`
  - Opciones: `initial` Default · `thin` Thin · `medium` Medium · `thick` Thick
- **`css_stroke_color`** (color) — Text stroke color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "-webkit-text-stroke-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "heading",
  "uid": "itm000001",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {
    "title": "This is the heading"
  }
}
```

## Variante shortcode inline (para `content` de column/plain_text/visual)

⚠️ Definición DISTINTA al elemento del builder — solo para el shortcode dentro de texto:
- **`tag`** (switch) — Heading size
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h2`
- **`align`** (switch) — Text align
  - Valor: String
  - Opciones: `left` Left · `center` Center · `right` Right
  - Default: `center`
- **`color`** (color) — Color
  - Valor: String
  - Default: `#000`
- **`style`** (switch) — Style
  - Valor: String
  - Opciones: `none` Default · `lines` Lines
  - Default: `lines`
- **`color2`** (color) — Color 2
  - Valor: String
  - Default: `#000`
- **`content`** (textarea) — Content
  - Valor: String

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*