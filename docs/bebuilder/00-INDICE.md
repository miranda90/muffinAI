# Documentación maestra BeBuilder (BeTheme / Muffin Builder)

Documentación generada a partir del análisis directo del código fuente del theme
(`betheme/functions/builder/`, `betheme/visual-builder/`, `betheme/functions/admin/class-mfn-helper.php`).
Objetivo: generar JSON válido para BeBuilder a partir de cualquier diseño, **sin CSS inline ni archivos CSS**,
usando exclusivamente las opciones que cada elemento permite.

## Índice

| Doc | Contenido |
|---|---|
| [01-arquitectura.md](01-arquitectura.md) | Estructura del JSON (sections → wraps → items), ciclo de vida completo (import, export, guardado en BD, render), campos obligatorios reales por nivel |
| [02-css-pipeline.md](02-css-pipeline.md) | Cómo los atributos `css_*` se convierten en CSS real: `Mfn_Helper::preparePostUpdate()`, placeholders de selector, breakpoints, estilos compuestos, atributos legacy prohibidos |
| [03-atributos-comunes.md](03-atributos-comunes.md) | Pestaña Advanced (común a todos los elementos), campos de sección, campos de wrap, switchers y condicionales, animaciones |
| [04-elementos.md](04-elementos.md) | Inventario completo: 149 elementos de builder + 24 shortcodes inline (167 IDs únicos), con campos propios de cada uno |
| [05-reglas-y-trampas.md](05-reglas-y-trampas.md) | Reglas de oro, trampas verificadas en código, checklist antes de entregar JSON, correcciones a documentación previa |
| [06-global-styles.md](06-global-styles.md) | Global styles (`be_classes`): estilos reutilizables de títulos, textos, botones, secciones y wraps. Formato del objeto clase, reescritura de selectores, generación de `be_classes.css`, export/import, aplicación en el front, trampas |
| [07-iconos.md](07-iconos.md) | Packs de iconos personalizados: CPT `icons`, post meta, estructura del pack en disco, carga del CSS y del selector, gestión completa por SSH/wp-cli, generación de un pack desde SVG sueltos, trampas |
| [09-medios-imagenes-video.md](09-medios-imagenes-video.md) | Imágenes y vídeo de principio a fin: inventario en Figma (`get_metadata`, `download_assets`, `export_video`), descarga a `assets/`, subida a WordPress por wp-cli/REST, `manifest.json`, formato `URL#ID` y por qué (`sc_image`, `mfn_get_attachment`), fondos, vídeo de sección e item `video`, trampas de medios, checklist |
| [08-tipografia-fuentes.md](08-tipografia-fuentes.md) | Tipografía en Theme Options: familia por rol (`font_select`), tamaños, Google Fonts (CDN/local/disabled), fuentes propias autoalojadas (`font-custom*`, generación de `@font-face`), almacenamiento en `wp_options.betheme`, gestión completa por SSH/wp-cli, trampa de `static-css`, trampas |

## Validador

`tools/validate_bebuilder_json.py` — comprueba un JSON contra el catálogo real de campos y el
comportamiento verificado del motor de CSS y del render. Uso y catálogo de códigos en
`tools/README.md`.

```bash
python3 tools/validate_bebuilder_json.py salida.json --strict
```

## Fuentes de verdad en el código

| Fichero | Rol |
|---|---|
| `betheme/functions/builder/class-mfn-builder-fields.php` | Catálogo de TODOS los campos/opciones (67.639 líneas). `set_section()` L181, `set_wrap()` L3497, `set_items()` L6507, `get_inline_shortcode()` L65386, `set_advanced()` L66752 |
| `betheme/functions/admin/class-mfn-helper.php` | **Motor real de CSS**: `preparePostUpdate()` L41, `mfnLocalStyle()` L404, `generate_css()` L479 |
| `betheme/functions/builder/class-mfn-builder-front.php` | Render front: `show()` L269, `show_sections()` L406, `show_wraps()` L1523, `show_items()` L2556 |
| `betheme/functions/builder/class-mfn-builder-items.php` | Despachador `type` → `sc_*()` shortcode PHP |
| `betheme/functions/theme-shortcodes.php` | Render de cada item: `sc_image()` L8060 (resolución `src` `#ID`), `sc_video()` L12877 (iframe vs HTML5) |
| `betheme/functions/theme-functions.php` | `mfn_get_attachment()` L2218, `mfn_get_attachment_id_url()` L2280, `mfn_mimes_support()` L265 (subida SVG) |
| `betheme/functions/builder/class-mfn-builder-helper.php` | `unique_ID()` L197, `unique_ID_reset()` L232 |
| `betheme/functions/builder/class-mfn-builder-ajax.php` | Import/export/revisiones del builder clásico |
| `betheme/visual-builder/visual-builder.php` | Endpoints AJAX del Visual Builder (guardar `updatevbview` L236, importar `importdata` L1044) |
| `betheme/visual-builder/classes/visual-builder-class.php` | `loadExistedElements()` L922: aplanado + enriquecimiento + automigración |
| `betheme/functions/builder/class-mfn-builder-styles.php` | **CÓDIGO MUERTO** (legacy MB2). Ignorar |
| `betheme/visual-builder/assets/js/scripts.js` | UI del builder: `mfn_classes` L3481 (global styles), `mfn_autocomplete` L3350, `addLocalStyle()` L10131 |
| `wp_options.be_classes` / `uploads/betheme/css/be_classes.css` | Almacén y hoja de estilos de los Global styles (ver 06) |

## Documentación previa del proyecto (estado)

- `docs/legacy/muffin-builder-json-guide.md` — guía inicial, movida a legacy; contenía un error sobre `item_is_wrap` (ver 05, corregido). La copia de `.cursor/skills/bebuilder-json/` se vació el 2026-08-28: la única skill viva es la de `.claude/`.
- `builder-elements/*.md` (167 fichas) — **regeneradas en 2026-07 ejecutando el PHP real** (`builder-elements/_generator/`): fiables, con todos los campos, opciones, defaults, selector/style y formato de valor. Incluyen `_advanced.md`, `_section.md`, `_wrap.md` y `_elements.json` íntegro. (Las fichas antiguas del parser regex roto quedaron sustituidas.)
- `builder-elements/GUIA-MAQUETACIONES.md`, `TMC-ABOUT-COMPARISON.md`, `examples/` — patrones de layout válidos y útiles.

- [10 — Flujo verificable](10-flujo-verificable.md): API, snapshots Figma/HTML/imagen, perfiles, medios, pruebas y entrega atómica.
