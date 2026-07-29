# `clients` — Clients

- **Categoría:** loops
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 14

## Campos
- **`in_row`** (text) — Items in row
  - Recommended: 3-6
  - Valor: String
  - Default: `6`
- **`style`** (switch) — Style
  - Valor: String
  - Opciones: `""` Default · `tiles` Tiles
- **`size`** (select) — Image size
  - Select image size from <a target="_blank" href="options-media.php">Settings > Media > Image sizes</a> (Media Library images only).<br />Does <b>not</b> work for SVG images.
  - Valor: String
  - Opciones: `be_clients` Default \| 150px x 55px · `full` Full size · `large` Large \| Array · `medium` Medium \| Array · `thumbnail` Thumbnail \| Array
  - Default: `be_clients`

### Options

- **`category`** (select) — Category
  - Valor: String
- **`orderby`** (switch) — Order by
  - Valor: String
  - Opciones: `date` Date · `menu_order` Menu order · `title` Title · `rand` Random
  - Default: `menu_order`
- **`order`** (switch) — Order
  - Valor: String
  - Opciones: `DESC` Descending · `ASC` Ascending
  - Default: `ASC`

### Advanced

- **`greyscale`** (switch) — Grayscale
  - Valor: String
  - Opciones: 
  - Default: `0`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Container

- **`css_ulclientsliclient_wrapper_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.clients li .client_wrapper", "style": "height", "val": "valor"}`
- **`css_ulclientsliclient_wrapper_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.clients li .client_wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ulclientsliclient_wrapper_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.clients li .client_wrapper", "style": "background-color", "val": "valor"}`
- **`css_ulclientsliclient_wrapper_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.clients li .client_wrapper:hover", "style": "background-color", "val": "valor"}`

### Style tiles

- **`css_ulclientsclients_tiles_mfn_clients_tiles`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.clients.clients_tiles", "style": "--mfn-clients-tiles", "val": "valor"}`
- **`css_ulclientsclients_tiles_clients_tiles_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul.clients.clients_tiles", "style": "--mfn-clients-tiles-hover", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "clients",
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