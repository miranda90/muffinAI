# `slider` — Slider

- **Categoría:** blocks
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 33

## Campos
- **`category`** (select) — Category
  - Valor: String
- **`orderby`** (switch) — Order by
  - Valor: String
  - Opciones: `date` Date · `menu_order` Menu order · `title` Title
  - Default: `date`
- **`order`** (switch) — Order
  - Valor: String
  - Opciones: `ASC` Ascending · `DESC` Descending
  - Default: `DESC`

### Advanced

- **`style`** (select) — Style
  - Valor: String
  - Opciones: `""` Default · `flat` Flat · `description` Flat with title and description · `carousel` Flat carousel with titles · `center` Center mode
  - Default: `flat`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h3`
- **`navigation`** (switch) — Navigation
  - Valor: String
  - Opciones: `""` Default · `hide-arrows` Hide Arrows · `hide-dots` Hide Dots · `hide` Hide

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Image

- **`css_image_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider.default .content_slider_ul .slick-list,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider:not(.default) .content_slider_ul li img", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_image_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider.default .content_slider_ul .slick-list,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider:not(.default) .content_slider_ul li img", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_slider_img` isnt `none`
- **`css_image_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider.default .content_slider_ul .slick-list,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider:not(.default) .content_slider_ul li img", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_slider_img` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider.default .content_slider_ul .slick-list,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider:not(.default) .content_slider_ul li img", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider.default .content_slider_ul,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider:not(.default) .content_slider_ul li img", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Title

- **`css_content_sliderullititle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider ul li .title", "style": "color", "val": "valor"}`
- **`css_content_sliderullititle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider ul li .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Excerpt

- **`css_content_sliderullidesc_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider ul li .desc", "style": "color", "val": "valor"}`
- **`css_content_sliderullidesc_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider ul li .desc", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Arrows

- **`css_content_slider_ulbutton_fontsize`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button", "style": "--mfn-slider-arrow-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `40px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_content_slider_ulbutton_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_content_slider_ulbutton_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_content_slider_ulbutton_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_slider` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_content_slider_ulbutton_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_content_slider_ulbutton_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button i", "style": "color", "val": "valor"}`
- **`css_content_slider_ulbutton_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_slider` isnt `none`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_content_slider_ulbutton_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_slider` is `default`
- **`css_content_slider_ulbutton_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_slider` is `gradient`
- **`css_content_slider_ulbutton_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button:hover i", "style": "color", "val": "valor"}`
- **`css_content_slider_ulbutton_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_slider` isnt `none`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_content_slider_ulbutton_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button:hover, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button:before", "style": "background", "val": "valor"}`
  - Visible si: `background_switcher_hover_slider` is `default`
- **`css_content_slider_ulbutton_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .content_slider .content_slider_ul .button:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover_slider` is `gradient`

### Dots

- **`css_dots_bg`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination a:after", "style": "background-color", "val": "valor"}`
- **`css_dots_bg_active`** (color) — Active color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination .slick-active a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination .slick-active a:after", "style": "background-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "slider",
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