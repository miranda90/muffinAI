# `offer_thumb` — Offer Slider Thumb

- **Categoría:** loops
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 33

## Campos
- **`category`** (select) — Category
  - Valor: String
- **`style`** (switch) — Thumbnails position
  - Valor: String
  - Opciones: `bottom` Bottom · `""` Left
  - Default: `bottom`

### Deprecated

- **`align`** (switch) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Text align
  - Text align center does not affect title if button is active
  - Valor: String
  - Opciones: `left` Left · `center` Center · `right` Right · `justify` Justify
  - Default: `left`
- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Image

- **`css_offer_thumboffer_thumb_liimage_wrapper_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .image_wrapper", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_offer_thumboffer_thumb_liimage_wrapper_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .image_wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_os_img` isnt `none`
- **`css_offer_thumboffer_thumb_liimage_wrapper_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .image_wrapper", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_os_img` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_offer_thumboffer_thumb_liimage_wrapper_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .image_wrapper", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Title

- **`css_offer_thumboffer_thumb_lidesc_wrappertitleh3_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title h3", "style": "color", "val": "valor"}`
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleh3_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title h3", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Content

- **`css_desc_wrapper_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc_wrapper", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_offer_thumboffer_thumb_lidesc_wrapperdesc_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .desc", "style": "color", "val": "valor"}`
- **`css_offer_thumboffer_thumb_lidesc_wrapperdesc_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .desc", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Nav

- **`css_offer_thumbslider_paginationlia_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .slider_pagination li a", "style": "background-color", "val": "valor"}`
- **`css_offer_thumbslider_paginationlia_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .slider_pagination li a", "style": "border-color", "val": "valor"}`
- **`css_offer_thumbslider_paginationlislick-a_background_color_active`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .slider_pagination li.slick-active a", "style": "background-color", "val": "valor"}`
- **`css_offer_thumbslider_paginationlislick-a_border_color_active`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .slider_pagination li.slick-active a", "style": "border-color", "val": "valor"}`

### Button

- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabutton_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabutton_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabutton_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabutton_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_osf_border` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabutton_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabutton_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button", "style": "color", "val": "valor"}`
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabutton_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_osf_border` isnt `none`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabutton_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_osf` is `default`
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabutton_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_osf` is `gradient`
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabuttonhover_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button:hover", "style": "color", "val": "valor"}`
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabuttonhover_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_osf_border` isnt `none`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabuttonhover_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button:hover, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button:before", "style": "background", "val": "valor"}`
  - Visible si: `background_switcher_hover_osf` is `default`
- **`css_offer_thumboffer_thumb_lidesc_wrappertitleabuttonhover_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .offer_thumb_li .desc_wrapper .title a.button:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover_osf` is `gradient`

### Decoration

- **`css_offer_thumbslider_paginationli_offer_thumbs_nav`** (color) — Active
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .offer_thumb .slider_pagination li", "style": "--mfn-offer-thumbs-nav", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "offer_thumb",
  "uid": "itm000001",
  "icon": "offer_thumb",
  "jsclass": "offer_thumb",
  "title": "Offer Slider Thumb",
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