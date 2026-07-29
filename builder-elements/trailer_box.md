# `trailer_box` — Trailer Box

- **Categoría:** boxes
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 21

## Campos
- **`image`** (upload) — Image
  - Recommended image width <b>768px - 1920px</b> depending on size of the item
  - Valor: String
  - Default: `{theme_uri}/muffin-options/svg/placeholders/image.svg`
- **`orientation`** (switch) — Image orientation
  - Valor: String
  - Opciones: `""` Vertical · `horizontal` Horizontal
- **`slogan`** (text) — Slogan
  - Valor: String
  - Default: `This is the slogan`
- **`title`** (text) — Title
  - Valor: String
  - Default: `This is the title`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h2`

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

### Advanced

- **`style`** (switch) — Style
  - Valor: String
  - Opciones: `""` Default · `plain` Plain

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Slogan

- **`css_trailer_boxdescsubtitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .trailer_box .desc .subtitle", "style": "color", "val": "valor"}`
- **`css_trailer_boxdescsubtitle_background`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .trailer_box .desc .subtitle", "style": "background", "val": "valor"}`
- **`css_trailer_boxdescsubtitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .trailer_box .desc .subtitle", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_trailer_boxdescsubtitle_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .trailer_box .desc .subtitle", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Title

- **`css_trailer_boxdesctitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .trailer_box .desc .title", "style": "color", "val": "valor"}`
- **`css_trailer_boxdesctitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .trailer_box .desc .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_trailer_boxdesctitle_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .trailer_box .desc .title", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Content

- **`css_simpletrailer_boxdesc_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".style-simple .mcb-section .mcb-wrap .mcb-item-mfnuidelement .trailer_box:hover .desc", "style": "background-color", "val": "valor"}`

### Line

- **`css_trailer_boxdescline_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .trailer_box .desc .line", "style": "background-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "trailer_box",
  "uid": "itm000001",
  "size": "1/4",
  "tablet_size": "1/4",
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