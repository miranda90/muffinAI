---
name: bebuilder-json
description: Genera y valida JSON para BeTheme/Muffin Builder (BeBuilder) a partir de diseños, HTML o ideas. Usar cuando se cree o edite JSON de mfn-page-items, se convierta un diseño a builder JSON, o se mencione BeBuilder, Muffin Builder o builder JSON.
---

# BeBuilder JSON Expert

Genera JSON importable en BeBuilder. Jerarquía: **secciones → wraps → items**. Raíz = array de secciones.

## Flujo vigente de scripts nuevos

Leer `docs/bebuilder/10-flujo-verificable.md`. Usar `build(context)` y
`python3 tools/build.py SCRIPT --check` antes de publicar con el mismo comando sin
`--check`. El módulo no escribe al importarse. El punto común comprueba diseño,
medios, perfiles y JSON, y conserva la última entrega válida si falla. Scripts
históricos: congelados; no ejecutarlos mediante el nuevo runner.

Figma: congelar snapshot por revisión y conservar Auto Layout/constraints/textos/medios.
HTML: capturar DOM y estilos calculados con `tools/browser_capture.js` por viewport.
Imagen: anotar bloques, escala y texto; no inventar OCR ni responsive observado.
Normalizar con `tools/design.py` y asignar bloques con `context.bind()`.

El catálogo actual contiene **128 tipos renderizables + 21 alias** (149 entradas).
Los alias se resuelven al construir; no se emiten como `type`. Shortcodes inline
no son items. Para campos nuevos usar `style_field()` y recetas nativas.

Perfil predeterminado: generated/visual. Nested wraps de un nivel son información
para Visual Builder y warning para classic. `--strict` exige cero warnings no
justificados. Excepciones concretas `{code,path,reason}`; nunca ignorar errores
estructurales. `accepted` y `exit_code` son el criterio automatizable, no `valid`
aislado. Los informes distinguen validación local de importación/visual pendientes.

## Estructura del taller — dónde va cada cosa

- **Todo encargo vive en `proyectos/<cliente>/`**: el script `build_<pagina>.py`, el JSON
  generado y los assets del diseño (`assets/` con su `manifest.json`, `icons/`). Nada de scripts
  ni JSON en la raíz.
- **El script escribe su JSON junto a sí mismo** (`HERE = Path(__file__).resolve().parent`),
  nunca en el CWD. Así la salida aparece siempre en la carpeta del proyecto, se ejecute desde
  donde se ejecute.
- **Página nueva → copiar `proyectos/_plantilla/build_plantilla.py`**, que ya importa los
  helpers comunes de `tools/mfn.py` (uid, css, typo, pad, section, wrap, nested, item,
  selectores base). Los tokens del diseño (colores, MEDIA, MAXW) se definen en el script.
- Los scripts anteriores a `tools/mfn.py` llevan los helpers duplicados dentro: están
  congelados a propósito, no migrarlos.

## Documentación maestra (leer según necesidad)

| Doc | Cuándo consultarla |
|---|---|
| `docs/bebuilder/01-arquitectura.md` | Estructura JSON, campos obligatorios reales, ciclo import/export/guardado, nested wraps |
| `docs/bebuilder/02-css-pipeline.md` | Formato `css_*` `{selector,style,val}`, placeholders, breakpoints, estilos compuestos, legacy prohibido |
| `docs/bebuilder/03-atributos-comunes.md` | Pestaña Advanced (todos los items), campos de sección/wrap, switchers, formatos por tipo de campo |
| `docs/bebuilder/04-elementos.md` | Inventario de los 128 tipos renderizables y sus alias con sus campos propios y línea en el PHP |
| `docs/bebuilder/05-reglas-y-trampas.md` | Reglas de oro, trampas verificadas, checklist final |
| `docs/bebuilder/09-medios-imagenes-video.md` | **Imágenes y vídeo**: inventario en Figma, descarga a `assets/`, subida a WordPress (wp-cli/REST), `manifest.json`, `URL#ID`, vídeo de fondo e item `video`, trampas de medios |
| `builder-elements/GUIA-MAQUETACIONES.md` | Patrones de layout reales (hero video, fila de tarjetas en grid, cifras con counter, CTA overlay…) |
| `examples/example2/home.json`, `examples/example1/about-us.json` | Exports reales de referencia |
| `tools/README.md` | Validador: uso, qué corrige `--fix` y catálogo de códigos |

**Fichas por elemento (fiables, regeneradas 2026-07 ejecutando el PHP real):**
`builder-elements/<elemento>.md` — todos los campos con opciones, defaults, selector/style y formato de valor.
`builder-elements/_advanced.md` — pestaña Advanced común. `_section.md` / `_wrap.md` — campos de sección y wrap.
`builder-elements/_elements.json` — volcado íntegro. Regenerar tras actualizar el theme:
`cd builder-elements/_generator && php extract.php && python3 generate_fichas.py`.

## Flujo de generación

0. **Medios primero** (doc 09): inventariar todas las imágenes, logos, iconos y vídeos del diseño
   (`get_metadata` + `get_design_context`/`download_assets` por sección; `export_video` si hay
   timeline), descargarlos a `proyectos/<cliente>/assets/` con nombre descriptivo, subirlos al
   WordPress destino y dejar `assets/manifest.json` con `id` + `url` de cada uno. El script los
   referencia con `media(MAN, "fichero")` → `URL#ID`. Un vídeo que Figma no entrega (video fill)
   se pide al cliente y se deja listado como pendiente; nunca se sustituye por stock.
1. Trocear el diseño: secciones (bandas) → wraps (filas/columnas) → items (bloques de contenido).
2. Elegir elementos nativos (`heading`, `button`, `image`, `list`, `counter`, `plain_text`, `column`…)
   según `docs/bebuilder/04-elementos.md`. Nunca empaquetar varias columnas o título+texto en un solo
   `column` con HTML+clases grid/flex.
   **Elegir por lo que el bloque ES, no por cómo se ve en el Figma** (el mockup siempre es estático):
   cifras de negocio → `counter` (animado y editable), pestañas → `tabs`, acordeón → `faq`,
   testimonio → `testimonial`, lista con iconos → `list`. Si un elemento nativo cubre el bloque, usarlo
   aunque el diseño no muestre el movimiento; degradar a texto estático solo con motivo explícito, y
   avisando de lo que se pierde.
3. Columnas = wraps hermanos con `size` (`1/2`, `1/3`…), o wrap con `grid: "grid"` +
   `grid_columns_switcher` + `css_grid_columns(_custom)`. Nested wraps (`item_is_wrap: 1`) solo si
   el destino es el Visual Builder.
   **Fila de tarjetas (2+ elementos por celda) con hueco definido en el diseño → SIEMPRE grid**:
   wrap `1/1` con `grid` + gaps y un `item_is_wrap: 1` por tarjeta. Los hermanos `1/4` no admiten
   `gap` (ver reglas abajo). Hermanos = columnas de contenido suelto (titular + botón, texto +
   imagen), donde el hueco no es una medida del diseño.
4. Todo estilo (color, fondo, tipografía, márgenes, paddings, bordes, posición, visibilidad,
   animación) via campos `css_*` y opciones del elemento — formatos en docs 02 y 03.
   Espaciados en `rem` y con valor `mobile` desde el primer momento: es más barato escribir los
   dos breakpoints al generar que revisarlos después bloque a bloque.
5. **Validar SIEMPRE antes de entregar** (paso obligatorio, ver abajo).

## Validación obligatoria antes de entregar

Nunca entregar un JSON sin haberlo pasado por el validador. Escribirlo a fichero y ejecutar
desde la raíz del taller:

```bash
python3 tools/validate_bebuilder_json.py proyectos/<cliente>/salida.json --strict
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
`class`→`classes`, sizes/uid/icon ausentes). Lo demás se corrige a mano.
Catálogo completo de códigos y su evidencia en el código del theme: `tools/README.md`.

## Reglas innegociables

- **Estilos nativos por defecto**. Evitar CSS inline, archivos CSS, `custom_css` y atributos legacy.
  Una limitación demostrada permite una excepción concreta de CSS/HTML documentada por ruta
  y probada al importar. No usarla para empaquetar una página completa como HTML opaco.
- Todo `css_*` = `{ "selector": "...mfnuidelement...", "style": "...", "val": ... }` con selector y
  style copiados de la definición del campo. Copiar la notación del catálogo; `|hover` es la convención, pero `:hover` también compila. No reescribir pseudoclases mediante regex.
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
- Item: `type` válido (128 tipos canónicos, doc 04) o `item_is_wrap: 1` con `items[]`.
- **Wraps anidados: un solo nivel.** El theme solo recorre uno (`unique_ID_reset`,
  `loadExistedElements`, `MfnLocalCssCompability::nested_wrap`); más abajo degrada en silencio.
  Trampa 16.
- **Query loops**: un loop de **sección** contiene wraps; uno de **wrap** contiene **UN wrap anidado**
  (`item_is_wrap: 1`) con los items de la tarjeta dentro. **Nunca varios items directos**: el primer
  guardado en el VB los borra y deja el wrap anidado vacío (medido en BD: 53 → 49 items), y sin nodos
  no hay CSS — el botón sale sin fondo y la imagen sin altura. Un único item directo sí es válido.
  Validador **E016**, trampa 20.
- **`gap` solo existe en modo grid.** `css_grid_columns_gap` / `css_grid_rows_gap` llevan
  `condition: wrap_grid is grid` y su selector exige `.mcb-wrap-grid`, clase que solo se añade si el
  wrap declara `grid` (`class-mfn-builder-fields.php:3582-3600`, `class-mfn-builder-front.php:1528`).
  Entre wraps hermanos el hueco es el gutter del theme (~2%) y solo se toca con márgenes, que comen
  ancho de columna. Por eso toda retícula de tarjetas va en grid. En el subwrap-tarjeta: `size` `1/1`
  en los tres breakpoints (reparte `css_grid_columns`, no el `size`), `height_switcher: "custom"` +
  `css_advanced_height` `{"desktop": "100%"}` para que el fondo llene la celda, y
  `css_advanced_align_content: "space-between"` si el botón va abajo. Sobran entonces
  `equal-height-wrap` y el `margin-bottom` por tarjeta. Trampa 21.
- **Anchos custom y saltos de fila** (`.section_wrapper` es flex con `wrap`): con
  `width_switcher: "custom"` + `css_advanced_flex`, el salto lo decide el ancho en px y no el `size`,
  así que un wrap posterior sube a la fila anterior si cabe (medido: titular 1119px + cifra 180px en
  un contenedor de 1656px). El bloque que deba ocupar fila propia va en un wrap `1/1` **sin** ancho
  custom, y el ancho del diseño se consigue con el `size` del item de dentro (`2/5` ≈ 650px,
  `2/3` ≈ 1104px sobre 1656px) + `css_advanced_justify_content` si hay que centrarlo. Trampa 22.
- **Cifras/estadísticas**: usar `counter` cuando formato y animación encajen con el diseño; preservar
  decimales/separadores con texto si el componente no los cubre. No añadir animación no solicitada.
  Comportamiento técnico de `counter`: anima de 0 al valor al entrar en viewport
  (`js/scripts.js:1425-1465`) y ya trae `.number-wrapper` (`.prefix`/`.number`/`.postfix`) + `.title`
  con campos propios de color y tipografía. `number` debe ser **entero pelado** (el JS hace
  `Math.floor`); el “+”, el “%” y la descripción van en `prefix`, `label` y `title`. Vaciar `icon`
  **e** `image` (default `icon-lamp`). `thousands_separator` solo admite `""`/`comma`/`space`: conservar el separador del diseño; si requiere punto o decimales, usar texto y documentar la limitación. Puede estar desactivada en Theme Options
  (`math-animations-disable`).
- **Ancho máximo del contenedor**: cuando el diseño fije un ancho de contenido (ej. 1728px),
  `width_switcher: "custom"` + `css_advanced_max_width` sobre
  `.mcb-section-mfnuidelement.custom-width .section_wrapper`, más el padding lateral del diseño en la
  sección. No usar wraps con ancho custom para simularlo.
- Con `grid` en el wrap del loop, cada `.mfn-queryloop-item-wrapper` es una celda = una tarjeta;
  estilarla con `css_queryloop_item_*` **del wrap**. Ese grupo no tiene `position`: para un badge
  superpuesto sobre la imagen usar `banner_box` (`image` + `overlay` + `bb_badge` + `bb_badge_pos`).
- **Tras importar, el CSS anterior queda huérfano**: el import regenera todos los `uid`
  (`helper.php:232-292`) y las reglas se indexan por `.mcb-item-{uid}`. Que `post-{ID}.css` exista y
  sea grande no prueba nada; buscar un valor concreto del diseño con `grep`. Trampa 17.
- **Al entregar, avisar de que hay que guardar una vez en el VB.** Importar no genera el CSS local:
  sin ese guardado la página sale con la estructura correcta pero sin colores ni alturas. Trampas 6 y 17.
  Y comprobar antes que `grep -c "figma.com\|localhost:3845\|placeholders/image.svg" salida.json` da 0.
- **En el VB solo la primera tarjeta del loop es interactiva** (`iframe.css:1544`,
  `pointer-events: none` en las demás). Si el cliente dice que un elemento del loop no abre opciones,
  preguntar antes si estaba pulsando en la primera. Trampa 18.
- **Fondos con switcher explícito**: todo `css_*_background_color` / `css_*_gradient` va acompañado de
  `"background_switcher": "default"` (o `"gradient"`) o el control queda oculto en el panel. Trampa 19.
- **Imágenes y vídeo siempre desde la Media Library del destino y como `URL#ID`** (formato del
  export real): `image.src`, `bg_video_mp4`, `mp4`, `placeholder` y fondos `url(...)`. Con `#ID` el
  item image puede servir `srcset`, `alt` y dimensiones (`wp_get_attachment_image`); sin él hace una consulta
  por render y, si la URL no coincide exactamente, cae a `<img>` crudo sin `srcset`
  (`theme-shortcodes.php:8116-8180`). Fondos y vídeos no obtienen srcset por llevar #ID.
  Comprobar alt vacío en el DOM, pues puede heredarse del adjunto. Prohibidas URLs de Figma, `localhost:3845`, rutas locales o
  URLs inventadas: el medio se sube y se registra en `assets/manifest.json`. `alt` con contenido
  en imágenes informativas, `""` en decorativas. Trampa 24.
- **Vídeo**: fondo de sección = `background_switcher: "video"` + `bg_video_mp4` (`URL#ID`) + color
  de fondo de respaldo (el poster solo existe vía `bg_image`, deprecado) + overlay si hay texto.
  Item `video` HTML5 = **`video: ""` obligatorio** (el default `n7-F-FMzM7Q` pinta un YouTube ajeno
  en vez del MP4), `mp4`, `placeholder` (poster) y `html5_parameters` en código (`a;;l;m;i` =
  autoplay loop muted playsinline). `object_fit` solo actúa con `css_video_width` **y**
  `css_video_height`. MP4 optimizado antes de subir (sin audio si es fondo, ≤1080p, `faststart`).
  Trampa 25, doc 09 §5.
- **Query loops sobre CPT de BeTheme** (`portfolio`, `client`, `offer`, `slide`, `testimonial`,
  `layout`, `template`): avisar de que deben estar activos en Theme Options → Post types. Si están
  desactivados, el loop sale vacío y el Visual Builder da un **fatal 500 en admin-ajax** al editar
  cualquier post de ese tipo (`visual-builder-class.php:52`, sin `class_exists`). Trampa 15.
- Secciones: `width_switcher` explícito. Heading: `attr.title` + `attr.header_tag` (el shortcode
  inline usa `tag`/`content` — no confundir). Clases → `classes` (no `class`). Anclas → `custom_id`.
- Gradient/transform/filter: subclave `string` obligatoria en `val`. Transform usa siete números CSV
  y parámetros editables coherentes: `transform()` de tools/mfn.py. Nunca `matrix(...)` como string.
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
