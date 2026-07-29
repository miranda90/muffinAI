# `image` — Image

- **Categoría:** typography
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 70

## Campos
- **`src`** (upload) — Image
  - Valor: String
  - Default: `{theme_uri}/muffin-options/svg/placeholders/image.svg`
- **`size`** (select) — Size
  - Select image size from <a target="_blank" href="options-media.php">Settings > Media > Image sizes</a> (Media Library images only)<br />or use below fields for HTML resize
  - Valor: String
  - Default: `full`
- **`stretch`** (select) — Stretch
  - Stretch image to column width, height will be changed proportionally
  - Valor: String
  - Opciones: `0` No · `1` Yes · `ultrawide` Yes, on ultrawide screens only > 1920px

### Lazy load

- **`lazy_load`** (switch) — Lazy load
  - Valor: String
  - Opciones: `""` Default · `disable` Disable · `lazy` Enable

### Link

- **`link_type`** (select) — On click action
  - Valor: String
  - Opciones: `""` Default · `1` Open popup template
- **`popup_id`** (text) — Popup ID
  - Valor: String
  - Visible si: `link_type` is `1`
- **`link_image`** (upload) — Popup image
  - This <b>image or embed video</b> will be opened in lightbox
  - Valor: String
  - Visible si: `link_type` is ``
- **`link`** (text) — Link
  - Valor: String
- **`rel`** (text) — Rel
  - "Rel" attribute to the link
  - Valor: String
- **`target`** (switch) — Target
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`link_title`** (text) — Link title
  - Valor: String
- **`hover`** (switch) — Hover effect
  - Hover effect selected in Theme Options
  - Valor: String
  - Opciones: `disable` Disable · `""` Enable
- **`onclick`** (text) — Onclick
  - Valor: String

### Description

- **`alt`** (text) — Alternate text
  - Valor: String
- **`caption`** (text) — Caption
  - Valor: String

### Mask shape

- **`mask_shape_type`** (select) — Mask type
  - Valor: String
  - Opciones: `0` None · `blob` Blob · `blob-2` Blob 2 · `brush` Brush · `brush-2` Brush 2 · `circle` Circle · `cross` Cross · `irregular-circle` Irregular Circle · `stain` Stain · `triangle` Triangle · `custom` Custom
  - Default: `0`
- **`css_image_mask_bg`** (color) — Mask color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_wrapper", "style": "background-color", "val": "valor"}`
  - Visible si: `mask_type` isnt `0`
- **`css_image_mask_img`** (upload) — Mask image
  - Only SVG type of image works
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame.mfn-mask-shape .image_wrapper img", "style": "-webkit-mask-image", "val": "valor"}`
  - Visible si: `mask_type` is `custom`
- **`mask_shape_size`** (select) — Size
  - Valor: String
  - Opciones: `cover` Cover · `contain` Contain · `custom` Custom
  - Default: `contain`
  - Visible si: `mask_type` isnt `0`
- **`css_image_mask_img_size`** (sliderbar) — Scale
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame.mfn-mask-shape .image_wrapper img", "style": "-webkit-mask-size", "val": "valor"}`
  - Visible si: `mask_shape_size` is `custom`
- **`mask_shape_position`** (select) — Position
  - Valor: String
  - Opciones: `center center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center · `custom` Custom
  - Default: `center center`
  - Visible si: `mask_type` isnt `0`
- **`css_image_mask_img_pos_x`** (sliderbar) — Position X
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame.mfn-mask-shape .image_wrapper img", "style": "-webkit-mask-position-x", "val": "valor"}`
  - Visible si: `mask_shape_position` is `custom`
- **`css_image_mask_img_pos_y`** (sliderbar) — Position Y
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame.mfn-mask-shape .image_wrapper img", "style": "-webkit-mask-position-y", "val": "valor"}`
  - Visible si: `mask_shape_position` is `custom`
- **`css_image_mask_img_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame.mfn-mask-shape .image_wrapper img", "style": "-webkit-mask-repeat", "val": "valor"}`
  - Opciones: `""` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y · `repeat` Repeat
  - Visible si: `mask_type` isnt `0`

### Deprecated

- **`border`** (switch) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Border
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`align`** (switch) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Align
  - If you want image to be <b>resized</b> to column width use <b>align none</b>
  - Valor: String
  - Opciones: `""` None · `left` Left · `center` Center · `right` Right
- **`margin`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Margin top
  - Valor: String
- **`margin_bottom`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Margin bottom
  - Valor: String
- **`width`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Width
  - HTML resize, optional
  - Valor: String
- **`height`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Height
  - Valor: String
- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Image

- **`css_image_frame_width`** (text) — Width
  - Use px, %, vw, vh or auto to set content width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`image_height`** (switch) — Height
  - Valor: String
  - Opciones: `""` Default · `custom` Custom
- **`image_height_style`** (switch) — Style
  - Valor: String
  - Opciones: `""` Fill · `fit` Fit
  - Visible si: `image_height` is `custom`
- **`css_image_cover_height`** (text) — Height value
  - Use px, %, vw, vh or auto to set image height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame.mfn-coverimg .image_wrapper img", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `image_height` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image_text_align`** (switch) — Align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_image_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_imgif` isnt `none`
- **`css_image_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_imgif` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image_border_radius`** (dimensions) — Border radius
  - Doesn't work with keyboard support enabled
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`greyscale`** (switch) — Grayscale
  - Valor: String
  - Opciones: 
  - Default: `0`

### Caption

- **`css_image_caption_text_align`** (switch) — Align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .wp-caption-text", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image_caption_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .wp-caption-text", "style": "color", "val": "valor"}`
- **`css_image_caption_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .wp-caption-text", "style": "background-color", "val": "valor"}`
- **`css_image_caption_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .wp-caption-text", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image_caption_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .wp-caption-text", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image_caption_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .wp-caption-text", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_image_caption_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .wp-caption-text", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_img_capt` isnt `none`
- **`css_image_caption_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .wp-caption-text", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_img_capt` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image_caption_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .wp-caption-text", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image_caption_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .wp-caption-text", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Badge

- **`css_product_onsale_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_product_onsale_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_badge` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_align`** (switch) — Alignment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges", "style": "align-items", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Left · `center` Center · `flex-end` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`product_badge_onsale_position`** (switch) — Position X
  - Valor: String
  - Opciones: `""` Left · `right` Right
- **`css_product_onsale_offset_left`** (sliderbar) — Offset left
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges-left .mfn-product-badges", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `product_badge_onsale_position` is ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_offset_right`** (sliderbar) — Offset right
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges-right .mfn-product-badges", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `product_badge_onsale_position` is `right`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_offset_top`** (sliderbar) — Offset top
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_onsale_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Default label (Sale)

- **`css_product_onsale_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale", "style": "color", "val": "valor"}`
- **`css_product_onsale_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale", "style": "background-color", "val": "valor"}`
- **`css_product_onsale_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_badge` isnt `none`

### Label (New)

- **`css_product_onsale_new_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.mfn-new-badge.onsale", "style": "color", "val": "valor"}`
- **`css_product_onsale_new_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.mfn-new-badge.onsale", "style": "background-color", "val": "valor"}`
- **`css_product_onsale_new_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.mfn-new-badge.onsale", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_badge` isnt `none`

### Extra label

- **`css_product_onsale_extra_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale.onsale-extra-label", "style": "color", "val": "valor"}`
- **`css_product_onsale_extra_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale.onsale-extra-label", "style": "background-color", "val": "valor"}`
- **`css_product_onsale_extra_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-product-badges span.onsale.onsale-extra-label", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_badge` isnt `none`

## Ejemplo mínimo

```json
{
  "type": "image",
  "uid": "itm000001",
  "size": "1/4",
  "tablet_size": "1/4",
  "mobile_size": "1/1",
  "attr": {}
}
```

## Variante shortcode inline (para `content` de column/plain_text/visual)

⚠️ Definición DISTINTA al elemento del builder — solo para el shortcode dentro de texto:
- **`src`** (upload) — Image
  - Valor: String
- **`align`** (switch) — Align
  - Valor: String
  - Opciones: `0` Default · `left` Left · `center` Center · `right` Right
- **`border`** (switch) — Border
  - Valor: String
  - Opciones: 
- **`margin_top`** (text) — Margin Top in px
  - Valor: String
- **`margin_bottom`** (text) — Margin Bottom in px
  - Valor: String
- **`link_image`** (upload) — Image on click
  - Link to image to open after click
  - Valor: String
- **`link`** (text) — Link
  - URL to open on click instead of image url
  - Valor: String
- **`target`** (select) — Target
  - Link target
  - Valor: String
  - Opciones: `0` Default · `_blank` New tab or window
- **`hover`** (switch) — Hover effect
  - Valor: String
  - Opciones: `""` ON · `disable` OFF
- **`alt`** (text) — Alternate text
  - Valor: String
- **`caption`** (text) — Caption
  - Short text under image
  - Valor: String
- **`greyscale`** (switch) — Grayscale
  - Valor: String
  - Opciones: `""` OFF · `1` ON
- **`animate`** (select) — Animation
  - Entrance animation
  - Valor: String
  - Opciones: `""` - Not Animated - · `fadeIn` Fade in · `fadeInUp` Fade in up · `fadeInDown` Fade in down · `fadeInLeft` Fade in left · `fadeInRight` Fade in right · `fadeInUpLarge` Fade in up large · `fadeInDownLarge` Fade in down large · `fadeInLeftLarge` Fade in left large · `fadeInRightLarge` Fade in right large · `zoomIn` Zoom in · `zoomInUp` Zoom in up · `zoomInDown` Zoom in down · `zoomInLeft` Zoom in left · `zoomInRight` Zoom in right · `zoomInUpLarge` Zoom in up large · `zoomInDownLarge` Zoom in down large · `zoomInLeftLarge` Zoom in left large · `bounceIn` Bounce in · `bounceInUp` Bounce in up · `bounceInDown` Bounce in down · `bounceInLeft` Bounce in left · `bounceInRight` Bounce in right

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*