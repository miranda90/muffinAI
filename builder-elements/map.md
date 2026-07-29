# `map` — Map Advanced

- **Categoría:** elements
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/4 · tablet_resized 0
- **Campos propios:** 31

## Campos
- **`lat`** (text) — Latitude
  - Valor: String
  - Default: `-33.87`
- **`lng`** (text) — Longitude
  - Valor: String
  - Default: `151.21`
- **`info_window`** (textarea) — Info window (optional)
  - Additional information that would appear in Info window on marker click
  - Valor: String
- **`zoom`** (text) — Zoom
  - Valor: String
  - Default: `13`

### Options

- **`type`** (switch) — Type
  - Valor: String
  - Opciones: `ROADMAP` Map · `SATELLITE` Satellite · `HYBRID` Satellite + Map · `TERRAIN` Terrain
  - Default: `ROADMAP`
- **`controls`** (select) — Controls
  - Valor: String
  - Opciones: `""` Zoom · `mapType` Map Type · `streetView` Street View · `zoom mapType` Zoom & Map Type · `zoom streetView` Zoom & Street View · `mapType streetView` Map Type & Street View · `zoom mapType streetView` Zoom, Map Type & Street View · `hide` Hide All
- **`draggable`** (switch) — Draggable
  - Valor: String
  - Opciones: `disable` Disable · `disable-mobile` Disable on mobile · `""` Enable
- **`border`** (switch) — Border
  - Valor: String
  - Opciones: 
  - Default: `0`

### Advanced

- **`icon`** (upload) — Marker icon
  - .png
  - Valor: String
- **`color`** (color) — Map color
  - Valor: String
- **`styles`** (textarea) — Styles
  - You can get predefined styles from <a target="_blank" href="https://snazzymaps.com/explore">snazzymaps.com/explore</a> or generate your own <a target="_blank" href="https://snazzymaps.com/editor">snazzymaps.com/editor</a>
  - Valor: String

### Additional markers

- **`tabs`** (tabs) — Markers
  - Valor: Array de objetos (formato propio del campo tabs)
  - Opciones: `title` ["input", "Title (optional)", ""] · `lat` ["input", "Lat", "-33.88"] · `lng` ["input", "Lng", "151.21"] · `icon` ["input", "Icon URL (optional)", ""] · `content` ["textarea", "Info window (optional)", ""]
  - Default: `[]`

### Contact box

- **`title`** (text) — Title
  - Valor: String
- **`content`** (textarea) — Address
  - HTML tags allowed
  - Valor: String
- **`telephone`** (text) — Telephone
  - Valor: String
- **`email`** (text) — Email
  - Valor: String
- **`www`** (text) — WWW
  - Valor: String
- **`style`** (select) — Style
  - Valor: String
  - Opciones: `box` Box on the map (for full width column/wrap) · `bar` Bar at the top

### Deprecated

- **`height`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Height
  - Valor: String
- **`latlng`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Lat,Lng,IconURL
  - Valor: String
- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Map

- **`css_mcb-column-innergoogle-map_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner .google-map", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Container

- **`css_google-map-contact-wrapperget_in_touch_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .google-map-contact-wrapper .get_in_touch", "style": "background-color", "val": "valor"}`

### Title

- **`css_get_in_touchh3_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch h3", "style": "color", "val": "valor"}`
- **`css_get_in_touchh3_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch h3", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_get_in_touchh3_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch h3", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Icon

- **`css_get_in_touchulliicon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch ul li .icon", "style": "color", "val": "valor"}`

### List

- **`css_get_in_touchget_in_touch_wrapperulli_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch .get_in_touch_wrapper ul li", "style": "color", "val": "valor"}`
- **`css_get_in_touchullia_color`** (color) — Links color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch ul li a", "style": "color", "val": "valor"}`
- **`css_get_in_touchullia_color_hover`** (color) — Links color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch ul li a:hover", "style": "color", "val": "valor"}`

### Lines

- **`css_get_in_touchulli_mfn_contactbox_line`** (color) — Line color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch ul li", "style": "--mfn-contactbox-line", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "map",
  "uid": "itm000001",
  "size": "1/4",
  "tablet_size": "1/4",
  "mobile_size": "1/4",
  "attr": {}
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*