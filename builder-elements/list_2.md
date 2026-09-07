# `list_2` — List

- **Categoría:** blocks
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 30

## Campos
- **`tabs`** (tabs) — Items
  - Valor: Array de objetos (formato propio del campo tabs)
  - Opciones: `content` ["textarea", "Content", "This is the list item"] · `link` ["input", "Link", ""] · `target` ["select", "Target", "", {"": "Default \| _self", "_blank": "New tab or window \| _blank"}] · `icon` ["icon", "Icon", ""] · `image` ["image", "Image", ""] · `color` ["color", "Icon color", ""] · `background` ["color", "Icon background", ""]
  - Default: `[{"content": "This is the 1st item"}, {"content": "This is the 2nd item"}]`

### Options

- **`type`** (switch) — Type
  - Valor: String
  - Opciones: `""` Unordered · `ordered` Ordered
- **`starting`** (text) — Starting number
  - Valor: String
  - Default: `1`
  - Visible si: `list-2-type` is `ordered`
- **`align`** (switch) — Alignment
  - Valor: String
  - Opciones: `left` Left · `center` Center · `right` Right
  - Default: `left`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`valign`** (switch) — Vertical alignment
  - Valor: String
  - Opciones: `top` Top · `middle` Middle · `bottom` Bottom
  - Default: `middle`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`divider`** (switch) — Divider
  - Valor: String
  - Opciones: `""` Disable · `enable` Enable

### Icon

- **`icon`** (icon) — Icon
  - Valor: String
  - Default: `icon-dot`
- **`image`** (upload) — Image
  - Image replaces icon selected above
  - Valor: String

### List item

- **`css_list-list-item_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list .mfn-list-item", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Icon wrapper

- **`css_list-icon_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-icon", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_list-icon_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-icon", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_list-icon_top`** (text) — Top
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-icon", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `list-2-valign` is `top`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_list___mfn_list_icon_spacing`** (sliderbar) — Spacing
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list", "style": "--mfn-list-icon-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_list___mfn_list_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list", "style": "--mfn-list-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `list-2-type` isnt `ordered`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_list-list-icon_after_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list .mfn-list-icon:after", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Visible si: `list-2-type` is `ordered`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_list___mfn_list_icon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list", "style": "--mfn-list-icon-color", "val": "valor"}`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_list-icon_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-icon", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_list2` is `default`
- **`css_-list-icon_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-icon", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_list2` is `gradient`
- **`css_list-icon_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-icon", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_list-icon_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-icon", "style": "border-color", "val": "valor"}`
  - Visible si: `list2-border-style` isnt `none`
- **`css_list-icon_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-icon", "style": "border-width", "val": "1px 1px 1px 1px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `list2-border-style` isnt `none`
- **`css_list-icon_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-icon", "style": "border-radius", "val": "8px 8px 8px 8px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)

### Description wrapper

- **`css_list-desc_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-desc", "style": "color", "val": "valor"}`
- **`css_list-desca_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-desc a", "style": "color", "val": "valor"}`
- **`css_list-desca_color_hover`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-desc a:hover", "style": "color", "val": "valor"}`
- **`css_list-desc_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list-desc", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Divider

- **`css_list___mfn_list_divider_width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list", "style": "--mfn-list-divider-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_list___mfn_list_divider_height`** (sliderbar) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list", "style": "--mfn-list-divider-height", "val": "valor"}`
- **`css_list___mfn_list_divider_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-list", "style": "--mfn-list-divider-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "list_2",
  "uid": "itm000001",
  "icon": "list_2",
  "jsclass": "list_2",
  "title": "List",
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