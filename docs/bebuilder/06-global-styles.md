# 06 — Global Styles (clases globales `be_classes`)

Cómo BeBuilder genera, guarda, exporta, importa y aplica los **Global styles**: estilos reutilizables
para títulos, textos, botones, secciones, wraps y cualquier elemento. Todo verificado contra el código
del theme (julio 2026).

> No confundir con:
> - **Presets** (panel «Presets», opción `mfn-presets`): plantillas de elemento completo, no estilos reutilizables vinculados.
> - **Global sections / Global wraps** (post type `template`): reutilización de *contenido*, no de estilos.
> - **Theme Options → Typography**: tipografía global del theme, otro sistema (`mfn_styles_dynamic()`).

---

## 1. Modelo mental

Un Global style es un **objeto tipo elemento fantasma**: mismo formato que un item del builder
(`{jsclass, uid, attr}`), pero:

- vive en `wp_options`, no en la página;
- su `uid` es también el **nombre de la clase CSS** que se imprime en el DOM (`be_<jsclass>_<rand>`);
- sus selectores `css_*` están reescritos para apuntar a esa clase en lugar de al uid de un elemento concreto;
- los elementos que lo usan lo referencian por uid en la propiedad **`be_classes`** (array, hermana de `attr`).

Consecuencia clave: **un Global style está atado a un `jsclass`**. Un estilo creado desde un `button`
solo puede aplicarse a otros `button`. No existen «estilos de texto» transversales: hay estilos de
`title`, de `divider_2`, de `list_2`, de `section`, de `wrap`, etc.

---

## 2. Dónde vive cada cosa

| Dato | Ubicación | Escritor |
|---|---|---|
| Definición de las clases | `wp_options.be_classes` (JSON) | `mfnvb_saveclasses()` — `visual-builder/visual-builder.php:510` |
| CSS compilado | `wp_options.be_classes` → clave `css` | mismo, L586 |
| Hoja de estilos real | `wp-content/uploads/betheme/css/be_classes.css` | `Mfn_Helper::generate_css()` — `functions/admin/class-mfn-helper.php:479` |
| Fuentes usadas por las clases | `wp_options.be_classes_fonts` (JSON array) | `visual-builder.php:573-583` |
| Referencia desde el contenido | `mfn-page-items` → cada bloque, clave `be_classes` | guardado normal de la página |
| Lista disponible en el builder | JS global `mfn.classes` | `visual-builder/classes/visual-builder-class.php:502` |

Estructura de la opción `be_classes`:

```json
{
  "builder": [ { "jsclass": "...", "type": "be_class", "title": "...", "uid": "be_...", "attr": {...} } ],
  "css": {
    "custom": {}, "desktop": { "<selector>": "prop:val;" },
    "laptop": {}, "tablet": {}, "mobile": {},
    "query_modifiers": {}, "fonts": ["Inter"], "sidemenus": []
  }
}
```

`builder` es la lista editable; `css` es caché de la última compilación (informativa: el front lee el
`.css`, no esta clave).

---

## 3. Formato exacto de un Global style

Creado en `mfn_classes.create()` — `visual-builder/assets/js/scripts.js:4073`:

```json
{
  "jsclass": "button",
  "type": "be_class",
  "title": "CTA primario",
  "uid": "be_button_k3f9a2xq",
  "attr": {
    "css_button_typography": { "selector": ".column.be_button_k3f9a2xq .button", "style": "typography", "val": { "desktop": { "font-size": "16px" } } },
    "button_style": "default"
  }
}
```

| Campo | Regla |
|---|---|
| `jsclass` | Copiado del elemento origen. Determina en qué elementos se puede usar |
| `type` | Literal `"be_class"` |
| `title` | Nombre visible. **Único**: la UI rechaza títulos repetidos (`scripts.js:4089`) |
| `uid` | `` `be_${jsclass}_${getUid()}` ``. `getUid()` = `Math.random().toString(36).substring(5)` (`scripts.js:194`), ~6-8 chars. **Es el nombre de la clase CSS** |
| `attr` | Solo las opciones seleccionadas en el modal + las «excepciones» (ver §4) |

---

## 4. Qué opciones entran en una clase

`mfn_classes.get_styles()` (`scripts.js:3920`) lista en el modal las opciones candidatas, y
`create()` (L4108-4113) las copia. Criterio:

1. `o.includes('css_')` **y** el usuario dejó marcada la opción en el modal (`mfn_classes.confirmed`), **o**
2. `o` está en `mfn_classes.exceptions`, o `` `${jsclass}_${o}` `` está en esa lista.

Además se descartan las opciones cuyo valor sea idéntico al default del elemento
(`mfn_classes.original`, L3926): una clase nunca guarda valores por defecto.

**Efecto lateral importante**: al crear la clase, las opciones `css_*` copiadas se **borran del elemento
origen** (`delete(edited_item.attr[o])`, L4111). Las «excepciones» NO se borran: quedan duplicadas en
elemento y clase.

### Lista completa de `exceptions` (`scripts.js:3493`)

Opciones NO-CSS que una clase global sí puede transportar (cambian markup, por eso al aplicarlas se
fuerza `re_render()`):

```
width_switcher, height_switcher, visibility,
banner_box_css_desc_justify, banner_box_css_desc_align, banner_box_style, banner_box_overlay,
banner_box_hover_effect, banner_box_image_height, banner_box_hidden_elements_mobile,
button_icon, button_icon_position, button_size, button_full_width, button_style,
divider_2_type, divider_2_align, divider_2_addon, divider_2_label, divider_2_image, divider_2_icon,
icon_2_hover, icon_box_2_icon_position, icon_box_2_icon_align, icon_box_2_hover,
image_mask_shape_type, image_mask_shape_size, image_mask_shape_position, image_image_height,
image_image_height_style, image_greyscale,
image_gallery_style, image_gallery_layout, image_gallery_columns, image_gallery_greyscale,
image_gallery_image_height,
list_2_type, list_2_starting, list_2_align, list_2_valign, list_2_divider, list_2_icon, list_2_image,
list_2_background_switcher,
toggle_type, toggle_starting, toggle_divider, toggle_open_first, toggle_open_all, toggle_open_more,
toggle_icon, toggle_active_icon, toggle_icon_animation
```

---

## 5. Reescritura de selectores (el paso crítico)

Los campos del theme definen selectores con placeholder `mfnuidelement`. Para una clase global ese
placeholder debe convertirse en la **clase**, no en un uid. Ocurre en dos sitios encadenados.

### 5.1 En JS, antes de enviar — `mfn_classes.ajax()` (`scripts.js:4133`)

```js
opt.selector = opt.selector
  .replaceAll('.mcb-section .mcb-wrap .mcb-item-mfnuidelement', '.column.'+uid)
  .replaceAll('.mcb-section .mcb-wrap-mfnuidelement',           '.wrap.'+uid)
  .replaceAll('mcb-section-mfnuidelement',                       uid);
```

| Selector original del campo | Selector guardado en la clase (`uid = be_x`) |
|---|---|
| `.mcb-section .mcb-wrap .mcb-item-mfnuidelement` | `.column.be_x` |
| `.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner` | `.column.be_x .mcb-column-inner` |
| `.mcb-section .mcb-wrap-mfnuidelement` | `.wrap.be_x` |
| `.mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner` | `.wrap.be_x .mcb-wrap-inner` |
| `.mcb-section-mfnuidelement` | `.be_x` |
| `.mcb-section-mfnuidelement .section_wrapper` | `.be_x .section_wrapper` |

### 5.2 En PHP, al compilar — `Mfn_Helper::mfnLocalStyle()` (`class-mfn-helper.php:404-428`)

La función **bifurca según el uid**:

```php
if( $uid && strpos($uid, 'be_') === false ) {   // elemento normal
    ... mfnuidelement → uid, mcb-column-inner → mcb-column-inner-{uid}, etc.
} else {                                        // GLOBAL STYLE
    $selector = str_replace('mcb-item-mfnuidelement',    $uid, $selector);
    $selector = str_replace('mcb-wrap-mfnuidelement',    $uid, $selector);
    $selector = str_replace('mcb-section-mfnuidelement', $uid, $selector);
}
```

Diferencias respecto a un elemento normal, todas relevantes:

- **NO** se sufijan `mcb-column-inner`, `mcb-wrap-inner`, `mcb-section-inner`, `section_wrapper`.
  Se quedan como clases genéricas dentro del contexto de la clase global.
- **NO** se antepone `section.` a `.mcb-section-mfnuidelement`.
- Solo actúa como red de seguridad para los `mfnuidelement` que el JS no cazó (selectores que no
  empiezan por el prefijo completo).
- El resto del pipeline es idéntico: `|` → `:`, limpieza de sufijos `_laptop/_tablet/_mobile/_v2`,
  prefijos/sufijos de valor (`url(...)`, `matrix(...)`, `0 0 ` en `flex`), tokens dinámicos
  (`{featured_image}` → `var(--mfn-featured-image)`).

**Especificidad**: el CSS de la página usa 3-4 clases encadenadas
(`.mcb-section .mcb-wrap .mcb-item-<uid> .button`), el global usa 2 (`.column.be_x .button`).
Por tanto **cualquier estilo local del elemento gana siempre al global**, sin necesidad de `!important`.
Es exactamente el comportamiento que anuncia la UI: *«Any local changes will overwrite the global styles»*
(`scripts.js:11440`).

---

## 6. Compilación a CSS

`mfnvb_saveclasses()` (`visual-builder.php:571`) llama:

```php
Mfn_Helper::preparePostUpdate( $all_classes['builder'], 'be_classes', 'mfn-be-classes-style' );
```

- Primer argumento: el **array completo de clases** (no la clase modificada). Cada guardado recompila
  todas las clases desde cero.
- `$post_id = 'be_classes'` → no es numérico, así que `preparePostUpdate()` **omite todas las escrituras
  de post meta** (`class-mfn-helper.php:350-390`, guardas `is_numeric($post_id)`), y `generate_css()`
  usa el nombre literal como fichero (L491): `uploads/betheme/css/be_classes.css`.
- El tercer argumento (`mfn-be-classes-style`) es irrelevante aquí por lo mismo: nunca se escribe meta.

Estructura del `.css` generado (`generate_css()` L503-594), idéntica a la de página:

```
<desktop>            → sin media query
@media(max-width: 1440px){ ... }   laptop
@media(max-width:  959px){ ... }   tablet
@media(max-width:  767px){ ... }   mobile
<custom>             → show/hide bajo breakpoint arbitrario
```

Se escribe con `WP_Filesystem::put_contents()`, sin minificar, sin cabecera de comentario.

---

## 7. Exportar / Importar

Panel lateral **Export / Import → Global styles**
(`visual-builder/partials/sidebar-export-import.php:37-66`).

### 7.1 Export

`scripts.js:12576`:

```js
$('#export-classes-data-textarea').val( JSON.stringify(mfn.classes) );
```

El export es **el array `builder` tal cual**, sin envoltorio y sin la clave `css`:

```json
[
  { "jsclass": "title", "type": "be_class", "title": "H2 Sección", "uid": "be_title_9fk2ax",
    "attr": { "css_title_typography": { "selector": ".column.be_title_9fk2ax .title", "style": "typography", "val": {"desktop": {"font-size":"32px","font-weight":"700"}} } } },
  { "jsclass": "button", "type": "be_class", "title": "CTA", "uid": "be_button_p1x8sd", "attr": { ... } }
]
```

Exporta **todas** las clases del sitio; no hay selección parcial. El botón usa `document.execCommand('copy')`
sobre el textarea.

### 7.2 Import — flujo

`mfn_classes.import` (`scripts.js:3618-3697`):

1. `JSON.parse` del textarea. JSON inválido → excepción en consola, sin aviso al usuario (solo se marca
   `.error` si el textarea está vacío).
2. `init()`: recorre una **copia profunda** y detecta duplicados por `uid` contra `mfn.classes`.
   A cada duplicado (en la copia) le asigna `uid = be_<jsclass>_<nuevoRand>` y `title += '_clone'`.
3. Sin duplicados → `import_data()` directo.
4. Con duplicados → modal «N duplicated styles detected» con tres salidas:
   - **Cancel** — nada.
   - **Overwrite** — envía `data` (los uids **originales**, sin clonar) → PHP reemplaza por uid.
   - **Keep both** — hace `data = duplicates` y envía **solo los clones**.
5. AJAX `action=mfnupdateclasses`, `type=import`, `val=JSON.stringify(data)`.
6. Respuesta = array `builder` actualizado → `mfn.classes = response` + `loopAllStyleFields()` (repinta
   el preview) + snackbar «Global styles imported.».

### 7.3 Import — lado PHP (`visual-builder.php:537-552`)

```php
$datas = json_decode( stripslashes($posted_data), true );
foreach( $datas as $pd ) {
    $index = array_search($pd['uid'], array_column($all_classes['builder'], 'uid'));
    if( $index !== false ) $all_classes['builder'][$index] = $pd;   // reemplaza
    else                   $all_classes['builder'][] = $pd;          // añade
}
```

Sin validación de esquema: se guarda lo que llegue. Después recompila `be_classes.css` y actualiza fuentes.

### 7.4 Import en migración de sitio completo

El importador de demos/backup trae las clases junto a las opciones
(`functions/importer/class-mfn-importer-helper.php:656-663`):

```php
update_option( 'be_classes', $options['be_classes'] );
Mfn_Helper::preparePostUpdate( json_decode($options['be_classes'], true)['builder'], 'be_classes', 'mfn-be-classes-style' );
update_option( 'be_classes_fonts', $options['be_classes_fonts'] );
```

Aquí el valor es el JSON **completo** (con `builder` y `css`), no el array plano del export manual.
Además `be_classes` y `be_classes_fonts` figuran en la lista de transients/options que el importador
limpia antes (L116).

---

## 8. Aplicación en el front

`Mfn_Builder_Front::__construct()` (`class-mfn-builder-front.php:124-130`) carga el índice:

```php
$this->be_classes[ $bc['uid'] ] = $bc['attr'];   // uid → attr
```

Y en cada nivel se hace lo mismo — sección L429, wrap L1543, item L2574:

```php
foreach($item['be_classes'] as $bc) {
    $item_class[] = $bc;                                   // 1) la clase va al DOM
    if( isset($this->be_classes[$bc]) ){
        if( ($item['attr']['width_switcher'] ?? '') == 'default' ) unset($item['attr']['width_switcher']);
        $item['attr'] = array_merge($this->be_classes[$bc], $item['attr']);   // 2) merge de atributos
    }
}
```

Dos mecanismos simultáneos, no uno:

1. **CSS**: la clase se imprime en el markup (`<div class="column mcb-column be_button_x ...">`, L2801;
   wrap `wrap mcb-wrap be_wrap_x`, L1525; sección `section mcb-section be_section_x`, L883) y la casa
   `be_classes.css`.
2. **Atributos**: los `attr` de la clase se fusionan en el elemento, con `array_merge(clase, elemento)`
   → **el elemento gana** en claves compartidas. Esto es lo que hace que funcionen las «excepciones»
   no-CSS (`button_style`, `visibility`, `width_switcher`…), que alteran el HTML renderizado.

Orden con varias clases: la **primera** del array manda, porque tras la primera iteración sus claves ya
están en `$item['attr']` y ganan en los merges siguientes. En cambio el CSS se emite en el orden de
creación dentro de `be_classes.css` — es decir, **atributos y CSS pueden resolver conflictos en orden
distinto**. En la práctica la UI impide el caso: solo permite una clase por elemento (§10).

### Encolado de la hoja

`enqueue_local_style()` (L195-204), solo cuando **no** se está dentro del builder:

```php
if( file_exists( uploads/betheme/css/be_classes.css ) )
    wp_enqueue_style( 'mfn-be-classes-styles-'.time(), <url>, false, time(), 'all' );
```

Va **antes** del CSS local de la página (encolado después en la misma función), lo cual refuerza el
orden de cascada correcto. Cache busting con `time()`: sin caché de navegador.

> **Código muerto**: `mfn_styles_be_classes()` (`functions/theme-head.php:816-824`) lee la opción y
> **no devuelve nada** — el `wp_add_inline_style('mfn-be-classes', ...)` de L718 no aporta CSS. Los
> global styles **siempre** se sirven como fichero, incluso con `local-styles-location = inline`.

---

## 9. Comportamiento dentro del builder (preview y edición)

| Pieza | Dónde | Qué hace |
|---|---|---|
| Panel «Global styles» del sidebar | `scripts.js:11413` | Se inyecta en todos los elementos salvo `placeholder` y wraps globales. Botones: crear / listar / autocompletar |
| Autocomplete de clases | `mfn_autocomplete` `scripts.js:3350+` | Filtra por `n.uid.includes(edited_item.jsclass)` (L3451). `singular: true` → **una sola clase por elemento** (L3447) |
| Aplicar una clase | `mfn_autocomplete.add()` L3402 | Borra del elemento los valores que igualan el default, añade el uid a `be_classes`, añade la clase al DOM del preview, y `re_render()` si la clase trae alguna «excepción» |
| Editar una clase | `mfn_classes.edit()` L4202 | `edited_item = <la clase>` y `sidebar_form.is_class = <uid>`: el formulario del sidebar edita el objeto clase en lugar del elemento |
| CSS en vivo al editar clase | `addLocalStyle()` L10131-10140 y `changeInlineStyles()` L10204 | Reescribe `mcb-item-mfnuidelement → mcb-column.<uid>`, `mcb-wrap-mfnuidelement → mcb-wrap.<uid>`, `mcb-section-mfnuidelement → mcb-section.<uid>`, y `.mcb-section .mcb-wrap .be_ → .column.be_`. Y **no** antepone `html ` cuando el uid contiene `be_` (L10171) |
| Guardar cambios de clase | botón `.mfn-class-editor-update` L3515 | `mfn_classes.ajax(edited_item)` + `re_render()` de todos los elementos del lienzo que llevan esa clase (L4157-4168) |
| Descartar | `.mfn-class-editor-dismiss` L3598 | Restaura `mfn_classes.backup.attr` |
| Renombrar / Clonar / Borrar | `mfn_classes.list_modal` L3698-3919 | Clonar reescribe los selectores del clon con el uid nuevo (L3818). Borrar → AJAX `type=delete` |
| Valores heredados en el formulario | `forms/form.js:33-41` + `values(obj, field, is_class=true)` L418 | Los valores de la clase se cargan como **placeholders** (`mfn-placeholder-inherited-class`), no como valores: el campo se ve relleno en gris pero el elemento no los guarda hasta que se editan |

> Ojo con el preview: usa `.mcb-column.<uid>` / `.mcb-section.<uid>`, mientras que el CSS definitivo
> guardado usa `.column.<uid>` / `.<uid>`. Ambos casan con el DOM real (el div lleva `column mcb-column`),
> pero la **especificidad difiere**, así que un caso límite puede verse distinto en builder y en front.

---

## 10. Fuentes (`be_classes_fonts`)

`preparePostUpdate()` recolecta en `$return['fonts']`:

- `attr.used_fonts` (CSV) de cada clase (L109-112),
- cualquier valor bajo una clave que contenga `font-family` (L234-237, L255-258, L274-277), que además
  se envuelve en comillas simples en el CSS.

`visual-builder.php:576-583`:

```php
if( !empty($styles['fonts']) ){
    $updated = array_merge($styles['fonts'], get_option('be_classes_fonts'));
    update_option('be_classes_fonts', json_encode(array_unique($updated)));
}
```

`theme-head.php:421` lo lee para encolar Google Fonts.

> **Trampa**: la lista solo crece. El `delete_option()` del `else` es inalcanzable cuando ya no queda
> ninguna fuente (la guarda exterior exige `!empty($styles['fonts'])`), así que una fuente retirada de
> todas las clases sigue cargándose hasta limpiar la opción a mano.

---

## 11. Cómo generar esto desde muffinAI

**Un JSON de página no puede crear global styles.** Viven en `wp_options`, fuera del contenido. El flujo
correcto para entregar un diseño que los use son dos artefactos:

1. `global-styles.json` — array plano, se pega en *Export/Import → Global styles → Import*.
2. El JSON de página, cuyos bloques referencian los uids.

Referencia desde un item (hermana de `attr`, **nunca dentro** de `attr`):

```json
{
  "uid": "abc123xyz",
  "type": "button",
  "jsclass": "button",
  "size": "1/3",
  "be_classes": ["be_button_p1x8sd"],
  "attr": { "button_title": "Comprar" }
}
```

Reglas al escribir el `global-styles.json`:

| Regla | Motivo |
|---|---|
| `uid` **debe** empezar por `be_` | Bifurca `mfnLocalStyle()`; sin ese prefijo el CSS se genera como si fuera un elemento y no casa nada |
| `uid` **debe** contener el `jsclass` | El autocomplete filtra con `uid.includes(jsclass)`; si no, la clase existe pero es inseleccionable |
| Patrón recomendado: `be_<jsclass>_<8 chars a-z0-9>` | Igual que `getUid()` |
| `title` único | La UI bloquea duplicados; por import no se valida y quedan dos con el mismo nombre |
| `jsclass` presente y válido | `mfn_classes.edit()` aborta con error de consola si falta |
| Selectores ya reescritos a `.column.<uid>` / `.wrap.<uid>` / `.<uid>` | El PHP no rehace el prefijo largo; si dejas `.mcb-section .mcb-wrap .mcb-item-mfnuidelement`, solo se sustituye el tramo `mcb-item-mfnuidelement` y sale `.mcb-section .mcb-wrap .be_x`, que sigue funcionando pero **con más especificidad que el CSS local**, invirtiendo la prioridad esperada |
| Pseudo-clases con `\|` (`\|hover`) | Igual que en los `css_*` de página (ver 02) |
| Nada de valores por defecto | La UI los descarta; incluirlos infla el CSS sin efecto |
| No dupliques en el elemento lo que ya está en la clase | El atributo local gana y anula la clase |
| Un `be_classes` por elemento | La UI es `singular`; más de uno funciona en PHP pero es territorio no probado |

Después del import hay que **recargar el builder** (o la página del front): `be_classes.css` se regenera
en el import, pero `mfn.classes` solo se refresca en la pestaña que hizo el import.

---

## 12. Trampas verificadas

1. **«Keep both» pierde estilos.** `mfn_classes.import.data = mfn_classes.import.duplicates` (`scripts.js:3656`)
   sustituye el lote completo por solo los duplicados clonados. Si importas 5 estilos y 2 son duplicados,
   con «Keep both» se importan **únicamente esos 2 clones**; los 3 nuevos se pierden sin aviso.
   Workaround: importar los nuevos en un lote aparte, o usar «Overwrite».
2. **Crear una clase muta el elemento origen.** Los `css_*` elegidos se borran de su `attr`. Si luego se
   borra la clase, el elemento se queda sin esos estilos (no hay rollback).
3. **Borrar una clase no limpia las referencias** en `mfn-page-items`. Quedan uids huérfanos en
   `be_classes`; el front los imprime como clase CSS inexistente y el builder los purga en silencio al
   abrir el elemento (`scripts.js:11410`, `11431`).
4. **El filtro del autocomplete es por substring.** Editando un elemento `icon` se listan también las
   clases `be_icon_box_2_*`, y aplicarlas produce selectores que no casan.
5. **Cada guardado recompila todas las clases.** Con muchas clases, cada edición reescribe el fichero
   completo; y un fallo de permisos en `uploads/betheme/css/` deja el CSS antiguo sin error visible.
6. **Las «excepciones» no-CSS quedan duplicadas** en clase y elemento; como el elemento gana en el merge,
   cambiarlas en la clase no afecta a los elementos que ya la usaban con ese valor propio.
7. **`be_classes.css` nunca se sirve inline**, ni siquiera con `local-styles-location = inline`
   (`mfn_styles_be_classes()` es código muerto). Es una request extra siempre.
8. **Dentro del builder no se encola** `be_classes.css` (`!self::$is_bebuilder`): el preview lo reconstruye
   con `<style>` inyectados por `loopAllStyleFields()`.
9. **Sin `WP_Filesystem` escribible no hay CSS**, pero la opción `be_classes` sí se guarda: la clase existe,
   se aplica al DOM y no pinta nada.

---

## 13. Mapa de código

| Fichero:línea | Rol |
|---|---|
| `visual-builder/visual-builder.php:508-593` | `mfnvb_saveclasses()` — AJAX `mfnupdateclasses` (save / delete / import), recompilación y fuentes |
| `visual-builder/classes/visual-builder-class.php:489-502` | Inyecta `mfn.classes` en el JS del builder |
| `visual-builder/partials/sidebar-export-import.php:37-66` | Panel Export/Import de Global styles |
| `visual-builder/assets/js/scripts.js:3350-3478` | `mfn_autocomplete` — selección y aplicación de clases |
| `visual-builder/assets/js/scripts.js:3481-4223` | `mfn_classes` — modal, create, ajax, remove, edit, import, list_modal |
| `visual-builder/assets/js/scripts.js:718-...` | `loopAllStyleFields()` — repintado de CSS del preview, incluye `mfn.classes` |
| `visual-builder/assets/js/scripts.js:10131-10196` | `addLocalStyle()` — bifurcación `be_` en el preview |
| `visual-builder/assets/js/scripts.js:11406-11443` | Render del panel «Global styles» y aviso de sobrescritura |
| `visual-builder/assets/js/scripts.js:12576` | Volcado del export |
| `visual-builder/assets/js/forms/form.js:33-41`, `418-511` | Valores de la clase como placeholders heredados |
| `functions/admin/class-mfn-helper.php:404-428` | `mfnLocalStyle()` — bifurcación de selector por `be_` |
| `functions/admin/class-mfn-helper.php:479-596` | `generate_css()` — escribe `be_classes.css` |
| `functions/builder/class-mfn-builder-front.php:124-130` | Índice `uid → attr` |
| `functions/builder/class-mfn-builder-front.php:195-204` | Encolado de `be_classes.css` |
| `functions/builder/class-mfn-builder-front.php:429-438 / 1543-1552 / 2574-2582` | Merge y clase en el DOM (sección / wrap / item) |
| `functions/theme-head.php:421` | Fuentes de clases → Google Fonts |
| `functions/theme-head.php:816-824` | `mfn_styles_be_classes()` — **código muerto** |
| `functions/importer/class-mfn-importer-helper.php:656-663` | Import de clases en migración completa |
