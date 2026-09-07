# `lottie` — Lottie

- **Categoría:** elements
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 13

## Campos
- **`source_switcher`** (switch) — Lottie Source
  - Valor: String
  - Opciones: `file` Media File · `url` External URL
  - Default: `file`
- **`file`** (upload) — Lottie File
  - Upload self-hosted JSON file
  - Valor: String
  - Visible si: `lottie_source_switcher` is `file`
- **`src`** (text) — Lottie URL
  - Your Lottie JSON url
  - Valor: String
  - Visible si: `lottie_source_switcher` is `url`

### Settings

- **`trigger`** (select) — Trigger
  - Valor: String
  - Opciones: `default` Default · `hover` On hover · `click` On click · `scroll` On scroll · `viewport` Viewport
  - Default: `default`
- **`loop`** (switch) — Loop
  - Valor: String
  - Opciones: 
  - Default: `0`
  - Visible si: `lottie_trigger` isnt `scroll`
- **`speed`** (sliderbar) — Speed
  - Valor: Número como string
  - Default: `1`
- **`viewport`** (sliderbar) — Viewport bottom offset
  - Valor: Número como string
  - Default: `10`
  - Visible si: `lottie_trigger` is `viewport,scroll`
- **`frame_start`** (sliderbar) — Start point
  - Valor: Número como string
  - Default: `1`
- **`frame_end`** (sliderbar) — End point
  - Valor: Número como string
  - Default: `100`
- **`direction`** (switch) — Direction
  - Valor: String
  - Opciones: `1` Forward · `-1` Backward
  - Default: `1`
  - Visible si: `lottie_trigger` isnt `scroll`
- **`link`** (text) — Link
  - Valor: String
  - Default: `Enter your custom URL`
  - Visible si: `lottie_trigger` isnt `click`

### Container

- **`css_lottie-wrapper_justify_content`** (switch) — Align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-lottie-wrapper", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_lottie-wrapperlottie_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-lottie-wrapper .lottie", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "lottie",
  "uid": "itm000001",
  "icon": "lottie",
  "jsclass": "lottie",
  "title": "Lottie",
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