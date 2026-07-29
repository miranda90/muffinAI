# `portfolio` — Portfolio

- **Categoría:** loops
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 88

## Campos
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h5`
- **`count`** (text) — Projects number
  - Valor: String
  - Default: `3`
- **`style`** (select) — Style
  - Valor: String
  - Opciones: `flat` Flat · `grid` Grid · `masonry` Masonry blog style · `masonry-hover` Masonry hover description · `masonry-minimal` Masonry minimal · `masonry-flat` Masonry flat · `list` List · `exposure` Exposure
  - Default: `grid`
- **`columns`** (switch) — Columns
  - for styles: Flat, Grid, Masonry blog style, Masonry hover description
  - Valor: String
  - Opciones: `2` 2 · `3` 3 · `4` 4 · `5` 5 · `6` 6
  - Default: `3`

### Options

- **`category`** (select) — Category
  - Valor: String
- **`category_multi`** (text) — Multiple categories
  - Slugs should be separated with <b>coma</b> ( , )
  - Valor: String
- **`orderby`** (switch) — Order by
  - Do <b>not</b> use random order with pagination or load more
  - Valor: String
  - Opciones: `date` Date · `menu_order` Menu order · `title` Title · `rand` Random
  - Default: `date`
- **`order`** (switch) — Order
  - Valor: String
  - Opciones: `ASC` Ascending · `DESC` Descending
  - Default: `DESC`

### Advanced

- **`portfolio-link`** (select) — Project link
  - Valor: String
  - Opciones: `""` Default (from Theme Options) · `details` Details · `popup` Popup Image · `disable` Disable Details \| Only Popup Image · `_self` Project Website \| Open in the same window · `_blank` Project Website \| Open in new window
- **`exclude_id`** (text) — Exclude posts
  - IDs should be separated with <b>coma</b> ( , )
  - Valor: String
- **`related`** (switch) — Use as related projects
  - Exclude current project on single project page. This option will overwrite exclude posts option above.
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`filters`** (switch) — Filters
  - for category: all or multiple categories (only selected categories show in filters)
  - Valor: String
  - Opciones: 
  - Default: `0`

### Pagination

- **`pagination`** (switch) — Pagination
  - Does <b>not</b> work on WMPL homepage
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`load_more`** (switch) — Load More button
  - Sliders will be replaced with featured images. Please use with pagination enabled.
  - Valor: String
  - Opciones: 
  - Default: `0`

### Style

- **`excerpt_hide`** (switch) — Excerpt
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Visible si: `style` is `['masonry', 'masonry-hover', 'list', 'exposure']`
- **`greyscale`** (switch) — Grayscale
  - Valor: String
  - Opciones: 
  - Default: `0`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Container

- **`css_portfolio-item_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item", "style": "background-color", "val": "valor"}`
- **`css_portfolio-item_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-item_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_portfolio-item_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_portfolio` isnt `none`
- **`css_portfolio-item_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_portfolio` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-item_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Image

- **`css_portfolio-itemimage_frame_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .image_frame", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_portfolio-itemimage_frame_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .image_frame", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_portfolio_img` isnt `none`
- **`css_portfolio-itemimage_frame_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .image_frame", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_portfolio_img` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-itemimage_frame_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .image_frame", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Content

- **`css_portfolio-itemdesc_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .desc", "style": "background-color", "val": "valor"}`
- **`css_portfolio-itemdesc_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .desc", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-itemdesc_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .desc", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Title

- **`css_title_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": "body .mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .entry-title a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .entry-title", "style": "color", "val": "valor"}`
- **`css_portfolio-itementry-title_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .entry-title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Excerpt

- **`css_portfolio-itemdesc-wrapper_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .desc-wrapper", "style": "color", "val": "valor"}`
- **`css_portfolio-itemdesc-wrapper_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .desc-wrapper", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Icons

- **`css_portfolio-itemai_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item a i", "style": "color", "val": "valor"}`
- **`css_portfolio-itemai_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item a:hover i", "style": "color", "val": "valor"}`

### Masonry hover

- **`css_masonry_portfolio-item_desc_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group.masonry-hover .portfolio-item .masonry-hover-wrapper .hover-desc", "style": "background-color", "val": "valor"}`
- **`css_masonry_portfolio-item_desch3after_background_hover`** (color) — Decoration
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group.masonry-hover .portfolio-item .masonry-hover-wrapper .hover-desc h3:after", "style": "background", "val": "valor"}`

### Meta

- **`css_details_wrapper_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .details-wrapper,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .details-wrapper h5", "style": "color", "val": "valor"}`
- **`css_portfolio-itemdetails-wrappera_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .details-wrapper a", "style": "color", "val": "valor"}`
- **`css_meta_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .details-wrapper,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .details-wrapper .column", "style": "border-color", "val": "valor"}`
- **`css_portfolio-itemdetails-wrapper_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .details-wrapper", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Exposure

- **`css_portfolio-itemdesc-innerline_background_color`** (color) — Line
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .desc-inner .line", "style": "background-color", "val": "valor"}`

### Button

- **`css_portfolio-itemlist__headerlinks_wrapperbutton_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-itemlist__headerlinks_wrapperbutton_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-itemlist__headerlinks_wrapperbutton_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_portfolio-itemlist__headerlinks_wrapperbutton_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_portfolio-itemlist__headerlinks_wrapperbutton_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button i", "style": "color", "val": "valor"}`
- **`css_portfolio-itemlist__headerlinks_wrapperbutton_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style` isnt `none`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_portfolio-itemlist__headerlinks_wrapperbutton_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher` is `default`
- **`css_portfolio-itemlist__headerlinks_wrapperbutton_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher` is `gradient`
- **`css_button_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button:hover,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button:hover i", "style": "color", "val": "valor"}`
- **`css_portfolio-itemlist__headerlinks_wrapperbuttonhover_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style` isnt `none`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_portfolio-itemlist__headerlinks_wrapperbuttonhover_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button:hover,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button:before", "style": "background", "val": "valor"}`
  - Visible si: `background_switcher_hover` is `default`
- **`css_portfolio-itemlist__headerlinks_wrapperbutton_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_group .portfolio-item .list_style_header .links_wrapper .button:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover` is `gradient`

### Filters


### Container

- **`css_filters_wrapper_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_wrapper_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_wrapper_background`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper", "style": "background", "val": "valor"}`
- **`css_filters_wrapper_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_filters_wrapper_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_blog_filters_wrapper` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_wrapper_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Items

- **`css_filters_wrapperli_width`** (select) — Items width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li", "style": "width", "val": "valor"}`
  - Opciones: `""` Default · `auto` Auto
- **`css_filters_wrapperlia_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_wrapperli_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_wrapperlia_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li a", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_filters_wrapperlia_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li a", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_blog_filters_wrapper_li` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_wrapperlia_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li a", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_wrapperli_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_wrapperlia_color`** (color) — Links color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li a", "style": "color", "val": "valor"}`
- **`css_filters_wrapperlia_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li a", "style": "background-color", "val": "valor"}`
- **`css_filters_wrapperlia_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_blog_filters_wrapper_li` isnt `none`
- **`css_filters_wrapperlia_color_hover`** (color) — Links color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li a:hover", "style": "color", "val": "valor"}`
- **`css_filters_wrapperlia_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li a:hover", "style": "background-color", "val": "valor"}`
- **`css_filters_wrapperlia_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li a:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_blog_filters_wrapper_li` isnt `none`
- **`css_filters_wrapperlicurrent-cata_color`** (color) — Links color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.current-cat a", "style": "color", "val": "valor"}`
- **`css_filters_wrapperlicurrent-cata_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.current-cat a", "style": "background-color", "val": "valor"}`
- **`css_filters_wrapperlicurrent-cata_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.current-cat a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_blog_filters_wrapper_li` isnt `none`

### Filters exit

- **`css_filters_wrapperliclosea_width`** (select) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.close a", "style": "width", "val": "valor"}`
  - Opciones: `""` Default · `auto` Auto
- **`css_filters_wrapperliclosea_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.close a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_wrapperliclosea_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.close a", "style": "color", "val": "valor"}`
- **`css_filters_wrapperliclosea_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.close a", "style": "background-color", "val": "valor"}`
- **`css_filters_wrapperliclosea_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.close a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_blog_filters_wrapper_li` isnt `none`
- **`css_filters_wrapperliclosea_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.close a:hover", "style": "color", "val": "valor"}`
- **`css_filters_wrapperliclosea_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.close a:hover", "style": "background-color", "val": "valor"}`
- **`css_filters_wrapperliclosea_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_wrapper li.close a:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_blog_filters_wrapper_li` isnt `none`

## Ejemplo mínimo

```json
{
  "type": "portfolio",
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