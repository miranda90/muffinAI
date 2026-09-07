# `product_reviews` — Product reviews

- **Categoría:** single-product
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 32

## Campos

### Title

- **`css_woocommerce-Reviews-title_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .woocommerce-Reviews-title", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_reviews-title_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .woocommerce-Reviews-title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-Reviews-title_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .woocommerce-Reviews-title", "style": "color", "val": "valor"}`

### Container

- **`css_reviews_comment-text_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #comments ol.commentlist li .comment-text", "style": "background-color", "val": "valor"}`
- **`css_reviews_comment-textpmetawoocommerce-review__author_color`** (color) — Author name color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #comments ol.commentlist li .comment-text p.meta .woocommerce-review__author", "style": "color", "val": "valor"}`
- **`css_date_color`** (color) — Date color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #comments ol.commentlist li .comment-text p.meta .woocommerce-review__published-date,.mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #comments ol.commentlist li .comment-text p.meta .woocommerce-review__dash", "style": "color", "val": "valor"}`
- **`css_reviews_comment-textdescription_color`** (color) — Comment color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #comments ol.commentlist li .comment-text .description", "style": "color", "val": "valor"}`
- **`css_reviews_comment-textpmeta_border_color`** (color) — Line color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #comments ol.commentlist li .comment-text p.meta", "style": "border-color", "val": "valor"}`

### Stars

- **`css_star-ratingspancomment-form-ratingpstarsabefore_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .star-rating span,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .comment-form-rating p.stars a:before", "style": "color", "val": "valor"}`

### Form title

- **`css_respondcomment-reply-title_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #respond .comment-reply-title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_comment-reply-title_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #respond .comment-reply-title", "style": "color", "val": "valor"}`

### Your rating

- **`css_reviews_form_wrappercomment-formlabel_color`** (color) — Label
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #review_form_wrapper .comment-form label", "style": "color", "val": "valor"}`
- **`css_comment-form-ratingpstarsa_color`** (color) — Number
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .comment-form-rating p.stars a", "style": "color", "val": "valor"}`
- **`css_comment-form-ratingpstarsa_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .comment-form-rating p.stars a", "style": "background-color", "val": "valor"}`

### Textarea

- **`css_reviews_form_comment_textarea_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #review_form_wrapper .comment-form .comment-form-comment textarea", "style": "color", "val": "valor"}`
- **`css_textarea_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #review_form_wrapper .comment-form .comment-form-comment textarea,.mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #review_form_wrapper .comment-form .comment-form-comment textarea:focus", "style": "background-color", "val": "valor"}`
- **`css_reviews_form_comment_textarea_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement #reviews #review_form_wrapper .comment-form .comment-form-comment textarea", "style": "border-color", "val": "valor"}`

### Button

- **`css_woocommerce_review_form_input_padding`** () — Padding
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input", "style": "padding", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce_review_form_input_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce_review_form_input_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_woocommerce_review_form_input_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_prodrev` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce_review_form_input_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce_review_form_input_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input", "style": "color", "val": "valor"}`
- **`css_woocommerce_review_form_input_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_prodrev` isnt `none`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_woocommerce_review_form_input_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input", "style": "background-color", "val": "valor"}`
  - Visible si: `background_shop_button` is `default`
- **`css_woocommerce_review_form_input_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_shop_button` is `gradient`
- **`css_woocommerce_review_form_inputhover_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input:hover", "style": "color", "val": "valor"}`
- **`css_woocommerce_review_form_inputhover_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_prodrev` isnt `none`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_woocommerce_review_form_inputhover_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input:hover", "style": "background", "val": "valor"}`
  - Visible si: `background_hover_shop_button` is `default`
- **`css_woocommerce_review_form_inputhover_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".woocommerce #Content .mcb-section .mcb-wrap .mcb-item-mfnuidelement #review_form #respond .form-submit input:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_hover_shop_button` is `gradient`

## Ejemplo mínimo

```json
{
  "type": "product_reviews",
  "uid": "itm000001",
  "icon": "product_reviews",
  "jsclass": "product_reviews",
  "title": "Product reviews",
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