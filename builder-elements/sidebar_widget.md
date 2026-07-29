# `sidebar_widget` — Sidebar Widget

- **Categoría:** other
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/4 · tablet_resized 0
- **Campos propios:** 2

## Campos
- **`sidebar`** (select) — Select Sidebar
  - 1. Create Sidebar in <a target="_blank" href="admin.php?page=be-options#sidebars">Theme Options > Sidebars</a><br />2. Add Widgets<br />3. Select your sidebar.
  - Valor: String

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

## Ejemplo mínimo

```json
{
  "type": "sidebar_widget",
  "uid": "itm000001",
  "size": "1/4",
  "tablet_size": "1/4",
  "mobile_size": "1/4",
  "attr": {}
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*