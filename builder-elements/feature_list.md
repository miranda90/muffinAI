# `feature_list` — Feature List

- **Categoría:** elements
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 13

## Campos
- **`tabs`** (tabs) — Items
  - Valor: Array de objetos (formato propio del campo tabs)
  - Opciones: `title` ["input", "Title", "List item"] · `icon` ["icon", "Icon", "icon-lamp"] · `link` ["input", "Link", ""] · `target` ["input", "Target", ""] · `animate` ["input", "Animate", ""]
  - Default: `[{"title": "This is the 1st item", "icon": "icon-book", "link": "", "target": "", "animate": ""}, {"title": "This is the 2nd item", "icon": "icon-bucket", "link": "", "target": "", "animate": ""}]`
- **`content`** (textarea) — Content
  - Valor: String
- **`columns`** (switch) — Columns
  - Valor: String
  - Opciones: `2` 2 · `3` 3 · `4` 4 · `5` 5 · `6` 6
  - Default: `4`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Container

- **`css_feature_listullip_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li p", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_feature_listullifeature_listullia_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li a", "style": "background-color", "val": "valor"}`
- **`css_feature_listullifeature_listullia_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li a", "style": "color", "val": "valor"}`
- **`css_feature_listullihoverfeature_listullihovera_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li:hover,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li:hover a", "style": "background-color", "val": "valor"}`
- **`css_feature_listullihoverfeature_listullihovera_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li:hover,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li:hover a", "style": "color", "val": "valor"}`

### Icon

- **`css_feature_listulliiconi_font_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li .icon i", "style": "font-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_feature_listulliiconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li .icon i", "style": "color", "val": "valor"}`
- **`css_feature_listulliiconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list ul li:hover .icon i", "style": "color", "val": "valor"}`

### Line

- **`css_feature_listhr_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .feature_list hr", "style": "background-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "feature_list",
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