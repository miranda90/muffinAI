# `post_content` — Post content

- **Categoría:** single-post
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 1

## Campos

### Content

- **`content`** (select) — Source
  - Valor: String
  - Opciones: `""` Default · `mfn` BeBuilder

## Ejemplo mínimo

```json
{
  "type": "post_content",
  "uid": "itm000001",
  "icon": "post_content",
  "jsclass": "post_content",
  "title": "Post content",
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