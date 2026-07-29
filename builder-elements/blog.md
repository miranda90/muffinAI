# `blog` — Blog

- **Categoría:** loops
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 108

## Campos
- **`count`** (text) — Posts number
  - Valor: String
  - Default: `3`
- **`style`** (select) — Style
  - Valor: String
  - Opciones: `classic` Classic - 1 column · `grid` Grid - 2-4 columns · `masonry` Masonry blog style - 2-4 columns · `masonry tiles` Masonry tiles - 2-4 columns · `photo` Photo - 1 column · `photo2` Photo 2 - 1-3 columns · `timeline` Timeline - 1 column
  - Default: `grid`
- **`columns`** (switch) — Columns
  - for style: Grid, Masonry, Photo 2
  - Valor: String
  - Opciones: `2` 2 · `3` 3 · `4` 4 · `5` 5 · `6` 6
  - Default: `3`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h2`
- **`images`** (switch) — Post image
  - for all styles except Masonry tiles
  - Valor: String
  - Opciones: `""` Default · `images-only` Featured images only

### Options

- **`category`** (select) — Category
  - Valor: String
- **`category_multi`** (text) — Multiple categories
  - Slugs should be separated with <b>coma</b> ( , )
  - Valor: String
- **`orderby`** (switch) — Order by
  - Do <b>not</b> use random order with pagination or load more
  - Valor: String
  - Opciones: `date` Date · `title` Title · `rand` Random
  - Default: `date`
- **`order`** (switch) — Order
  - Valor: String
  - Opciones: `DESC` Descending · `ASC` Ascending
  - Default: `DESC`
- **`sticky_posts`** (switch) — Sticky posts
  - Valor: String
  - Opciones: `""` Include · `1` Exclude

### Advanced

- **`exclude_id`** (text) — Exclude posts
  - IDs should be separated with <b>coma</b> ( , )
  - Valor: String
- **`related`** (switch) — Use as related posts
  - Exclude current post on single post page. This option will overwrite exclude posts option above.
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`filters`** (select) — Filters
  - for style: Masonry and category: All<br />Does <b>not</b> work with pagination or load more
  - Valor: String
  - Opciones: `0` Hide · `1` Show · `only-categories` Show only categories · `only-tags` Show only tags · `only-authors` Show only authors
  - Default: `0`
- **`excerpt`** (switch) — Excerpt
  - Valor: String
  - Opciones: 
  - Default: `1`
- **`more`** (switch) — Read more
  - Valor: String
  - Opciones: 
  - Default: `1`

### Pagination

- **`pagination`** (switch) — Pagination
  - Does <b>not</b> work on WMPL homepage
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`load_more`** (switch) — Load more
  - Sliders will be replaced with featured images
  - Valor: String
  - Opciones: 
  - Default: `0`

### Style

- **`greyscale`** (switch) — Grayscale
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`margin`** (switch) — Margin
  - For style: Masonry tiles
  - Valor: String
  - Opciones: 
  - Default: `0`

### Plugins

- **`events`** (switch) — Events
  - for category: All<br />requires free The Events Calendar plugin
  - Valor: String
  - Opciones: 
  - Default: `0`

### Deprecated

- **`margin`** (switch) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Margin
  - for style: Masonry tiles
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Container

- **`css_post-item_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item", "style": "background-color", "val": "valor"}`
- **`css_post-item_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-item_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_post-item_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_blog_item` isnt `none`
- **`css_post-item_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_blog_item` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-item_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Image

- **`css_post-itemimage_frame_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .image_frame", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_post-itemimage_frame_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .image_frame", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_blogitem` isnt `none`
- **`css_post-itemimage_frame_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .image_frame", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_blogitem` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-itemimage_frame_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .image_frame", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Content

- **`css_post-desc_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc", "style": "background-color", "val": "valor"}`
- **`css_post-desc-wrapper_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc-wrapper", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-desc_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Post header

- **`css_post-descpost-head_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head", "style": "background-color", "val": "valor"}`
- **`css_post-descpost-headpost-meta_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head .post-meta", "style": "color", "val": "valor"}`
- **`css_post-descpost-head_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-head_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-head_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_post-descpost-head_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bloghead` isnt `none`
- **`css_post-descpost-head_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_bloghead` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-head_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-head_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-headpost-metaa_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head .post-meta a", "style": "color", "val": "valor"}`
- **`css_post-descpost-headpost-metaahover_color_hover`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-head .post-meta a:hover", "style": "color", "val": "valor"}`

### Title

- **`css_post-descpost-titleentry-titlea_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-title .entry-title a", "style": "color", "val": "valor"}`
- **`css_post-descpost-titleentry-title_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-title .entry-title", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-titleentry-title_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-title .entry-title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Excerpt

- **`css_post-descpost-excerpt_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-excerpt", "style": "color", "val": "valor"}`
- **`css_post-descpost-excerpt_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-excerpt", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-excerpt_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-excerpt", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Post footer

- **`css_post-descpost-footer_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer", "style": "background-color", "val": "valor"}`
- **`css_post_footer_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer .button-love a .label", "style": "color", "val": "valor"}`
- **`css_post-descpost-footer_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-footer_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-footer_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_post-descpost-footer_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_blogpf` isnt `none`
- **`css_post-descpost-footer_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_blogpf` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-footer_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-footer_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-descpost-footera_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer a", "style": "color", "val": "valor"}`
- **`css_post-descpost-footera_color_hover`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-desc .post-footer a:hover", "style": "color", "val": "valor"}`

### Masonry tiles line

- **`css_post-titleafter_background`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .post-title:after", "style": "background", "val": "valor"}`

### Timeline

- **`css_post-itemdate_label_color`** (color) — Date color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .date_label", "style": "color", "val": "valor"}`
- **`css_post-itemdate_label_blog_date_bg`** (color) — Date background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .date_label", "style": "--mfn-blog-date-bg", "val": "valor"}`
- **`css_post-itemdate_label_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item .date_label", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_post-itembefore_border_color`** (color) — Dot color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_wrapper .post-item:before", "style": "border-color", "val": "valor"}`

### Filters


### Nav

- **`css_filters_buttons_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_buttons", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_buttons_background`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_buttons", "style": "background", "val": "valor"}`
- **`css_filters_buttons_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_buttons", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_filters_buttons_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_buttons", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_blog_filters` isnt `none`
- **`css_filters_buttons_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_buttons", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_blog_filters` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_buttons_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_buttons", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_buttonsli_color`** (color) — Label color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_buttons li", "style": "color", "val": "valor"}`
- **`css_filters_buttonsli_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_buttons li", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_filters_buttonslia_color`** (color) — Links color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_buttons li a", "style": "color", "val": "valor"}`
- **`css_filters_buttonslia_color_hover`** (color) — Links color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #Filters .filters_buttons li a:hover", "style": "color", "val": "valor"}`

### Filters

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

### Filters items

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
  "type": "blog",
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