# `portfolio_slider` — Portfolio Slider

- **Categoría:** loops
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 13

## Campos
- **`count`** (text) — Projects number
  - Valor: String
  - Default: `6`

### Options

- **`category`** (select) — Category
  - Valor: String
- **`category_multi`** (text) — Multiple categories
  - Slugs should be separated with <strong>coma</strong> (,).
  - Valor: String
- **`orderby`** (switch) — Order by
  - Valor: String
  - Opciones: `date` Date · `menu_order` Menu order · `title` Title · `rand` Random
  - Default: `date`
- **`order`** (switch) — Order
  - Valor: String
  - Opciones: `ASC` Ascending · `DESC` Descending
  - Default: `DESC`

### Advanced

- **`arrows`** (switch) — Navigation
  - Valor: String
  - Opciones: `""` Hide · `always` Show · `hover` Show on hover
- **`size`** (switch) — Image size
  - Valor: String
  - Opciones: `small` Small · `medium` Medium · `large` Large
  - Default: `small`
- **`scroll`** (switch) — Slides to scroll
  - Valor: String
  - Opciones: `page` One page · `slide` Single slide
  - Default: `page`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Nav

- **`css_portfolio_slider_nav_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_slider .slider_nav", "style": "background-color", "val": "valor"}`
- **`css_portfolio_slider_nav_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_slider .slider_nav", "style": "color", "val": "valor"}`
- **`css_portfolio_slider_nav_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_slider .slider_nav:hover", "style": "background-color", "val": "valor"}`
- **`css_portfolio_slider_nav_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .portfolio_slider .slider_nav:hover", "style": "color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "portfolio_slider",
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