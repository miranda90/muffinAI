# `header_burger` — Menu burger

- **Categoría:** header
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 104

## Campos

### Icon

- **`icon`** (icon) — Icon
  - Valor: String
- **`image`** (upload) — Image
  - Image instead of an icon
  - Valor: String
- **`desc`** (text) — Desc
  - Valor: String
- **`link_title`** (text) — Link title
  - Valor: String

### Nav

- **`sidebar_type`** (select) — Nav type
  - Valor: String
  - Default: `0`

### Menu

- **`menu_display`** (select) — Menu to display
  - Valor: String
  - Visible si: `sidebar_type` is `['0', 'classic']`
- **`css_menu-sidebar-wrapper_align_items`** (select) — Vertical align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-tmpl-menu-sidebar-wrapper", "style": "align-items", "val": "valor"}`
  - Opciones: `flex-start` Top · `center` Center · `flex-end` Bottom
  - Default: `center`
  - Visible si: `sidebar_type` is `0`
- **`menu_pos`** (select) — Sidebar position
  - Valor: String
  - Opciones: `left` Left · `right` Right
  - Default: `right`
  - Visible si: `sidebar_type` is `0`
- **`animation`** (select) — Item Animation
  - Valor: String
  - Opciones: `""` None · `text-line-bottom` Text line bottom · `text-toggle-line-bottom` Text toggle line bottom · `toggle-line-bottom` Toggle line bottom · `toggle-line-top` Toggle line top · `text-bg-line` Text bg line · `bg-left` Bg left
  - Visible si: `sidebar_type` is `['0', 'classic']`
- **`submenu_icon_display`** (switch) — Submenu Icon
  - Valor: String
  - Opciones: `off` Off · `on` On
  - Default: `on`
  - Visible si: `sidebar_type` is `['0', 'classic']`
- **`submenu_animation`** (select) — Submenu Animation
  - Valor: String
  - Opciones: `""` None · `fade-in` Fade In · `fade-up` Fade In Up
  - Visible si: `sidebar_type` is `['0', 'classic']`
- **`submenu_icon`** (icon) — Submenu icon
  - Valor: String
  - Default: `fas fa-arrow-down`
  - Visible si: `sidebar_type` is `['0', 'classic']`
- **`menu_icon_align`** (switch) — Icon align
  - Valor: String
  - Opciones: `left` Left · `top` Top · `right` Right
  - Default: `left`
  - Visible si: `sidebar_type` is `['0', 'classic']`
- **`icon_animation`** (select) — Icon animation
  - Valor: String
  - Opciones: `""` None · `rotate` Rotate · `zoom` Zoom
  - Visible si: `sidebar_type` is `['0', 'classic']`

### Submenu

- **`submenu_subicon`** (icon) — Submenu icon
  - Valor: String
  - Default: `fas fa-arrow-right`
  - Visible si: `sidebar_type` is `['0', 'classic']`
- **`submenu_icon_animation`** (select) — Icon Animation
  - Valor: String
  - Opciones: `""` None · `rotate` Rotate · `zoom` Zoom
  - Visible si: `sidebar_type` is `['0', 'classic']`

### Burger wrapper

- **`css_menu-burger_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu-burger", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-burger_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu-burger", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_menu-burger_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu-burger", "style": "border-width", "val": "1px 1px 1px 1px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_header_burger_wrapper` isnt `none`
- **`css_menu-burger_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu-burger", "style": "border-radius", "val": "8px 8px 8px 8px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
- **`css_menu-burger_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu-burger", "style": "background-color", "val": "valor"}`
- **`css_menu-burger_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu-burger", "style": "border-color", "val": "valor"}`
  - Visible si: `border_header_burger_wrapper` isnt `none`
- **`css_menu-burger_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu-burger:hover", "style": "background-color", "val": "valor"}`
- **`css_menu-burger_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-menu-burger:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_header_burger_wrapper` isnt `none`

### Icon

- **`icon_position`** (switch) — Icon position
  - Valor: String
  - Opciones: `top` Top · `bottom` Bottom · `left` Left · `right` Right
  - Default: `top`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`icon_align`** (switch) — Icon alignment
  - Valor: String
  - Opciones: `start` Start · `center` Center · `end` End
  - Default: `center`
  - Visible si: `header-icon-desc` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxicon_icon_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "--mfn-header-menu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxicon-wrapper_width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxicon-wrapper_height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxicon-wrapper_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxicon-wrapper_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-wrapper_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper", "style": "background-color", "val": "valor"}`
- **`css_icon-wrapper_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_icon-wrapper_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_icon` isnt `none`
- **`css_icon-wrapper_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper", "style": "border-width", "val": "1px 1px 1px 1px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_header_icon` isnt `none`
- **`css_icon-boxicon-wrapper_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "border-radius", "val": "8px 8px 8px 8px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
- **`css_icon-wrapperi_color`** (color) — Icon color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper i", "style": "color", "val": "valor"}`
- **`css_icon-boxicon-wrapper_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box:hover .icon-wrapper", "style": "background-color", "val": "valor"}`
- **`css_icon-boxicon-wrapper_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box:hover .icon-wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_icon` isnt `none`
- **`css_icon-boxicon-wrapperi_color_hover`** (color) — Icon color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box:hover .icon-wrapper i", "style": "color", "val": "valor"}`

### Desc

- **`header_icon_desc_visibility`** (switch) — Responsive visibility
  - Valor: String de tokens separados por espacio, con espacio inicial (ej. `" hide-mobile hide-tablet"`)
  - Opciones: `hide-desktop` Hide on Desktop · `hide-laptop` Hide on Laptop · `hide-tablet` Hide on Tablet · `hide-mobile` Hide on Mobile
- **`css_desc-wrapper_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc-wrapper", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxdesc-wrapper_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .desc-wrapper", "style": "color", "val": "valor"}`
- **`css_icon-boxdesc-wrapper_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box:hover .desc-wrapper", "style": "color", "val": "valor"}`

### Menu wrapper


### Container

- **`css_menu-sidebar_header_menu_sidebar_width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar", "style": "--mfn-header-menu-sidebar-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `sidebar_type` is `0`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-sidebar-wrapper_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-tmpl-menu-sidebar-wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_menu-sidebar_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar", "style": "background-color", "val": "valor"}`
  - Visible si: `bg_menu-tmpl-sidebar` is `default`
- **`css_menu-sidebar_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `bg_menu-tmpl-sidebar` is `gradient`
- **`css_menu-sidebar_background_image`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `bg_menu-tmpl-sidebar` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-sidebar_background_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar", "style": "background-repeat", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `repeat` Repeat · `no-repeat` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y
  - Visible si: `bg_menu-tmpl-sidebar` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-sidebar_background_position`** (select) — Position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar", "style": "background-position", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center
  - Visible si: `bg_menu-tmpl-sidebar` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-sidebar_background_attachment`** (select) — Attachment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar", "style": "background-attachment", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `scroll` Scroll · `fixed` Fixed
  - Visible si: `bg_menu-tmpl-sidebar` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-sidebar_background_size`** (select) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar", "style": "background-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px
  - Visible si: `bg_menu-tmpl-sidebar` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Close

- **`sidebar-menu-close-icon-position`** (switch) — Position
  - Valor: String
  - Opciones: `""` Default · `left` Left · `right` Right
  - Visible si: `sidebar_type` is `0`
- **`css_menu-sidebar-close-icon_font_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-close-icon", "style": "font-size", "val": "valor"}`
  - Default: `20px`
  - Visible si: `sidebar_type` is `0`
- **`css_menu_-toggleicon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu-toggle .icon", "style": "color", "val": "valor"}`
  - Visible si: `sidebar_type` is `0`

### Content overlay

- **`css_menu-activebefore_display`** (switch) — Visibility
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement.mfn-header-tmpl-menu-active:before", "style": "display", "val": "valor"}`
  - Opciones: `""` Hidden · `block` Visible
- **`css_menu-activebefore_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement.mfn-header-tmpl-menu-active:before", "style": "background-color", "val": "valor"}`

### Menu


### Items

- **`items_align`** (switch) — Alignment
  - Valor: String
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Default: `top`
  - Visible si: `menu_icon_align` isnt `top`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_li_header_menu_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li", "style": "--mfn-header-menu-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_lia_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_lia_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_lia_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_menu_lia_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_header_menu_link` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_lia_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_lia_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a", "style": "color", "val": "valor"}`
- **`css_menu_lia_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a", "style": "background-color", "val": "valor"}`
- **`css_menu_lia_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_menu_link` isnt `none`
- **`css_menu_lia_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_lia_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li:hover > a", "style": "color", "val": "valor"}`
- **`css_menu_lihovera_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li:hover > a", "style": "background-color", "val": "valor"}`
- **`css_menu_lihovera_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li:hover > a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_menu_link` isnt `none`
- **`css_menu_lihovera_box_shadow_hover`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li:hover > a", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_licurrent-menu-itema_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li.current-menu-item > a", "style": "color", "val": "valor"}`
- **`css_menu_licurrent-menu-itema_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li.current-menu-item > a", "style": "background-color", "val": "valor"}`
- **`css_menu_licurrent-menu-itema_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li.current-menu-item > a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_menu_link` isnt `none`
- **`css_menu_licurrent-menu-itema_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li.current-menu-item > a", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Animation

- **`css_menu-li-menu-link_header_menu_animation_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-li > .mfn-menu-link", "style": "--mfn-header-menu-animation-color", "val": "valor"}`
  - Visible si: `header_menu_animation` isnt ``

### Icon

- **`css_menu_li_header_menu_icon_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li", "style": "--mfn-header-menu-icon-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_li_header_menu_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li", "style": "--mfn-header-menu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu .menu-icon > i", "style": "color", "val": "valor"}`
- **`css_menu_ahovermenu-iconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu a:hover > .menu-icon > i", "style": "color", "val": "valor"}`
- **`css_menu_licurrent-menu-itemamenu-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li.current-menu-item > a > .menu-icon i", "style": "color", "val": "valor"}`

### Submenu icon

- **`css_menu_li_header_menu_submenu_icon_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li", "style": "--mfn-header-menu-submenu-icon-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `submenu_icon_display` is `on`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_limenu-subi_header_submenu_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .menu-sub i", "style": "--mfn-header-submenu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_liamenu-subi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a .menu-sub i", "style": "color", "val": "valor"}`
- **`css_menu_liahovermenu-subi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li > a:hover .menu-sub i", "style": "color", "val": "valor"}`
- **`css_menu_licurrent-menu-itemamenu-subi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu > li.current-menu-item > a .menu-sub i", "style": "color", "val": "valor"}`

### Submenu


### Container

- **`css_menu_li-submenulia_justify_content`** (switch) — Alignment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu li a", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Left · `center` Center · `flex-end` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_li-submenu_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu", "style": "background-color", "val": "valor"}`
- **`css_menu_li-submenu_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_li-submenu_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_li-submenu_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_li-submenu_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_menu_li-submenu_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_header_submenu_link` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu_li-submenu_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_submenu_link` isnt `none`
- **`css_menu_li-submenu_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Items

- **`css_menu_li-submenulia_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu li a", "style": "color", "val": "valor"}`
- **`css_menu_li-submenulia_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu li a", "style": "background-color", "val": "valor"}`
- **`css_menu_li-submenulihovera_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu li:hover > a", "style": "color", "val": "valor"}`
- **`css_menu_li-submenulihovera_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu li:hover > a", "style": "background-color", "val": "valor"}`
- **`css_menu_li-submenulicurrent-menu-itema_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu li.current-menu-item > a", "style": "color", "val": "valor"}`
- **`css_menu_li-submenulicurrent-menu-itema_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-header-tmpl-menu-sidebar .mfn-header-menu li .mfn-submenu li.current-menu-item > a", "style": "background-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "header_burger",
  "uid": "itm000001",
  "icon": "header_burger",
  "jsclass": "header_burger",
  "title": "Menu burger",
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