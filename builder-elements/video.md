# `video` — Video

- **Categoría:** elements
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 20

## Campos

### YouTube or Vimeo

- **`video`** (text) — Video ID
  - <b>YouTube:</b> http://www.youtube.com/watch?v=<u>WoJhnRczeNg</u><br /><b>Vimeo:</b> http://vimeo.com/<u>62954028</u>
  - Valor: String
  - Default: `n7-F-FMzM7Q`
- **`parameters`** (text) — Parameters
  - Multiple parameters should be connected with "&"<br />Example: <b>autoplay=1&loop=1</b><br />Notice: Vimeo authors may disable some parameters for their videos
  - Valor: String

### HTML5

- **`mp4`** (upload) — MP4 video
  - Please add both mp4 and ogv for cross-browser compatibility
  - Valor: String
- **`ogv`** (upload) — OGV video
  - Valor: String
- **`placeholder`** (upload) — Placeholder image
  - Placeholder Image will be used as video placeholder before video loads and on mobile devices
  - Valor: String
- **`html5_parameters`** (select) — Parameters
  - WebKit browsers and iOS do not support autoplay
  - Valor: String
  - Opciones: `""` autoplay controls loop muted · `a;c;l;m;i` autoplay controls loop muted playsinline · `a;c;l;` autoplay controls loop · `a;c;l;;i` autoplay controls loop playsinline · `a;c;;m` autoplay controls muted · `a;c;;m;i` autoplay controls muted playsinline · `a;;l;m` autoplay loop muted · `a;;l;m;i` autoplay loop muted playsinline · `a;c;;` autoplay controls · `a;c;;;i` autoplay controls playsinline · `a;;l;` autoplay loop · `a;;l;;i` autoplay loop playsinline · `a;;;m` autoplay muted · `a;;;m;p` autoplay muted playsinline · `a;;;` autoplay · `a;;;;p` autoplay playsinline · `;c;l;m` controls loop muted · `;c;l;m;p` controls loop muted playsinline · `;c;l;` controls loop · `;c;l;;p` controls loop playsinline · `;c;;m` controls muted · `;c;;m;p` controls muted playsinline · `;c;;` controls · `;c;;;p` controls playsinline

### Advanced

- **`css_video_width`** (text) — Width
  - Use px, %, vw, vh or auto to set video width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-video", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_video_height`** (text) — Height
  - Use px, %, vw, vh or auto to set video height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-video", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`object_fit`** (switch) — Style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-video", "style": "object-fit", "val": "valor"}`
  - Opciones: `""` Fit · `cover` Cover
  - Visible si: `video` is ``
- **`object_position`** (select) — Position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-video", "style": "object-position", "val": "valor"}`
  - Opciones: `left top` left top · `center top` center top · `right top` right top · `left center` left center · `center center` center center · `right center` right center · `left bottom` left bottom · `center bottom` center bottom · `right bottom` right bottom
  - Default: `center center`
  - Visible si: `video` is ``

### Mask shape

- **`mask_shape_type`** (select) — Mask type
  - Valor: String
  - Opciones: `0` None · `blob` Blob · `blob-2` Blob 2 · `brush` Brush · `brush-2` Brush 2 · `circle` Circle · `cross` Cross · `irregular-circle` Irregular Circle · `stain` Stain · `triangle` Triangle · `custom` Custom
  - Default: `0`
- **`css_mask_img`** (upload) — Mask image
  - Only SVG type of image works
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape iframe, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape video", "style": "-webkit-mask-image", "val": "valor"}`
  - Visible si: `mask_type` is `custom`
- **`css_content_video-mask-shape_background_color`** (color) — Mask color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape", "style": "background-color", "val": "valor"}`
  - Visible si: `mask_type` isnt `0`
- **`mask_shape_size`** (select) — Size
  - Valor: String
  - Opciones: `auto` Default · `cover` Cover · `contain` Contain · `custom` Custom
  - Default: `contain`
  - Visible si: `mask_type` isnt `0`
- **`css_mask_size`** (sliderbar) — Scale
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape iframe, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape video", "style": "-webkit-mask-size", "val": "valor"}`
  - Visible si: `mask_shape_size` is `custom`
- **`mask_shape_position`** (select) — Position
  - Valor: String
  - Opciones: `center center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center · `custom` Custom
  - Default: `center center`
  - Visible si: `mask_type` isnt `0`
- **`css_mask_pos_x`** (sliderbar) — Position X
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape iframe, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape video", "style": "-webkit-mask-position-x", "val": "valor"}`
  - Visible si: `mask_shape_position` is `custom`
- **`css_mask_pos_y`** (sliderbar) — Position Y
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape iframe, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape video", "style": "-webkit-mask-position-y", "val": "valor"}`
  - Visible si: `mask_shape_position` is `custom`
- **`css_mask_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape iframe, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_video.mfn-mask-shape video", "style": "-webkit-mask-repeat", "val": "valor"}`
  - Opciones: `""` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y · `repeat` Repeat
  - Visible si: `mask_type` isnt `0`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

## Ejemplo mínimo

```json
{
  "type": "video",
  "uid": "itm000001",
  "icon": "video",
  "jsclass": "video",
  "title": "Video",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {
    "video": ""
  }
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*