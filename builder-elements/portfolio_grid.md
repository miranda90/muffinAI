# `portfolio_grid` — Portfolio Grid

- **Categoría:** loops
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 24

## Campos
- **`count`** (text) — Projects number
  - Valor: String
  - Default: `4`

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

- **`greyscale`** (switch) — Grayscale
  - Valor: String
  - Opciones: 
  - Default: `0`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Box

- **`css_portfolio_gridli_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio_gridli_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio_gridli_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_portfolio_gridli_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_portgrid` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio_gridli_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio_gridli_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li", "style": "background-color", "val": "valor"}`
- **`css_portfolio_gridliimage_frameimage_wrappermaskafter_background_color`** (color) — Mask
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li .image_frame .image_wrapper .mask:after", "style": "background-color", "val": "valor"}`
- **`css_portfolio_gridli_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_portgrid` isnt `none`
- **`css_portfolio_gridli_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li:hover", "style": "background-color", "val": "valor"}`
- **`css_grid_image_frameimage_wrappermaskafter_background_color_hover`** (color) — Mask
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li:hover .image_frame .image_wrapper .mask:after", "style": "background-color", "val": "valor"}`
- **`css_portfolio_gridli_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_portgrid` isnt `none`

### Icons

- **`css_portfolio_gridliimage_linksa_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li .image_links a", "style": "background-color", "val": "valor"}`
- **`css_portfolio_gridliimage_linksapath_stroke`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li .image_links a .path", "style": "stroke", "val": "valor"}`
- **`css_portfolio_gridliimage_linksa_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li .image_links a", "style": "border-color", "val": "valor"}`
- **`css_portfolio_gridliimage_linksa_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li .image_links a:hover", "style": "background-color", "val": "valor"}`
- **`css_portfolio_gridliimage_linksapath_stroke_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li .image_links a:hover .path", "style": "stroke", "val": "valor"}`
- **`css_portfolio_gridliimage_linksa_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_grid li .image_links a:hover", "style": "border-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "portfolio_grid",
  "uid": "itm000001",
  "size": "1/4",
  "tablet_size": "1/4",
  "mobile_size": "1/1",
  "attr": {}
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*