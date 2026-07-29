# `tabs` — Tabs

- **Categoría:** blocks
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 26

## Campos
- **`title`** (text) — Title
  - Valor: String
  - Default: `This is the title`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h4`

### Tabs

- **`tabs`** (tabs) — Tabs
  - <b>JavaScript</b> content like Google Maps and some plugins shortcodes do <b>not work</b> in tabs. You can use Drag & Drop to set the order
  - Valor: Array de objetos (formato propio del campo tabs)
  - Opciones: `title` ["input", "Title", "Sample tab"] · `content` ["textarea", "Content", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."]
  - Default: `[{"title": "This is the 1st tab", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."}, {"title": "This is the 2nd tab", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."}]`

### Options

- **`type`** (switch) — Style
  - Valor: String
  - Opciones: `horizontal` Horizontal · `centered` Centered · `vertical` Vertical
  - Default: `horizontal`

### Custom

- **`uid`** (text) — Unique ID [optional]
  - Use if you want to open specified tab from link (does not work on the same page).<br />For example: Your Unique ID is <b>offer</b> and you want to open 2nd tab, please use link: <b>your-url/#offer-2</b>
  - Valor: String

### Deprecated

- **`padding`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Content padding
  - Use value with <b>px</b> or <b>%</b><br />Example: <b>20px</b> or <b>15px 20px 20px</b> or <b>20px 1%</b>
  - Valor: String
  - Default: `20px`
- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Title

- **`css_title_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_title_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "color", "val": "valor"}`
- **`css_title_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_title_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Container

- **`css_tabs_wrapper_mfn_tabs_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .tabs_wrapper", "style": "--mfn-tabs-border-color", "val": "valor"}`
- **`css_tabs_wrapper_mfn_tabs_border_width`** (sliderbar) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .tabs_wrapper", "style": "--mfn-tabs-border-width", "val": "valor"}`
- **`css_tabs_wrapper_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .tabs_wrapper", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Title bar

- **`css_tabs_wrapperui-tabs-nav_background`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .tabs_wrapper .ui-tabs-nav", "style": "background", "val": "valor"}`

### Title tab

- **`css_tabs_wrapperullia_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .tabs_wrapper ul li a", "style": "color", "val": "valor"}`
- **`css_tabs_wrapperullia_background`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .tabs_wrapper ul li a", "style": "background", "val": "valor"}`
- **`css_tabs_wrapperulliui-state-activea_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .tabs_wrapper ul li.ui-state-active a", "style": "color", "val": "valor"}`
- **`css_tabs_wrapperulliui-state-activea_background`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .tabs_wrapper ul li.ui-state-active a", "style": "background", "val": "valor"}`
- **`css_ui-tabsui-tabs-navliui-state-aafter_background_active`** (color) — Line
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .ui-tabs .ui-tabs-nav li.ui-state-active a:after", "style": "background", "val": "valor"}`
- **`css_tabs_wrapperullia_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .tabs_wrapper ul li a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_tabs_wrapperullia_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .tabs_wrapper ul li a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Content

- **`css_ui-tabsui-tabs-panel_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .ui-tabs .ui-tabs-panel", "style": "color", "val": "valor"}`
- **`css_ui-tabs-nav-li-ui-state-after_background_active`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .ui-tabs .ui-tabs-panel,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .ui-tabs .ui-tabs-nav li.ui-state-active:after", "style": "background", "val": "valor"}`
- **`css_ui-tabsui-tabs-panel_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .ui-tabs .ui-tabs-panel", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ui-tabsui-tabs-panel_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .ui-tabs .ui-tabs-panel", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "tabs",
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