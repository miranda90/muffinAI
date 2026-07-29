# `toggle` — Toggle

- **Categoría:** blocks
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 83

## Campos
- **`tabs`** (tabs) — Items
  - Valor: Array de objetos (formato propio del campo tabs)
  - Opciones: `title` ["input", "Title", "This is the title"] · `content` ["textarea", "Content", "This is the content"] · `icon` ["icon", "Icon", ""] · `image` ["image", "Image", ""]
  - Default: `[{"title": "This is the 1st title", "content": "This is the 1st content"}, {"title": "This is the 2nd title", "content": "This is the 2nd content"}]`
- **`tag`** (switch) — Question tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h5`

### Options

- **`type`** (switch) — Type
  - Valor: String
  - Opciones: `unordered` Unordered · `ordered` Ordered
  - Default: `unordered`
- **`starting`** (text) — Starting number
  - Valor: String
  - Default: `1`
  - Visible si: `toggle-type` is `ordered`
- **`divider`** (switch) — Divider
  - Valor: String
  - Opciones: `disable` Disable · `enable` Enable
  - Default: `disable`
- **`open_first`** (switch) — Open first
  - Valor: String
  - Opciones: `disable` Disable · `enable` Enable
  - Default: `disable`
- **`open_all`** (switch) — Open all
  - Valor: String
  - Opciones: `disable` Disable · `enable` Enable
  - Default: `disable`
- **`open_more`** (switch) — Open more than one at a time
  - Valor: String
  - Opciones: `disable` Disable · `enable` Enable
  - Default: `disable`

### Icon

- **`icon`** (icon) — Icon
  - Valor: String
  - Default: `fas fa-plus`
- **`active_icon`** (icon) — Icon
  - Valor: String
  - Default: `fas fa-minus`
- **`icon_animation`** (switch) — Animation
  - Valor: String
  - Opciones: `disable` Disable · `zoom` Zoom · `rotate` Rotate
  - Default: `disable`

### Toggle item

- **`css_toggle_mfn_toggle_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle", "style": "--mfn-toggle-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle-item_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_toggle-item_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item", "style": "border-width", "val": "1px 1px 1px 1px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `toggle-border-style` isnt `none`
- **`css_toggle-item_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item", "style": "border-radius", "val": "8px 8px 8px 8px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
- **`css_toggle-item_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-border-style` isnt `none`
- **`css_toggle-item_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item", "style": "background-color", "val": "valor"}`
- **`css_toggle-item_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item", "style": "box-shadow", "val": "valor"}`
- **`css_toggle-item_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-border-style` isnt `none`
- **`css_toggle-item_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover", "style": "background-color", "val": "valor"}`
- **`css_toggle-item_box_shadow_hover`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover", "style": "box-shadow", "val": "valor"}`
- **`css_toggle-itemactive_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .mfn-toggle-item.active", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-border-style` isnt `none`
- **`css_toggle-itemactive_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .mfn-toggle-item.active", "style": "background-color", "val": "valor"}`
- **`css_toggle-itemactive_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .mfn-toggle-item.active", "style": "box-shadow", "val": "valor"}`

### Divider

- **`css_toggletoggle-divider_height`** (sliderbar) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .toggle-divider", "style": "height", "val": "valor"}`
  - Visible si: `toggle-divider` is `enable`
- **`css_toggle_mfn_toggle_divider_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle", "style": "--mfn-toggle-divider-color", "val": "valor"}`
  - Visible si: `toggle-divider` is `enable`

### Title bar

- **`css_toggle-itemtoggle-bar_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item .toggle-bar", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle-itemtoggle-heading_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item .toggle-heading", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle-itemtoggle-bar_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item .toggle-bar", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_toggle-itemtoggle-bar_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item .toggle-bar", "style": "border-width", "val": "1px 1px 1px 1px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `toggle-title-border-style` isnt `none`
- **`css_toggle-itemtoggle-bar_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item .toggle-bar", "style": "border-radius", "val": "8px 8px 8px 8px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
- **`css_toggle-itemtoggle-bar_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item .toggle-bar", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-title-border-style` isnt `none`
- **`css_toggle-itemtoggle-heading_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item .toggle-heading", "style": "color", "val": "valor"}`
- **`css_toggle-itemtoggle-bar_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item .toggle-bar", "style": "background-color", "val": "valor"}`
- **`css_toggle-itemtoggle-bar_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item .toggle-bar", "style": "box-shadow", "val": "valor"}`
- **`css_toggle-itemtoggle-bar_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover .toggle-bar", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-title-border-style` isnt `none`
- **`css_toggle-itemtoggle-heading_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover .toggle-heading", "style": "color", "val": "valor"}`
- **`css_toggle-itemtoggle-bar_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover .toggle-bar", "style": "background-color", "val": "valor"}`
- **`css_toggle-itemtoggle-bar_box_shadow_hover`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover .toggle-bar", "style": "box-shadow", "val": "valor"}`
- **`css_toggle-itemtoggle-bar_border_color_active`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .mfn-toggle-item.active .toggle-bar", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-title-border-style` isnt `none`
- **`css_toggle-itemactivetoggle-heading_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .mfn-toggle-item.active .toggle-heading", "style": "color", "val": "valor"}`
- **`css_toggle-itemtoggle-bar_background_color_active`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .mfn-toggle-item.active .toggle-bar", "style": "background-color", "val": "valor"}`
- **`css_toggle-itemtoggle-bar_box_shadow_active`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .mfn-toggle-item.active .toggle-bar", "style": "box-shadow", "val": "valor"}`

### Content

- **`css_toggletoggle-content_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .toggle-content", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggletoggle-content_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .toggle-content", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggletoggle-content_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .toggle-content", "style": "color", "val": "valor"}`
- **`css_toggletoggle-contenta_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .toggle-content a", "style": "color", "val": "valor"}`
- **`css_toggletoggle-contenta_color_hover`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .toggle-content a:hover", "style": "color", "val": "valor"}`
- **`css_toggletoggle-content_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle .toggle-content", "style": "background-color", "val": "valor"}`

### Title icon

- **`css_toggle-bar-icon_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-bar-icon", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle-bar-icon_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-bar-icon", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle_mfn_toggle_bar_icon_spacing`** (sliderbar) — Spacing
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle", "style": "--mfn-toggle-bar-icon-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle_mfn_toggle_bar_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle", "style": "--mfn-toggle-bar-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `toggle-type` isnt `ordered`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle-bar-iconafter_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-bar-icon:after", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Visible si: `toggle-type` is `ordered`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle-bar-icon_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-bar-icon", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_toggle-bar-icon_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-bar-icon", "style": "border-width", "val": "1px 1px 1px 1px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `toggle-ti-border-style` isnt `none`
- **`css_toggle-bar-icon_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-bar-icon", "style": "border-radius", "val": "8px 8px 8px 8px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
- **`css_toggle-bar-icon_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-bar-icon", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-ti-border-style` isnt `none`
- **`css_toggle_mfn_toggle_bar_icon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle", "style": "--mfn-toggle-bar-icon-color", "val": "valor"}`
- **`css_toggle-bar-icon_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-bar-icon", "style": "background-color", "val": "valor"}`
- **`css_toggle-itemtoggle-bar-icon_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover .toggle-bar-icon", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-ti-border-style` isnt `none`
- **`css_toggle-item_toggle_bar_icon_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover", "style": "--mfn-toggle-bar-icon-color", "val": "valor"}`
- **`css_toggle-itemtoggle-bar-icon_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover .toggle-bar-icon", "style": "background-color", "val": "valor"}`
- **`css_toggle-itemactivetoggle-bar-icon_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item.active .toggle-bar-icon", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-ti-border-style` isnt `none`
- **`css_toggle-itemactive_toggle_bar_icon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item.active", "style": "--mfn-toggle-bar-icon-color", "val": "valor"}`
- **`css_toggle-itemactivetoggle-bar-icon_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item.active .toggle-bar-icon", "style": "background-color", "val": "valor"}`

### Toggle icon

- **`css_toggle-icon_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-icon", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle-icon_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-icon", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle_mfn_toggle_icon_spacing`** (sliderbar) — Spacing
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle", "style": "--mfn-toggle-icon-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle_mfn_toggle_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle", "style": "--mfn-toggle-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `toggle-type` isnt `ordered`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle-iconafter_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-icon:after", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Visible si: `toggle-type` is `ordered`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_toggle-icon_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-icon", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_toggle-icon_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-icon", "style": "border-width", "val": "1px 1px 1px 1px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `toggle-ti-icon-border-style` isnt `none`
- **`css_toggle-icon_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-icon", "style": "border-radius", "val": "8px 8px 8px 8px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
- **`css_toggle-icon_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-icon", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-ti-icon-border-style` isnt `none`
- **`css_toggle_mfn_toggle_icon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle", "style": "--mfn-toggle-icon-color", "val": "valor"}`
- **`css_toggle-icon_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .toggle-icon", "style": "background-color", "val": "valor"}`
- **`css_toggle-itemtoggle-icon_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover .toggle-icon", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-ti-icon-border-style` isnt `none`
- **`css_toggle-item_mfn_toggle_icon_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover", "style": "--mfn-toggle-icon-color", "val": "valor"}`
- **`css_toggle-itemtoggle-icon_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item:hover .toggle-icon", "style": "background-color", "val": "valor"}`
- **`css_toggle-itemactivetoggle-icon_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item.active .toggle-icon", "style": "border-color", "val": "valor"}`
  - Visible si: `toggle-ti-icon-border-style` isnt `none`
- **`css_toggle-itemactive_toggle_icon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item.active", "style": "--mfn-toggle-icon-color", "val": "valor"}`
- **`css_toggle-itemactivetoggle-icon_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-toggle-item.active .toggle-icon", "style": "background-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "toggle",
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