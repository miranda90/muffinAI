# `footer_menu` — Menu

- **Categoría:** footer
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 9

## Campos

### Menu

- **`menu_display`** (select) — Menu to display
  - Valor: String
- **`menu_style`** (select) — Style
  - Valor: String
  - Opciones: `vertical` Vertical · `horizontal` Horizontal
  - Default: `vertical`
- **`css_mcb-column-innerul-footer-menu--vertical_text_align`** (select) — Alignment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner ul.mfn-footer-menu-style-vertical", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Default: `left`
  - Visible si: `menu_style` is `vertical`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_mcb-column-innerul-footer-menu--horizontal_justify_content`** (select) — Alignment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner ul.mfn-footer-menu-style-horizontal", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `flex-start` Left · `center` Center · `flex-end` Right · `space-between` Space between · `space-around` Space around · `space-evenly` Space evenly
  - Default: `center`
  - Visible si: `menu_style` is `horizontal`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Menu

- **`css_ula_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul a", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ula_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul a", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_ula_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul a", "style": "color", "val": "valor"}`
- **`css_ula_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul a:hover", "style": "color", "val": "valor"}`
- **`css_ulcurrent-menu-itema_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement ul .current-menu-item > a", "style": "color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "footer_menu",
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