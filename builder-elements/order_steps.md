# `order_steps` — Order steps

- **Categoría:** order-shared
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 22

## Campos

### Labels

- **`cart_label`** (text) — Cart label
  - Valor: String
  - Default: `Cart`
- **`checkout_label`** (text) — Checkout label
  - Valor: String
  - Default: `Checkout`
- **`order_label`** (text) — Order label
  - Valor: String
  - Default: `Order`

### Items

- **`css_order_steps_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps", "style": "--mfn-order-steps-gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Number

- **`css_order_steps_number_size`** (sliderbar) — Wrapper size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps", "style": "--mfn-order-steps-number-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_order_steps_number_font_size`** (sliderbar) — Number size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li .mfn-step-number", "style": "font-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_order_steps_number_offset`** (sliderbar) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li .mfn-step-number", "style": "margin-right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_order_steps_number_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li .mfn-step-number", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_order_steps_number_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li .mfn-step-number", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_order_steps_nr` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_order_steps_number_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li .mfn-step-number", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_order_steps_number_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li .mfn-step-number", "style": "color", "val": "valor"}`
- **`css_order_steps_number_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li .mfn-step-number", "style": "background-color", "val": "valor"}`
- **`css_order_steps_number_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li .mfn-step-number", "style": "border-color", "val": "valor"}`
  - Visible si: `border_order_steps_nr` isnt `none`
- **`css_order_steps_number_color_active`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li.active .mfn-step-number", "style": "color", "val": "valor"}`
- **`css_order_steps_number_background_color_active`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li.active .mfn-step-number", "style": "background-color", "val": "valor"}`
- **`css_order_steps_number_border_color_active`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li.active .mfn-step-number", "style": "border-color", "val": "valor"}`
  - Visible si: `border_order_steps_nr` isnt `none`

### Label

- **`css_order_steps_label_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li .mfn-step-label", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_order_steps_label_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li .mfn-step-label", "style": "color", "val": "valor"}`
- **`css_order_steps_label_color_active`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li.active .mfn-step-label", "style": "color", "val": "valor"}`

### Separator

- **`css_order_steps_separator_opacity`** (sliderbar) — Opacity
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li:after", "style": "opacity", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_order_steps_separator_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li:after", "style": "font-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_order_steps_separator_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-checkout-steps li:after", "style": "color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "order_steps",
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