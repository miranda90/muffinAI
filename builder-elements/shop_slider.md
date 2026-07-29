# `shop_slider` — Shop Slider

- **Categoría:** loops
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 78

## Campos
- **`title`** (text) — Title
  - Valor: String
  - Default: `This is the title`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h4`
- **`count`** (text) — Products number
  - Valor: String
  - Default: `5`
- **`show`** (select) — Display
  - Valor: String
  - Opciones: `""` All (or category selected below) · `featured` Featured · `onsale` Onsale · `best-selling` Best Selling (order by: Sales)
- **`out_of_stock`** (switch) — Out of stock products
  - Valor: String
  - Opciones: `hide` Hide · `""` Show
- **`add_to_cart_button`** (switch) — Add to Cart button
  - Valor: String

### Options

- **`category`** (select) — Category
  - Valor: String
- **`orderby`** (switch) — Order by
  - Valor: String
  - Opciones: `date` Date · `title` Title
  - Default: `date`
- **`order`** (switch) — Order
  - Valor: String
  - Opciones: `ASC` Ascending · `DESC` Descending
  - Default: `DESC`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Item title

- **`css_blog_slider_headertitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_slider_header .title", "style": "color", "val": "valor"}`
- **`css_blog_slider_headertitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_slider_header .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_blog_slider_headertitle_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_slider_header .title", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Image

- **`css_shop_slider_ulliimage_frame_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .image_frame", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_shop_slider_ulliimage_frame_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .image_frame", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_sc-img` isnt `none`
- **`css_shop_slider_ulliimage_frame_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .image_frame", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_sc-img` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_slider_ulliimage_frame_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .image_frame", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Content

- **`css_shop_slider_ullidesc_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .desc", "style": "background-color", "val": "valor"}`
- **`css_shop_slider_ullidesc_text_align`** (switch) — Align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .desc", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_slider_ullidesc_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .desc", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_slider_ullidesc_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .desc", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Title

- **`css_shop_slider_ullih4a_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li h4 a", "style": "color", "val": "valor"}`
- **`css_shop_slider_ullih4_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li h4", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_slider_ullih4_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li h4", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Price

- **`css_shop_slider_ulliprice_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .price", "style": "color", "val": "valor"}`
- **`css_shop_slider_ulliprice_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .price", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_slider_ulliprice_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .price", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Regular price

- **`css_shop_slider_ullipricedel_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .price del", "style": "color", "val": "valor"}`
- **`css_shop_slider_ullipricedel_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .shop_slider_ul li .price del", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Arrows

- **`css_shop_sliderbutton_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_sliderbutton_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_sliderbutton_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_shop_sliderbutton_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_shopslider` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_sliderbutton_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_slider_button_icon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button i, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button .button_icon i", "style": "color", "val": "valor"}`
- **`css_shop_sliderbutton_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_shopslider` isnt `none`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_shop_sliderbutton_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_shopslider` is `default`
- **`css_shop_sliderbutton_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_shopslider` is `gradient`
- **`css_shop_sliderbutton_iconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button:hover i, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button:hover .button_icon i", "style": "color", "val": "valor"}`
- **`css_shop_sliderbutton_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_shopslider` isnt `none`
- **`background_switcher_hover_shopslider`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_shop_sliderbutton_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button:hover, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button:before", "style": "background", "val": "valor"}`
  - Visible si: `background_switcher_hover_shopslider` is `default`
- **`css_shop_sliderbutton_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider .button:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover_shopslider` is `gradient`

### Badge

- **`css_product_onsale_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_product_onsale_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_badge` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_align`** (switch) — Alignment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges", "style": "align-items", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Left · `center` Center · `flex-end` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`product_badge_onsale_position`** (switch) — Position X
  - Valor: String
  - Opciones: `""` Left · `right` Right
- **`css_product_onsale_offset_left`** (sliderbar) — Offset left
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges-left li.product .mfn-product-badges", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `product_badge_onsale_position` is ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_offset_right`** (sliderbar) — Offset right
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges-right li.product .mfn-product-badges", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `product_badge_onsale_position` is `right`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_offset_top`** (sliderbar) — Offset top
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Default label (Sale)

- **`css_product_onsale_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale", "style": "color", "val": "valor"}`
- **`css_product_onsale_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale", "style": "background-color", "val": "valor"}`
- **`css_product_onsale_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_badge` isnt `none`

### Label (New)

- **`css_product_onsale_new_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.mfn-new-badge.onsale", "style": "color", "val": "valor"}`
- **`css_product_onsale_new_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.mfn-new-badge.onsale", "style": "background-color", "val": "valor"}`
- **`css_product_onsale_new_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.mfn-new-badge.onsale", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_badge` isnt `none`

### Extra label

- **`css_product_onsale_extra_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale.onsale-extra-label", "style": "color", "val": "valor"}`
- **`css_product_onsale_extra_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale.onsale-extra-label", "style": "background-color", "val": "valor"}`
- **`css_product_onsale_extra_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li.product .mfn-product-badges span.onsale.onsale-extra-label", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_badge` isnt `none`

### Button

- **`css_shop_sliderlidescbutton_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_sliderlidescbutton_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_sliderlidescbutton_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_shop_sliderlidescbutton_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_ssb` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_sliderlidescbutton_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_shop_sliderlidescbutton_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button", "style": "color", "val": "valor"}`
- **`css_shop_sliderlidescbutton_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_ssb` isnt `none`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_shop_sliderlidescbutton_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher` is `default`
- **`css_shop_sliderlidescbutton_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher` is `gradient`
- **`css_shop_sliderlidescbutton_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button:hover", "style": "color", "val": "valor"}`
- **`css_shop_sliderlidescbutton_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_ssb` isnt `none`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_shop_sliderlidescbutton_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button:hover, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button:before", "style": "background", "val": "valor"}`
  - Visible si: `background_switcher_hover` is `default`
- **`css_shop_sliderlidescbutton_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .shop_slider li .desc .button:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover` is `gradient`

## Ejemplo mínimo

```json
{
  "type": "shop_slider",
  "uid": "itm000001",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {
    "title": "This is the title"
  }
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*