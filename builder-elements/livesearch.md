# `livesearch` — Live search

- **Categoría:** 
- **Size por defecto:** 1/3 · tablet — · mobile — · tablet_resized —
- **Campos propios:** 4

## Campos
- **`min_characters`** (text) — Minimal characters
  - Minimal amount of characters in input to load posts
  - Valor: String
  - Default: `3`
- **`container_height`** (text) — Search results container height
  - Valor: String
  - Default: `300`
- **`featured_image`** (switch) — Featured image
  - Valor: String
  - Opciones: 
  - Default: `1`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

## Ejemplo mínimo

```json
{
  "type": "livesearch",
  "uid": "itm000001",
  "size": "1/3",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {}
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*