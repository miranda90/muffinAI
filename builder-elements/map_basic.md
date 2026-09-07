# `map_basic` — Map Basic

- **Categoría:** elements
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 4

## Campos

### Iframe

- **`iframe`** (textarea) — Iframe
  - Visit <a target="_blank" href="https://google.com/maps">Google Maps</a> and follow these instructions:<br />1. Find place. 2. Click the share button in the left panel. 3. Select "embed a map" 4. Choose size. 5. Click "copy HTML" and paste it above
  - Valor: String

### Embed

- **`address`** (text) — Address or place name
  - Valor: String
- **`zoom`** (text) — Zoom
  - Valor: String
  - Default: `13`
- **`height`** (text) — Height
  - Valor: String
  - Default: `300`

## Ejemplo mínimo

```json
{
  "type": "map_basic",
  "uid": "itm000001",
  "icon": "map_basic",
  "jsclass": "map_basic",
  "title": "Map Basic",
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