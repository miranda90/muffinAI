# `breadcrumbs` — Breadcrumbs

- **Categoría:** elements
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 10

## Campos
- **`separator`** (text) — Separator
  - Valor: String
  - Default: `>`
- **`breadcrumb_home`** (switch) — Home page
  - Valor: String
  - Opciones: 
  - Default: `0`

### Container

- **`css_breadcrumbs_justify_content`** (switch) — Align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .breadcrumbs", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Items

- **`css_breadcrumbs_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .breadcrumbs", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_breadcrumbs_gap`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .breadcrumbs", "style": "gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_breadcrumbsli_color`** (color) — Text color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .breadcrumbs li", "style": "color", "val": "valor"}`
- **`css_breadcrumbslia_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .breadcrumbs li a", "style": "color", "val": "valor"}`
- **`css_breadcrumbslia_color_hover`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .breadcrumbs li:hover a", "style": "color", "val": "valor"}`

### Separator

- **`css_breadcrumbsli-breadcrumbs-separator_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .breadcrumbs li .mfn-breadcrumbs-separator", "style": "color", "val": "valor"}`
- **`css_breadcrumbsli-breadcrumbs-separator_font_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .breadcrumbs li .mfn-breadcrumbs-separator", "style": "font-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "breadcrumbs",
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