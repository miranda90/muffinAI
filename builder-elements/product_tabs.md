# `product_tabs` — Product tabs

- **Categoría:** single-product
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 30

## Campos

### Navigation

- **`nav`** (select) — Position
  - Valor: String
  - Opciones: `""` Top · `left` Left · `right` Right
- **`css_woocommerce-tabs-nav-top-woocommerce-tabs-nav_justify_content`** (select) — Align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs.mfn-woocommerce-tabs-nav-top .mfn-woocommerce-tabs-nav", "style": "justify-content", "val": "valor"}`
  - Opciones: `""` Left · `center` Center · `flex-end` Right · `space-around` Space around · `space-between` Space between
  - Visible si: `nav` is ``

### Navigation

- **`css_woocommerce-tabs-nav_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav", "style": "background-color", "val": "valor"}`
- **`css_woocommerce-tabs-nav_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-tabs-nav_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-tabs-nav_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_woocommerce-tabs-nav_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav", "style": "border-color", "val": "valor"}`
  - Visible si: `border_tabs_nav_ul` isnt `none`
- **`css_woocommerce-tabs-nav_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_tabs_nav_ul` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-tabs-nav_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Nav items

- **`css_woocommerce-tabs-navlia_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-tabs-navli_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-tabs-navlia_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-tabs-navlia_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_woocommerce-tabs-navlia_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_tabs_nav_ul_li` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-tabs-navlia_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-tabs-navlia_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a", "style": "color", "val": "valor"}`
- **`css_woocommerce-tabs-navlia_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a", "style": "background-color", "val": "valor"}`
- **`css_woocommerce-tabs-navlia_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_tabs_nav_ul_li` isnt `none`
- **`css_woocommerce-tabs-navlia_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a:hover", "style": "color", "val": "valor"}`
- **`css_woocommerce-tabs-navliahover_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a:hover", "style": "background-color", "val": "valor"}`
- **`css_woocommerce-tabs-navliahover_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li a:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_tabs_nav_ul_li` isnt `none`
- **`css_woocommerce-tabs-navlia_color_active`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li.active a", "style": "color", "val": "valor"}`
- **`css_woocommerce-tabs-navlia_background_color_active`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li.active a", "style": "background-color", "val": "valor"}`
- **`css_woocommerce-tabs-navlia_border_color_active`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-nav li.active a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_tabs_nav_ul_li` isnt `none`

### Content

- **`css_woocommerce-tabs-content_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-content", "style": "background-color", "val": "valor"}`
- **`css_woocommerce-tabs-content_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-content", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-tabs-content_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-content", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_woocommerce-tabs-content_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-content", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_tabs_content` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-tabs-content_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-content", "style": "border-color", "val": "valor"}`
  - Visible si: `border_tabs_content` isnt `none`
- **`css_woocommerce-tabs-content_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-tabs .mfn-woocommerce-tabs-content", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "product_tabs",
  "uid": "itm000001",
  "icon": "product_tabs",
  "jsclass": "product_tabs",
  "title": "Product tabs",
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