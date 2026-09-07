# `header_menu` — Menu

- **Categoría:** header
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 80

## Campos

### Menu

- **`menu_display`** (select) — Menu to display
  - Valor: String
- **`css_header_menu_justify`** (select) — Alignment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `flex-start` Left · `center` Center · `flex-end` Right · `space-between` Space between · `space-around` Space around · `space-evenly` Space evenly
  - Default: `flex-end`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-li_flex_grow`** (select) — Fit container
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "flex-grow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `unset` Default · `1` Fit
  - Visible si: `menu-items-alignment` is `['space-between', 'space-around', 'space-evenly']`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`animation`** (select) — Item Animation
  - Valor: String
  - Opciones: `""` None · `text-line-bottom` Text line bottom · `text-toggle-line-bottom` Text toggle line bottom · `toggle-line-bottom` Toggle line bottom · `toggle-line-top` Toggle line top · `text-bg-line` Text bg line · `bg-left` Bg left
- **`separator`** (switch) — Separator
  - Valor: String
  - Opciones: `off` Off · `on` On
  - Default: `off`
- **`submenu_display`** (switch) — Display submenu on
  - Valor: String
  - Opciones: `hover` Hover · `click` Click
  - Default: `hover`
- **`submenu_icon_display`** (switch) — Submenu Icon
  - Valor: String
  - Opciones: `off` Off · `on` On
  - Default: `on`
- **`submenu_icon`** (icon) — Submenu icon
  - Valor: String
  - Default: `fas fa-arrow-down`
  - Visible si: `submenu_icon_display` is `on`

### Icon

- **`icon_align`** (switch) — Icon align
  - Valor: String
  - Opciones: `left` Left · `top` Top · `right` Right
  - Default: `left`
- **`icon_animation`** (select) — Icon animation
  - Valor: String
  - Opciones: `""` None · `rotate` Rotate · `zoom` Zoom
- **`submenu_subicon`** (icon) — Submenu icon
  - Valor: String
  - Default: `fas fa-arrow-right`
  - Visible si: `submenu_icon_display` is `on`
- **`submenu_icon_animation`** (select) — Icon Animation
  - Valor: String
  - Opciones: `""` None · `rotate` Rotate · `zoom` Zoom
  - Visible si: `submenu_icon_display` is `on`
- **`submenu_animation`** (select) — Submenu Animation
  - Valor: String
  - Opciones: `""` None · `fade-in` Fade In · `fade-up` Fade In Up
- **`submenu_fold_to_right`** (switch) — Submenu fold last two items to left
  - Valor: String
  - Opciones: 

### Menu


### Items

- **`css_menu-li_header_menu_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "--mfn-header-menu-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-link_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-link_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-link_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_menu-link_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_header_menu_link` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-link_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-link_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link", "style": "color", "val": "valor"}`
- **`css_menu-link_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link", "style": "background-color", "val": "valor"}`
- **`css_menu-link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_menu_link` isnt `none`
- **`css_menu-link_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-link_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li:hover > a.mfn-menu-link", "style": "color", "val": "valor"}`
- **`css_menu-lihovera-menu-link_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li:hover > a.mfn-menu-link", "style": "background-color", "val": "valor"}`
- **`css_menu-lihovera-menu-link_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li:hover > a.mfn-menu-link", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_menu_link` isnt `none`
- **`css_menu-lihovera-menu-link_box_shadow_hover`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li:hover > a.mfn-menu-link", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menulicurrent-menu-itema-menu-link_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-menu-item > a.mfn-menu-link, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-menu-ancestor > a.mfn-menu-link, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-product_cat-ancestor > a.mfn-menu-link", "style": "color", "val": "valor"}`
- **`css_menulicurrent-menu-itema-menu-link_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-menu-item > a.mfn-menu-link, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-menu-ancestor > a.mfn-menu-link, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-product_cat-ancestor > a.mfn-menu-link", "style": "background-color", "val": "valor"}`
- **`css_menulicurrent-menu-itema-menu-link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-menu-item > a.mfn-menu-link, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-menu-ancestor > a.mfn-menu-link, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-product_cat-ancestor > a.mfn-menu-link", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_menu_link` isnt `none`
- **`css_menulicurrent-menu-itema-menu-link_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-menu-item > a.mfn-menu-link, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-menu-ancestor > a.mfn-menu-link, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-product_cat-ancestor > a.mfn-menu-link", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Icon

- **`css_menu-li_header_menu_icon_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "--mfn-header-menu-icon-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-li_header_menu_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "--mfn-header-menu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-menu-item-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu .mfn-menu-item-icon > i", "style": "color", "val": "valor"}`
- **`css_menua-menu-linkhover-menu-item-iconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu a.mfn-menu-link:hover > .mfn-menu-item-icon > i", "style": "color", "val": "valor"}`
- **`css_menulicurrent-menu-link-menu-item-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-menu-item.mfn-menu-li > a.mfn-menu-link > .mfn-menu-item-icon i", "style": "color", "val": "valor"}`

### Submenu icon

- **`css_menu-li_header_menu_submenu_icon_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "--mfn-header-menu-submenu-icon-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `submenu_icon_display` is `on`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-li-menu-subiconi_header_submenu_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li .mfn-menu-subicon i", "style": "--mfn-header-submenu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-link-menu-subiconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link .mfn-menu-subicon i", "style": "color", "val": "valor"}`
- **`css_menu-linkhover-menu-subiconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li > a.mfn-menu-link:hover .mfn-menu-subicon i", "style": "color", "val": "valor"}`
- **`css_menulicurrent-menu-link-menu-subiconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.current-menu-item.mfn-menu-li > a.mfn-menu-link .mfn-menu-subicon i", "style": "color", "val": "valor"}`

### Submenu


### Container

- **`css_menu-liul-submenu_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li > ul.mfn-submenu", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-liul-submenu_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li > ul.mfn-submenu", "style": "background-color", "val": "valor"}`
- **`css_menu-liul-submenu_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li > ul.mfn-submenu", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_menu-liul-submenu_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_header_submenu` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-liul-submenu_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_submenu` isnt `none`
- **`css_menu-liul-submenu_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu", "style": "box-shadow", "val": "valor"}`
- **`css_menu-liul-submenu_header_submenu_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu", "style": "--mfn-header-submenu-border-radius", "val": {"top": "...", "right": "...", "bottom": "...", "left": "..."}}`

### Items

- **`css_menu-liul-submenu_menu-link_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li a.mfn-menu-link", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-liul-submenu_menu-link_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li a.mfn-menu-link", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_menu-liul-submenu_menu-link_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li a.mfn-menu-link", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_header_submenu_links` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-liul-submenu_menu-link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li a.mfn-menu-link", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_submenu_links` isnt `none`
- **`css_menu-liul-submenu_menu-link_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li a.mfn-menu-link", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_submenu_item_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li a.mfn-menu-link", "style": "color", "val": "valor"}`
- **`css_submenu_item_bg`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li a.mfn-menu-link", "style": "background-color", "val": "valor"}`
- **`css_submenu_item_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li a.mfn-menu-link:hover", "style": "color", "val": "valor"}`
- **`css_submenu_item_bg_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li a.mfn-menu-link:hover", "style": "background-color", "val": "valor"}`
- **`css_submenu_item_color_active`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.current-menu-item.mfn-menu-li > a.mfn-menu-link", "style": "color", "val": "valor"}`
- **`css_submenu_item_bg_active`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.current-menu-item.mfn-menu-li > a.mfn-menu-link", "style": "background-color", "val": "valor"}`

### Icon

- **`css_menu-liul-submenu_menu-li_header_submenu_subicon_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li", "style": "--mfn-header-submenu-subicon-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-liul-submenu_menu-li_header_submenu_subicon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li", "style": "--mfn-header-submenu-subicon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-liul-submenu_menu-li-menu-item-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li .mfn-menu-item-icon > i", "style": "color", "val": "valor"}`
- **`css_menu-liul-submenu_menu-link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li a.mfn-menu-link", "style": "border-color", "val": "valor"}`
- **`css_menu-liul-submenu_menu-lihovera-menu-link-menu-item-iconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li:hover > a.mfn-menu-link > .mfn-menu-item-icon > i", "style": "color", "val": "valor"}`
- **`css_menu-liul-submenu_menu-lihovera-menu-link_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li:hover > a.mfn-menu-link", "style": "border-color", "val": "valor"}`
- **`css_menu-liul-submenulicurrent-menu-link-menu-item-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu > li.current-menu-item.mfn-menu-li > a.mfn-menu-link > .mfn-menu-item-icon i", "style": "color", "val": "valor"}`
- **`css_menu-liul-submenulicurrent-menu-link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu > li.current-menu-item.mfn-menu-li > a.mfn-menu-link", "style": "border-color", "val": "valor"}`

### Submenu icon

- **`css_menu-liul-submenu_menu-li-menu-sub-subiconi_header_submenu_submenu_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu li.mfn-menu-li .mfn-menu-sub-subicon i", "style": "--mfn-header-submenu-submenu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-liul-submenu_menu-link-menu-sub-subiconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu > li.mfn-menu-li > a.mfn-menu-link .mfn-menu-sub-subicon i", "style": "color", "val": "valor"}`
- **`css_menu-liul-submenu_menu-linkhover-menu-sub-subiconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu > li.mfn-menu-li > a.mfn-menu-link:hover .mfn-menu-sub-subicon i", "style": "color", "val": "valor"}`
- **`css_menu-liul-submenulicurrent-menu-link-menu-sub-subiconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu li.mfn-menu-li ul.mfn-submenu > li.current-menu-item.mfn-menu-li > a.mfn-menu-link .mfn-menu-sub-subicon i", "style": "color", "val": "valor"}`

### Separator

- **`css_menu-li_header_menu_sep`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "--mfn-header-menu-sep", "val": "valor"}`
  - Visible si: `menu_separator` is `on`

### Animation

- **`css_menu-li_header_menu_animation_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "--mfn-header-menu-animation-color", "val": "valor"}`
  - Visible si: `header_menu_animation` isnt ``
- **`css_menu-li_header_menu_animation_height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "--mfn-header-menu-animation-height", "val": "valor"}`
  - Visible si: `header_menu_animation` is `['text-line-bottom', 'text-toggle-line-bottom', 'toggle-line-bottom', 'toggle-line-top']`

### Dropdown pointer

- **`dropdown_pointer`** (switch) — Visibility
  - Valor: String
  - Opciones: `""` Hide · `1` Show
- **`css_menu-li_header_submenu_dropdown_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "--mfn-header-submenu-dropdown-size", "val": "valor"}`
  - Visible si: `dropdown_pointer` is `1`
- **`dropdown_alignment`** (switch) — Icon align
  - Valor: String
  - Opciones: `left` Left · `center` Center · `right` Right
  - Default: `left`
  - Visible si: `dropdown_pointer` is `1`
- **`css_menu-li_header_submenu_dropdown_offset`** (sliderbar) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "--mfn-header-submenu-dropdown-offset", "val": "valor"}`
  - Visible si: `dropdown_pointer` is `1`
- **`css_menu-li_header_submenu_dropdown_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu > li.mfn-menu-li", "style": "--mfn-header-submenu-dropdown-color", "val": "valor"}`
  - Visible si: `dropdown_pointer` is `1`

## Ejemplo mínimo

```json
{
  "type": "header_menu",
  "uid": "itm000001",
  "icon": "header_menu",
  "jsclass": "header_menu",
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