# `tag_cloud` — Tag cloud

- **Categoría:** blocks
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 18

## Campos
- **`category`** (select) — Taxonomy
  - Valor: String
  - Default: `category`
- **`reference`** (select) — Reference
  - Valor: String
  - Opciones: `""` All items · `not_empty` Not empty items · `post` Current post terms
- **`orderby`** (select) — Order by
  - Valor: String
  - Opciones: `""` Default · `name` Name · `count` Count
  - Visible si: `reference` isnt `post`
- **`order`** (select) — Order
  - Valor: String
  - Opciones: `""` DESC · `asc` ASC
  - Visible si: `reference` isnt `post`
- **`design`** (select) — Design
  - Valor: String
  - Opciones: `""` Simple list · `pills` Pills

### Item

- **`css_tag-cloud_justify_content`** (select) — Align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Left · `center` Center · `flex-end` Right · `space-between` Space between · `space-around` Space around
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_tag-cloud_mfn_tag_cloud_offset`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud", "style": "--mfn-tag-cloud-offset", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_tag-cloudlia_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud li a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_tag-cloud-pillslia_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud.mfn-tag-cloud-pills li a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Visible si: `design` is `pills`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_tag-cloud-pillslia_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud.mfn-tag-cloud-pills li a", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
  - Visible si: `design` is `pills`
- **`css_tag-cloud-pillslia_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud.mfn-tag-cloud-pills li a", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_tags` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_tag-cloud-pillslia_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud.mfn-tag-cloud-pills li a", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `design` is `pills`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_tag-cloudlia_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud li a", "style": "color", "val": "valor"}`
- **`css_tag-cloudlia_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud li a", "style": "background-color", "val": "valor"}`
  - Visible si: `design` is `pills`
- **`css_tag-cloudlia_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud li a", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_tags` isnt `none`
- **`css_tag-cloudlia_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud li a:hover", "style": "color", "val": "valor"}`
- **`css_tag-cloudlia_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud li a:hover", "style": "background-color", "val": "valor"}`
  - Visible si: `design` is `pills`
- **`css_tag-cloudlia_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-tag-cloud li a:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_tags` isnt `none`

## Ejemplo mínimo

```json
{
  "type": "tag_cloud",
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