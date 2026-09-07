# `header_promo_bar` — Promo bar

- **Categoría:** header
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 7

## Campos
- **`tabs`** (tabs) — Slides
  - Valor: Array de objetos (formato propio del campo tabs)
  - Opciones: `title` ["textarea", "Content", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."]
  - Default: `[{"title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."}]`
- **`slider_speed`** (text) — Autoplay speed
  - Valor: String
  - Default: `3`

### Container

- **`css_mcb-column-inner_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_mcb-column-inner_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_mcb-column-inner_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner", "style": "color", "val": "valor"}`
- **`css_mcb-column-innera_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner a", "style": "color", "val": "valor"}`
- **`css_mcb-column-innera_color_hover`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner a:hover", "style": "color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "header_promo_bar",
  "uid": "itm000001",
  "icon": "header_promo_bar",
  "jsclass": "header_promo_bar",
  "title": "Promo bar",
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