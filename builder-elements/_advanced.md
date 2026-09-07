# Pestaña Advanced (común a TODOS los items)

Campos comunes.


### Dimensions

- **`width_switcher`** (select) — Width
  - Valor: String
  - Opciones: `""` Default · `inline` Inline · `custom` Custom
- **`css_advanced_flex`** (text) — Width
  - Use px, %, vw, vh or auto to set content width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `item_width_switcher_adv` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`height_switcher`** (select) — Height
  - Valor: String
  - Opciones: `""` Default · `custom` Custom
- **`css_advanced_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `item_height_switcher_adv` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Spacing

- **`css_advanced_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Default: `{"desktop": {"top": [{"val": "0px", "type": "std", "screen": "desktop"}], "bottom": [{"val": "40px", "type": "std", "screen": "desktop"}], "left": [{"val": "12px", "type": "std", "screen": "desktop"}], "right": [{"val": "12px", "type": "std", "screen": "desktop"}]}, "mobile": {"bottom": [{"val": "20px", "type": "std", "screen": "mobile"}], "left": [{"val": "0px", "type": "std", "screen": "mobile"}], "right": [{"val": "0px", "type": "std", "screen": "mobile"}]}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Positioning

- **`css_advanced_position`** (select) — Position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "position", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `relative` Offset · `absolute` Absolute
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_top`** (text) — Top
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `item_position_rwd` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_bottom`** (text) — Bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `item_position_rwd` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_left`** (text) — Left
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `item_position_rwd` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_right`** (text) — Right
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `item_position_rwd` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_z_index`** (text) — Z-index
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "z-index", "val": "valor"}`
- **`css_advanced_order`** (text) — Order
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "order", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Background

- **`css_advanced_transition`** (sliderbar) — Transition duration
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "transition", "val": "valor"}`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_advanced_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_adv` is `default`
- **`css_advanced_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_adv` is `gradient`
- **`css_advanced_background_img`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher_adv` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "background-repeat", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `repeat` Repeat · `no-repeat` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y
  - Visible si: `background_switcher_adv` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_position`** (select) — Position
  - Doesn't work with Attachment / Parallax
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "background-position", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center · `custom` Custom
  - Visible si: `background_switcher_adv` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_position_v2`** (text) — Custom background position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "background-position_v2", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `bgposopt_rwd` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_attachment`** (select) — Attachment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "background-attachment", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `scroll` Scroll · `fixed` Fixed
  - Visible si: `background_switcher_adv` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_size`** (select) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "background-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px · `custom` Custom
  - Visible si: `background_switcher_adv` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_size_v2`** (text) — Custom background size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "background-size_v2", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `custombgsize` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_backdrop_filter`** (backdrop_filter) — Backdrop filter
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "backdrop-filter", "val": {..., "string": "blur(...) ..."} — solo string se emite}`
- **`css_advanced_transition_hover`** (sliderbar) — Transition duration
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner:hover", "style": "transition", "val": "valor"}`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_advanced_background_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner:hover", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_hover_adv` is `default`
- **`css_advanced_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover_adv` is `gradient`
- **`css_advanced_background_img_hover`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner:hover", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher_hover_adv` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_backdrop_filter_hover`** (backdrop_filter) — Backdrop filter
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner:hover", "style": "backdrop-filter", "val": {..., "string": "blur(...) ..."} — solo string se emite}`

### Border

- **`css_advanced_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_advanced_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_adv` isnt `none`
- **`css_advanced_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_adv` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_overflow`** (select) — Overflow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "overflow", "val": "valor"}`
  - Opciones: `""` Default · `hidden` Hidden · `auto` Auto

### Responsive


### Device type

- **`visibility`** (switch) — Responsive visibility
  - Valor: String de tokens separados por espacio, con espacio inicial (ej. `" hide-mobile hide-tablet"`)
  - Opciones: `hide-desktop` Hide on Desktop · `hide-laptop` Hide on Laptop · `hide-tablet` Hide on Tablet · `hide-mobile` Hide on Mobile

### Custom

- **`custom-responsive`** (switch) — Custom visibility
  - Valor: String
  - Opciones: `hide` Hide under · `show` Show under
  - Default: `hide`
- **`css_advanced_hide_under_custom`** (sliderbar) — Hide under
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "hide_under_custom", "val": "valor"}`
  - Visible si: `custom-responsive` is `hide`
- **`css_advanced_show_under_custom`** (sliderbar) — Show under
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "show_under_custom", "val": "valor"}`
  - Visible si: `custom-responsive` is `show`

### Animation

- **`animate`** (select) — Animation
  - Entrance animation
  - Valor: String
  - Opciones: `""` - Not Animated - · `fadeIn` Fade in · `fadeInUp` Fade in up · `fadeInDown` Fade in down · `fadeInLeft` Fade in left · `fadeInRight` Fade in right · `fadeInUpLarge` Fade in up large · `fadeInDownLarge` Fade in down large · `fadeInLeftLarge` Fade in left large · `fadeInRightLarge` Fade in right large · `zoomIn` Zoom in · `zoomInUp` Zoom in up · `zoomInDown` Zoom in down · `zoomInLeft` Zoom in left · `zoomInRight` Zoom in right · `zoomInUpLarge` Zoom in up large · `zoomInDownLarge` Zoom in down large · `zoomInLeftLarge` Zoom in left large · `bounceIn` Bounce in · `bounceInUp` Bounce in up · `bounceInDown` Bounce in down · `bounceInLeft` Bounce in left · `bounceInRight` Bounce in right
- **`css_advanced_animation_delay`** (sliderbar) — Animation delay
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "animation-delay", "val": "valor"}`
  - Visible si: `animate` isnt ``

### Transform

- **`css_advanced_transform`** (transform) — 
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "transform", "val": {"desktop": {"scaleX":1,"skewY":0,"skewX":0,"scaleY":1,"translateX":0,"translateY":0,"rotate":0,"string":"1,0,0,1,0,0,0"}, "tablet": ..., "mobile": ...}}`
  - Default: `0`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_transform_origin`** (select) — Transform origin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "transform-origin", "val": "valor"}`
  - Opciones: `""` Default · `top left` Top Left · `top center` Top Center · `top right` Top Right · `center left` Center Left · `center` Center · `center right` Center Right · `bottom left` Bottom Left · `bottom center` Bottom Center · `bottom right` Bottom Right
- **`css_advanced_transition`** (sliderbar) — Transition duration
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "transition", "val": "valor"}`
- **`css_advanced_transform_hover`** (transform) — Transform options
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner:hover", "style": "transform", "val": {"desktop": {"scaleX":1,"skewY":0,"skewX":0,"scaleY":1,"translateX":0,"translateY":0,"rotate":0,"string":"1,0,0,1,0,0,0"}, "tablet": ..., "mobile": ...}}`
  - Default: `0`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Conditional logic

- **`conditions`** (logic) — Conditional logic
  - Valor: String

### Custom

- **`classes`** (pills) — CSS classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)
- **`custom_id`** (text) — Custom ID
  - Valor: String
- **`custom_css`** (textarea) — Additional CSS
  - Valor: String

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*