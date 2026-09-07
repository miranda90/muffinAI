# `image_gallery` — Image Gallery

- **Categoría:** typography
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 24

## Campos
- **`ids`** (upload_multi) — Images
  - Valor: IDs de adjuntos separados por coma (ej. `"12,45,88"`)

### Options

- **`size`** (select) — Size
  - Valor: String
  - Default: `full`
- **`style`** (switch) — Style
  - Valor: String
  - Opciones: `""` Default · `flat` Flat · `fancy` Fancy · `masonry` Masonry
- **`layout`** (switch) — Layout
  - Valor: String
  - Opciones: `""` Equal columns · `1` Equal heights
  - Visible si: `style` isnt `masonry`
- **`columns`** (text) — Columns
  - min: <b>1</b> \| max: <b>9</b>
  - Valor: String
  - Default: `3`
  - Visible si: `layout` is ``

### Advanced

- **`greyscale`** (switch) — Grayscale
  - Valor: String
  - Opciones: 
  - Default: `0`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Image

- **`image_height`** (switch) — Height
  - Valor: String
  - Opciones: `""` Default · `mfn_custom_img_height` Custom
- **`css_gallery_custom_img_heightimage_frameimage_wrapperimg_mfn_gal_img_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery.mfn_custom_img_height .image_frame .image_wrapper img", "style": "--mfn-gal-img-height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `300px`
  - Visible si: `image_height` is `mfn_custom_img_height`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_galleryequal-heightsimage_frameimage_wrapperimg_mfn_gal_img_max_width`** (sliderbar) — Max width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery.equal-heights .image_frame .image_wrapper img", "style": "--mfn-gal-img-max-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `300px`
  - Visible si: `layout` is `1`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_galleryimage_frame_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .image_frame", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_galleryimage_frame_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .image_frame", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_ig` isnt `none`
- **`css_galleryimage_frame_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .image_frame", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_ig` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_galleryimage_frame_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .image_frame", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_galleryimage_frame_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .image_frame", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Caption

- **`css_gallerygallery-itemgallery-caption_display`** (switch) — Visibility
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .gallery-item .gallery-caption", "style": "display", "val": "valor"}`
  - Opciones: `""` Visible · `none` Hidden
- **`image_caption_style`** (switch) — Style
  - Valor: String
  - Opciones: `""` Default · `img_caption_overlay` Overlay
  - Visible si: `image_caption` is ``
- **`css_gallerygallery-itemgallery-caption_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .gallery-item .gallery-caption", "style": "background-color", "val": "valor"}`
  - Visible si: `image_caption` is ``
- **`css_gallerygallery-itemgallery-caption_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .gallery-item .gallery-caption", "style": "color", "val": "valor"}`
  - Visible si: `image_caption` is ``
- **`css_gallerygallery-itemgallery-caption_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .gallery-item .gallery-caption", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_gallerygallery-itemgallery-caption_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .gallery-item .gallery-caption", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_gallerygallery-itemgallery-caption_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .gallery-item .gallery-caption", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Item

- **`css_gallerygallery-item_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .gallery-item", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_gallerygallery-item_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .gallery .gallery-item", "style": "background-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "image_gallery",
  "uid": "itm000001",
  "icon": "image_gallery",
  "jsclass": "image_gallery",
  "title": "Image Gallery",
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