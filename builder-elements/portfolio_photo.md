# `portfolio_photo` — Portfolio Photo

- **Categoría:** loops
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 28

## Campos
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h3`
- **`count`** (text) — Projects number
  - Valor: String
  - Default: `5`

### Options

- **`category`** (select) — Category
  - Valor: String
- **`category_multi`** (text) — Multiple categories
  - Slugs should be separated with <b>coma</b> ( , )
  - Valor: String
- **`orderby`** (switch) — Order by
  - Valor: String
  - Opciones: `date` Date · `menu_order` Menu order · `title` Title · `rand` Random
  - Default: `date`
- **`order`** (switch) — Order
  - Valor: String
  - Opciones: `ASC` Ascending · `DESC` Descending
  - Default: `DESC`

### Advanced

- **`target`** (switch) — Link target
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`greyscale`** (switch) — Grayscale
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`margin`** (switch) — Margin
  - Valor: String
  - Opciones: 
  - Default: `0`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Box

- **`css_portfolio-photoportfolio-itemportfolio-detailsdetails_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .details", "style": "background-color", "val": "valor"}`
- **`css_portfolio-photoportfolio-itemportfolio-detailsdetails_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .details", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_portfolio-photoportfolio-itemportfolio-detailsdetails_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .details", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_port_photo` isnt `none`
- **`css_portfolio-photoportfolio-itemportfolio-detailsdetails_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .details", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_port_photo` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-photoportfolio-itemportfolio-detailsdetails_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .details", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Title

- **`css_portfolio-photoportfolio-itemportfolio-detailsdetailstitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .details .title", "style": "color", "val": "valor"}`
- **`css_portfolio-photoportfolio-itemportfolio-detailsdetailstitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .details .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Decoration

- **`css_portfolio-photoportfolio-itemportfolio-detailsdetailstitle_border_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .details .title", "style": "border-color", "val": "valor"}`

### Meta

- **`css_portfolio-photoportfolio-itemportfolio-detailsdetailscategories_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .details .categories", "style": "color", "val": "valor"}`
- **`css_portfolio-photoportfolio-itemportfolio-detailsdetailscategories_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .details .categories", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Button

- **`css_portfolio-photoportfolio-itemportfolio-detailsmore_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .more", "style": "background-color", "val": "valor"}`
- **`css_portfolio-photoportfolio-itemportfolio-detailsmoreh4_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .more h4", "style": "color", "val": "valor"}`
- **`css_portfolio-photoportfolio-itemportfolio-detailsmore_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .more", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-photoportfolio-itemportfolio-detailsmore_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .more", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-photoportfolio-itemportfolio-detailsmore_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .more", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_portfolio-photoportfolio-itemportfolio-detailsmore_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .more", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_port_photo` isnt `none`
- **`css_portfolio-photoportfolio-itemportfolio-detailsmore_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .more", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_port_photo` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-photoportfolio-itemportfolio-detailsmore_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio-photo .portfolio-item .portfolio-details .more", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "portfolio_photo",
  "uid": "itm000001",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {}
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*