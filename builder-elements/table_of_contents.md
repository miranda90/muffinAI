# `table_of_contents` — Table of Contents

- **Categoría:** blocks
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 17

## Campos
- **`title`** (text) — Title
  - Valor: String
  - Default: `Table of contents`

### Options

- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h4`
- **`tags_anchors`** (pills) — Anchor by HTML tags
  - Separated with space button.<br/>Maximal depth level: <b>3</b>
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)
  - Default: `H1 H2 H3 H4 H5 H6`
- **`marker_view`** (switch) — Marker view
  - Valor: String
  - Opciones: `numbers` Numbers · `bullets` Bullets
  - Default: `numbers`
- **`icon`** (icon) — Bullets icon
  - Only for <b>Bullets</b> type of marker
  - Valor: String
- **`url_format`** (switch) — Link format
  - Use <b>Simple</b> for languages based on non URL friendly characters
  - Valor: String
  - Opciones: `""` SEO friendly · `simple` Simple
- **`allow_hide`** (select) — Toggle the Visibility
  - Valor: String
  - Opciones: `""` Disable · `enable` Enable · `hide` Enable and hide initially
- **`text_show`** (text) — Show text
  - Valor: String
  - Default: `Show`
  - Visible si: `toc_allow_hide` isnt ``
- **`text_hide`** (text) — Hide text
  - Valor: String
  - Default: `Hide`
  - Visible si: `toc_allow_hide` isnt ``

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Title

- **`css_table_of_contenttitletitle-inner_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .table_of_content .title .title-inner", "style": "color", "val": "valor"}`
- **`css_table_of_contenttitletitle-inner_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .table_of_content .title .title-inner", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_table_of_contenttitle_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .table_of_content .title", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### List row

- **`css_table_of_content_wrapperli_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .table_of_content .table_of_content_wrapper li", "style": "color", "val": "valor"}`
- **`css_table_of_content_wrapperlia_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .table_of_content .table_of_content_wrapper li a", "style": "color", "val": "valor"}`
- **`css_table_of_content_wrapperlia_color_hover`** (color) — Link hover
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .table_of_content .table_of_content_wrapper li a:hover", "style": "color", "val": "valor"}`
- **`css_table_of_content_wrapperli_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .table_of_content .table_of_content_wrapper li", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "table_of_contents",
  "uid": "itm000001",
  "icon": "table_of_contents",
  "jsclass": "table_of_contents",
  "title": "Table of Contents",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {
    "title": "Título de ejemplo"
  }
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*