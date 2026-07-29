# `sidemenu_menu` — Menu

- **Categoría:** sidemenu
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 90

## Campos

### Menu

- **`tabs`** (tabs) — Menu
  - Add multiple menus easily in tabs. You can add one menu in single tab as well.
  - Valor: Array de objetos (formato propio del campo tabs)
  - Opciones: `title` ["input", "Title", "Menu title"] · `menu` ["select", "Menu to display", "", "menus"]
  - Default: `[{"title": "Menu 1", "menu": ""}]`

### Icon

- **`css_sidemenu-menu-a-icon_display`** (switch) — Icon visibility
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu a .menu-icon", "style": "display", "val": "valor"}`
  - Opciones: `block` Show · `none` Hide
  - Default: `block`

### Submenu

- **`submenu`** (switch) — Submenu
  - Valor: String
  - Opciones: `on` Show · `off` Hide
  - Default: `on`
- **`submenu_on`** (select) — Submenu visibility
  - Valor: String
  - Opciones: `visible` Visible · `toggled` Toggled · `replace` Replace current
  - Default: `visible`
  - Visible si: `submenu` is `on`
- **`submenu_icon_display`** (switch) — Submenu icon visibility
  - Valor: String
  - Opciones: `on` Show · `off` Hide
  - Default: `on`
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

- **`css_sidemenu-menu-a-desc_display`** (switch) — Desc visibility
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu a .menu-desc", "style": "display", "val": "valor"}`
  - Opciones: `block` Show · `none` Hide
  - Default: `block`

### Menu


### Container

- **`css_menu-wrapper_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-wrapper_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper", "style": "background-color", "val": "valor"}`
- **`css_menu-wrapper_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_menu-wrapper_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_sidemenu_tabs_content` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-wrapper_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_content` isnt `none`
- **`css_menu-wrapper_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Items

- **`css_ul-sidemenu-menulia-menu-link_justify_content`** (switch) — Alignment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Left · `center` Center · `flex-end` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ul-sidemenu-menulia-menu-link_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ul-sidemenu-menulia-menu-link_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_sidemenu-menulia-menu-link_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ul-sidemenu-menu-link_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_ul-sidemenu-menu-link_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_sidemenu_tabs_ulli2` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ul-sidemenu-menu-link_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ul-sidemenu-menulia-menu-link_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link", "style": "color", "val": "valor"}`
- **`css_ul-sidemenu-menu-link_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link", "style": "background-color", "val": "valor"}`
- **`css_ul-sidemenu-menu-link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_ulli2` isnt `none`
- **`css_ul-sidemenu-menu-link_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link:hover", "style": "color", "val": "valor"}`
- **`css_ul-sidemenu-link_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link:hover", "style": "background-color", "val": "valor"}`
- **`css_ul-sidemenu-link_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li a.mfn-menu-link:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_ulli2` isnt `none`
- **`css_ul-sidemenu-licurrent-menu-itema-menu-link_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li.current-menu-item > a.mfn-menu-link", "style": "color", "val": "valor"}`
- **`css_ul-sidemenu-menulicurrent-menu-itema-menu-link_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li.current-menu-item > a.mfn-menu-link", "style": "background-color", "val": "valor"}`
- **`css_ul-sidemenu-menulicurrent-menu-itema-menu-link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li.current-menu-item > a.mfn-menu-link", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_ulli2` isnt `none`

### Icon

- **`css_sidemenu-menuli_mfn_sidemenu_icon_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li", "style": "--mfn-sidemenu-icon-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `5px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_sidemenu-menuli_sidemenu_icon_width`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li", "style": "--mfn-sidemenu-icon-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_sidemenu-menumenu-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu .menu-icon i", "style": "color", "val": "valor"}`
- **`css_sidemenu-menu-a-iconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu a:hover .menu-icon i", "style": "color", "val": "valor"}`
- **`css_sidemenu-menulicurrent-menu-itemamenu-iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li.current-menu-item > a .menu-icon i", "style": "color", "val": "valor"}`

### Submenu icon

- **`css_sidemenu-menuli_sidemenu_submenu_icon_width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li", "style": "--mfn-sidemenu-submenu-icon-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_sidemenu-menuli_sidemenu_submenu_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li", "style": "--mfn-sidemenu-submenu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_sidemenu-menuliouter-menu-subi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li .outer-menu-sub i", "style": "color", "val": "valor"}`
- **`css_sidemenu-menuliouter-menu-sub_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li .outer-menu-sub", "style": "background-color", "val": "valor"}`
- **`css_sidemenu-menuliouter-menu-subi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li:hover > .outer-menu-sub i", "style": "color", "val": "valor"}`
- **`css_sidemenu-menuliouter-menu-sub_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li:hover > .outer-menu-sub", "style": "background-color", "val": "valor"}`
- **`css_sidemenu-menulicurrent-menu-itemouter-menu-subi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li.current-menu-item > .outer-menu-sub i", "style": "color", "val": "valor"}`
- **`css_-sidemenu-menulicurrent-menu-itemouter-menu-sub_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-menu li.current-menu-item > .outer-menu-sub", "style": "background-color", "val": "valor"}`

### Submenu


### Container

- **`css_menu-wrapperliul_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper li ul", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-wrapperliul_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper li ul", "style": "background-color", "val": "valor"}`
- **`css_menu-wrapperliul_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper li ul", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_menu-wrapperliul_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper li ul", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_sidemenu_tabs_content` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-wrapperliul_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper li ul", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_content` isnt `none`
- **`css_menu-wrapperliul_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-wrapper li ul", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Items

- **`css_ul-sidemenu-menuliullia-menu-link_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ul-sidemenu-menuliullia-menu-link_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_sidemenu-menuliullia-menu-link_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ul-sidemenu-liullia-menu-link_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_ul-sidemenu-liullia-menu-link_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_sidemenu_tabs_ulli` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ul-sidemenu-liullia-menu-link_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ul-sidemenu-menuliullia-menu-link_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link", "style": "color", "val": "valor"}`
- **`css_ul-sidemenu-liullia-menu-link_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link", "style": "background-color", "val": "valor"}`
- **`css_ul-sidemenu-liullia-menu-link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_ulli` isnt `none`
- **`css_ul-sidemenu-menuliullia-menu-link_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link:hover", "style": "color", "val": "valor"}`
- **`css_ul-sidemenu-menuliullia-menu-linkhover_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link:hover", "style": "background-color", "val": "valor"}`
- **`css_ul-sidemenu-liullia-menu-link_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li a.mfn-menu-link:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_ulli` isnt `none`
- **`css_ul-sidemenu-menuliullicurrent-menu-itema-menu-link_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li.current-menu-item > a.mfn-menu-link", "style": "color", "val": "valor"}`
- **`css_ul-sidemenu-menuliullicurrent-menu-itema-menu-link_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li.current-menu-item > a.mfn-menu-link", "style": "background-color", "val": "valor"}`
- **`css_ul-sidemenu-menuliullicurrent-menu-itema-menu-link_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.mfn-sidemenu-menu li ul li.current-menu-item > a.mfn-menu-link", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_ulli` isnt `none`

### Tabs


### Nav

- **`css_menu-tabs-wrapperul-menu-tabs-nav_mfn_sidemenu_menu_tabber_padding`** (sliderbar) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav", "style": "--mfn-sidemenu-menu-tabber-padding", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `5px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-tabs-wrapperul-menu-tabs-nav_margin_bottom`** (sliderbar) — Margin bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav", "style": "margin-bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `5px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-tabs-wrapperul-menu-tabs-nav_mfn_sidemenu_menu_tabber_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav", "style": "--mfn-sidemenu-menu-tabber-bg", "val": "valor"}`
- **`css_menu-tabs-wrapperul-menu-tabs-nav_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_menu-tabs-wrapperul-menu-tabs-nav_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_sidemenu_tabs_ul` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-tabs-wrapperul-menu-tabs-nav_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_ul` isnt `none`
- **`css_menu-tabs-wrapperul-menu-tabs-nav_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Nav items

- **`css_menu-tabs-wrapperul-menu-tabs-navli_mfn_sidemenu_menu_tabber_tab_spacing`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li", "style": "--mfn-sidemenu-menu-tabber-tab-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `5px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_sidemenu_tabs_ulli` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a", "style": "color", "val": "valor"}`
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a", "style": "background-color", "val": "valor"}`
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_ulli` isnt `none`
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a:hover", "style": "color", "val": "valor"}`
- **`css_menu-tabs-wrapperul-menu-tabs-navliahover_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a:hover", "style": "background-color", "val": "valor"}`
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li a:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_ulli` isnt `none`
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_color_active`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li.active a", "style": "color", "val": "valor"}`
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_background_color_active`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li.active a", "style": "background-color", "val": "valor"}`
- **`css_menu-tabs-wrapperul-menu-tabs-navlia_border_color_active`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-menu-tabs-wrapper ul.mfn-menu-tabs-nav li.active a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sidemenu_tabs_ulli` isnt `none`

### Breadcrumbs


### Links

- **`css_sidemenu-breadcrumbsa_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-breadcrumbs a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_sidemenu-breadcrumbsa_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-breadcrumbs a", "style": "color", "val": "valor"}`
- **`css_sidemenu-breadcrumbsa_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-breadcrumbs a:hover", "style": "color", "val": "valor"}`

### Separator

- **`css_sidemenu-breadcrumbs-sidemenu-breadcrumbs-separator_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-sidemenu-breadcrumbs .mfn-sidemenu-breadcrumbs-separator", "style": "color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "sidemenu_menu",
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