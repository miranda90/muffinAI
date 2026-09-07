# `before_after` — Before After

- **Categoría:** boxes
- **Size por defecto:** 1/3 · tablet 1/3 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 9

## Campos

### Image

- **`image_before`** (upload) — Before
  - Recommended image width <b>768px - 1920px</b> depending on size of the item
  - Valor: String
  - Default: `{theme_uri}/muffin-options/svg/placeholders/image.svg`
- **`image_after`** (upload) — After
  - Both images <b>must have the same size</b>
  - Valor: String
  - Default: `{theme_uri}/muffin-options/svg/placeholders/image.svg`
- **`size`** (select) — Size
  - Select image size from <a target="_blank" href="options-media.php">Settings > Media > Image sizes</a> (Media Library images only)<br />or use below fields for HTML resize
  - Valor: String
  - Default: `full`

### Label

- **`label_before`** (text) — Before
  - Valor: String
- **`label_after`** (text) — After
  - Valor: String

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Slider

- **`css_twentytwenty-wrapper_before_after_slider`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .twentytwenty-wrapper", "style": "--mfn-before-after-slider", "val": "valor"}`

### Label

- **`css_twentytwenty-wrapper_mfn_before_after_label`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .twentytwenty-wrapper", "style": "--mfn-before-after-label", "val": "valor"}`
- **`css_twentytwenty-wrapper_before_after_label_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .twentytwenty-wrapper", "style": "--mfn-before-after-label-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "before_after",
  "uid": "itm000001",
  "icon": "before_after",
  "jsclass": "before_after",
  "title": "Before After",
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