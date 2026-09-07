# `product_meta` — Product meta

- **Categoría:** single-product
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 11

## Campos

### Options

- **`layout`** (switch) — Layout
  - Valor: String
  - Opciones: `inline` Inline · `stacked` Stacked · `table` Table
  - Default: `inline`

### Container

- **`css_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .product_meta, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .product_meta th, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .product_meta td", "style": "text-align", "val": "valor"}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
- **`css_product_metastacked-metali_border_color`** (color) — Stacked line color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .product_meta .stacked-meta li", "style": "border-color", "val": "valor"}`

### Label

- **`css_product_meta_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta span.tagged_as,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta span.posted_in,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta span.stacked-meta-title,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .table-meta th", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_product_meta_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta span.tagged_as,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta span.posted_in,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta span.stacked-meta-title,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .table-meta th", "style": "color", "val": "valor"}`

### Value

- **`css_product_meta_links_color`** (color) — Links color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .table-meta td,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .table-meta td,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .table-meta td a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta .stacked-categories span.stacked-meta-value a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta span.posted_in a", "style": "color", "val": "valor"}`

### Tags

- **`css_tags_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .product_meta .stacked-meta li.stacked-tags .stacked-meta-value a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .tagged_as a", "style": "color", "val": "valor"}`
  - Visible si: `prod_meta_layout` isnt `table`
- **`css_tags_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .product_meta .stacked-meta li.stacked-tags .stacked-meta-value a,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .tagged_as a", "style": "background", "val": "valor"}`
  - Visible si: `prod_meta_layout` isnt `table`

### SKU

- **`css_sku_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .stacked-sku .stacked-meta-value,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta .sku_wrapper", "style": "color", "val": "valor"}`
  - Visible si: `prod_meta_layout` isnt `table`
- **`css_sku_bg`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .stacked-sku .stacked-meta-value,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta .sku_wrapper", "style": "background", "val": "valor"}`
  - Visible si: `prod_meta_layout` isnt `table`
- **`css_sku_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .stacked-sku .stacked-meta-value,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn_product_meta .sku_wrapper", "style": "border-color", "val": "valor"}`
  - Visible si: `prod_meta_layout` isnt `table`

## Ejemplo mínimo

```json
{
  "type": "product_meta",
  "uid": "itm000001",
  "icon": "product_meta",
  "jsclass": "product_meta",
  "title": "Product meta",
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