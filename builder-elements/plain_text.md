# `plain_text` — Plain Text

- **Categoría:** typography
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/4 · tablet_resized 0
- **Campos propios:** 6

## Campos
- **`content`** (textarea) — Text
  - Some shortcodes and HTML tags allowed
  - Valor: String
  - Default: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.`
- **`shortcodes_parser`** (switch) — Shortcodes parser
  - Valor: String
  - Opciones: `""` Disabled · `1` Enabled

### Content

- **`css_desc_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_descdesca_color`** (color) — Color
  - May be overwritten by individual tags or inline CSS
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc a", "style": "color", "val": "valor"}`
- **`css_desc_text_shadow`** (text_shadow) — Text shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc", "style": "text-shadow", "val": "valor"}`
- **`css_desc_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .desc", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "plain_text",
  "uid": "itm000001",
  "icon": "plain_text",
  "jsclass": "plain_text",
  "title": "Plain Text",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {
    "content": "Contenido de ejemplo"
  }
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*