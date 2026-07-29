# Campos de WRAP

Campos disponibles en `attr` de cada wrap (incluye grid, query loop, sticky...).


### Options

- **`grid`** (switch) — Display
  - In the Grid model, the widths of columns are determined by the Column Size. The elements’ margins are set to zero.
  - Valor: String
  - Opciones: `""` Flexbox · `grid` Grid
- **`grid_columns_switcher`** (switch) — Columns
  - Valor: String
  - Opciones: `""` Defined · `custom` Custom
  - Visible si: `wrap_grid` is `grid`
- **`css_grid_columns`** (switch) — Columns
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "grid-template-columns", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `1fr` 1 · `repeat(2, 1fr)` 2 · `repeat(3, 1fr)` 3 · `repeat(4, 1fr)` 4 · `repeat(5, 1fr)` 5 · `repeat(6, 1fr)` 6
  - Default: `repeat(3, 1fr)`
  - Visible si: `wrap_grid` is `grid` AND `grid_columns_switcher` is ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_grid_columns_custom`** (text) — Grid template columns
  - Defines the number and width of columns in a CSS Grid layout e.g. <code>repeat(3, 1fr)</code>, <code>300px 1fr 400px</code>
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-grid.mcb-wrap-grid-col-custom.mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "grid-template-columns", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `wrap_grid` is `grid` AND `grid_columns_switcher` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_grid_columns_gap`** (text) — Column gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "column-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `wrap_grid` is `grid`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_grid_rows_gap`** (text) — Row gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "row-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `wrap_grid` is `grid`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`sticky`** (switch) — Sticky
  - Does <b>not</b> work with Move up and Parallax
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`sticky_offset`** (sliderbar) — Sticky offset
  - Offset from top during scrolling
  - Valor: Número como string
  - Visible si: `wrap_sticky_rwd` is `1`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`type`** (switch) — Type
  - Query loop displays wrap&apos;s content in designed loop
  - Valor: String
  - Opciones: `""` Default · `query` Query loop
- **`query_type`** (select) — Query type
  - Valor: String
  - Opciones: `""` Select · `posts` Posts · `terms` Terms
  - Visible si: `wrap_type` is `query`
- **`query_post_type`** (select) — Post type
  - Valor: String
  - Default: `post`
  - Visible si: `query_type` is `posts`
- **`query_post_type_{mfn.current_post_type}`** (multiselect) — Taxonomies included
  - Valor: String
  - Visible si: `query_post_type` isnt ``
- **`query_post_type_{mfn.current_post_type}_exclude`** (multiselect) — Taxonomies excluded
  - Valor: String
  - Visible si: `query_post_type` isnt ``
- **`query_post_type_product_order`** (select) — Display
  - This option turns off standard order settings
  - Valor: String
  - Opciones: `""` Default · `on_sale` On sale · `best_selling` Best selling · `top_rated` Top rated
  - Visible si: `query_post_type` is `product`
- **`query_post_orderby`** (select) — Order by
  - Valor: String
  - Opciones: `""` None · `ID` ID · `date` Date · `modified` Modified · `menu_order` Menu order · `title` Title · `rand` Rand
  - Default: `date`
  - Visible si: `query_type` is `posts`
- **`query_post_order`** (select) — Order
  - Valor: String
  - Opciones: `ASC` Ascending · `DESC` Descending
  - Default: `DESC`
  - Visible si: `query_type` is `posts`
- **`query_post_per_page`** (text) — Limit
  - By default limit from Admin > Settings > Reading > Blog pages show at most
  - Valor: String
  - Default: `0`
  - Visible si: `query_type` is `posts`
- **`query_post_offset`** (text) — Offset
  - This option omits provided quantity of posts (from the beginning)
  - Valor: String
  - Default: `0`
  - Visible si: `query_type` is `posts`
- **`query_terms_taxonomy`** (select) — Taxonomy
  - Valor: String
  - Default: `category`
  - Visible si: `query_type` is `terms`
- **`query_terms_includes_{mfn.current_tax}`** (multiselect) — Includes
  - IDs of taxonomies to include
  - Valor: String
  - Visible si: `query_terms_taxonomy` isnt ``
- **`query_terms_excludes_{mfn.current_tax}`** (multiselect) — Excludes
  - IDs of taxonomies to exclude
  - Valor: String
  - Visible si: `query_terms_taxonomy` isnt ``
- **`query_terms_child_of_product_cat`** (select) — Child of
  - Valor: String
  - Visible si: `query_terms_taxonomy` is `product_cat`
- **`query_terms_orderby`** (select) — Order by
  - Valor: String
  - Opciones: `""` None · `term_order` Term order · `term_id` ID · `name` Name · `count` Count
  - Default: `ID`
  - Visible si: `query_type` is `terms`
- **`query_terms_order`** (select) — Order
  - Valor: String
  - Opciones: `ASC` Ascending · `DESC` Descending
  - Default: `ASC`
  - Visible si: `query_type` is `terms`
- **`query_terms_hide_empty`** (select) — Hide empty
  - Valor: String
  - Opciones: `""` False · `1` True
  - Visible si: `query_type` is `terms`
- **`query_terms_number`** (text) — Limit
  - Valor: String
  - Default: `0`
  - Visible si: `query_type` is `terms`

### Deprecated

- **`bg_color`** (color) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background color
  - Valor: String
- **`bg_image`** (upload) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background image
  - Recommended image width <b>320px - 1920px</b> depending on size of the wrap
  - Valor: String
- **`bg_position`** (select) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background position
  - iOS does <b>not</b> support background-position: fixed<br/>For parallax required background image size is at least 1920px x 1080px
  - Valor: String
  - Opciones: `""` Default · `no-repeat;left top;;` Left Top \| no-repeat · `repeat;left top;;` Left Top \| repeat · `no-repeat;left center;;` Left Center \| no-repeat · `repeat;left center;;` Left Center \| repeat · `no-repeat;left bottom;;` Left Bottom \| no-repeat · `repeat;left bottom;;` Left Bottom \| repeat · `no-repeat;center top;;` Center Top \| no-repeat · `repeat;center top;;` Center Top \| repeat · `repeat-x;center top;;` Center Top \| repeat-x · `repeat-y;center top;;` Center Top \| repeat-y · `no-repeat;center;;` Center Center \| no-repeat · `repeat;center;;` Center Center \| repeat · `no-repeat;center bottom;;` Center Bottom \| no-repeat · `repeat;center bottom;;` Center Bottom \| repeat · `repeat-x;center bottom;;` Center Bottom \| repeat-x · `repeat-y;center bottom;;` Center Bottom \| repeat-y · `no-repeat;right top;;` Right Top \| no-repeat · `repeat;right top;;` Right Top \| repeat · `no-repeat;right center;;` Right Center \| no-repeat · `repeat;right center;;` Right Center \| repeat · `no-repeat;right bottom;;` Right Bottom \| no-repeat · `repeat;right bottom;;` Right Bottom \| repeat · `no-repeat;center top;fixed;;still` Center \| no-repeat \| fixed · `no-repeat;center;fixed;cover;still` Center \| no-repeat \| fixed \| cover · `no-repeat;center top;fixed;cover` Parallax
- **`bg_size`** (select) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background size
  - Does <b>not</b> work with position fixed or parallax
  - Valor: String
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px
- **`move_up`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Move up
  - Move this wrap to overflow on previous section. Does <b>not</b> work with parallax
  - Valor: String
- **`padding`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Padding
  - Use value with <b>px</b> or <b>%</b><br />Example: 20px or 20px 10px 20px 10px or 20px 1%
  - Valor: String
- **`column_margin`** (select) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Elements margin bottom
  - Valor: String
  - Opciones: `""` - Default - · `0px` 0px · `10px` 10px · `20px` 20px · `30px` 30px · `40px` 40px · `50px` 50px
- **`vertical_align`** (select) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Elements vertical align
  - for Section style: <b>Equal height of wraps</b>
  - Valor: String
  - Opciones: `""` Default · `top` Top · `middle` Middle · `bottom` Bottom
- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Wrap classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)
- **`style`** (textarea) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Wrap inline CSS
  - Example: <b>border: 1px solid #999;</b>
  - Valor: String

### Container

- **`query_display`** (switch) — Display
  - Valor: String
  - Opciones: `""` Default · `slider` Slider
- **`query_slider_columns`** (text) — Columns
  - Valor: String
  - Default: `1`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`query_slider_infinity`** (switch) — Infinite loop
  - Valor: String
  - Opciones: `""` Off · `1` On
  - Visible si: `query_display` is `slider`
- **`query_slider_autoplay`** (sliderbar) — Autoplay speed
  - Leave empty to disallow autoplay
  - Valor: Número como string
  - Visible si: `query_display` is `slider`
- **`query_slider_speed`** (sliderbar) — Animation speed
  - Valor: Número como string
  - Visible si: `query_display` is `slider`
- **`query_slider_animation`** (select) — Animation type
  - Valor: String
  - Opciones: `""` Default · `fade` Fade · `cards` Cards · `flip` Flip · `cube` Cube
  - Visible si: `query_display` is `slider`
- **`query_slider_arrows`** (switch) — Arrows
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Visible si: `query_display` is `slider`
- **`query_slider_arrows_style`** (switch) — Arrows style
  - Valor: String
  - Opciones: `""` Standard · `overlay` Overlay · `custom` Custom
  - Visible si: `query_slider_arrows` is `1`
- **`query_slider_arrows_visibility`** (switch) — Arrows visibility
  - Valor: String de tokens separados por espacio, con espacio inicial (ej. `" hide-mobile hide-tablet"`)
  - Opciones: `arrows-hide-desktop` Hide on Desktop · `arrows-hide-laptop` Hide on Laptop · `arrows-hide-tablet` Hide on Tablet · `arrows-hide-mobile` Hide on Mobile
  - Visible si: `query_slider_arrows` is `1`
- **`query_slider_dots`** (switch) — Dots
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Visible si: `query_display` is `slider`
- **`query_slider_dots_style`** (switch) — Dots style
  - Valor: String
  - Opciones: `""` Standard · `overlay` Overlay · `custom` Custom
  - Visible si: `query_slider_dots` is `1`
- **`query_slider_dots_count`** (switch) — Dots count
  - Valor: String
  - Opciones: `""` Standard · `dynamic` Dynamic
  - Visible si: `query_slider_dots` is `1`
- **`query_slider_dots_visibility`** (switch) — Dots visibility
  - Valor: String de tokens separados por espacio, con espacio inicial (ej. `" hide-mobile hide-tablet"`)
  - Opciones: `dots-hide-desktop` Hide on Desktop · `dots-hide-laptop` Hide on Laptop · `dots-hide-tablet` Hide on Tablet · `dots-hide-mobile` Hide on Mobile
  - Visible si: `query_slider_dots` is `1`
- **`query_slider_mousewheel`** (switch) — Mousewheel
  - Valor: String
  - Opciones: `""` Disabled · `1` Enabled
  - Visible si: `query_display` is `slider`
- **`query_slider_linear`** (switch) — Linear mode
  - Linear mode skips setting the number of columns and autoplay speed
  - Valor: String
  - Opciones: `""` Disabled · `1` Enabled
  - Visible si: `query_display` is `slider`
- **`query_display_style`** (switch) — Style
  - Valor: String
  - Opciones: `""` Default · `masonry` Masonry
  - Visible si: `query_display` isnt `slider`
- **`css_queryloop_item_width`** (sliderbar) — Item width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper.mfn-ql-item-default", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` isnt `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Item

- **`css_queryloop_item_min_height`** (text) — Min height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "min-height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_align_content`** (switch) — Vertical align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "align-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Top · `center` Center · `flex-end` Bottom
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_justify_content`** (select) — Horizontal align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Left · `center` Center · `flex-end` Right · `space-around` Space around · `space-between` Space between
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Spacing

- **`css_queryloop_item_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Border

- **`css_queryloop_item_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_queryloop_item_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_ql` isnt `none`
- **`css_queryloop_item_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_ql` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Background

- **`background_switcher_ql`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_query_loop_item_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_ql` is `gradient`
- **`css_queryloop_item_bg_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_ql` is `default`
- **`css_queryloop_item_bg_image`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher_ql` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_bg_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "background-repeat", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `repeat` Repeat · `no-repeat` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y
  - Visible si: `background_switcher_ql` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_bg_position`** (select) — Position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "background-position", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center
  - Visible si: `background_switcher_ql` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_bg_attachment`** (select) — Attachment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "background-attachment", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `scroll` Scroll · `fixed` Fixed · `parallax` Parallax
  - Visible si: `background_switcher_ql` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_bg_size`** (select) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner .mfn-queryloop-item-wrapper", "style": "background-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px
  - Visible si: `background_switcher_ql` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Pagination

- **`css_queryloop_slider_pagination_top`** (text) — Top
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-dots-custom .swiper-pagination", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_dots_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_bottom`** (text) — Bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-dots-custom .swiper-pagination", "style": "bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_dots_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_left`** (text) — Left
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-dots-custom .swiper-pagination", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_dots_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_right`** (text) — Right
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-dots-custom .swiper-pagination", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_dots_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_spacing`** (sliderbar) — Offset
  - Works with Standard and Overlay pagination mode
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .swiper-pagination", "style": "--mfn-swiper-pagination-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_bullet_inactive_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .swiper-pagination .swiper-pagination-bullet", "style": "--swiper-pagination-bullet-inactive-color", "val": "valor"}`
  - Visible si: `query_display` is `slider`
- **`css_queryloop_slider_pagination_bullet_active_color`** (color) — Active color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .swiper-pagination .swiper-pagination-bullet-active", "style": "--mfn-swiper-pagination-bullet-active-color", "val": "valor"}`
  - Visible si: `query_display` is `slider`
- **`css_queryloop_slider_pagination_bullet_width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .swiper-pagination-bullet", "style": "--mfn-swiper-pagination-bullet-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_bullet_height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .swiper-pagination-bullet", "style": "--mfn-swiper-pagination-bullet-height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_bullet_border_radius`** (sliderbar) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .swiper-pagination-bullet", "style": "border-radius", "val": "valor"}`
  - Visible si: `query_display` is `slider`
- **`css_queryloop_slider_pagination_bullet_opacity`** (sliderbar) — Opacity
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .swiper-pagination-bullet", "style": "opacity", "val": "valor"}`
  - Default: `0`
  - Visible si: `query_display` is `slider`

### Arrows


### Prev arrow custom style

- **`css_queryloop_slider_arrow_prev_top`** (text) — Top
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .swiper-button-prev.mfn-swiper-arrow", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_prev_bottom`** (text) — Bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .swiper-button-prev.mfn-swiper-arrow", "style": "bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_prev_left`** (text) — Left
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .swiper-button-prev.mfn-swiper-arrow", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_prev_right`** (text) — Right
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .swiper-button-prev.mfn-swiper-arrow", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Next arrow custom style

- **`css_queryloop_slider_arrow_next_top`** (text) — Top
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .swiper-button-next.mfn-swiper-arrow", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_next_bottom`** (text) — Bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .swiper-button-next.mfn-swiper-arrow", "style": "bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_next_left`** (text) — Left
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .swiper-button-next.mfn-swiper-arrow", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_next_right`** (text) — Right
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .swiper-button-next.mfn-swiper-arrow", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_transformtranslatey`** (sliderbar) — Translate(Y)
  - Moves navigation arrows along the Y-axis by the percent height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .mfn-swiper-arrow", "style": "transformtranslatey", "val": "valor"}`
  - Visible si: `query_slider_arrows_style` is `custom`

### Custom arrows

- **`query_display_slider_arrow_prev`** (icon) — Prev arrow
  - Valor: String
  - Default: `icon-left-open-big`
  - Visible si: `query_display` is `slider`
- **`query_display_slider_arrow_next`** (icon) — Next arrow
  - Valor: String
  - Default: `icon-right-open-big`
  - Visible si: `query_display` is `slider`

### Size

- **`css_queryloop_slider_arrow_width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow", "style": "--mfn-swiper-arrow-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow", "style": "--mfn-swiper-arrow-height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_icon_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow i", "style": "--mfn-swiper-arrow-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_spacing`** (sliderbar) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow", "style": "--mfn-swiper-arrow-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Border

- **`css_queryloop_slider_arrow_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_queryloop_slider_arrow_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_qlarr` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrowbox_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow", "style": "box-shadow", "val": "valor"}`

### Color

- **`css_queryloop_slider_arrow_navigation_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow", "style": "--swiper-navigation-color", "val": "valor"}`
- **`css_queryloop_slider_arrow_bg_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow", "style": "background-color", "val": "valor"}`
- **`css_queryloop_slider_arrow_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_qlarr` isnt `none`
- **`css_queryloop_slider_arrow_navigation_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow:hover", "style": "--swiper-navigation-color", "val": "valor"}`
- **`css_queryloop_slider_arrow_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow:hover", "style": "background-color", "val": "valor"}`
- **`css_queryloop_slider_arrow_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement.mfn-looped-items-slider-wrapper .mfn-swiper-arrow:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_qlarr` isnt `none`

### Dimensions

- **`width_switcher`** (select) — Width
  - Valor: String
  - Opciones: `""` Default · `custom` Custom
- **`css_advanced_flex`** (text) — Width
  - Use px, %, vw, vh or auto to set content width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `wrap_width_switcher` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`height_switcher`** (select) — Height
  - Valor: String
  - Opciones: `""` Default · `custom` Custom
- **`css_advanced_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `wrap_height_switcher` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_min_height`** (text) — Min height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "min-height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_flex_grow`** (select) — Fit container
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement", "style": "flex-grow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `unset` Default · `1` Fit
  - Visible si: `wrap_width_switcher` is ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_flex_wrap`** (select) — Wrap elements
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "flex-wrap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `nowrap` Nowrap · `wrap` Wrap
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Spacing

- **`css_advanced_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Positioning

- **`css_advanced_align_self`** (radio_img) — Wrap position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement", "style": "align-self", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Top · `flex-end` Bottom · `center` Center · `stretch` Stretch
  - Visible si: `wrap_sticky_rwd` isnt `1`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_align_content`** (radio_img) — Wrap content position
  - Works with <b>Stretch</b> only
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "align-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Top · `flex-end` Bottom · `center` Center · `stretch` Stretch · `space-between` Space between · `space-around` Space around · `space-evenly` Space evenly
  - Visible si: `wrap_grid` is ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_align_items`** (radio_img) — Elements vertical align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "align-items", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Top · `flex-end` Bottom · `center` Center · `stretch` Stretch columns
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_justify_content`** (radio_img) — Elements horizontal align
  - Works with flexbox and custom grid template columns
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Left · `center` Center · `flex-end` Right · `space-between` Space between · `space-around` Space around
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_z_index`** (text) — Z-index
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement", "style": "z-index", "val": "valor"}`
- **`css_advanced_order`** (text) — Order
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement", "style": "order", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_position`** (select) — Position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "position", "val": "valor"}`
  - Opciones: `""` Default · `relative` Offset
- **`css_advanced_top`** (text) — Top
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `wrap_position` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_bottom`** (text) — Bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `wrap_position` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_left`** (text) — Left
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `wrap_position` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_right`** (text) — Right
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `wrap_position` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Background

- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_advanced_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher` is `default`
- **`css_advanced_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher` is `gradient`
- **`css_advanced_background_image`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "background-repeat", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `repeat` Repeat · `no-repeat` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y
  - Visible si: `background_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_position`** (select) — Position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "background-position", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center · `custom` Custom
  - Visible si: `background_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_position_v2`** (text) — Custom background position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "background-position_v2", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `bgposopt_rwd` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_attachment`** (select) — Attachment
  - Parallax doesn't work with responsive options
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "background-attachment", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `scroll` Scroll · `fixed` Fixed · `parallax` Parallax
  - Visible si: `background_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_size`** (select) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "background-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px · `custom` Custom
  - Visible si: `background_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_size_v2`** (text) — Custom background size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "background-size_v2", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `custombgsize_rwd` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_backdrop_filter`** (backdrop_filter) — Backdrop filter
  - Doesn't work with animations
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "backdrop-filter", "val": {..., "string": "blur(...) ..."} — solo string se emite}`
- **`css_advanced_transition`** (sliderbar) — Transition duration
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "transition", "val": "valor"}`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_advanced_background_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner:hover", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_hover` is `default`
- **`css_advanced_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover` is `gradient`
- **`css_advanced_background_image_hover`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner:hover", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher_hover` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Background Overlay

- **`css_advanced_background_overlay_opacity`** (sliderbar) — Opacity
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner > .mcb-wrap-background-overlay", "style": "opacity", "val": "valor"}`
  - Default: `0`
- **`background_overlay_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_advanced_background_overlay_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner > .mcb-wrap-background-overlay", "style": "background-color", "val": "valor"}`
  - Visible si: `background_overlay_switcher` is `default`
- **`css_advanced_overlay_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner > .mcb-wrap-background-overlay", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_overlay_switcher` is `gradient`
- **`css_advanced_background_overlay_background_image`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner > .mcb-wrap-background-overlay", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_overlay_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_overlay_background_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner > .mcb-wrap-background-overlay", "style": "background-repeat", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `repeat` Repeat · `no-repeat` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y
  - Visible si: `background_overlay_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_overlay_background_position`** (select) — Position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner > .mcb-wrap-background-overlay", "style": "background-position", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center
  - Visible si: `background_overlay_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_overlay_background_attachment`** (select) — Attachment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner > .mcb-wrap-background-overlay", "style": "background-attachment", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `scroll` Scroll · `fixed` Fixed · `parallax` Parallax
  - Visible si: `background_overlay_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_overlay_background_size`** (select) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner > .mcb-wrap-background-overlay", "style": "background-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px
  - Visible si: `background_overlay_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_overlay_filter`** (css_filters) — CSS Filters
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner > .mcb-wrap-background-overlay", "style": "filter", "val": {..., "string": "blur(...) ..."} — solo string se emite}`
  - Visible si: `background_overlay_switcher` is `default`
- **`css_advanced_background_overlay_transition`** (sliderbar) — Transition duration
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner > .mcb-wrap-background-overlay", "style": "transition", "val": "valor"}`
- **`css_advanced_background_overlay_opacity_hover`** (sliderbar) — Opacity
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner:hover > .mcb-wrap-background-overlay", "style": "opacity", "val": "valor"}`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_advanced_background_overlay_background_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner:hover > .mcb-wrap-background-overlay", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_hover` is `default`
- **`css_advanced_overlay_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner|hover > .mcb-wrap-background-overlay", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover` is `gradient`
- **`css_advanced_background_overlay_background_image_hover`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner:hover > .mcb-wrap-background-overlay", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher_hover` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Border

- **`css_advanced_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_advanced_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_wrap` isnt `none`
- **`css_advanced_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_wrap` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Responsive

- **`visibility`** (switch) — Responsive visibility
  - Valor: String de tokens separados por espacio, con espacio inicial (ej. `" hide-mobile hide-tablet"`)
  - Opciones: `hide-desktop` Hide on Desktop · `hide-laptop` Hide on Laptop · `hide-tablet` Hide on Tablet · `hide-mobile` Hide on Mobile
- **`reverse_order`** (switch) — Order on mobile
  - Valor: String
  - Opciones: 
  - Default: `0`

### Custom

- **`custom-responsive`** (switch) — Custom visibility
  - Valor: String
  - Opciones: `hide` Hide under · `show` Show under
  - Default: `hide`
- **`css_advanced_hide_under`** (sliderbar) — Hide under
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement", "style": "hide_under_custom", "val": "valor"}`
  - Visible si: `custom-responsive` is `hide`
- **`css_advanced_show_under`** (sliderbar) — Show under
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement", "style": "show_under_custom", "val": "valor"}`
  - Visible si: `custom-responsive` is `show`

### Conditional logic

- **`conditional_logic`** (logic) — Conditional logic
  - Valor: String

### Custom

- **`classes`** (pills) — Classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)
- **`custom_id`** (text) — ID
  - Valor: String
- **`custom_css`** (textarea) — Additional CSS
  - Valor: String

### Animation

- **`animate`** (select) — Animation
  - Entrance animation
  - Valor: String
  - Opciones: `""` - Not Animated - · `fadeIn` Fade in · `fadeInUp` Fade in up · `fadeInDown` Fade in down · `fadeInLeft` Fade in left · `fadeInRight` Fade in right · `fadeInUpLarge` Fade in up large · `fadeInDownLarge` Fade in down large · `fadeInLeftLarge` Fade in left large · `fadeInRightLarge` Fade in right large · `zoomIn` Zoom in · `zoomInUp` Zoom in up · `zoomInDown` Zoom in down · `zoomInLeft` Zoom in left · `zoomInRight` Zoom in right · `zoomInUpLarge` Zoom in up large · `zoomInDownLarge` Zoom in down large · `zoomInLeftLarge` Zoom in left large · `bounceIn` Bounce in · `bounceInUp` Bounce in up · `bounceInDown` Bounce in down · `bounceInLeft` Bounce in left · `bounceInRight` Bounce in right
- **`css_advanced_animation_delay`** (sliderbar) — Animation delay
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap-mfnuidelement", "style": "animation-delay", "val": "valor"}`
  - Visible si: `wrap-animate` isnt ``

### Global Wraps

- **`global_wraps_select`** (select) — Select template
  - Valor: String

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*