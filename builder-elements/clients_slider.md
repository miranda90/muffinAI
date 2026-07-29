# `clients_slider` — Clients Slider

- **Categoría:** loops
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 31

## Campos
- **`title`** (text) — Title
  - Valor: String
  - Default: `This is the title`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h4`

### Options

- **`category`** (select) — Category
  - Valor: String
- **`orderby`** (switch) — Order by
  - Valor: String
  - Opciones: `date` Date · `menu_order` Menu order · `title` Title · `rand` Random
  - Default: `menu_order`
- **`order`** (switch) — Order
  - Valor: String
  - Opciones: `DESC` Descending · `ASC` Ascending
  - Default: `ASC`
- **`per_slide`** (sliderbar) — Clients per slide
  - The amount will be automatically reduced in the narrow screen
  - Valor: Número como string
  - Default: `3`
- **`scroll`** (switch) — Slides to scroll
  - Valor: String
  - Opciones: `""` One slide · `1` One client
- **`navigation`** (switch) — Navigation position
  - Valor: String
  - Opciones: `""` Header · `content` Content

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Item title

- **`css_blog_slider_headertitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_slider_header .title", "style": "color", "val": "valor"}`
- **`css_blog_slider_headertitle_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_slider_header .title", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_blog_slider_headertitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .blog_slider_header .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Container

- **`css_clients_slider_ulliclient_wrapper_height`** (text) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider_ul li .client_wrapper", "style": "height", "val": "valor"}`
- **`css_clients_slider_ulliclient_wrapper_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider_ul li .client_wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_clients_slider_ulliclient_wrapper_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider_ul li .client_wrapper", "style": "background-color", "val": "valor"}`
- **`css_clients_slider_ulliclient_wrapper_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider_ul li .client_wrapper:hover", "style": "background-color", "val": "valor"}`

### Button

- **`css_clients_sliderbutton_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_clients_sliderbutton_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_clients_sliderbutton_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_clients_sliderbutton_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_csb` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_clients_sliderbutton_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_clients_sliderbuttonbutton_iconi_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button .button_icon i", "style": "color", "val": "valor"}`
- **`css_clients_sliderbutton_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style` isnt `none`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_clients_sliderbutton_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher` is `default`
- **`css_clients_sliderbutton_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher` is `gradient`
- **`css_clients_sliderbuttonbutton_iconi_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button:hover .button_icon i", "style": "color", "val": "valor"}`
- **`css_clients_sliderbutton_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style` isnt `none`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_clients_sliderbutton_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button:hover, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button:before", "style": "background", "val": "valor"}`
  - Visible si: `background_switcher_hover` is `default`
- **`css_clients_sliderbutton_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .clients_slider .button:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover` is `gradient`

## Ejemplo mínimo

```json
{
  "type": "clients_slider",
  "uid": "itm000001",
  "size": "1/1",
  "tablet_size": "1/1",
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