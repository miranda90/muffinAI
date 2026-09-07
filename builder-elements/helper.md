# `helper` — Helper

- **Categoría:** blocks
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 25

## Campos
- **`title`** (text) — Title
  - Valor: String
  - Default: `This is the title`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h4`

### Item 1

- **`title1`** (text) — Title
  - Valor: String
  - Default: `This is the 1st item title`
- **`content1`** (textarea) — Content
  - Some shortcodes and HTML tags allowed
  - Valor: String
  - Default: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.`
- **`link1`** (text) — Link
  - Use if you want to link to another page instead of showing the content
  - Valor: String
- **`link_type`** (select) — On click action
  - Valor: String
  - Opciones: `""` Default · `1` Open popup
- **`popup_id`** (text) — Popup ID
  - Valor: String
  - Visible si: `link_type` is `1`
- **`target1`** (switch) — Link target
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`class1`** (text) — Link class
  - e.g. <b>prettyphoto</b> or <b>scroll</b>
  - Valor: String

### Item 2

- **`title2`** (text) — Title
  - Valor: String
- **`content2`** (textarea) — Content
  - Some shortcodes and HTML tags allowed
  - Valor: String
- **`link2`** (text) — Link
  - Use if you want to link to another page instead of showing the content
  - Valor: String
- **`link_type_2`** (select) — On click action
  - Valor: String
  - Opciones: `""` Default · `1` Open popup
- **`popup_id_2`** (text) — Popup ID
  - Valor: String
  - Visible si: `link_type_2` is `1`
- **`target2`** (switch) — Link target
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`class2`** (text) — Link class
  - e.g. <b>prettyphoto</b> or <b>scroll</b>
  - Valor: String

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Title

- **`css_helper_headertitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .helper_header .title", "style": "color", "val": "valor"}`
- **`css_helper_headertitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .helper_header .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Button

- **`css_helper_headerlink_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .helper_header .links .link", "style": "color", "val": "valor"}`
- **`css_helper_headerlink_background`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .helper_header .links .link", "style": "background", "val": "valor"}`
- **`css_headerlink_helper_color_active_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .helper_header .links .link:hover,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .helper_header .links .link.active", "style": "color", "val": "valor"}`
- **`css_headerlink_helper_background_active_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .helper_header .links .link:hover,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .helper_header .links .link.active", "style": "background", "val": "valor"}`

### Content

- **`css_helper_contentitem_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .helper_content .item", "style": "color", "val": "valor"}`
- **`css_helper_contentitem_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .helper_content .item", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "helper",
  "uid": "itm000001",
  "icon": "helper",
  "jsclass": "helper",
  "title": "Helper",
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