---
name: bebuilder-json
description: Genera y valida JSON para BeTheme/Muffin Builder (BeBuilder) a partir de diseños, HTML o ideas. Usar cuando se cree o edite JSON de mfn-page-items, se convierta un diseño a builder JSON, o se mencione BeBuilder, Muffin Builder o builder JSON.
---

# BeBuilder JSON Expert

Genera JSON importable en BeBuilder. Jerarquía: **secciones → wraps → items**. Raíz = array de secciones.

## Documentación maestra (leer según necesidad)

| Doc | Cuándo consultarla |
|---|---|
| `docs/bebuilder/01-arquitectura.md` | Estructura JSON, campos obligatorios reales, ciclo import/export/guardado, nested wraps |
| `docs/bebuilder/02-css-pipeline.md` | Formato `css_*` `{selector,style,val}`, placeholders, breakpoints, estilos compuestos, legacy prohibido |
| `docs/bebuilder/03-atributos-comunes.md` | Pestaña Advanced (todos los items), campos de sección/wrap, switchers, formatos por tipo de campo |
| `docs/bebuilder/04-elementos.md` | Inventario de los 167 elementos con sus campos propios y línea en el PHP |
| `docs/bebuilder/05-reglas-y-trampas.md` | Reglas de oro, 13 trampas verificadas, checklist final |
| `builder-elements/GUIA-MAQUETACIONES.md` | Patrones de layout reales (hero video, grids, CTA overlay…) |
| `examples/example2/home.json`, `examples/example1/about-us.json` | Exports reales de referencia |
| `tools/README.md` | Validador: uso, qué corrige `--fix` y catálogo de códigos |

**Fichas por elemento (fiables, regeneradas 2026-07 ejecutando el PHP real):**
`builder-elements/<elemento>.md` — todos los campos con opciones, defaults, selector/style y formato de valor.
`builder-elements/_advanced.md` — pestaña Advanced común. `_section.md` / `_wrap.md` — campos de sección y wrap.
`builder-elements/_elements.json` — volcado íntegro. Regenerar tras actualizar el theme:
`cd builder-elements/_generator && php extract.php && python3 generate_fichas.py`.

## Flujo de generación

1. Trocear el diseño: secciones (bandas) → wraps (filas/columnas) → items (bloques de contenido).
2. Elegir elementos nativos (`heading`, `button`, `image`, `list`, `counter`, `plain_text`, `column`…)
   según `docs/bebuilder/04-elementos.md`. Nunca empaquetar varias columnas o título+texto en un solo
   `column` con HTML+clases grid/flex.
3. Columnas = wraps hermanos con `size` (`1/2`, `1/3`…), o wrap con `grid: "grid"` +
   `grid_columns_switcher` + `css_grid_columns(_custom)`. Nested wraps (`item_is_wrap: 1`) solo si
   el destino es el Visual Builder.
4. Todo estilo (color, fondo, tipografía, márgenes, paddings, bordes, posición, visibilidad,
   animación) via campos `css_*` y opciones del elemento — formatos en docs 02 y 03.
   Espaciados en `rem` y con valor `mobile` desde el primer momento: es más barato escribir los
   dos breakpoints al generar que revisarlos después bloque a bloque.
5. **Validar SIEMPRE antes de entregar** (paso obligatorio, ver abajo).

## Validación obligatoria antes de entregar

Nunca entregar un JSON sin haberlo pasado por el validador. Escribirlo a fichero y ejecutar:

```bash
python3 tools/validate_bebuilder_json.py salida.json --strict
```

- **Exit 0** → entregable.
- **Exit 1 (errores)** → corregir y volver a validar. Un error significa que el JSON se
  degradará en silencio (bloques que no se renderizan, CSS que no se genera) o romperá el render.
- **Exit 2 (warnings)** → revisar uno a uno; entregar solo si cada warning es una decisión
  consciente, y explicarla.
- **Exit 3** → JSON no parseable: el mensaje indica línea y columna.

Iterar hasta llegar a 0 errores. Atajos útiles:

```bash
python3 tools/validate_bebuilder_json.py salida.json --json          # informe estructurado
python3 tools/validate_bebuilder_json.py salida.json --fix -o ok.json # corrige lo mecánico
python3 tools/validate_bebuilder_json.py salida.json --level error    # solo lo bloqueante
```

`--fix` solo arregla lo determinista (basura `vb`/`vb_postid`/`rwd`, `border-radius` con objeto,
`class`→`classes`, `:hover`→`|hover`, sizes/uid/icon ausentes). Lo demás se corrige a mano.
Catálogo completo de códigos y su evidencia en el código del theme: `tools/README.md`.

## Reglas innegociables

- **Prohibido CSS inline y archivos CSS**: nada de `style=""` en `content`, ni `custom_css`, ni
  atributos legacy (`bg_color`, `padding_top/bottom/horizontal`, `padding` de wrap, `style` crudo).
  Equivalencias modernas en `docs/bebuilder/02-css-pipeline.md` §7.
- Todo `css_*` = `{ "selector": "...mfnuidelement...", "style": "...", "val": ... }` con selector y
  style copiados de la definición del campo. Pseudo-clases con `|hover` (pipe, no `:`).
- `val` responsive: claves `desktop`/`laptop`/`tablet`/`mobile` (≤1440/≤959/≤767). Una clave
  no-dispositivo a primer nivel se emite solo en desktop.
- **Generar SIEMPRE pensando en responsive**, no como retoque posterior. Todo wrap e item con
  `size` + `tablet_size` + `mobile_size` explícitos, y todo espaciado y tipografía con valor
  `mobile` además del `desktop` (`tablet`/`laptop` cuando el diseño lo pida). Un JSON con estilos
  solo en `desktop` no está terminado.
- **Márgenes y paddings en `rem`**: `"1.5rem"`, `"5rem"` — nunca `px` ni `em`. Admitidos además
  `0`, `auto`, `%`, unidades de viewport y `calc()`/`var()`. Bordes, radios, anchuras fijas y
  sombras sí pueden ir en `px`.
- **Campos `dimensions`: dos formatos, no intercambiables.** Objeto `{top,right,bottom,left}` **solo**
  en `margin` y `padding` (los únicos con `version: "separated-fields"`). `border-width` y
  `border-radius` van en **string shorthand**: `{"desktop": "1px 1px 1px 1px"}` — orden
  `top right bottom left`, y en radius `top-left top-right bottom-right bottom-left`. Con objeto el
  helper emite `border-width-top` (propiedad inexistente → borde invisible) y el panel del VB muestra
  los campos de tamaño vacíos. Trampa 14 en `docs/bebuilder/05-reglas-y-trampas.md`.
- Todo wrap e item con `size` válido (`1/6`,`1/5`,`1/4`,`1/3`,`2/5`,`1/2`,`3/5`,`2/3`,`3/4`,`4/5`,`5/6`,`1/1`)
  + `tablet_size` + `mobile_size`. Sin `size` → el front lo descarta en silencio.
- Item: `type` válido (167 IDs, doc 04) o `item_is_wrap: 1` con `items[]`.
- Secciones: `width_switcher` explícito. Heading: `attr.title` + `attr.header_tag` (el shortcode
  inline usa `tag`/`content` — no confundir). Clases → `classes` (no `class`). Anclas → `custom_id`.
- Gradient/transform/filter: subclave `string` obligatoria en `val`.
- No emitir `attr.vb`, `attr.vb_postid`, `attr.rwd`, ni `uid` como referencia cruzada (se regeneran).

## Esqueleto mínimo válido

```json
[
  {
    "uid": "sec000001", "icon": "section", "jsclass": "section", "title": "Section", "ver": "default",
    "attr": {
      "width_switcher": "full",
      "css_advanced_background_color": {
        "selector": ".mcb-section-mfnuidelement", "style": "background-color", "val": "#1D242C"
      },
      "css_advanced_padding": {
        "selector": ".mcb-section-mfnuidelement", "style": "padding",
        "val": { "desktop": { "top": "5rem", "bottom": "5rem" }, "mobile": { "top": "2rem", "bottom": "2rem" } }
      }
    },
    "wraps": [
      {
        "uid": "wrp000001", "icon": "wrap", "jsclass": "wrap", "title": "Wrap",
        "size": "1/1", "tablet_size": "1/1", "mobile_size": "1/1",
        "attr": {},
        "items": [
          {
            "type": "heading", "jsclass": "heading", "title": "Heading", "icon": "heading",
            "uid": "itm000001", "size": "1/1", "tablet_size": "1/1", "mobile_size": "1/1",
            "attr": {
              "title": "Título", "header_tag": "h2",
              "css_txt_align": {
                "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title",
                "style": "text-align", "val": { "desktop": "center" }
              },
              "css_advanced_margin": {
                "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner",
                "style": "margin",
                "val": { "desktop": { "bottom": "1.5rem" }, "mobile": { "bottom": "1rem" } }
              }
            }
          }
        ]
      }
    ]
  }
]
```

## Import y CSS

- Importar por el panel Export/Import del Visual Builder (`wp_ajax_importdata`). Los `uid` se regeneran.
- El CSS local (`uploads/betheme/css/post-{ID}.css`) se genera al guardar en el VB. Si se escribe
  `mfn-page-items` por código, invocar además `Mfn_Helper::preparePostUpdate($plano, $post_id)` o
  abrir+guardar la página en el VB una vez.
- Un guardado con secciones vacías **borra la página** — nunca enviar `[]` por error.
