# `timeline` — Timeline

- **Categoría:** elements
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 17

## Campos
- **`tabs`** (tabs) — Timeline
  - <b>JavaScript</b> content like Google Maps and some plugins shortcodes do <b>not work</b> in tabs
  - Valor: Array de objetos (formato propio del campo tabs)
  - Opciones: `title` ["input", "Title", "Sample event"] · `date` ["input", "Date", "2021"] · `content` ["textarea", "Content", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."]
  - Default: `[{"title": "This is the 1st event", "date": "2021", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."}, {"title": "This is the 2nd event", "date": "2022", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."}]`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Title

- **`css_timeline_itemslih3_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items > li h3", "style": "color", "val": "valor"}`
- **`css_timeline_itemslih3_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items > li h3", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Date

- **`css_timeline_itemslih3span_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li h3 span", "style": "color", "val": "valor"}`
- **`css_timeline_itemslih3_mfn_timeline_date_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li h3", "style": "--mfn-timeline-date-bg", "val": "valor"}`
- **`css_timeline_itemslih3span_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li h3 span", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_timeline_itemslih3span_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li h3 span", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Content

- **`css_timeline_itemslidesc_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li .desc", "style": "color", "val": "valor"}`
- **`css_timeline_itemslidesc_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li .desc", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Dot

- **`css_timeline_itemslih3before_border_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li h3:before", "style": "border-color", "val": "valor"}`

### Placeholder

- **`css_timeline_itemslidescbefore_background_image`** (upload) — Image
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li .desc:before", "style": "background-image", "val": "valor"}`

### Content lines

- **`css_timeline_itemslidesc_text_decoration_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li .desc", "style": "text-decoration-color", "val": "valor"}`
- **`css_timeline_itemslidesc_text_underline_offset`** (text) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li .desc", "style": "text-underline-offset", "val": "valor"}`
- **`css_timeline_itemslidesc_text_decoration_thickness`** (text) — Thickness
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li .desc", "style": "text-decoration-thickness", "val": "valor"}`

### Line

- **`css_timeline_itemslih3lidesc_border_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li h3,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li .desc", "style": "border-color", "val": "valor"}`
- **`css_timeline_itemslihoverh3lihoverdesc_border_color_hover`** (color) — Hover color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li:hover h3,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .timeline_items li:hover .desc", "style": "border-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "timeline",
  "uid": "itm000001",
  "icon": "timeline",
  "jsclass": "timeline",
  "title": "Timeline",
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