# `share` — Share

- **Categoría:** elements
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 43

## Campos

### Copy link

- **`copy_link`** (switch) — Copy link
  - Valor: String
  - Opciones: `1` Show · `""` Hide
  - Default: `1`
- **`copy_link_icon`** (icon) — Icon
  - Valor: String
  - Default: `far fa-copy`
  - Visible si: `copy_link` is `1`
- **`copy_link_label`** (text) — Label
  - Valor: String
  - Default: `Copy link`
  - Visible si: `copy_link` is `1`

### Facebook

- **`facebook`** (switch) — Facebook
  - Valor: String
  - Opciones: `1` Show · `""` Hide
  - Default: `1`
- **`facebook_icon`** (icon) — Icon
  - Valor: String
  - Default: `icon-facebook`
  - Visible si: `facebook` is `1`
- **`facebook_label`** (text) — Label
  - Valor: String
  - Visible si: `facebook` is `1`

### X

- **`twitter`** (switch) — X
  - Valor: String
  - Opciones: `1` Show · `""` Hide
  - Default: `1`
- **`twitter_icon`** (icon) — Icon
  - Valor: String
  - Default: `icon-x-twitter`
  - Visible si: `twitter` is `1`
- **`twitter_label`** (text) — Label
  - Valor: String
  - Visible si: `twitter` is `1`

### LinkedIn

- **`linkedin`** (switch) — LinkedIn
  - Valor: String
  - Opciones: `1` Show · `""` Hide
  - Default: `1`
- **`linkedin_icon`** (icon) — Icon
  - Valor: String
  - Default: `icon-linkedin`
  - Visible si: `linkedin` is `1`
- **`linkedin_label`** (text) — Label
  - Valor: String
  - Visible si: `linkedin` is `1`

### Container

- **`css_share-post_justify_content`** (switch) — Align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Items

- **`css_share-post_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_share-post_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post", "style": "gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_share-post-button_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_share-post-button_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_share-post-button_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_sharepost_button` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_share-post-button_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_share-post-button_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post-button", "style": "color", "val": "valor"}`
- **`css_share-post-button_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post-button", "style": "background-color", "val": "valor"}`
- **`css_share-post-button_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post-button", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sharepost_button` isnt `none`
- **`css_share-post-button_color_hover`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post-button:hover", "style": "color", "val": "valor"}`
- **`css_share-post-button_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post-button:hover", "style": "background-color", "val": "valor"}`
- **`css_share-post-button_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post-button:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sharepost_button` isnt `none`

### Facebook

- **`css_share-post-button-facebook_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-facebook", "style": "color", "val": "valor"}`
- **`css_share-post-button-facebook_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-facebook", "style": "background-color", "val": "valor"}`
- **`css_share-post-button-facebook_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-facebook", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sharepost_button` isnt `none`
- **`css_share-post-button-facebookhover_color_hover`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-facebook:hover", "style": "color", "val": "valor"}`
- **`css_share-post-button-facebookhover_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-facebook:hover", "style": "background-color", "val": "valor"}`
- **`css_share-post-button-facebookhover_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-facebook:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sharepost_button` isnt `none`

### X

- **`css_share-post-button-twitter_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-twitter", "style": "color", "val": "valor"}`
- **`css_share-post-button-twitter_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-twitter", "style": "background-color", "val": "valor"}`
- **`css_share-post-button-twitter_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-twitter", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sharepost_button` isnt `none`
- **`css_share-post-button-twitterhover_color_hover`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-twitter:hover", "style": "color", "val": "valor"}`
- **`css_share-post-button-twitterhover_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-twitter:hover", "style": "background-color", "val": "valor"}`
- **`css_share-post-button-twitterhover_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-twitter:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sharepost_button` isnt `none`

### LinkedIn

- **`css_share-post-button-linkedin_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-linkedin", "style": "color", "val": "valor"}`
- **`css_share-post-button-linkedin_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-linkedin", "style": "background-color", "val": "valor"}`
- **`css_share-post-button-linkedin_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-linkedin", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sharepost_button` isnt `none`
- **`css_share-post-button-linkedinhover_color_hover`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-linkedin:hover", "style": "color", "val": "valor"}`
- **`css_share-post-button-linkedinhover_background_color_hover`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-linkedin:hover", "style": "background-color", "val": "valor"}`
- **`css_share-post-button-linkedinhover_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-share-post .mfn-share-post-button.mfn-share-post-linkedin:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_sharepost_button` isnt `none`

## Ejemplo mínimo

```json
{
  "type": "share",
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