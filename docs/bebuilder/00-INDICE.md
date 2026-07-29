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
| `betheme/functions/builder/class-mfn-builder-helper.php` | `unique_ID()` L197, `unique_ID_reset()` L232 |
| `betheme/functions/builder/class-mfn-builder-ajax.php` | Import/export/revisiones del builder clásico |
| `betheme/visual-builder/visual-builder.php` | Endpoints AJAX del Visual Builder (guardar `updatevbview` L236, importar `importdata` L1044) |
| `betheme/visual-builder/classes/visual-builder-class.php` | `loadExistedElements()` L922: aplanado + enriquecimiento + automigración |
| `betheme/functions/builder/class-mfn-builder-styles.php` | **CÓDIGO MUERTO** (legacy MB2). Ignorar |
| `betheme/visual-builder/assets/js/scripts.js` | UI del builder: `mfn_classes` L3481 (global styles), `mfn_autocomplete` L3350, `addLocalStyle()` L10131 |
| `wp_options.be_classes` / `uploads/betheme/css/be_classes.css` | Almacén y hoja de estilos de los Global styles (ver 06) |

## Documentación previa del proyecto (estado)

- `muffin-builder-json-guide.md`, `.cursor/skills/bebuilder-json/` — válidos en lo esencial; contenían un error sobre `item_is_wrap` (ver 05, corregido).
- `builder-elements/*.md` (167 fichas) — **regeneradas en 2026-07 ejecutando el PHP real** (`builder-elements/_generator/`): fiables, con todos los campos, opciones, defaults, selector/style y formato de valor. Incluyen `_advanced.md`, `_section.md`, `_wrap.md` y `_elements.json` íntegro. (Las fichas antiguas del parser regex roto quedaron sustituidas.)
- `builder-elements/GUIA-MAQUETACIONES.md`, `TMC-ABOUT-COMPARISON.md`, `examples/` — patrones de layout válidos y útiles.
