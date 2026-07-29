# Campos de SECCIÓN

Campos disponibles en `attr` de cada sección.


### Header options

- **`scroll-visibility`** (switch) — Scroll visibility
  - Sections hidden on the scroll should be at the top of the header. It takes effect with fixed type of Header
  - Valor: String
  - Opciones: `show` Default · `hide` Hide
  - Default: `show`
- **`closeable`** (switch) — Closeable
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`closeable-time`** (text) — Show again after
  - How many days should it stay hidden after closing?
  - Valor: String
  - Default: `0`
  - Visible si: `closable-field` is `1`
- **`closeable-x`** (switch) — Close button position
  - Valor: String
  - Opciones: `left` Left · `right` Right
  - Default: `left`
  - Visible si: `closable-field` is `1`
- **`css_closeable_icon_color`** (color) — Close icon color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .close-closeable-section .icon", "style": "color", "val": "valor"}`
  - Visible si: `closable-field` is `1`
- **`title`** (text) — Title
  - Label in admin panel only
  - Valor: String

### Type

- **`type`** (switch) — Type
  - Query loop displays section&apos;s content in designed loop
  - Valor: String
  - Opciones: `""` Default · `query` Query loop
- **`query_type`** (select) — Query type
  - Valor: String
  - Opciones: `""` Select · `posts` Posts · `terms` Terms
  - Visible si: `section_type` is `query`
- **`query_post_type`** (select) — Post type
  - Valor: String
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
- **`query_post_pagination`** (select) — Pagination
  - Valor: String
  - Opciones: `""` Hidden · `numbers` Numbers + links · `dots` Dots + links · `prevnext` Prev / Next links · `loadmore` Load more · `infiniteload` Infinite load
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

### Style

- **`style`** (checkbox_pseudo) — Style
  - <strong>Notice!</strong> Options grayed out and marked with OLD tag are deprecated and will be removed in the future. Please use <a href="https://support.muffingroup.com/documentation/muffin-live-builder/positioning/" target="_blank">Positioning</a> instead.
  - Valor: String
  - Opciones: `no-margin-h` Columns \| remove horizontal margin · `no-margin-v` Columns \| remove vertical margin · `dark` Dark · `full-width-ex-mobile` Full Width \| except mobile · `highlight-left` Highlight \| left · `highlight-right` Highlight \| right<span>in highlight section please use two 1/2 wraps</span> · `full-screen` Full Screen · `full-width` Full Width · `equal-height` Equal Height \| items in wrap · `equal-height-wrap` Equal Height \| wraps

### Shape divider

- **`shape_divider_type_top`** (select) — Type
  - Valor: String
  - Opciones: `""` None · `arc_opacity_1` Arc Opacity · `arc_opacity_2` Arc Opacity 2 · `arrow_1` Arrow · `blobs_1` Blobs · `blobs_2` Blobs 2 · `book_1` Book · `christmas_trees_1` Christmas Trees · `clouds_1` Clouds · `clouds_2` Clouds 2 · `curve_1` Curve · `curve_corner_opacity_1` Curve Corner Opacity · `curve_asymmetrical_1` Curve Asymmetrical · `crazy_waves_1` Crazy Waves · `gradient_opacity_1` Gradient Opacity · `hexagons_opacity_1` Hexagons Opacity · `hills_1` Hills · `hills_opacity_1` Hills Opacity · `mountains_1` Mountains · `mountains_2` Mountains 2 · `spikes_opacity_1` Spikes Opacity · `split_1` Split · `tilt_opacity_1` Tilt Opacity · `tilt_opacity_2` Tilt Opacity 2 · `triangle_1` Triangle · `triangle_asymmetrical_1` Triangle Asymmetrical · `tilt` Tilt · `waves_1` Waves · `waves_opacity_1` Waves Opacity · `waves_opacity_2` Waves Opacity 2 · `waves_opacity_3` Waves Opacity 3 · `waves_opacity_4` Waves Opacity 4
  - Default: `0`
- **`css_shape_divider_top_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-shape-divider-top svg", "style": "--mfn-shape-divider", "val": "valor"}`
  - Visible si: `shape_divider_type_top` isnt `0`
- **`css_shape_divider_top_width`** (sliderbar) — Width %
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-shape-divider-top svg", "style": "width", "val": "valor"}`
  - Visible si: `shape_divider_type_top` isnt `0`
- **`css_shape_divider_top_height`** (sliderbar) — Height px
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-shape-divider-top svg", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `shape_divider_type_top` isnt `0`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`shape_divider_flip_top`** (switch) — Flip
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Visible si: `shape_divider_type_top` isnt `0`
- **`shape_divider_invert_top`** (switch) — Invert
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Visible si: `shape_divider_type_top` is `arrow_1,book_1,curve_1,curve_asymmetrical_1,split_1,triangle_1,triangle_asymmetrical_1,waves_1`
- **`shape_divider_bring_front_top`** (switch) — Bring to front
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Visible si: `shape_divider_type_top` isnt `0`
- **`shape_divider_type_bottom`** (select) — Type
  - Valor: String
  - Opciones: `""` None · `arc_opacity_1` Arc Opacity · `arc_opacity_2` Arc Opacity 2 · `arrow_1` Arrow · `blobs_1` Blobs · `blobs_2` Blobs 2 · `book_1` Book · `christmas_trees_1` Christmas Trees · `clouds_1` Clouds · `clouds_2` Clouds 2 · `curve_1` Curve · `curve_corner_opacity_1` Curve Corner Opacity · `curve_asymmetrical_1` Curve Asymmetrical · `crazy_waves_1` Crazy Waves · `gradient_opacity_1` Gradient Opacity · `hexagons_opacity_1` Hexagons Opacity · `hills_1` Hills · `hills_opacity_1` Hills Opacity · `mountains_1` Mountains · `mountains_2` Mountains 2 · `spikes_opacity_1` Spikes Opacity · `split_1` Split · `tilt_opacity_1` Tilt Opacity · `tilt_opacity_2` Tilt Opacity 2 · `triangle_1` Triangle · `triangle_asymmetrical_1` Triangle Asymmetrical · `tilt` Tilt · `waves_1` Waves · `waves_opacity_1` Waves Opacity · `waves_opacity_2` Waves Opacity 2 · `waves_opacity_3` Waves Opacity 3 · `waves_opacity_4` Waves Opacity 4
  - Default: `0`
- **`css_shape_divider_bottom_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-shape-divider-bottom svg", "style": "--mfn-shape-divider", "val": "valor"}`
  - Visible si: `shape_divider_type_bottom` isnt `0`
- **`css_shape_divider_bottom_width`** (sliderbar) — Width %
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-shape-divider-bottom svg", "style": "width", "val": "valor"}`
  - Visible si: `shape_divider_type_bottom` isnt `0`
- **`css_shape_divider_bottom_height`** (sliderbar) — Height px
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-shape-divider-bottom svg", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `shape_divider_type_bottom` isnt `0`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`shape_divider_flip_bottom`** (switch) — Flip
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Visible si: `shape_divider_type_bottom` isnt `0`
- **`shape_divider_invert_bottom`** (switch) — Invert
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Visible si: `shape_divider_type_bottom` is `arrow_1,book_1,curve_1,curve_asymmetrical_1,split_1,triangle_1,triangle_asymmetrical_1,waves_1`
- **`shape_divider_bring_front_bottom`** (switch) — Bring to front
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Visible si: `shape_divider_type_bottom` isnt `0`

### Background decoration

- **`divider`** (select) — Pattern
  - Please select background color in Advanced tab<br />Does <b>not</b> work with parallax and some section styles
  - Valor: String
  - Opciones: `""` None · `circle up` Circle up · `square up` Square up · `triangle up` Triangle up · `triple-triangle up` Triple triangle up · `circle down` Circle down · `square down` Square down · `triangle down` Triangle down · `triple-triangle down` Triple triangle down
- **`decor_top`** (upload) — Image top
  - for images from <b> Media library</b><br/>Recommended width: 1920px
  - Valor: String
- **`decor_bottom`** (upload) — Image bottom
  - for images from <b> Media library</b><br/>Recommended width: 1920px
  - Valor: String

### Options

- **`navigation`** (select) — Navigation
  - Valor: String
  - Opciones: `""` None · `arrows` Arrows
- **`hide`** (text) — Hide
  - Valor: String
- **`collapse`** (text) — Collapse
  - Valor: String

### Deprecated

- **`bg_color`** (color) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background color
  - Valor: String
- **`bg_image`** (upload) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background image
  - Recommended image size <b>1920px x 1080px</b>
  - Valor: String
- **`bg_position`** (select) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background position
  - iOS does <b>not</b> support background-position: fixed<br/>For parallax required background image size is at least 1920px x 1080px
  - Valor: String
  - Opciones: `""` Default · `no-repeat;left top;;` Left Top \| no-repeat · `repeat;left top;;` Left Top \| repeat · `no-repeat;left center;;` Left Center \| no-repeat · `repeat;left center;;` Left Center \| repeat · `no-repeat;left bottom;;` Left Bottom \| no-repeat · `repeat;left bottom;;` Left Bottom \| repeat · `no-repeat;center top;;` Center Top \| no-repeat · `repeat;center top;;` Center Top \| repeat · `repeat-x;center top;;` Center Top \| repeat-x · `repeat-y;center top;;` Center Top \| repeat-y · `no-repeat;center;;` Center Center \| no-repeat · `repeat;center;;` Center Center \| repeat · `no-repeat;center bottom;;` Center Bottom \| no-repeat · `repeat;center bottom;;` Center Bottom \| repeat · `repeat-x;center bottom;;` Center Bottom \| repeat-x · `repeat-y;center bottom;;` Center Bottom \| repeat-y · `no-repeat;right top;;` Right Top \| no-repeat · `repeat;right top;;` Right Top \| repeat · `no-repeat;right center;;` Right Center \| no-repeat · `repeat;right center;;` Right Center \| repeat · `no-repeat;right bottom;;` Right Bottom \| no-repeat · `repeat;right bottom;;` Right Bottom \| repeat · `no-repeat;center top;fixed;;still` Center \| no-repeat \| fixed · `no-repeat;center;fixed;cover;still` Center \| no-repeat \| fixed \| cover · `no-repeat;center top;fixed;cover` Parallax
- **`bg_size`** (select) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background size
  - Does <b>not</b> work with position fixed or parallax
  - Valor: String
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px
- **`padding_top`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Padding top
  - Valor: String
- **`padding_bottom`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Padding bottom
  - Valor: String
- **`padding_horizontal`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Padding left & right
  - Use <b>px</b> or <b>%</b>
  - Valor: String
- **`visibility`** (select) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Responsive visibility
  - Valor: String
  - Opciones: `""` - Default - · `hide-desktop` Hide on Desktop \| 960px + · `hide-tablet` Hide on Tablet \| 768px - 959px · `hide-mobile` Hide on Mobile \| - 768px · `hide-desktop hide-tablet` Hide on Desktop & Tablet · `hide-desktop hide-mobile` Hide on Desktop & Mobile · `hide-tablet hide-mobile` Hide on Tablet & Mobile
- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Section classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)
- **`section_id`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Section ID
  - Use this option to create One Page sites<br />Example: Your <b>Section ID</b> is <b>offer</b> and you want to open this section, please use link: <b>your-url/#offer</b>
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
- **`css_queryloop_slider_pagination_transformtranslatex`** (sliderbar) — Translate(X)
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-dots-custom .mcb-section-inner .swiper-pagination", "style": "transformtranslatex", "val": "valor"}`
  - Visible si: `query_slider_dots_style` is `custom`
- **`query_slider_mousewheel`** (switch) — Mousewheel
  - Valor: String
  - Opciones: `""` Disabled · `1` Enabled
  - Visible si: `query_display` is `slider`
- **`query_slider_centered`** (switch) — Center mode
  - Valor: String
  - Opciones: `""` Disabled · `2` Wrapper offset
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
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper.mfn-ql-item-default", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` isnt `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Item

- **`css_queryloop_item_min_height`** (text) — Min height
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "min-height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_align_content`** (switch) — Vertical align
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "align-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Top · `center` Center · `flex-end` Bottom
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_justify_content`** (select) — Horizontal align
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Left · `center` Center · `flex-end` Right · `space-around` Space around · `space-between` Space between
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Spacing

- **`css_queryloop_item_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Border

- **`css_queryloop_item_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_queryloop_item_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_ql` isnt `none`
- **`css_queryloop_item_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_ql` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Background

- **`background_switcher_ql`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_query_loop_item_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_ql` is `gradient`
- **`css_queryloop_item_bg_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_ql` is `default`
- **`css_queryloop_item_bg_image`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher_ql` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_bg_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "background-repeat", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `repeat` Repeat · `no-repeat` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y
  - Visible si: `background_switcher_ql` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_bg_position`** (select) — Position
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "background-position", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center
  - Visible si: `background_switcher_ql` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_bg_attachment`** (select) — Attachment
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "background-attachment", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `scroll` Scroll · `fixed` Fixed · `parallax` Parallax
  - Visible si: `background_switcher_ql` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_item_bg_size`** (select) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-section-inner .mfn-queryloop-item-wrapper", "style": "background-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px
  - Visible si: `background_switcher_ql` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Slider dots

- **`css_queryloop_slider_pagination_top`** (text) — Top
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-dots-custom .mcb-section-inner .swiper-pagination", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_dots_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_bottom`** (text) — Bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-dots-custom .mcb-section-inner .swiper-pagination", "style": "bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_dots_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_left`** (text) — Left
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-dots-custom .mcb-section-inner .swiper-pagination", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_dots_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_right`** (text) — Right
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-dots-custom .mcb-section-inner .swiper-pagination", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_dots_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_spacing`** (sliderbar) — Offset
  - Works with Standard and Overlay pagination mode
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .swiper-pagination", "style": "--mfn-swiper-pagination-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_bullet_width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .swiper-pagination-bullet", "style": "--mfn-swiper-pagination-bullet-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_bullet_height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .swiper-pagination-bullet", "style": "--mfn-swiper-pagination-bullet-height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_pagination_bullet_border_radius`** (sliderbar) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .swiper-pagination-bullet", "style": "border-radius", "val": "valor"}`
  - Visible si: `query_display` is `slider`
- **`css_queryloop_slider_pagination_bullet_opacity`** (sliderbar) — Opacity
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .swiper-pagination-bullet", "style": "opacity", "val": "valor"}`
  - Default: `0`
  - Visible si: `query_display` is `slider`
- **`css_queryloop_slider_pagination_bullet_inactive_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .swiper-pagination .swiper-pagination-bullet", "style": "--swiper-pagination-bullet-inactive-color", "val": "valor"}`
  - Visible si: `query_display` is `slider`
- **`css_queryloop_slider_pagination_bullet_active_color`** (color) — Active color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .swiper-pagination .swiper-pagination-bullet-active", "style": "--mfn-swiper-pagination-bullet-active-color", "val": "valor"}`
  - Visible si: `query_display` is `slider`

### Arrows


### Prev arrow custom style

- **`css_queryloop_slider_arrow_prev_top`** (text) — Top
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .mcb-section-inner .swiper-button-prev.mfn-swiper-arrow", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_prev_bottom`** (text) — Bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .mcb-section-inner .swiper-button-prev.mfn-swiper-arrow", "style": "bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_prev_left`** (text) — Left
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .mcb-section-inner .swiper-button-prev.mfn-swiper-arrow", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_prev_right`** (text) — Right
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .mcb-section-inner .swiper-button-prev.mfn-swiper-arrow", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Next arrow custom style

- **`css_queryloop_slider_arrow_next_top`** (text) — Top
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .mcb-section-inner .swiper-button-next.mfn-swiper-arrow", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_next_bottom`** (text) — Bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .mcb-section-inner .swiper-button-next.mfn-swiper-arrow", "style": "bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_next_left`** (text) — Left
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .mcb-section-inner .swiper-button-next.mfn-swiper-arrow", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_next_right`** (text) — Right
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .mcb-section-inner .swiper-button-next.mfn-swiper-arrow", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_slider_arrows_style` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_transformtranslatey`** (sliderbar) — Translate(Y)
  - Moves navigation arrows along the Y-axis by the percent height
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper.mfn-arrows-custom .mcb-section-inner .mfn-swiper-arrow", "style": "transformtranslatey", "val": "valor"}`
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
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow", "style": "--mfn-swiper-arrow-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow", "style": "--mfn-swiper-arrow-height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_icon_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow i", "style": "--mfn-swiper-arrow-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_spacing`** (sliderbar) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow", "style": "--mfn-swiper-arrow-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `query_display` is `slider`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Border

- **`css_queryloop_slider_arrow_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_queryloop_slider_arrow_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_qlarr` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_slider_arrow_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow", "style": "box-shadow", "val": "valor"}`

### Color

- **`css_queryloop_slider_arrow_navigation_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow", "style": "--swiper-navigation-color", "val": "valor"}`
- **`css_queryloop_slider_arrow_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow", "style": "background-color", "val": "valor"}`
- **`css_queryloop_slider_arrow_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_qlarr` isnt `none`
- **`css_queryloop_slider_arrow_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow:hover", "style": "--swiper-navigation-color", "val": "valor"}`
- **`css_queryloop_slider_arrow_bg_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow:hover", "style": "background-color", "val": "valor"}`
- **`css_queryloop_slider_arrow_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.mfn-looped-items-slider-wrapper .mcb-section-inner .mfn-swiper-arrow:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_qlarr` isnt `none`

### Pagination


### Container

- **`css_queryloop_pagination_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination", "style": "background-color", "val": "valor"}`
- **`css_queryloop_pagination_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_pagination_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Items

- **`css_queryloop_pagination_numbers_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers", "style": "gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_pagination_numbers_min_width`** (sliderbar) — Min width
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers li .page-numbers", "style": "min-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_pagination_numbers_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers .page-numbers", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_pagination_numbers_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers .page-numbers", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_queryloop_pagination_numbers_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers .page-numbers", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_pag` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_pagination_numbers_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers .page-numbers", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_queryloop_pagination_numbers_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers li .page-numbers", "style": "--mfn-pagination-items-color", "val": "valor"}`
- **`css_queryloop_pagination_numbers_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers li .page-numbers", "style": "background-color", "val": "valor"}`
- **`css_queryloop_pagination_numbers_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers .page-numbers", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_pag` isnt `none`
- **`css_queryloop_pagination_numbers_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers a.page-numbers:hover", "style": "--mfn-pagination-items-color", "val": "valor"}`
- **`css_queryloop_pagination_numbers_bg_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers a.page-numbers:hover", "style": "background-color", "val": "valor"}`
- **`css_queryloop_pagination_numbers_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers .page-numbers:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_pag` isnt `none`
- **`css_queryloop_pagination_numbers_color_active`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers li .current", "style": "--mfn-pagination-items-color", "val": "valor"}`
- **`css_queryloop_pagination_numbers_bg_active`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers li .current", "style": "background-color", "val": "valor"}`
- **`css_queryloop_pagination_numbers_border_color_active`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mfn-query-pagination ul.page-numbers li .current", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_pag` isnt `none`

### Dimensions

- **`width_switcher`** (select) — Width
  - Valor: String
  - Opciones: `""` Default · `full` Full width · `custom` Custom
- **`css_advanced_max_width`** (text) — Custom width
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement.custom-width .section_wrapper", "style": "max-width", "val": "valor"}`
  - Visible si: `sect_width_switcher` is `custom`
- **`height_switcher`** (select) — Height
  - Valor: String
  - Opciones: `""` Default · `full-screen` Full screen · `custom` Custom
- **`css_advanced_height`** (text) — Custom height
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `sect_height_switcher` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Spacing

- **`css_advanced_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Positioning

- **`css_advanced_align_content`** (radio_img) — Section content position
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .section_wrapper", "style": "align-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Top · `flex-end` Bottom · `center` Center
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_align_items`** (radio_img) — Wraps vertical spacing
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .section_wrapper", "style": "align-items", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `flex-start` Top · `flex-end` Bottom · `center` Center · `stretch` Stretch
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_justify_content`** (radio_img) — Horizontal align
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .section_wrapper", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `flex-start` Left · `center` Center · `flex-end` Right · `space-between` Space between · `space-around` Space around
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_z_index`** (text) — Z-index
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "z-index", "val": "valor"}`

### Background

- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `video` Video · `gradient` Gradient
  - Default: `default`
- **`css_advanced_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher` is `gradient`
- **`css_advanced_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher` is `default`
- **`css_advanced_background_image`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`bg_video_mp4`** (upload) — Video MP4
  - Image will be used as placeholder before video loads and on mobile devices
  - Valor: String
  - Visible si: `background_switcher` is `video`
- **`bg_video_dots`** (switch) — Video dotted overlay
  - It hides the pixelation of lower-resolution video but slightly darkens it
  - Valor: String
  - Opciones: `hide` Hide · `""` Show
  - Visible si: `background_switcher` is `video`
- **`css_advanced_background_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "background-repeat", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `repeat` Repeat · `no-repeat` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y
  - Visible si: `background_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_position`** (select) — Position
  - Doesn't work with Attachment / Parallax
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "background-position", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center · `custom` Custom
  - Visible si: `background_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_position_v2`** (text) — Custom background position
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "background-position_v2", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `bgposopt_rwd` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_attachment`** (select) — Attachment
  - Parallax doesn't work with responsive options
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "background-attachment", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `scroll` Scroll · `fixed` Fixed · `parallax` Parallax
  - Visible si: `background_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_size`** (select) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "background-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px · `custom` Custom
  - Visible si: `background_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_size_v2`** (text) — Custom background size
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "background-size_v2", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `custombgsize` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_backdrop_filter`** (backdrop_filter) — Backdrop filter
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "backdrop-filter", "val": {..., "string": "blur(...) ..."} — solo string se emite}`
- **`css_advanced_transition`** (sliderbar) — Transition duration
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "transition", "val": "valor"}`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_advanced_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover` is `gradient`
- **`css_advanced_background_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement:hover", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_hover` is `default`
- **`css_advanced_background_image_hover`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement:hover", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher_hover` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_header_transition`** (sliderbar) — Transition duration
  - Valor: Objeto CSS: `{"selector": ".mfn-header-tmpl .mcb-section-mfnuidelement", "style": "transition", "val": "valor"}`
- **`background_switcher_scroll`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_header_scrolled_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mfn-header-scrolled .mfn-header-tmpl .mcb-section-mfnuidelement", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_scroll` is `gradient`
- **`css_advanced_scrolled_header_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mfn-header-scrolled .mfn-header-tmpl .mcb-section-mfnuidelement", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_scroll` is `default`
- **`css_advanced_scrolled_header_background_image`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mfn-header-scrolled .mfn-header-tmpl .mcb-section-mfnuidelement", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher_scroll` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Background overlay

- **`css_advanced_background_overlay_opacity`** (sliderbar) — Opacity
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "opacity", "val": "valor"}`
  - Default: `0`
- **`background_overlay_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_advanced_overlay_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_overlay_switcher` is `gradient`
- **`css_advanced_background_overlay_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "background-color", "val": "valor"}`
  - Visible si: `background_overlay_switcher` is `default`
- **`css_advanced_background_overlay_background_image`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_overlay_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_overlay_background_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "background-repeat", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `repeat` Repeat · `no-repeat` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y
  - Visible si: `background_overlay_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_overlay_background_position`** (select) — Position
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "background-position", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center
  - Visible si: `background_overlay_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_overlay_background_attachment`** (select) — Attachment
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "background-attachment", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `scroll` Scroll · `fixed` Fixed · `parallax` Parallax
  - Visible si: `background_overlay_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_overlay_background_size`** (select) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "background-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px
  - Visible si: `background_overlay_switcher` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_background_overlay_filter`** (css_filters) — CSS Filters
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "filter", "val": {..., "string": "blur(...) ..."} — solo string se emite}`
  - Visible si: `background_overlay_switcher` is `default`
- **`css_advanced_background_overlay_transition`** (sliderbar) — Transition duration
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "transition", "val": "valor"}`
- **`css_advanced_background_overlay_opacity_hover`** (sliderbar) — Opacity
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement:hover .mcb-background-overlay", "style": "opacity", "val": "valor"}`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_advanced_overlay_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement:hover .mcb-background-overlay", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover` is `gradient`
- **`css_advanced_background_overlay_background_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement:hover .mcb-background-overlay", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_hover` is `default`
- **`css_advanced_background_overlay_background_image_hover`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement:hover .mcb-background-overlay", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher_hover` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Border

- **`css_advanced_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_advanced_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_sect` isnt `none`
- **`css_advanced_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_sect` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_advanced_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section-mfnuidelement", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Responsive

- **`visibility`** (switch) — Responsive visibility
  - Valor: String de tokens separados por espacio, con espacio inicial (ej. `" hide-mobile hide-tablet"`)
  - Opciones: `hide-desktop` Hide on Desktop · `hide-laptop` Hide on Laptop · `hide-tablet` Hide on Tablet · `hide-mobile` Hide on Mobile
- **`reverse_order`** (switch) — Order on mobile
  - Valor: String
  - Opciones: 
  - Default: `0`

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

### Global Section

- **`global_sections_select`** (select) — Select template
  - Valor: String

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*