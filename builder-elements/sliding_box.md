# `sliding_box` — Sliding Box

- **Categoría:** boxes
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 13

## Campos
- **`image`** (upload) — Image
  - Recommended image width <b>768px - 1920px</b> depending on size of the item
  - Valor: String
  - Default: `{theme_uri}/muffin-options/svg/placeholders/image.svg`
- **`title`** (text) — Title
  - Allowed HTML tags: span, strong, b, em, i, u
  - Valor: String
  - Default: `This is the title`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h4`

### Link

- **`link`** (text) — Link
  - Valor: String
- **`target`** (select) — Target
  - Valor: String
  - Opciones: `0` Default \| _self · `1` New tab or window \| _blank · `lightbox` Lightbox (image or embed video)
- **`link_title`** (text) — Link title
  - Valor: String

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Title

- **`css_sliding_boxdesc_wrappertitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .sliding_box .desc_wrapper .title", "style": "color", "val": "valor"}`
- **`css_sliding_boxdesc_wrapper_sliding_box_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .sliding_box .desc_wrapper", "style": "--mfn-sliding-box-bg", "val": "valor"}`
- **`css_sliding_boxdesc_wrappertitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .sliding_box .desc_wrapper .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_sliding_boxdesc_wrapper_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .sliding_box .desc_wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Divider

- **`css_sliding_boxdesc_wrapperafter_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .sliding_box .desc_wrapper:after", "style": "background-color", "val": "valor"}`
- **`css_sliding_boxdesc_wrapperafter_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .sliding_box .desc_wrapper:after", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "sliding_box",
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