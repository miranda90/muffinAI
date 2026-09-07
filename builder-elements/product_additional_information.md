# `product_additional_information` — Additional information

- **Categoría:** single-product
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 10

## Campos

### Options

- **`title`** (switch) — Title
  - Valor: String
  - Opciones: 
  - Default: `1`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h3`
  - Visible si: `title` is `1`

### Item title

- **`css_title_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "text-align", "val": "valor"}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
- **`css_title_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "color", "val": "valor"}`
- **`css_title_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_title_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Content

- **`css_woocommerce-product-attributesthwoocommerce-product-attributestd_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .woocommerce-product-attributes th, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .woocommerce-product-attributes td", "style": "text-align", "val": "valor"}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
- **`css_woocommerce-product-attributesth_color`** (color) — Label color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .woocommerce-product-attributes th", "style": "color", "val": "valor"}`
- **`css_woocommerce-product-attributestdwoocommerce-product-attributestda_color`** (color) — Value color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .woocommerce-product-attributes td,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .woocommerce-product-attributes td a", "style": "color", "val": "valor"}`

### Line

- **`css_tablewoocommerce-product-attributestdspanbefore_background`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement table.woocommerce-product-attributes td span:before", "style": "background", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "product_additional_information",
  "uid": "itm000001",
  "icon": "product_additional_information",
  "jsclass": "product_additional_information",
  "title": "Additional information",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {
    "title": "Título de ejemplo"
  }
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*