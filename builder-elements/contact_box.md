# `contact_box` — Contact Box

- **Categoría:** elements
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 18

## Campos
- **`title`** (text) — Title
  - Valor: String
  - Default: `This is the title`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h3`
- **`address`** (textarea) — Address
  - HTML tags allowed
  - Valor: String
  - Default: `This is the address`
- **`telephone`** (text) — Phone
  - Valor: String
- **`telephone_2`** (text) — Second phone
  - Valor: String
- **`fax`** (text) — Fax
  - Valor: String
- **`email`** (text) — Email
  - Valor: String
- **`www`** (text) — WWW
  - Valor: String

### Deprecated

- **`image`** (upload) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background image
  - Recommended image width <b>768px - 1920px</b> depending on size of the item
  - Valor: String
- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Item title

- **`css_get_in_touchtitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch .title", "style": "color", "val": "valor"}`
- **`css_get_in_touchtitle_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch .title", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_get_in_touchtitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .get_in_touch .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
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
  "type": "contact_box",
  "uid": "itm000001",
  "icon": "contact_box",
  "jsclass": "contact_box",
  "title": "Contact Box",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {
    "title": "Título de ejemplo"
  }
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*