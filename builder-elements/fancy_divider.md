# `fancy_divider` — Fancy Divider

- **Categoría:** elements
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 4

## Campos
- **`style`** (select) — Style
  - Valor: String
  - Opciones: `circle up` Circle up · `circle down` Circle down · `curve up` Curve up · `curve down` Curve down · `stamp` Stamp · `triangle up` Triangle up · `triangle down` Triangle down
  - Default: `circle up`
- **`color_top`** (color) — Color top
  - Valor: String
- **`color_bottom`** (color) — Color bottom
  - Valor: String

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

## Ejemplo mínimo

```json
{
  "type": "fancy_divider",
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