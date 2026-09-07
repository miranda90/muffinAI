# 05 — Reglas de oro, trampas verificadas y checklist

> Actualización: el flujo verificable, las excepciones por ruta y las precisiones sobre transformaciones, medios y perfiles están en [10-flujo-verificable.md](10-flujo-verificable.md). Las pruebas del código prevalecen sobre reglas históricas.
## 1. Reglas de oro

1. **Cero CSS inline y cero archivos CSS.** Toda apariencia = campos `css_*` con `{selector, style, val}`.
   Prohibidos: `bg_color`, `bg_image`, `bg_position`, `bg_size`, `padding_top/bottom/horizontal`,
   `padding` (wrap), `style` crudo, `custom_css`, atributos `style=""` dentro de `content`.
2. **`selector` y `style` se copian literalmente** de la definición del campo en
   `class-mfn-builder-fields.php`. Placeholder `mfnuidelement`; pseudo-clases con `|hover` (pipe).
3. **`val` responsive** solo con claves `desktop`/`laptop`/`tablet`/`mobile` (breakpoints 1440/959/767).
   Clave no-dispositivo a primer nivel = sub-propiedad SOLO en desktop.
4. **Cada wrap e item lleva `size`** (fracción válida: 1/6…1/1). Sin `size` → no se renderiza (silencioso).
5. **Siempre responsive.** El JSON se genera pensando en los cuatro tamaños desde el principio,
   no como un retoque posterior. En la práctica:
   - Todo wrap e item con `size`, `tablet_size` y `mobile_size` explícitos.
   - Todo espaciado (`css_advanced_padding` / `_margin`) y toda tipografía (`css_typography`,
     `font-size`) con valor `mobile` además del `desktop`: en móvil un `5rem` de desktop es casi
     siempre excesivo.
   - `laptop` y `tablet` solo cuando el diseño lo pida; la cascada CSS cubre el resto.
   - Reglas de layout que cambian por tamaño (`grid-template-columns`, `flex`, `position`,
     `text-align`) declaradas por dispositivo, no heredadas por accidente.
6. **Espaciados en `rem`.** Márgenes y paddings se expresan siempre en `rem`
   (`"1.5rem"`, `"5rem"`), nunca en `px` ni `em`. `rem` escala con la raíz del documento y mantiene
   el ritmo vertical coherente entre bloques y entre breakpoints. Excepciones admitidas: `0`,
   `auto`, `%`, unidades de viewport y `calc()`/`var()`. La regla aplica a `padding` y `margin`;
   bordes, radios y tamaños fijos pueden ir en `px`.
7. **`type` de item** = uno de los 149 de `set_items()`; inexistente → ignorado en silencio.
8. **Un elemento por celda**: columnas = wraps hermanos con `size` (o wrap grid); nunca un solo
   `column` con HTML+clases grid/flex simulando columnas.
8.bis **Fila de tarjetas (2+ elementos por celda) = wrap `grid` + un subwrap por tarjeta.**
   Los hermanos con `size` valen para columnas sueltas, pero no admiten `gap`: los campos
   `css_grid_columns_gap` / `css_grid_rows_gap` solo existen en modo grid (trampa 21). Si el diseño
   fija separación entre tarjetas —casi siempre— la retícula va en un wrap `1/1` con
   `grid: "grid"` + `css_grid_columns` + gaps, y cada tarjeta es un `item_is_wrap: 1`. El grid
   estira las celdas a la misma altura (no hace falta `equal-height-wrap`); poner `height: 100%`
   en el inner del subwrap para que su fondo llene la celda, y `align-content: space-between`
   si el botón debe quedar pegado abajo. Coste asumido: un W005 por tarjeta (trampa 10).
9. **Elementos nativos primero**: `heading` (`title`+`header_tag`), `button`, `image`, `list`,
   `counter`, `plain_text`… antes que HTML en `column`.
9.bis **Elegir el elemento por lo que el bloque ES, no por cómo se ve en el Figma.** Un mockup es
   estático: si el bloque es una cifra de negocio (“+1.000 profesionales”, “98% clientes
   recurrentes”), el elemento es **`counter`**, no dos `plain_text` — anima solo, trae la estructura
   `.prefix`/`.number`/`.postfix`/`.title` con estilos por parte y es lo que el cliente espera editar
   en el panel. Mismo criterio en el resto: pestañas → `tabs`, acordeón → `faq`, testimonio →
   `testimonial`, lista con iconos → `list`, no HTML dentro de un `column`. Detalles de `counter`
   en la trampa 23; catálogo completo en `04-elementos.md` y `builder-elements/<elemento>.md`.
10. **`classes`** (pills) para clases CSS, `custom_id` para anclas. No `class` (deprecated).
11. **Switchers explícitos** cuando se active su subcampo: `width_switcher`, `height_switcher`,
    `background_switcher`, `grid_columns_switcher`, `background_overlay_switcher`.
12. **Gradient/transform/filter**: obligatoria la subclave `string` en `val`.
13. **uid**: 9 chars únicos; legibles ayudan a depurar, pero el import los regenera siempre —
    no crear referencias cruzadas por uid.

## 2. Trampas verificadas en código

| # | Trampa | Evidencia |
|---|---|---|
| 1 | Wrap/item sin `size` desaparece sin error (causa nº1 de "importé y no sale nada") | `front.php:1625`, `:2614` |
| 2 | `type` inexistente → item ignorado sin aviso | `front.php:2608` |
| 3 | `size` con valor no listado → warnings + layout roto | `front.php:1636` |
| 4 | `css_*` sin `selector`+`val` no genera CSS | `class-mfn-helper.php:198` |
| 5 | Guardar con `sections` vacío **BORRA la página** (`delete_post_meta`) | `visual-builder.php:385` |
| 6 | Escribir `mfn-page-items` directo (SQL/CLI) no genera CSS: invocar `Mfn_Helper::preparePostUpdate($plano, $post_id)` o re-guardar en VB | `visual-builder.php:353` |
| 7 | No emitir `attr.vb`, `attr.vb_postid`, `attr.rwd` (runtime del VB; `vb_postid` altera dynamic data) | `front.php:2638-2640` |
| 8 | `attr.tabs` tiene formato propio (array por índice); pasarlo como string → TypeError en el shortcode | `ajax.php:1046-1060` |
| 9 | Imports "wrap only" exigen `[0]['wraps'][0]` | `ajax.php:918` |
| 10 | `item_is_wrap` desactiva BeBuilder Blocks Classic y da warnings en builder clásico admin (no en VB) | `admin.php:1637-1646`, `:833` |
| 11 | En BeBuilder los query loops limitan `posts_per_page` a 8 (solo en editor) | `front.php:1315` |
| 12 | `woo_alert` no se renderiza sin notices fuera del builder | `front.php:2562` |
| 13 | Import no valida esquema: JSON incompleto se acepta y degrada en silencio | `visual-builder.php:1059` |
| 14 | `border-width`/`border-radius` con objeto `{top,right,bottom,left}` → CSS inválido (`border-width-top`) + inputs vacíos en el panel del VB. Van en **string shorthand** | `class-mfn-helper.php:260`, `forms/fields/dimensions.js:9` |
| 15 | **Fatal 500 en admin-ajax al abrir/importar en un post cuyo CPT está desactivado en Theme Options.** No depende del JSON: falla igual con un import vacío | `visual-builder-class.php:52` y `:638`, `functions.php:118-146` |
| 16 | Wrap anidado dentro de otro wrap anidado: el theme solo recorre **un** nivel de `item_is_wrap` | `helper.php:246-282`, `visual-builder-class.php:1005`, `local-css-compability.php:365-371` |
| 17 | **Tras importar, ningún `css_*` existe todavía**: el CSS local se escribe al guardar en el VB. Síntoma: estructura correcta pero sin colores, alturas ni espaciados | `visual-builder.php:354`, `class-mfn-helper.php:41` |
| 18 | En el VB **solo la primera iteración del loop es interactiva**: las demás llevan `pointer-events: none` | `iframe.css:1544` |
| 19 | Fondo (`background-color`/`gradient`) sin `background_switcher` explícito: el control queda oculto en el panel | `class-mfn-builder-fields.php`, condición `background_switcher_*` |
| 20 | **Varios items directos en un query loop de wrap: el primer guardado en el VB los BORRA** y deja un wrap anidado vacío. La tarjeta va dentro de un `item_is_wrap: 1` | medido en BD (post 715, 53→49 items); `scripts.js:2317-2323` y `:7364` |
| 21 | **`gap` solo existe en modo grid.** `css_grid_columns_gap`/`css_grid_rows_gap` llevan `condition: wrap_grid is grid` y su selector exige `.mcb-wrap-grid`, clase que solo se añade si `attr.grid`. Entre wraps hermanos el hueco es el gutter del theme y solo se modula con márgenes | `class-mfn-builder-fields.php:3582-3600`, `class-mfn-builder-front.php:1528` |
| 22 | **Wraps con ancho custom + flex-wrap: un wrap sube a la fila anterior si cabe.** `css_advanced_flex` fija anchos en px y el `size` deja de gobernar el salto de fila; con 1119px + 180px (1299 < 1656) la primera cifra se coloca junto al titular | `class-mfn-builder-front.php:1528` y CSS de `.section_wrapper` (flex + wrap) |
| 23 | **`counter` con `icon`/`image` sin vaciar pinta un `icon-lamp`** (es el `std` del campo), y su `number` debe ser entero pelado: el JS anima `data-to` con `Math.floor`. `thousands_separator` no tiene opción de punto | `theme-shortcodes.php:7770-7780`, `js/scripts.js:1425-1465`, ficha `builder-elements/counter.md` |
| 24 | Imagen/vídeo sin `#ID` en `src`/`bg_video_mp4`/`mp4`/fondos → consulta por render y, si la URL no coincide, `<img>` crudo sin `srcset`; URLs de Figma/`localhost` mueren tras la sesión | `theme-shortcodes.php:8116-8180`, `theme-functions.php:2280` — doc 09 |
| 25 | Item `video` con `video` sin vaciar → pinta el YouTube por defecto (`n7-F-FMzM7Q`) en lugar del MP4 | `theme-shortcodes.php:12960`, ficha `video.md` — doc 09 |

### Trampa 15 — el 500 real de admin-ajax (verificado en servidor, 2026-07-29)

**Síntoma**: `admin-ajax.php` devuelve 500 al importar en el Visual Builder. Es tentador culpar al
JSON. **No es el JSON**: falla igual con un import vacío, y ningún cambio en el JSON lo arregla.

**Traza** (`wp-content/debug.log` con `WP_DEBUG_LOG`):

```
PHP Fatal error: Uncaught Error: Class "Mfn_Post_Type_Portfolio" not found
  in .../betheme/visual-builder/classes/visual-builder-class.php:52
Stack trace:
#0 visual-builder.php(1598): MfnVisualBuilder->__construct()
#1 visual-builder.php(1125): mfnvb_renderView()
#2 class-wp-hook.php(341): mfnvb_import_data()
#5 wp-admin/admin-ajax.php(192): do_action()
```

**Cadena causal**, las tres piezas verificadas:

1. `functions.php:118-146` hace el `require_once` de cada clase de CPT **bajo condición**:
   `if (! isset($post_types_disable['portfolio'])) { require_once(...); }`. Si el CPT está marcado
   en Theme Options → Post types, la clase nunca se carga.
2. Los posts de ese tipo **siguen en la base de datos** con su `post_type` intacto: desactivar el
   CPT no borra nada, solo deja de registrarlo.
3. `MfnVisualBuilder::__construct()` hace `$this->post_type = get_post_type($this->post_id)` —que
   lee la columna de la BD, no el registro de CPT— y en la línea 52 ejecuta
   `new Mfn_Post_Type_Portfolio()` **sin `class_exists()`**. Fatal. Mismo patrón sin guard en `:638`.

Afecta a los siete CPT desactivables: `portfolio`, `client`, `offer`, `slide`, `testimonial`,
`layout`, `template`.

**Diagnóstico** — la opción serializada dice la verdad:

```bash
wp db query "SELECT option_value FROM {prefijo}options WHERE option_name='betheme'" \
  --skip-column-names | grep -o 'post-type-disable[^}]*}'
```

**Solución**: reactivar el CPT en Theme Options → Post types (o no editar con el VB posts de un tipo
desactivado). El validador avisa con **W063** cuando un query loop consume uno de esos CPT.

### Trampa 16 — un solo nivel de `item_is_wrap`

Los wraps anidados son canónicos, pero el theme solo recorre **un** nivel. Tres rutinas
independientes de la ruta de import se paran ahí:

| Rutina | Evidencia | Qué pasa a partir del nivel 2 |
|---|---|---|
| `Mfn_Builder_Helper::unique_ID_reset()` | `helper.php:246-282` | No regenera los `uid`: colisionan con los del destino |
| `MfnVisualBuilder::loadExistedElements()` | `visual-builder-class.php:1005` | `if(!isset($jtem['type'])) continue;` — el wrap desaparece del formulario del panel |
| `MfnLocalCssCompability::nested_wrap()` | `local-css-compability.php:365-371` | Llama a `nested_item()` para todo hijo sin volver a comprobar `item_is_wrap`: trata el wrap como item y sus `css_*` no se normalizan |

Degrada en silencio, no lanza fatal. Para maquetar tarjetas complejas con un solo nivel:
posicionar con `css_advanced_position: "absolute"` + `top`/`left`/`z-index` en vez de anidar
contenedores, y usar fracciones de `size` hermanas (`4/5` + `1/5`) para las filas internas.
El validador lo bloquea con **E014**.

### Trampa 17 — "importé y no tiene estilos" (verificado en servidor, 2026-07-29)

**Síntoma**: la estructura aparece correcta pero faltan colores, alturas o espaciados. Típicamente se
nota en lo más visible: un botón con los colores del theme en vez de los del diseño, una imagen sin su
altura fija.

**Causa**: importar **no genera CSS**. El fichero `uploads/betheme/css/post-{ID}.css` se escribe solo
al guardar en el VB (`visual-builder.php:354` → `Mfn_Helper::preparePostUpdate()`). Antes de ese
guardado no existe ni una regla: los `css_*` están en `mfn-page-items` pero nadie los ha compilado.
Lo que sí se ve sin guardar es lo que no depende del CSS local: estructura, textos, imágenes y los
estilos que vengan de Theme Options.

**Solución**: abrir la página en el Visual Builder y **guardar una vez**. Es la misma causa de la
trampa 6 vista desde el otro lado: ahí el disparador era escribir `mfn-page-items` por código, aquí es
importar por el panel. En ambos casos el remedio es un guardado en el VB (o invocar
`Mfn_Helper::preparePostUpdate($plano, $post_id)`).

**Cómo confirmarlo en un minuto**, sin adivinar:

```bash
ls -la wp-content/uploads/betheme/css/post-{ID}.css      # ¿existe? ¿fecha posterior al import?
grep -c "mcb-item" wp-content/uploads/betheme/css/post-{ID}.css
```

Si el fichero no existe o es anterior al import, el JSON no tiene nada que ver.

**Ojo con el CSS heredado**: que `post-{ID}.css` exista y tenga miles de reglas no significa nada.
El import regenera **todos** los `uid` (`unique_ID_reset`, `helper.php:232-292`), y las reglas se
indexan por `.mcb-item-{uid}`: tras importar, el CSS anterior queda huérfano por completo. Sirve de
poco comparar tamaños; hay que buscar un valor concreto del diseño:

```bash
grep -c "background-color:#001689" wp-content/uploads/betheme/css/post-{ID}.css
```

**Y guardar no siempre basta**: si la página lleva un query loop de wrap con varios items directos,
ese primer guardado además **borra** la tarjeta (trampa 20). Comprobar E016 antes de importar.

Nota sobre `preparePostUpdate`: recibe una **lista plana** de elementos (`class-mfn-helper.php:41`,
`foreach ($object as $item)`), no el árbol de secciones. La aplana el JS del VB al guardar. Por eso un
guardado parcial o un elemento que el panel no haya registrado se queda sin CSS.

### Trampa 20 — la tarjeta de un query loop de wrap va en un wrap anidado (medido en BD, 2026-07-29)

| Query loop en | Qué debe contener | Envoltura de cada iteración |
|---|---|---|
| **Sección** (`attr.type: "query"` en la sección) | wraps | `.mfn-queryloop-item-wrapper` alrededor de los wraps |
| **Wrap** (`attr.type: "query"` en el wrap) | **UN wrap anidado** (`item_is_wrap: 1`) con los items dentro | ídem alrededor del contenido del wrap |

Un solo item directo también es válido — lo exporta el propio VB
(`examples/example1/about-us.json` `$[1].wraps[4]`: loop en slider con un único `image`). Lo que
rompe es **agrupar varios items sueltos** en el wrap del loop.

**Medición** (post 715 del entorno de pruebas): se importó un JSON de 5 secciones / 24 wraps /
**53 items**, con la tarjeta del loop como 5 items directos (`plain_text`, `image`, `heading`,
`button`, `plain_text`). Tras **un** guardado en el VB, la BD contenía:

```
wrap query c55fb4303  (grid, per_page=12)
  └ item c88184b59  item_is_wrap=1  hijos=0      ← los 5 items han desaparecido
```

**49 items** guardados. El resto de la página (24 wraps) intacto.

**Mecanismo**: el front envuelve cada iteración en `.mfn-queryloop-item-wrapper`
(`class-mfn-builder-front.php:2310`, `:2489`), y el VB añade el suyo al activar el loop
(`scripts.js:7364`). Al reconstruir el árbol para guardar, `prepareForm.items()` baja por una
cascada de `.children()` (`scripts.js:2317-2323`) y resuelve ese contenedor como wrap anidado:
entra por la rama `jsclass == 'wrap'` (`scripts.js:2372-2377`), le asigna `items: []` y delega en
`nested_items()`, que no encuentra los hijos donde los espera. Se guarda el envoltorio vacío.

**Consecuencia en cascada** — explica tres síntomas que parecen independientes:

1. Los elementos del loop no abren opciones: ya no existen.
2. El botón sale sin los colores del diseño: sin nodo no hay entrada en la lista plana, y
   `preparePostUpdate` no escribe ninguna regla para él.
3. La imagen sale sin altura: idéntico motivo.

**Forma correcta**, la que exporta el propio VB (`examples/example2/home.json`: wrap query →
`item_is_wrap: 1` → `image` + `button` + `heading`):

```json
{ "attr": { "type": "query", "grid": "grid", "...": "..." },
  "items": [
    { "uid": "...", "jsclass": "wrap", "icon": "wrap", "title": "Wrap", "item_is_wrap": 1,
      "size": "1/1", "tablet_size": "1/1", "mobile_size": "1/1", "attr": {},
      "items": [ "...los items de la tarjeta..." ] }
  ] }
```

Validador: **E016**.

Con `grid` en el wrap del loop, los `.mfn-queryloop-item-wrapper` son las celdas del grid: una
tarjeta por post. Para estilar la tarjeta completa (fondo, padding, borde, radio) están los campos
`css_queryloop_item_*` **del wrap**. Ese grupo **no incluye `position`**, así que no hay contenedor
posicionado fiable para superponer un item en absoluto: si el diseño pide un badge sobre la imagen,
`banner_box` (`image` + `overlay` + `bb_badge` + `bb_badge_pos`) lo resuelve en un solo item.

### Trampa 18 — en el VB solo la primera tarjeta del loop es interactiva

`iframe.css:1544`:

```css
.mfn-queryloop-item-wrapper ~ .mfn-queryloop-item-wrapper { opacity: .5; pointer-events: none; }
```

Es deliberado, y el PHP va en la misma dirección: solo la iteración 0 recibe `vb-item`, `data-uid` y
la barra de herramientas del módulo — `class-mfn-builder-front.php:2793`, `if( $vb && !$w_iterate )`.
Las iteraciones siguientes son `<div class="column mcb-column ...">` sin nada a lo que enganchar.

**Editar siempre sobre la primera tarjeta.** Si un elemento no responde, comprobar antes de nada que
no se está pulsando en una iteración atenuada; no es un fallo del JSON. Si tampoco responde en la
primera, entonces el elemento no existe: ver trampa 20.

### Trampa 19 — switchers de fondo

`css_*_background_color` y `css_*_gradient` están condicionados por `background_switcher`
(`attr_id` `background_switcher_button`, `background_switcher_ql`, etc.). El CSS se genera igual,
pero sin el switcher el control queda **oculto en el panel**: quien edite después no ve el valor y lo
sobrescribe sin querer. Emitir siempre `"background_switcher": "default"` (o `"gradient"`) junto al
subcampo. Validador: **W064**.

### Trampa 21 — el `gap` no existe fuera del grid (por qué una fila de tarjetas va en grid)

Los dos campos de separación del wrap están condicionados y su selector exige la clase de grid:

```php
// class-mfn-builder-fields.php:3582-3600
'id' => 'css_grid_columns_gap',
'selector' => '.mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement .mcb-wrap-inner',
'condition' => array( 'id' => 'wrap_grid', 'opt' => 'is', 'val' => 'grid' ),
```

Y la clase solo se añade si el wrap declara `grid` (`class-mfn-builder-front.php:1528`). Consecuencias
al maquetar una fila de N tarjetas:

| Enfoque | Separación entre tarjetas | Igualar alturas | Wraps anidados |
|---|---|---|---|
| N wraps hermanos `1/4` | **No configurable**: gutter por defecto del theme (~2%); solo se altera con `css_advanced_margin` por wrap, y el margen come ancho de columna | `classes: "equal-height-wrap"` en la sección | 0 |
| 1 wrap `1/1` con `grid` + N subwraps | `column-gap`/`row-gap` exactos y por breakpoint | gratis (las celdas del grid se estiran) | N (un W005 cada uno) |

Regla práctica: **si el diseño especifica el hueco entre tarjetas, grid**. Los hermanos con `size`
quedan para columnas de contenido suelto (titular + botón, texto + imagen), donde el hueco es
tipográfico y no una medida del diseño.

Detalles del subwrap-tarjeta:

- `size`/`tablet_size`/`mobile_size` = `1/1` (el reparto lo hace `css_grid_columns`, no el `size`).
- `height_switcher: "custom"` + `css_advanced_height` `{"desktop": "100%"}` sobre `.mcb-wrap-inner`:
  sin esto el fondo/borde de la tarjeta no llena la celda estirada.
- `css_advanced_align_content: "space-between"` para clavar el botón abajo.
- El `margin-bottom` por tarjeta sobra: lo cubre `css_grid_rows_gap`.

### Trampa 22 — anchos custom y saltos de fila inesperados

`.section_wrapper` es flex con `wrap`. Al fijar `width_switcher: "custom"` + `css_advanced_flex`, el
salto de fila lo decide el ancho en px, no el `size`: cualquier wrap posterior que quepa en el
espacio libre **sube a la fila anterior**. Casos reales medidos sobre un contenedor de 1656px:

- titular 1119px + primera cifra 180px = 1299px → la cifra se coloca a la derecha del titular.
- titular 650px + tarjeta 500px = 1150px → la tarjeta sube a la fila del titular.

Solución: el bloque que debe ocupar fila propia va en un wrap `1/1` **sin ancho custom**, y el ancho
del diseño se consigue con el `size` del item de dentro (`2/5` ≈ 650px, `2/3` ≈ 1104px sobre 1656px)
más `css_advanced_justify_content` en el wrap si hay que centrarlo. Los anchos custom se reservan
para wraps que sí comparten fila a propósito (tarjeta 500px + texto 564px con la sección en
`justify-content: space-between`).

### Trampa 23 — cifras: `counter`, no `plain_text` (y cómo no estropearlo)

Un bloque de estadísticas del Figma (“+1.000 / PROFESIONALES EN PLANTILLA”) se ve como texto plano,
pero el elemento correcto es **`counter`**: anima de 0 al valor al entrar en viewport y ya trae la
estructura completa. Maquetarlo con dos `plain_text` funciona y pasa el validador, pero entrega un
bloque muerto que además el cliente no puede editar como cifra en el panel.

Estructura que genera el shortcode (`theme-shortcodes.php:7770-7800`):

```
.counter.counter_vertical.animate-math
  └ .icon_wrapper        ← solo si icon o image
  └ .desc_wrapper
      └ .number-wrapper  → .prefix + .number + .postfix
      └ .title
```

Cada parte tiene sus propios campos (`css_counternumber-wrappernumber_typography`,
`css_counternumber-wrapperprefix_color`, `css_countertitle_typography`…), así que el diseño se
reproduce sin tocar HTML.

Mapa Figma → campos:

| En el diseño | Campo |
|---|---|
| `+`, `€`, `~` | `prefix` |
| la cifra | `number` — **entero pelado**, sin puntos ni símbolos |
| `%`, `k`, `+` final | `label` (es el *postfix*, pese al nombre) |
| descripción bajo la cifra | `title` + `title_tag` |
| velocidad | `duration` en ms (ej. `"1500"`) |

Tres trampas concretas:

1. **`icon` e `image` hay que vaciarlos explícitamente.** El `std` de `icon` es `icon-lamp`
   (`bebuilder-28.1.3.js`, campo `icon`), y el shortcode pinta `.icon_wrapper` si hay cualquiera de
   los dos. Sin `"icon": "", "image": ""` aparece una bombilla que el diseño no tiene.
2. **`number` debe ser un entero.** El JS anima `data-to` con
   `Math.floor(this.property)` (`js/scripts.js:1441-1455`): `"1.000"` o `"98%"` rompen el contador.
3. **`thousands_separator` solo admite `""`, `"comma"` y `"space"`** — no hay opción de punto. Para
   miles en español, `"space"` (`1 000`, la forma que recomienda la RAE). Si el cliente exige
   `1.000` literal, entonces sí `plain_text` estático, **avisando de que se pierde la animación**.

Además, la animación puede estar apagada en todo el sitio con la opción `math-animations-disable`
de Theme Options (`theme-shortcodes.php:7728`): si las cifras salen fijas, mirar ahí antes que al JSON.

Ejemplo mínimo fiel a un diseño “+1.000 profesionales en plantilla”:

```json
{
  "type": "counter", "uid": "itm000001",
  "size": "1/4", "tablet_size": "1/4", "mobile_size": "1/2",
  "attr": {
    "icon": "", "image": "",
    "prefix": "+", "number": "1000", "label": "",
    "thousands_separator": "space", "duration": "1500", "type": "vertical",
    "title": "Profesionales en plantilla", "title_tag": "p"
  }
}
```

### Trampa 24 — medios: siempre desde la Media Library del destino y como `URL#ID`

**Síntoma**: las imágenes "se ven" pero sin `srcset` ni dimensiones (CLS, LCP alto, `size` ignorado),
o dejan de verse al día siguiente, o desaparecen al pasar de desarrollo a producción.

**Causa**: `sc_image()` (`theme-shortcodes.php:8116-8180`) resuelve `src` en tres pasos: con
`#ID` usa el adjunto directamente (`wp_get_attachment_image()` → `srcset`, `sizes`, `alt`,
`width`/`height`); sin `#ID` hace `attachment_url_to_postid()` por imagen y por render
(`theme-functions.php:2280`), que devuelve 0 si la URL difiere en algo de la guardada (http/https,
dominio, `-scaled`, sufijo de tamaño); y con 0 cae a un `<img src>` crudo. Las URLs que devuelve el
MCP de Figma (`figma.com/...` firmadas o `localhost:3845/assets/...`) son temporales.

**Regla**: todo medio se descarga a `proyectos/<cliente>/assets/`, se sube al WordPress destino, se
registra en `assets/manifest.json` (`id` + `url`) y se referencia con `media(MAN, "fichero")` →
`URL#ID`, que es el formato del export real (`examples/example2/home.json:475`). Flujo completo,
subida por wp-cli/REST, SVG (`--user=` con `edit_theme_options`) y vídeo en
`docs/bebuilder/09-medios-imagenes-video.md`.

### Trampa 25 — item `video` HTML5: `video: ""` obligatorio

El campo `video` (ID de YouTube/Vimeo) trae default `n7-F-FMzM7Q` y `sc_video()` decide con
`if ($video) { iframe } elseif ($mp4) { <video> }` (`theme-shortcodes.php:12960-13020`). Si se
rellena `mp4` sin vaciar `video`, la página muestra un YouTube ajeno. Además: `placeholder` es el
poster; `html5_parameters` es un código (`a;;l;m;i` = autoplay loop muted playsinline); y
`object_fit`/`object_position` solo se aplican si van **ambos** `css_video_width` y
`css_video_height`. Vídeo de fondo de sección: `background_switcher: "video"` + `bg_video_mp4`
(`URL#ID`) + color de respaldo, porque el poster solo sale del deprecado `bg_image`
(`front.php:928`). Doc 09 §5.

## 3. Correcciones a documentación previa del proyecto

- **FALSO: "item con `item_is_wrap` sin `type` → error 500 en import admin-ajax".**
  El nested wrap sin `type` es la forma canónica y está soportada en front (`front.php:2569`),
  helper y VB. El origen del mito: warnings PHP 8 del **builder clásico admin** (formulario viejo)
  que con `display_errors` parecen un 500. Regla real: nested wraps OK para VB; evitarlos solo si
  la página debe editarse con builder clásico/Blocks Classic.
  **El 500 real de admin-ajax tiene otra causa, ya identificada**: un CPT desactivado en Theme
  Options (trampa 15). Si aparece un 500 al importar, mirar ahí antes que al JSON.
- **Fichas de `builder-elements/*.md` regeneradas (2026-07)**: el antiguo `extract_builder_elements.py`
  (parser regex) producía fichas corruptas (27% cobertura, id↔type desalineados, definiciones inline
  equivocadas para `heading`/`button`/`image`/`blockquote`/`code`/`divider`). Sustituido por
  `builder-elements/_generator/` (extract.php ejecuta el PHP real + generate_fichas.py). Las 167 fichas
  actuales son fiables; regenerar tras cada actualización del theme.
- El shortcode inline `heading` usa `tag`/`content`; el **item** `heading` usa `title`/`header_tag`.
  Mezclarlos produce títulos vacíos.
- **FALSO: "todo campo `dimensions` lleva objeto `{top,right,bottom,left}`"** (docs 02 y 03 anteriores,
  y las fichas hasta 2026-07). Hay **dos formatos incompatibles** de `dimensions`, discriminados por la
  clave `version` de la definición del campo. El reparto es limpio, sin excepciones (660 definiciones):

  | `version` | Campos | Formato de `val` por dispositivo |
  |---|---|---|
  | `"separated-fields"` | solo `margin` (171) y `padding` (150) | objeto `{top,right,bottom,left}` |
  | ausente | `border-width` (171), `border-radius` (163) | string shorthand `"1px 1px 1px 1px"` |

  Con objeto en un `border-*` fallan las dos mitades del sistema:
  1. **CSS**: `class-mfn-helper.php:260` concatena a ciegas `$style_name.'-'.$v` y escribe
     `border-width-top: 1px` — propiedad inexistente, el navegador la descarta y el borde no se ve.
     Con `padding` sale `padding-top`, que sí es válida: de ahí que nadie lo notara antes.
  2. **Panel del VB**: `forms/fields/dimensions.js:9` solo parsea string (`value.split(' ')`); con objeto
     `splited_value` queda vacío, los 4 inputs salen en blanco (`:78`) y el hidden guarda
     `"[object Object]"` (`:30`), que corrompe el valor al siguiente guardado.

  Orden del shorthand: `border-width` = `top right bottom left`; `border-radius` =
  `top-left top-right bottom-right bottom-left` (`dimensions.js:7`). Confirmado contra el export real
  del VB en `examples/example1/about-us.json` (`"val": {"desktop": "1px 1px 1px 1px"}`).
  Las fichas ya lo reflejan campo a campo desde la regeneración de 2026-07-29.

## 4. Checklist antes de entregar JSON

**Automatizado**: casi todo este checklist lo comprueba el validador, que contrasta el JSON contra
el catálogo real de campos (`builder-elements/_elements.json`) y contra el comportamiento
verificado de `class-mfn-helper.php` y `class-mfn-builder-front.php`:

```bash
python3 tools/validate_bebuilder_json.py salida.json --strict
```

Exit 0 = entregable; 1 = errores (corregir); 2 = solo warnings; 3 = JSON no parseable.
`--fix -o ok.json` corrige lo mecánico. Códigos y evidencia: `tools/README.md`.

Checklist manual (lo que el validador no puede juzgar por sí solo):

- [ ] Raíz = array de secciones; cada sección con `attr` y `wraps`.
- [ ] Toda sección: `width_switcher` explícito (`"full"`/`""`/`"custom"`).
- [ ] Todo wrap: `size`, `tablet_size`, `mobile_size` (fracciones válidas).
- [ ] Todo item: `type` válido (o `item_is_wrap: 1` + `items`), `size`, `tablet_size`, `mobile_size`, `uid`.
- [ ] Ningún atributo legacy inline (lista doc 02 §7) ni `style=""` en HTML de `content`.
- [ ] Todos los `css_*` con `selector` (copiado del PHP, con `mfnuidelement`), `style`, `val`.
- [ ] **Responsive contemplado en todo el documento** (regla 5): `tablet_size`/`mobile_size` en
      cada wrap e item, y valor `mobile` en espaciados, tipografías y cualquier regla de layout
      que deba cambiar de tamaño. Nunca entregar un JSON solo con `desktop`.
- [ ] **Márgenes y paddings en `rem`** (regla 6). `px`/`em` solo fuera de `padding`/`margin`.
- [ ] `dimensions`: objeto `{top,right,bottom,left}` **solo** en `margin`/`padding`;
      `border-width`/`border-radius` en string shorthand (`"1px 1px 1px 1px"`). Trampa 14.
- [ ] Gradientes/transform/filter con `string`.
- [ ] `heading`: `title` + `header_tag`. `column`/`visual`: `content` HTML limpio semántico.
- [ ] Espaciados vía `css_advanced_margin`/`css_advanced_padding` (nunca inline): headings
      margin-bottom ~1.5rem, párrafos ~1rem (convención del proyecto).
- [ ] Columnas = wraps hermanos o wrap grid; un elemento por celda.
- [ ] **Elemento elegido por función, no por apariencia** (regla 9.bis): cifras → `counter`
      (`icon`/`image` vacíos, `number` entero, `prefix`/`label` para símbolos, `title` para la
      descripción, `thousands_separator: "space"` en español). Pestañas → `tabs`, acordeón → `faq`,
      testimonio → `testimonial`. Nunca `plain_text` estático para un bloque que el theme ya
      resuelve animado y editable. Trampa 23.
- [ ] **Filas de tarjetas con hueco definido en el diseño → wrap grid + un subwrap por tarjeta**
      (regla 8.bis, trampa 21), con `height: 100%` en el inner del subwrap. Nunca wraps hermanos
      `1/4` si el diseño fija el gap: en flexbox no hay `gap`.
- [ ] Ningún wrap con ancho custom colocado antes de otro que deba abrir fila nueva (trampa 22):
      el bloque de fila propia va en un wrap `1/1` y su ancho lo pone el `size` del item.
- [ ] Nested wraps (`item_is_wrap`) solo si el destino es Visual Builder, y **nunca más de un nivel**
      (trampa 16).
- [ ] Query loops: comprobar que el CPT consumido está **activo** en el destino (trampa 15).
- [ ] **Medios** (doc 09, trampas 24/25): todos los del diseño subidos al destino y en
      `assets/manifest.json`; `src`, `bg_video_mp4`, `mp4`, `placeholder` y fondos como `URL#ID`;
      `grep -c "figma.com\|localhost:3845\|placeholders/image.svg" salida.json` → 0; `alt` en
      imágenes informativas; item `video` HTML5 con `video: ""`; sección con vídeo con color de
      respaldo. Medios no conseguidos, listados como pendientes en la entrega.
- [ ] Paridad VB deseada → incluir `icon`, `jsclass`, `title`, `ver` (opcionales pero exportables).
- [ ] Sin `attr.vb`, `attr.vb_postid`, `attr.rwd`.

## 4.bis Comprobaciones en el sitio de destino (antes de importar)

El JSON puede ser perfecto y el import fallar igual. Verificar en el destino:

1. **CPT activos**: Theme Options → Post types. Si el JSON usa un query loop sobre `portfolio`
   (o cualquier CPT desactivable) y está desactivado, el loop sale vacío — y editar con el VB
   cualquier post de ese tipo da un 500 (trampa 15).
2. **Campos personalizados** que usen los tokens de dynamic data (`{postmeta:x}`): que existan.
3. **Medios subidos** (imágenes, SVG, vídeo) a la Media Library del destino y
   `assets/manifest.json` generado desde ese sitio: los `#ID` del JSON deben ser los de ese
   WordPress, no los de desarrollo. Si se migra de dev a prod, `wp search-replace` del dominio
   o manifest nuevo (doc 09, trampa M7).
4. **Formularios** (`cf7`): el `form` vacío no rompe nada, pero no pinta nada.

Si algo falla, activar el log antes de improvisar — la traza da fichero y línea en un renglón:

```php
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', false );   // en true corrompe el JSON de admin-ajax
```

```bash
grep -n "Fatal error\|Uncaught" wp-content/debug.log | tail
```

`WP_DEBUG_DISPLAY` en `false` no es cosmético: en `true`, los avisos de PHP se imprimen dentro de la
respuesta de `admin-ajax.php` y provocan un fallo distinto del que se está persiguiendo.

## 5. Patrones de maquetación

Ver `builder-elements/GUIA-MAQUETACIONES.md` (validada): hero con video, barra sólida + grid custom,
grid de categorías con query, card sobre imagen, partner + counters, CTA con overlay degradado,
imagen en posición absoluta "saliendo" del bloque.
