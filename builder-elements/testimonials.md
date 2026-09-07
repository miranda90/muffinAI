# `testimonials` — Testimonials

- **Categoría:** loops
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 40

## Campos
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h5`
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

### Options

- **`style`** (switch) — Style
  - Valor: String
  - Opciones: `""` Default · `single-photo` Single photo
- **`hide_photos`** (switch) — Photos
  - Valor: String
  - Opciones: `1` Hide · `0` Show
  - Default: `0`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Container

- **`css_testimonials_slidertestimonials_slider_ulli_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .testimonials_slider_ul li", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Blockquote

- **`css_testimonials_slider_ullibq_wrapperblockquote_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement  .testimonials_slider .testimonials_slider_ul li .bq_wrapper blockquote", "style": "color", "val": "valor"}`
- **`css_testimonials_slider_ullibq_wrapper_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement  .testimonials_slider .testimonials_slider_ul li .bq_wrapper", "style": "background-color", "val": "valor"}`
- **`css_testimonials_slider_ullibq_wrapperblockquote_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement  .testimonials_slider .testimonials_slider_ul li .bq_wrapper blockquote", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_testimonials_slidertestimonials_slider_ullibq_wrapper_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .testimonials_slider_ul li .bq_wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_testimonials_slidertestimonials_slider_ullibq_wrapper_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .testimonials_slider_ul li .bq_wrapper", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Blockquote icon

- **`css_testimonials_sliderblockquote-icon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .blockquote .mfn-blockquote-icon", "style": "color", "val": "valor"}`

### Blockquote lines

- **`css_testimonials_sliderblockquoteblockquote_text_decoration_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .blockquote blockquote", "style": "text-decoration-color", "val": "valor"}`
- **`css_testimonials_sliderblockquoteblockquote_text_underline_offset`** (text) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .blockquote blockquote", "style": "text-underline-offset", "val": "valor"}`
- **`css_testimonials_sliderblockquoteblockquote_text_decoration_thickness`** (text) — Thickness
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .blockquote blockquote", "style": "text-decoration-thickness", "val": "valor"}`

### Dots

- **`css_slider_paginationa_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination a", "style": "background-color", "val": "valor"}`
- **`css_dots_bg_active`** (color) — Color active
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination li.slick-active a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .slider_pagination li.slick-active a:after", "style": "background-color", "val": "valor"}`

### Author

- **`css_author_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .testimonials_slider_ul li .author .title a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .testimonials_slider_ul li .author .title", "style": "color", "val": "valor"}`
- **`css_testimonials_slider_ulliauthortitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .testimonials_slider_ul li .author .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Company

- **`css_testimonials_slider_ulliauthorcompany_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .testimonials_slider_ul li .author .company", "style": "color", "val": "valor"}`
- **`css_testimonials_slider_ulliauthorcompany_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .testimonials_slider_ul li .author .company", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Arrows

- **`css_testimonials_sliderabutton_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_testimonials_sliderabutton_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_testimonials_sliderabutton_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_testi` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_testimonials_sliderabutton_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_testimonials_sliderabuttoni_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button i", "style": "color", "val": "valor"}`
- **`css_testimonials_sliderabutton_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_testi` isnt `none`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_testimonials_sliderabutton_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_testi` is `default`
- **`css_testimonials_sliderabutton_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_testi` is `gradient`
- **`css_testimonials_sliderabuttoni_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button:hover i", "style": "color", "val": "valor"}`
- **`css_testimonials_sliderabutton_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_testi` isnt `none`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_testimonials_sliderabutton_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button:hover, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button:before", "style": "background", "val": "valor"}`
  - Visible si: `background_switcher_hover_testi` is `default`
- **`css_testimonials_sliderabutton_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider a.button:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover_testi` is `gradient`

### Decoration

- **`css_testimonials_slider_ullihr_dotsspan_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .testimonials_slider_ul li .hr_dots span", "style": "background-color", "val": "valor"}`

### Line

- **`css_testimonials_slider_imagesliaafter_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .slider_images li a:after", "style": "background-color", "val": "valor"}`

### Photos background

- **`css_photos_bg`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .slider_images,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .testimonials_slider .slider_images:before", "style": "background-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "testimonials",
  "uid": "itm000001",
  "icon": "testimonials",
  "jsclass": "testimonials",
  "title": "Testimonials",
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