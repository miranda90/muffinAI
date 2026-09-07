# `header_currency_switcher` — Currency switcher

- **Categoría:** other
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 46

## Campos
- **`style`** (select) — Style
  - Valor: String
  - Opciones: `inline` Inline · `""` Dropdown
- **`flags`** (switch) — Flags
  - Valor: String
  - Opciones: `1` Show · `""` Hide
  - Default: `1`
- **`dropdown_icon`** (switch) — Dropdown icon
  - Valor: String
  - Opciones: `1` Show · `""` Hide
  - Default: `1`
  - Visible si: `style` is ``
- **`dropdown_icon_html`** (icon) — Dropdown icon
  - Valor: String
  - Default: `icon-down-open`
  - Visible si: `dropdown_icon` is `1`

### Item

- **`css_currency_switcher_submenu_items_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-default ul", "style": "gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `style` is `inline`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_link_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_link_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_currency_switcher_link_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_wcml_swi` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_link_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_link_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_link_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a", "style": "color", "val": "valor"}`
- **`css_currency_switcher_link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_wcml_swi` isnt `none`
- **`css_currency_switcher_link_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a", "style": "background-color", "val": "valor"}`
- **`css_currency_switcher_link_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a:hover", "style": "color", "val": "valor"}`
- **`css_currency_switcher_link_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_wcml_swi` isnt `none`
- **`css_currency_switcher_link_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li > a:hover", "style": "background", "val": "valor"}`
- **`css_currency_switcher_link_color_active`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li.> wcml-cs-active-currency > a", "style": "color", "val": "valor"}`
- **`css_currency_switcher_link_border_color_active`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li.> wcml-cs-active-currency > a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_wcml_swi` isnt `none`
- **`css_currency_switcher_link_background_active`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper > .wcml_currency_switcher > ul > li.> wcml-cs-active-currency > a", "style": "background", "val": "valor"}`

### Flag

- **`css_currency_switcher_flag_width`** (sliderbar) — Flag size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li a img.mfn-wcml-flag", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `20px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Dropdown icon

- **`css_currency_switcher_dropdown_arrow_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown.mfn-currency-switcher-dropdown-icon ul li a .mfn-arrow-icon", "style": "--mfn-wpml-arrow-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `10px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_dropdown_arrow_icon_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown ul li a .mfn-arrow-icon", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_dropdown_arrow_icon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown ul li a .mfn-arrow-icon", "style": "color", "val": "valor"}`

### Submenu

- **`css_currency_switcher_submenu_offset`** (sliderbar) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul.mfn-wcml-dropdown-ready > li.wcml-cs-active-currency > ul", "style": "margin-top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown ul li ul", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown ul li ul", "style": "background-color", "val": "valor"}`
- **`css_currency_switcher_submenu_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown ul li ul", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown ul li ul", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_currency_switcher_submenu_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown ul li ul", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_wcml_submenu` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown ul li ul", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_wcml_submenu` isnt `none`
- **`css_currency_switcher_submenu_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown ul li ul", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-dropdown ul li ul", "style": "box-shadow", "val": "valor"}`

### Submenu items

- **`css_currency_switcher_submenu_items_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul", "style": "gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_link_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_link_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_currency_switcher_submenu_link_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_wcml_swi` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_link_border_width_last_child`** (dimensions) — Border width last item
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li:last-child a", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_wcml_swi` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_link_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_link_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_currency_switcher_submenu_link_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a", "style": "color", "val": "valor"}`
- **`css_currency_switcher_submenu_link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_wcml_swi` isnt `none`
- **`css_currency_switcher_submenu_link_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a", "style": "background-color", "val": "valor"}`
- **`css_currency_switcher_submenu_link_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a:hover", "style": "color", "val": "valor"}`
- **`css_currency_switcher_submenu_link_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_wcml_swi` isnt `none`
- **`css_currency_switcher_submenu_link_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-currency-switcher-wrapper ul li ul li a:hover", "style": "background", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "header_currency_switcher",
  "uid": "itm000001",
  "icon": "header_currency_switcher",
  "jsclass": "header_currency_switcher",
  "title": "Currency switcher",
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