# `zoom_box` — Zoom Box

- **Categoría:** boxes
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 21

## Campos
- **`image`** (upload) — Image
  - Recommended image width <b>768px - 1920px</b> depending on size of the item
  - Valor: String
  - Default: `{theme_uri}/muffin-options/svg/placeholders/image.svg`
- **`content_image`** (upload) — Content image
  - Valor: String
- **`content`** (textarea) — Content
  - Valor: String
  - Default: `Lorem ipsum dolor`

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
  - Opciones: `0` Default \| _self · `1` New tab or window \| _blank · `lightbox` Lightbox (image or embed video)
- **`link_title`** (text) — Link title
  - Valor: String

### Deprecated

- **`bg_color`** (color) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Overlay background
  - Valor: String
- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Overlay

- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_zoom_boxdesc_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .zoom_box .desc", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_zoom` is `default`
- **`css_zoom_boxdesc_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .zoom_box .desc", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_zoom` is `gradient`
- **`css_zoom_boxdesc_background_image`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .zoom_box .desc", "style": "background-image", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `background_switcher_zoom` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_zoom_boxdesc_background_repeat`** (select) — Repeat
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .zoom_box .desc", "style": "background-repeat", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `repeat` Repeat · `no-repeat` No repeat · `repeat-x` Repeat X · `repeat-y` Repeat Y
  - Visible si: `background_switcher_zoom` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_zoom_boxdesc_background_position`** (select) — Position
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .zoom_box .desc", "style": "background-position", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `center` Center Center · `center left` Center Left · `center right` Center Right · `top left` Top Left · `top right` Top Right · `top center` Top Center · `bottom left` Bottom Left · `bottom right` Bottom Right · `bottom center` Bottom Center
  - Visible si: `background_switcher_zoom` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_zoom_boxdesc_background_attachment`** (select) — Attachment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .zoom_box .desc", "style": "background-attachment", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `scroll` Scroll · `fixed` Fixed
  - Visible si: `background_switcher_zoom` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_zoom_boxdesc_background_size`** (select) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .zoom_box .desc", "style": "background-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px
  - Visible si: `background_switcher_zoom` is `default`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Content

- **`css_zoom_boxdescdesc_txt_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .zoom_box .desc .desc_txt", "style": "color", "val": "valor"}`
- **`css_zoom_boxdescdesc_txt_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .zoom_box .desc .desc_txt", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_zoom_boxdescdesc_txt_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .zoom_box .desc .desc_txt", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "zoom_box",
  "uid": "itm000001",
  "size": "1/4",
  "tablet_size": "1/4",
  "mobile_size": "1/1",
  "attr": {
    "content": "Lorem ipsum dolor"
  }
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*