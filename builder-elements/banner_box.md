# `banner_box` — Banner box

- **Categoría:** boxes
- **Size por defecto:** 1/3 · tablet 1/3 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 117

## Campos

### Box

- **`style`** (switch) — Style
  - Valor: String
  - Opciones: `""` Full · `boxed` Boxed
- **`css_desc_justify`** (switch) — Horizontal position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-desc", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `flex-start` Left · `center` Center · `flex-end` Right
  - Default: `center`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_desc_align`** (switch) — Vertical position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-desc", "style": "align-items", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `flex-start` Top · `center` Center · `flex-end` Bottom
  - Default: `center`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Image

- **`image`** (upload) — Image
  - Valor: String
  - Default: `{theme_uri}/muffin-options/svg/placeholders/image.svg`
- **`size`** (select) — Size
  - Select image size from <a target="_blank" href="options-media.php">Settings > Media > Image sizes</a> (Media Library images only)<br />or use below fields for HTML resize
  - Valor: String
  - Default: `full`
- **`overlay`** (switch) — Overlay
  - Valor: String
  - Opciones: `""` Off · `1` On
- **`hover_effect`** (select) — Hover effect
  - Valor: String
  - Opciones: `""` Default · `toggle` Toggle · `zoom-in` Zoom In · `zoom-out` Zoom Out · `blur` Blur

### Title

- **`title`** (text) — Title
  - Valor: String
  - Default: `This is the title`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h3`

### Subtitle

- **`subtitle`** (text) — Subtitle
  - Valor: String
  - Default: `This is the subtitle`
- **`subtitle_tag`** (switch) — Subtitle tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `p`

### Excerpt

- **`bb_excerpt`** (textarea) — Excerpt
  - Valor: String

### Call To Action

- **`cta`** (select) — CTA type
  - Valor: String
  - Opciones: `""` Text · `icon` Icon · `image` Image
- **`cta_icon`** (icon) — Icon
  - Valor: String
  - Visible si: `cta` is `icon`
- **`cta_image`** (upload) — Image
  - Valor: String
  - Visible si: `cta` is `image`
- **`link_title`** (text) — Call to action
  - Valor: String
  - Default: `Read more`
  - Visible si: `cta` is ``
- **`cta_hover_effect`** (select) — Hover effect
  - Valor: String
  - Opciones: `""` Default · `zoom-in` Zoom In

### Link

- **`link_type`** (select) — On click action
  - Valor: String
  - Opciones: `""` Default · `1` Open popup
- **`popup_id`** (text) — Popup ID
  - Valor: String
  - Visible si: `link_type` is `1`
- **`link`** (text) — Link
  - Valor: String
- **`target`** (select) — Target
  - Valor: String
  - Opciones: `""` Default \| _self · `1` New tab or window \| _blank · `lightbox` Lightbox (image or embed video)
- **`link_title_2`** (text) — Link title
  - Valor: String
  - Default: `Link title`
  - Visible si: `cta` is ``

### Order

- **`order`** (order) — Order
  - Valor: String
  - Default: `title,subtitle,excerpt,divider,cta`

### Responsive

- **`hidden_elements_mobile`** (select) — Hidden elements on mobile
  - Valor: String
  - Opciones: 
  - Default: `0`

### Badge

- **`bb_badge`** (text) — Badge
  - Valor: String

### Box

- **`css_box_offset`** (sliderbar) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "--mfn-banner-box-offset", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_box_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_box_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_bannerbox` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_box_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_box_animation_duration`** (sliderbar) — Transition duration
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "--mfn-banner-box-animation-duration", "val": "valor"}`
- **`css_banner-box_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "background-color", "val": "valor"}`
- **`css_banner-box_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannerbox` isnt `none`
- **`css_banner-box_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover", "style": "background-color", "val": "valor"}`
- **`css_banner-box_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannerbox` isnt `none`

### Image

- **`image_height`** (select) — Height
  - Valor: String
  - Opciones: `""` Auto · `1` Custom
- **`css_banner-box-banner-box-heightbanner-imageimg_height`** (text) — Height
  - Use px, %, vw, vh or auto to set content width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box.mfn-banner-box-height .banner-image img", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `image_height` is `1`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Overlay

- **`css_banner-box-image-overlaybanner-imageafter_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box-image-overlay .banner-image:after", "style": "background-color", "val": "valor"}`
- **`css_banner-box-image-overlayhoverbanner-imageafter_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box-image-overlay:hover .banner-image:after", "style": "background-color", "val": "valor"}`

### Description wrapper

- **`css_banner-box-wrapper_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box.mfn-banner-box-boxed .banner-wrapper", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `60%`
  - Visible si: `style` is `boxed`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_max_width`** (text) — Max width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper", "style": "max-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `100%`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box-wrapper_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box.mfn-banner-box-boxed .banner-wrapper", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
  - Visible si: `style` is `boxed`
- **`css_banner-box-wrapper_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box.mfn-banner-box-boxed .banner-wrapper", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_bannerdesc` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box-wrapper_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box.mfn-banner-box-boxed .banner-wrapper", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `style` is `boxed`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box-wrapper_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box.mfn-banner-box-boxed .banner-wrapper", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `style` is `boxed`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_mfn_banner_box_hidden_content_gap`** (text) — Hidden content gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "--mfn-banner-box-hidden-content-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `15px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box-wrapper_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box.mfn-banner-box-boxed .banner-wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannerdesc` isnt `none`
- **`css_banner-box-wrapper_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box.mfn-banner-box-boxed .banner-wrapper", "style": "background-color", "val": "valor"}`
  - Visible si: `style` is `boxed`
- **`css_banner-box-banner-box-boxedhoverbanner-wrapper_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box.mfn-banner-box-boxed:hover .banner-wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannerdesc` isnt `none`
- **`css_banner-box-boxedhoverbanner-wrapper_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box.mfn-banner-box-boxed.mfn-banner-box-boxed:hover .banner-wrapper", "style": "background-color", "val": "valor"}`
  - Visible si: `style` is `boxed`

### Title

- **`css_banner-box_title_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_title_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .title", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_title_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .title", "style": "color", "val": "valor"}`
- **`css_banner-box_title_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .title", "style": "color", "val": "valor"}`

### Subtitle

- **`css_banner-box_subtitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .subtitle", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_subtitle_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .subtitle", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_subtitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .subtitle", "style": "color", "val": "valor"}`
- **`css_banner-box_subtitle_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .subtitle", "style": "color", "val": "valor"}`

### Excerpt

- **`css_banner-box_excerpt_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .excerpt", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_excerpt_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .excerpt", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_excerpt_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .excerpt", "style": "color", "val": "valor"}`
- **`css_banner-box_excerpt_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .excerpt", "style": "color", "val": "valor"}`

### CTA

- **`css_banner-box_cta-text_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-text", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-text_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-text", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-text_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-text", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-text_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-text", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_banner-box_cta-text_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-text", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_bannercta` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-text_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-text", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-text_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-text", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-text_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-text", "style": "color", "val": "valor"}`
- **`css_banner-box_cta-text_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-text", "style": "background-color", "val": "valor"}`
- **`css_banner-box_cta-text_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-text", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannercta` isnt `none`
- **`css_banner-box_cta-text_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .cta-text", "style": "color", "val": "valor"}`
- **`css_banner-box_cta-text_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .cta-text", "style": "background-color", "val": "valor"}`
- **`css_banner-box_cta-text_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .cta-text", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannercta` isnt `none`

### CTA

- **`css_banner-box_mfn_banner_box_cta_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "--mfn-banner-box-cta-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-icon_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-icon", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-icon_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-icon", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-icon_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-icon", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-icon_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-icon", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_banner-box_cta-icon_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-icon", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_bannericoncta` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-icon_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-icon", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-icon_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-icon", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-icon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-icon", "style": "color", "val": "valor"}`
- **`css_banner-box_cta-icon_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-icon", "style": "background-color", "val": "valor"}`
- **`css_banner-box_cta-icon_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-icon", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannericoncta` isnt `none`
- **`css_banner-box_cta-icon_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .cta-icon", "style": "color", "val": "valor"}`
- **`css_banner-box_cta-icon_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .cta-icon", "style": "background-color", "val": "valor"}`
- **`css_banner-box_cta-icon_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .cta-icon", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannericoncta` isnt `none`

### CTA

- **`css_banner-box_mfn_banner_box_cta_image_width`** (sliderbar) — Image size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "--mfn-banner-box-cta-image-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-image_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-image", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-image_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-image", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-image_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-image", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-image_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-image", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_banner-box_cta-image_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-image", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_bannerimagecta` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-image_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-image", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-image_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-image", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box_cta-image_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-image", "style": "background-color", "val": "valor"}`
- **`css_banner-box_cta-image_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-wrapper .cta-image", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannerimagecta` isnt `none`
- **`css_banner-box_cta-image_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .cta-image", "style": "background-color", "val": "valor"}`
- **`css_banner-box_cta-image_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-wrapper .cta-image", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannerimagecta` isnt `none`

### Badge

- **`bb_badge_pos`** (select) — Position
  - Valor: String
  - Opciones: `""` Top Right · `top-left` Top Left · `bottom-right` Bottom Right · `bottom-left` Bottom Left
- **`css_banner-box_mfn_banner_box_badge_offset`** (sliderbar) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box", "style": "--mfn-banner-box-badge-offset", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box-badge_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-badge", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box-badge_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-badge", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box-badge_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-badge", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_banner-box-badge_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-badge", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_bannerimagecta` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box-badge_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-badge", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box-badge_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-badge", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_banner-box-badge_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-badge", "style": "color", "val": "valor"}`
- **`css_banner-box-badge_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-badge", "style": "background-color", "val": "valor"}`
- **`css_banner-box-badge_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box .banner-badge", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannerimagecta` isnt `none`
- **`css_banner-box-badge_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-badge", "style": "color", "val": "valor"}`
- **`css_banner-box-badge_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-badge", "style": "background-color", "val": "valor"}`
- **`css_banner-box-badge_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-banner-box:hover .banner-badge", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_bannerimagecta` isnt `none`

## Ejemplo mínimo

```json
{
  "type": "banner_box",
  "uid": "itm000001",
  "size": "1/3",
  "tablet_size": "1/3",
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