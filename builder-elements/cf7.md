# `cf7` — Contact Form 7

- **Categoría:** plugins
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 34

## Campos
- **`form`** (select) — Contact form
  - Valor: String

### Labels

- **`css_formformlabel_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form label", "style": "color", "val": "valor"}`
- **`css_formpformlabel_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form p,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form label", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_formformlabel_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form label", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_formformlabel_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form label", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Inputs

- **`css_field_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit),.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_field_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit),.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_field_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit),.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_field_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit),.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_field_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit),.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_field_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit),.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_cf7inputs` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_field_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit),.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_field_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit),.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "color", "val": "valor"}`
- **`css_field_placeholder_color`** (color) — Placeholder color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input::placeholder, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea::placeholder", "style": "color", "val": "valor"}`
- **`css_field_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit),.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "background-color", "val": "valor"}`
- **`css_field_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit),.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_cf7inputs` isnt `none`
- **`css_field_color_focus`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit):focus,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select:focus, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea:focus", "style": "color", "val": "valor"}`
- **`css_field_placeholder_color_focus`** (color) — Placeholder color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:focus::placeholder, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea:focus::placeholder", "style": "color", "val": "valor"}`
- **`css_field_bg_focus`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit):focus,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select:focus, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea:focus", "style": "background-color", "val": "valor"}`
- **`css_field_border_color_focus`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input:not(.wpcf7-submit):focus,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form select:focus, .mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea:focus", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_cf7inputs` isnt `none`

### Textarea

- **`css_textarea_height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form textarea", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Fields wrapper

- **`css_formcolumn_padding`** (dimensions) — Padding
  - Modifies div.column that is included by default in the Betheme forms.
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form .column", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Button

- **`css_button_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_button_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_cf7button` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button", "style": "color", "val": "valor"}`
- **`css_button_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button", "style": "background-color", "val": "valor"}`
- **`css_button_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_cf7button` isnt `none`
- **`css_button_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit:hover,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button:hover", "style": "color", "val": "valor"}`
- **`css_button_bg_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit:hover,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button:hover", "style": "background-color", "val": "valor"}`
- **`css_button_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement form input.wpcf7-submit:hover,.mcb-section .mcb-wrap .mcb-item-mfnuidelement form button:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_cf7button` isnt `none`

## Ejemplo mínimo

```json
{
  "type": "cf7",
  "uid": "itm000001",
  "icon": "cf7",
  "jsclass": "cf7",
  "title": "Contact Form 7",
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