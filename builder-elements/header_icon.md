# `header_icon` — Icon

- **Categoría:** header
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 52

## Campos

### Icon

- **`type`** (select) — Icon type
  - For icons: Shop cart, My account and Wishlist, woocommerce plugin is required
  - Valor: String
  - Opciones: `tel` Phone · `mail` E-mail · `search` Search · `default` Custom · `cart` Shop cart · `account` My account · `wishlist` Wishlist
  - Default: `tel`
- **`icon`** (icon) — Icon
  - Valor: String
- **`image`** (upload) — Image
  - Image instead of an icon
  - Valor: String

### Additional

- **`desc`** (text) — Desc
  - Valor: String
- **`cart_total`** (switch) — Cart total
  - Valor: String
  - Opciones: 
  - Default: `1`
  - Visible si: `header_icon_type` is `cart`
- **`count`** (switch) — Icon count
  - Valor: String
  - Opciones: 
  - Default: `1`
  - Visible si: `header_icon_type` is `['wishlist', 'cart']`
- **`count_if_zero`** (switch) — Icon count if 0
  - Valor: String
  - Opciones: `1` Hide · `""` Show
  - Visible si: `header_icon_type` is `['wishlist', 'cart']`
- **`link`** (text) — Link
  - Valor: String
  - Visible si: `header_icon_type` is `tel,mail,default`
- **`target`** (select) — Target
  - Valor: String
  - Opciones: 
  - Visible si: `header_icon_type` is `tel,mail,default`
- **`link_title`** (text) — Link title
  - Valor: String

### Icon

- **`icon_position`** (switch) — Icon position
  - Work with desc only
  - Valor: String
  - Opciones: `top` Top · `bottom` Bottom · `left` Left · `right` Right
  - Default: `top`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`icon_align`** (switch) — Icon alignment
  - Valor: String
  - Opciones: `start` Start · `center` Center · `end` End
  - Default: `center`
  - Visible si: `header-icon-desc` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxicon_icon_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "--mfn-header-menu-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxicon-wrapper_width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxicon-wrapper_height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxicon-wrapper_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxicon-wrapper_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-wrapper_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper", "style": "background-color", "val": "valor"}`
- **`css_icon-wrapper_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_icon-wrapper_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_icon` isnt `none`
- **`css_icon-wrapper_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper", "style": "border-width", "val": "1px 1px 1px 1px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_header_icon` isnt `none`
- **`css_icon-boxicon-wrapper_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper", "style": "border-radius", "val": "8px 8px 8px 8px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
- **`css_icon-wrapper_header_icon_color`** (color) — Icon color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .icon-wrapper", "style": "--mfn-header-icon-color", "val": "valor"}`
- **`css_icon-boxicon-wrapper_background_color_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box:hover .icon-wrapper", "style": "background-color", "val": "valor"}`
- **`css_icon-boxicon-wrapper_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box:hover .icon-wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_header_icon` isnt `none`
- **`css_icon-boxicon-wrapper_header_icon_color_hover`** (color) — Icon color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box:hover .icon-wrapper", "style": "--mfn-header-icon-color", "val": "valor"}`

### Icon count

- **`icon_count_posv`** (switch) — Vertical offset
  - Valor: String
  - Opciones: 
  - Visible si: `header_icon_count` is `1`
- **`css_icon_count_top`** (sliderbar) — Top
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-cart-count,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-wishlist-count", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `-9px`
  - Visible si: `icon_count_posv` is `0`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon_count_bottom`** (sliderbar) — Bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-cart-count,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-wishlist-count", "style": "bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `icon_count_posv` is `1`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`icon_count_posh`** (switch) — Horizontal offset
  - Valor: String
  - Opciones: 
  - Default: `1`
  - Visible si: `header_icon_count` is `1`
- **`css_icon_count_right`** (sliderbar) — Right
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-cart-count,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-wishlist-count", "style": "right", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `-11px`
  - Visible si: `icon_count_posh` is `1`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon_count_left`** (sliderbar) — Left
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-cart-count,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-wishlist-count", "style": "left", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `icon_count_posh` is `0`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon_count_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-cart-count,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-wishlist-count", "style": "color", "val": "valor"}`
  - Visible si: `header_icon_count` is `1`
- **`css_icon_count_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-cart-count,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-wishlist-count", "style": "background-color", "val": "valor"}`
  - Visible si: `header_icon_count` is `1`
- **`css_icon_count_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-cart-count,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .icon-wrapper .header-wishlist-count", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Desc

- **`header_icon_desc_visibility`** (switch) — Responsive visibility
  - Valor: String de tokens separados por espacio, con espacio inicial (ej. `" hide-mobile hide-tablet"`)
  - Opciones: `hide-desktop` Hide on Desktop · `hide-laptop` Hide on Laptop · `hide-tablet` Hide on Tablet · `hide-mobile` Hide on Mobile
- **`css_desc-wrapper_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc-wrapper", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_icon-boxdesc-wrapper_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box .desc-wrapper", "style": "color", "val": "valor"}`
- **`css_icon-boxdesc-wrapper_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-icon-box:hover .desc-wrapper", "style": "color", "val": "valor"}`

### Search results


### Container

- **`css_live-search-box_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box", "style": "background-color", "val": "valor"}`
- **`css_live-search-box_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_live-search-box_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box", "style": "border-width", "val": "1px 1px 1px 1px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_live-search_results` isnt `none`
- **`css_live-search-box_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box", "style": "border-color", "val": "valor"}`
  - Visible si: `border_live-search_results` isnt `none`

### Label

- **`css_live-search-box-live-search-heading_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box .mfn-live-search-heading", "style": "color", "val": "valor"}`
- **`css_live-search-box-live-search-heading_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box .mfn-live-search-heading", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_live-search-box-live-search-heading_opacity`** (sliderbar) — Opacity
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box .mfn-live-search-heading", "style": "opacity", "val": "valor"}`
  - Default: `0.6`

### Items

- **`css_live-search-box-live-search-texts_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box .mfn-live-search-texts", "style": "color", "val": "valor"}`
- **`css_live-search-boxlia_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box li a", "style": "color", "val": "valor"}`
- **`css_live-search-box-live-search-textsspan-ls-price_color`** (color) — Price color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box .mfn-live-search-texts span.mfn-ls-price", "style": "color", "val": "valor"}`
- **`css_live-search-box-live-search-texts_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box .mfn-live-search-texts", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_live-search-box-live-search-textsp_typography`** (typography_vb) — Desc typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box .mfn-live-search-texts p", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_live-search-box-live-search-textsspan-ls-price_typography`** (typography_vb) — Price typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-live-search-box .mfn-live-search-texts span.mfn-ls-price", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "header_icon",
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