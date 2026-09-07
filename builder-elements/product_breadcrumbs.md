# `product_breadcrumbs` — Breadcrumbs

- **Categoría:** single-product
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 7

## Campos

### Custom

- **`breadcrumb_delimiter`** (text) — Delimiter
  - Valor: String
  - Default: `/`
- **`breadcrumb_home`** (switch) — Home page
  - Valor: String
  - Opciones: 
  - Default: `1`

### Breadcrumbs

- **`css_woocommerce-breadcrumb_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-breadcrumb", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-breadcrumb_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-breadcrumb", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_woocommerce-breadcrumb_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-breadcrumb", "style": "color", "val": "valor"}`

### Delimiter

- **`css_woocommerce-breadcrumbspan_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-breadcrumb span", "style": "color", "val": "valor"}`
- **`css_woocommerce-breadcrumbspan_opacity`** (sliderbar) — Opacity
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-woocommerce-breadcrumb span", "style": "opacity", "val": "valor"}`
  - Default: `0.2`

## Ejemplo mínimo

```json
{
  "type": "product_breadcrumbs",
  "uid": "itm000001",
  "icon": "product_breadcrumbs",
  "jsclass": "product_breadcrumbs",
  "title": "Breadcrumbs",
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