# `divider` — &bull; Divider Basic

- **Categoría:** other
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 6

## Campos
- **`height`** (text) — Height
  - Valor: String
- **`style`** (switch) — Style
  - Valor: String
  - Opciones: `default` Default · `dots` Dots · `zigzag` ZigZag
  - Default: `default`
- **`line`** (switch) — Line
  - Valor: String
  - Opciones: `""` No line · `default` Default · `narrow` Narrow · `wide` Wide
  - Visible si: `divider_style` is `default`
- **`color`** (color) — Color
  - Valor: String
- **`themecolor`** (switch) — Theme color
  - Overwrites color selected above
  - Valor: String
  - Opciones: 
  - Default: `0`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

## Ejemplo mínimo

```json
{
  "type": "divider",
  "uid": "itm000001",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {}
}
```

## Variante shortcode inline (para `content` de column/plain_text/visual)

⚠️ Definición DISTINTA al elemento del builder — solo para el shortcode dentro de texto:
- **`height`** (text) — Height
  - Valor: String
  - Default: `30`
- **`style`** (switch) — Style
  - Valor: String
  - Opciones: `default` Default · `dots` Dots · `zigzag` ZigZag
  - Default: `default`
- **`line`** (switch) — Line
  - for style: default
  - Valor: String
  - Opciones: `""` No line · `default` Default · `narrow` Narrow · `wide` Wide
- **`color`** (color) — Color
  - Valor: String
- **`themecolor`** (switch) — Theme color
  - Overwrites color selected above
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`classes`** (pills) — CSS classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*