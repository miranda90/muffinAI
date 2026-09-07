# `megamenu_menu` — Menu

- **Categoría:** megamenu
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 64

## Campos

### Menu

- **`menu_display`** (select) — Menu to display
  - Valor: String
- **`menu_style`** (select) — Style
  - Valor: String
  - Opciones: `vertical` Vertical · `horizontal` Horizontal
  - Default: `vertical`
- **`css_megamenu-menu-mm-menu-horizontal_justify_content`** (select) — Alignment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu.mfn-mm-menu-horizontal", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `flex-start` Left · `center` Center · `flex-end` Right · `space-between` Space between · `space-around` Space around · `space-evenly` Space evenly
  - Default: `flex-start`
  - Visible si: `menu_style` is `horizontal`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menu-mm-menu-horizontalli_flex_grow`** (select) — Fit container
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu.mfn-mm-menu-horizontal > li", "style": "flex-grow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `unset` Default · `1` Fit
  - Visible si: `menu_style` is `horizontal`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`submenu_on`** (switch) — Submenu visibility
  - Valor: String
  - Opciones: `visible` Visible · `toggled` Toggled
  - Default: `visible`
  - Visible si: `menu_style` is `vertical`
- **`submenu_hori_on`** (switch) — Submenu visibility
  - Valor: String
  - Opciones: `hover` on Hover · `click` on Click
  - Default: `hover`
  - Visible si: `menu_style` is `horizontal`

### Icon

- **`css_megamenu-icon_display`** (switch) — Icon visibility
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu a .menu-icon", "style": "display", "val": "valor"}`
  - Opciones: `block` Show · `none` Hide
  - Default: `block`
- **`icon_align`** (switch) — Icon align
  - Valor: String
  - Opciones: `left` Left · `top` Top · `right` Right
  - Default: `left`
- **`icon_animation`** (select) — Icon animation
  - Valor: String
  - Opciones: `""` None · `rotate` Rotate · `zoom` Zoom

### Submenu

- **`submenu`** (switch) — Submenu
  - Valor: String
  - Opciones: `on` Show · `off` Hide
  - Default: `on`
- **`submenu_animation`** (select) — Submenu Animation
  - Valor: String
  - Opciones: `""` None · `fade-in` Fade In · `fade-up` Fade In Up
  - Visible si: `submenu` is `on`
- **`submenu_icon`** (icon) — Submenu icon
  - Valor: String
  - Default: `fas fa-arrow-down`
  - Visible si: `submenu` is `on`
- **`submenu_icon_animation`** (select) — Icon Animation
  - Valor: String
  - Opciones: `""` None · `rotate` Rotate · `zoom` Zoom
  - Visible si: `submenu` is `on`

### Desc

- **`css_megamenu-desc_display`** (switch) — Desc visibility
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu a .menu-desc", "style": "display", "val": "valor"}`
  - Opciones: `block` Show · `none` Hide
  - Default: `block`

### Decoration icon

- **`decoration_icon`** (icon) — Decoration icon
  - Valor: String

### Menu


### Items

- **`css_megamenu-menua_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menua_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menulia_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li > a", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_megamenu-menulia_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li > a", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_header_mm_menu_link` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menulia_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li > a", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menua_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu a", "style": "color", "val": "valor"}`
- **`css_megamenu-menua_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu a", "style": "background-color", "val": "valor"}`
- **`css_megamenu-menulia_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li > a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_mm_menu_link` isnt `none`
- **`css_megamenu-menua_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-megamenu-menu li a:hover", "style": "color", "val": "valor"}`
- **`css_megamenu-menua_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu a:hover", "style": "background-color", "val": "valor"}`
- **`css_megamenu-menulia_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li > a:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_mm_menu_link` isnt `none`
- **`css_megamenu-menucurrent-menu-itema_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu .current-menu-item > a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu .current-menu-ancestor > a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu .current-product_cat-ancestor > a", "style": "color", "val": "valor"}`
- **`css_megamenu-menucurrent-menu-itema_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu .current-menu-item > a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu .current-menu-ancestor > a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu .current-product_cat-ancestor > a", "style": "background-color", "val": "valor"}`
- **`css_megamenu-menucurrent-menu-itemlia_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu .current-menu-item > a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu .current-menu-ancestor > a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu .current-product_cat-ancestor > a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_mm_menu_link` isnt `none`

### Icon

- **`css_megamenu-menuli_menu_icon_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li", "style": "--mfn-megamenu-menu-icon-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menuli_menu_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li", "style": "--mfn-megamenu-menu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menumenu-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu .menu-icon > i", "style": "color", "val": "valor"}`
- **`css_megamenu-menuamenu-iconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu a:hover > .menu-icon > i", "style": "color", "val": "valor"}`
- **`css_megamenu-menulicurrent-menu-itemamenu-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li.current-menu-item > a > .menu-icon i", "style": "color", "val": "valor"}`

### Submenu icon

- **`css_megamenu-menuli_menu_submenu_icon_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li", "style": "--mfn-megamenu-menu-submenu-icon-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menulimenu-subi_megamenu_submenu_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li .menu-sub i", "style": "--mfn-megamenu-submenu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menuliamenu-subi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li > a .menu-sub i", "style": "color", "val": "valor"}`
- **`css_megamenu-menuliamenu-subi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li > a:hover .menu-sub i", "style": "color", "val": "valor"}`
- **`css_megamenu-menulicurrent-menu-itemamenu-subi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li.current-menu-item > a .menu-sub i", "style": "color", "val": "valor"}`

### Submenu


### Container

- **`css_megamenu-menuliul_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li > ul", "style": "background-color", "val": "valor"}`
- **`css_megamenu-menuliul_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li > ul", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_megamenu-menuliul_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_header_submenu` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menuliul_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_submenu` isnt `none`
- **`css_megamenu-menuliul_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul", "style": "box-shadow", "val": "valor"}`
- **`css_megamenu-menuliul_megamenu_submenu_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul", "style": "--mfn-megamenu-submenu-border-radius", "val": {"top": "...", "right": "...", "bottom": "...", "left": "..."}}`

### Items

- **`css_megamenu-menuliula_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menuliullia_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul li a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menuliula_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul a", "style": "color", "val": "valor"}`
- **`css_megamenu-menuliullia_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul li a", "style": "background-color", "val": "valor"}`
- **`css_megamenu-menuliula_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul a:hover", "style": "color", "val": "valor"}`
- **`css_megamenu-menuliulcurrent-menu-itema_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul .current-menu-item > a", "style": "color", "val": "valor"}`

### Icon

- **`css_megamenu-menuli_submenu_subicon_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li", "style": "--mfn-megamenu-submenu-subicon-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menuliullimenu-iconi_megamenu_submenu_subicon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul li .menu-icon i", "style": "--mfn-megamenu-submenu-subicon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menuliamenu-subi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li > a .menu-sub i", "style": "color", "val": "valor"}`
- **`css_megamenu-menuliamenu-subi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li > a:hover .menu-sub i", "style": "color", "val": "valor"}`
- **`css_megamenu-menulicurrent-menu-itemamenu-subi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu > li.current-menu-item > a .menu-sub i", "style": "color", "val": "valor"}`

### Submenu icon

- **`css_megamenu-menuliullimenu-subi_megamenu_submenu_submenu_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul li .menu-sub i", "style": "--mfn-megamenu-submenu-submenu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_megamenu-menuliulliamenu-subi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul > li > a .menu-sub i", "style": "color", "val": "valor"}`
- **`css_megamenu-menuliulliamenu-subi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul > li > a:hover .menu-sub i", "style": "color", "val": "valor"}`
- **`css_megamenu-menuliullicurrent-menu-itemamenu-subi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li ul > li.current-menu-item > a .menu-sub i", "style": "color", "val": "valor"}`

### Decoration icon

- **`css_megamenu-menuliadecoration-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li a .decoration-icon i", "style": "color", "val": "valor"}`
- **`css_megamenu-menuliadecoration-iconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li:hover > a > .decoration-icon i", "style": "color", "val": "valor"}`
- **`css_megamenu-menulicurrent-menu-itemadecoration-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li.current-menu-item > a .decoration-icon i", "style": "color", "val": "valor"}`
- **`css_megamenu-menuliadecoration-iconi_font_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-megamenu-menu li a .decoration-icon i", "style": "font-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "megamenu_menu",
  "uid": "itm000001",
  "icon": "megamenu_menu",
  "jsclass": "megamenu_menu",
  "title": "Menu",
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