# 08 — Tipografía y fuentes: Theme Options

Cómo BeTheme gestiona las fuentes desde **Theme Options** (no confundir con los packs de
iconos, ver [07-iconos.md](07-iconos.md)): selección de familia tipográfica por rol (Google
Fonts / sistema), tamaños, y subida de fuentes propias autoalojadas. Todo verificado leyendo
el código del theme y comprobado en vivo en el dev de Nordés Ancín.

## 1. Dos sistemas independientes

| Sistema | Qué hace | Fields |
|---|---|---|
| **Familia por rol** | Asigna una fuente (Google o del sistema) a cada rol semántico: contenido, menú, títulos, headings… | `font_select` |
| **Fuente propia autoalojada** | Sube `.woff`/`.ttf` propios y genera un `@font-face` con el nombre que le des | `text` + `upload` (repetibles) |

Ambos comparten el mismo almacén (`wp_options.betheme`, ver §2) y el mismo selector: una fuente
subida manualmente aparece en los desplegables de "familia por rol" bajo el grupo *Custom Fonts*.

## 2. Dónde vive todo: una única fila en `wp_options`

Todas las opciones del tema —no solo fuentes— se guardan en **una fila serializada**:

```
wp_options.option_name = 'betheme'     (id opt_name definido en muffin-options/options.php:38)
```

La clase `MFN_Options` (`muffin-options/options.php:12`) la carga entera en `$this->options` al
construirse (`get_option($this->args['opt_name'])`, L77) y expone lectura vía la función global:

```php
mfn_opts_get( 'font-content' )                    // → "Poppins"
mfn_opts_get( 'font-size-h1' )                    // → array( size, line_height, weight_style, letter_spacing )
```

No hay tabla propia, no hay CPT: es un array PHP plano con claves `id` de cada campo, tal cual
las define `muffin-options/theme-options.php`.

## 3. Familia por rol (`font_select`)

Sección `sections['font-family']`, `muffin-options/theme-options.php:8521`. Cada campo asigna
una fuente a un selector CSS fijo:

| `id` | Rol | Selector CSS objetivo (`data-csspath`) |
|---|---|---|
| `font-content` | Cuerpo de texto | `body, button, textarea, select, …` |
| `font-lead` | Párrafo destacado | `p.lead, p.big` |
| `font-menu` | Menú principal | `#menu > ul > li > a, a.action_button, …` |
| `font-title` | Título de página (Subheader) | `#Subheader .title` |
| `font-headings` | H1–H4 | `h1, h2, h3, h4, .text-logo #logo` |
| `font-headings-small` | H5–H6 | `h5, h6` |
| `font-blockquote` | Blockquote | `body blockquote` |
| `font-decorative` | Cifras decorativas (Chart, Counter, precio…) | varios |

El valor guardado es **el nombre de la fuente tal cual**, sin más estructura:
`"Poppins"`, `"Montserrat"`, `"Arial"` (sistema), o `"NombreDeFuenteCustom"` si es una fuente
subida manualmente. **Corrección (2026-09-07):** el `#` NO se guarda; solo existe dentro de `mfn_fonts()['custom']`
para el selector, `field_font_select.php` pinta el `<option>` sin él y `style.php` lo quita al consumir. Verificado en el dev:
`wp option pluck betheme font-headings` → `Avenir Medium`. Detalle en `temini/docs/betheme-ssh/05-fuentes.md`.

`font_select` construye la lista desde `mfn_fonts()` (`muffin-options/fonts.php:15`), que
devuelve tres grupos:

- `system` — Arial, Georgia, Tahoma, Times, Trebuchet, Verdana, y vacío (`""` = heredar)
- `custom` — fuentes subidas manualmente (§5), con prefijo `#`
- `all` — catálogo completo de Google Fonts embebido en el propio fichero (miles de nombres)

### Tamaños

Sección `sections['font-size']` (mismo fichero, campos `font-size-h1` … `font-size-h6`,
`font-size-content`, `font-size-big`, `font-size-menu`, cada uno con variantes `-tablet`/`-mobile`).
Campo tipo `typography`: valor = `{ size, line_height, weight_style, letter_spacing }`.
`weight_style` combina peso y estilo (`"600"`, `"700italic"`…).

## 4. Google Fonts: carga, subconjuntos y modo local

`sections['font-family']` también tiene el switch `google-font-mode` (L10681):

| Valor | Comportamiento |
|---|---|
| `''` (std) | Carga cada fuente desde `fonts.googleapis.com` en cada visita |
| `local` | Descarga los `.woff`/`.ttf` al servidor (botón "Download files") y los sirve desde `uploads/betheme/fonts/` |
| `disabled` | No carga ninguna Google Font (corta `mfn_head_google_fonts` en seco, `functions/theme-head.php:410`) |

Qué fuentes se piden a Google lo decide `mfn_fonts_selected()` (`functions/theme-head.php:267`):
recoge `font-content`, `font-menu`, `font-headings`, etc., **más** las fuentes usadas dentro del
Visual Builder (postmeta `mfn-page-fonts` de cada `template`/página, guardado como JSON al
guardar cada página — así una fuente elegida solo dentro de un elemento del builder también se
encola). `font-weight` y `font-subset` (checkboxes, misma sección, más abajo en el fichero)
controlan qué pesos/subconjuntos se piden.

El modo `local` lo ejecuta `Mfn_Builder_Ajax::_tool_regenerate_fonts()`
(`functions/builder/class-mfn-builder-ajax.php:274`, acción AJAX `mfn_regenerate_fonts`,
botón en *Herramientas*): recalcula la lista de fuentes en uso, **borra por completo**
`uploads/betheme/fonts/` y vuelve a descargar cada fuente desde Google. No hay forma de
descargar solo una fuente nueva sin repetir todas.

## 5. Fuentes propias autoalojadas (`font-custom*`)

Sección `sections['font-custom']`, `muffin-options/theme-options.php:9118`. Dos slots fijos
(`font-custom`/`font-custom2`) más slots dinámicos ilimitados que la UI añade con
"+ Add new font" (JS `mfn_new_font`, backend `custom_font_loader()`,
`muffin-options/options.php:2240`).

Por cada slot, 3 opciones:

| `id` | Tipo | Contenido |
|---|---|---|
| `font-custom{N}` | `text` | Nombre de la fuente (el que verá el usuario en los `font_select`) |
| `font-custom{N}-woff` | `upload` | URL del `.woff` subido a la Media Library |
| `font-custom{N}-ttf` | `upload` | URL del `.ttf` subido a la Media Library |

`N` vacío o `2` para los dos slots fijos; `3, 4, 5…` para los dinámicos. Cuántos dinámicos hay
lo cuenta el campo oculto `font-custom-fields` (entero). **Importante**: en cada carga,
`MFN_Options::_register_custom_fonts()` (`muffin-options/options.php:1012`) recorre los slots
`3..N`, **descarta los que tengan el nombre vacío y compacta los que quedan** reescribiéndolos
desde `font-custom3` hacia arriba. Por eso no hay "huecos": si borras el Font 2 de tres
dinámicos, el 3 pasa a ocupar el hueco del 2 en el siguiente guardado.

### Generación del `@font-face`

`mfn_styles_custom_font()` (`functions/theme-head.php:965`) recorre todos los slots con nombre
no vacío y genera, **en cada carga de página, sin caché ni fichero**:

```css
@font-face{
  font-family:"{font-custom}";
  src:url("{woff-url}") format("woff"), url("{ttf-url}") format("truetype");
  font-weight:normal; font-style:normal; font-display:swap
}
```

Se imprime inline vía `wp_add_inline_style('mfn-dynamic', …)` (`mfn_styles_inline()`,
`functions/theme-head.php:698-708`) — **siempre**, incluso con `static-css` activo (ver §6).

No hay proceso de subida especial: es la Media Library estándar de WordPress. Por eso el aviso
en pantalla sobre WordPress bloqueando `.woff`/`.ttf` por MIME type — hay que permitirlos
(Advanced → Theme functions, o plugin "Disable Real MIME Check") antes de que la URL exista.

## 6. Trampa: `static-css` puede dejar la fuente "congelada"

Si Theme Options tiene activado **Advanced → Static CSS** (`mfn_opts_get('static-css')`),
`mfn_styles_dynamic()` —que es donde se traduce `font-content`, `font-headings`, etc. a reglas
CSS reales (vía `style.php`, incluido en `mfn_styles_dynamic()`,
`functions/theme-head.php:1298`)— **deja de imprimirse inline** y en su lugar el theme sirve
`uploads/betheme/css/static.css` (`functions/theme-head.php:634-637`).

Ese fichero solo se regenera en `MFN_Options::_static_CSS()` (`muffin-options/options.php:843`),
y **solo** cuando la petición trae `$_GET['settings-updated']` — es decir, al guardar el
formulario de Theme Options desde el wp-admin. Un cambio hecho por SSH/wp-cli directamente sobre
`wp_options.betheme` **no dispara esa regeneración**: la familia tipográfica de las etiquetas
(`h1`, `body`, menú…) seguiría sirviendo la versión vieja hasta forzar la regeneración a mano
(§8). El `@font-face` de una fuente autoalojada (§5) no sufre esto porque se imprime siempre
inline, nunca pasa por `static.css`.

## 7. Gestión por SSH (wp-cli)

Confirmado con wp-cli 2.12.0. Toda la configuración vive en la fila `betheme`;
`wp option patch` la trata como el array PHP que es.

### Leer valores actuales

```bash
wp option pluck betheme font-content
wp option pluck betheme google-font-mode
wp option get betheme --format=json | python3 -c '
import json,sys
d=json.load(sys.stdin)
print({k:v for k,v in d.items() if k.startswith("font-") or k=="google-font-mode"})'
```

### Cambiar la familia de un rol (Google Font ya soportada por el theme)

```bash
wp option patch update betheme font-content   "Inter"
wp option patch update betheme font-headings  "Inter"
wp option patch update betheme font-headings-small "Inter"
```

Basta con que el nombre exista en `mfn_fonts()['all']` (catálogo de Google Fonts embebido,
`muffin-options/fonts.php`); no hace falta subir ni descargar nada — Google Fonts en modo por
defecto (`google-font-mode` vacío) la sirve directamente desde su CDN en cuanto detecta el
nombre en `font-content`/`font-headings`/etc.

Si `google-font-mode` está en `local`, hay que forzar la descarga después de cambiar el nombre
(equivalente al botón "Download files"):

```bash
wp eval '
check_admin_referer;  // no aplica en CLI, se llama el método directamente
global $MFN_Options;
// _tool_regenerate_fonts() vive en Mfn_Builder_Ajax, no en MFN_Options:
$ajax = new Mfn_Builder_Ajax();
$ajax->_tool_regenerate_fonts();
echo "regenerado\n";
'
```

(`_tool_regenerate_fonts()` comprueba `check_ajax_referer` y `current_user_can` — en `wp eval`
se ejecuta como usuario del sistema/CLI, sin sesión HTTP, así que ambas comprobaciones deben
saltarse o el método debe invocarse tras un `wp_set_current_user()` con un admin real. Más simple:
entrar como admin y pulsar "Download files" una vez tras el cambio, si el volumen de cambios no
justifica automatizarlo.)

### Subir una fuente propia por SSH

Sin pasar por la Media Library del admin — subir el fichero directamente a `uploads/` y apuntar
la meta a esa URL:

```bash
cd ~/public_html
YEAR_MONTH=$(date +%Y/%m)
mkdir -p "wp-content/uploads/$YEAR_MONTH"
cp /ruta/MiFuente.woff "wp-content/uploads/$YEAR_MONTH/"
cp /ruta/MiFuente.ttf  "wp-content/uploads/$YEAR_MONTH/"

BASE="$(wp option get home)/wp-content/uploads/$YEAR_MONTH"

# usar el primer slot fijo si está libre, o el siguiente número si no
wp option patch update betheme font-custom       "Mi Fuente"
wp option patch update betheme font-custom-woff   "$BASE/MiFuente.woff"
wp option patch update betheme font-custom-ttf    "$BASE/MiFuente.ttf"
```

No es obligatorio pasar por `wp media import` — el theme solo lee la **URL** guardada en
`font-custom{N}-woff`/`-ttf`, no un ID de adjunto. Aun así, si quieres que el fichero aparezca
en la Media Library del admin (para poder gestionarlo desde ahí), usa `wp media import` y toma
la URL que devuelve en vez de construirla a mano.

Para añadir un slot dinámico nuevo (4º, 5º… fuente) sin pisar los existentes:

```bash
wp eval '
$opts = get_option("betheme");
$n = intval($opts["font-custom-fields"] ?? 0) + 1;   // siguiente slot: 3+n
$slot = 3 + $n - 1;
$opts["font-custom".$slot]         = "Mi Fuente 2";
$opts["font-custom".$slot."-woff"] = "https://.../MiFuente2.woff";
$opts["font-custom".$slot."-ttf"]  = "https://.../MiFuente2.ttf";
$opts["font-custom-fields"]        = $n;
update_option("betheme", $opts);
echo "slot ".$slot." creado\n";
'
```

Recuerda: en la próxima carga `_register_custom_fonts()` compacta los slots >3 con nombre no
vacío empezando desde el 3, así que si ya existían huecos el número final puede no coincidir
con el que acabas de asignar — usa `wp option pluck betheme font-custom-fields` después para
confirmar cuántos hay realmente.

### Editar / eliminar una fuente propia

```bash
# renombrar (afecta también a los font_select que la tengan seleccionada, porque el valor
# guardado en esos campos es el nombre literal, no un id — hay que actualizarlos también)
wp option patch update betheme font-custom "Nuevo Nombre"

# eliminar: vaciar el nombre es suficiente, _register_custom_fonts() limpia woff/ttf solo
wp option patch update betheme font-custom ""
wp option patch update betheme font-custom-woff ""
wp option patch update betheme font-custom-ttf ""
```

### Forzar regeneración de `static.css` si está activo

```bash
wp option pluck betheme static-css     # comprobar si está activo

wp eval '
global $MFN_Options;
$MFN_Options->_static_CSS(true);       // segundo parámetro $force = true
echo "static.css regenerado\n";
'
```

Sin este paso, cualquier cambio de fuente por SSH con `static-css` activo no se reflejará en
`h1`, `body`, menú, etc. — solo en el `@font-face` de fuentes autoalojadas, que siempre es inline.

## 8. Trampas verificadas

- **El valor de un `font_select` es el nombre literal**, no un id estable. Renombrar una fuente
  custom (`font-custom`) no actualiza automáticamente los `font-content`/`font-headings`/…
  que ya la tuvieran seleccionada — hay que tocarlos a mano o quedan apuntando a un nombre que
  ya no existe (el theme cae al valor por defecto del navegador).
- **`static-css` activo + cambio por SSH = cambio invisible** hasta forzar `_static_CSS(true)`
  (§6, §7). El `@font-face` de fuentes propias es la única pieza que nunca depende de esto.
- **Modo `local` de Google Fonts + `.woff`/`.ttf` bloqueados por MIME** (WordPress 5.0+): si no
  se han habilitado esas extensiones, la descarga local puede fallar en silencio.
- **`_tool_regenerate_fonts()` borra `uploads/betheme/fonts/` entero** antes de re-descargar.
  No usarlo si hay ficheros ahí que no vengan de Google Fonts.
- **Slots dinámicos se compactan solos**: un slot `font-custom5` con nombre vacío desaparece
  (se sobreescribe) en la siguiente carga de `init`, aunque no se guarde nada desde el admin.
- **`google-font-mode: disabled` no borra el `@font-face` de fuentes propias** (§5); solo corta
  la carga de Google Fonts. Un sitio puede tener Google Fonts desactivado y aun así usar
  tipografías propias con normalidad.
- **Una fuente propia autoalojada declara SIEMPRE `font-weight:normal`** en su `@font-face`
  (`mfn_styles_custom_font()`, §5) — el peso real que se ve depende únicamente de qué ficheros
  subiste bajo ese nombre, nunca de un `font-weight` numérico puesto encima. Si un rol
  (`font-headings`, etc.) usa una fuente propia y el `weight_style` del campo `typography`
  correspondiente (`font-size-h1`…`font-size-h6`) pide un peso distinto de `400`/`normal`, el
  navegador **sintetiza** ("fake bold") sobre la única variante registrada → trazo engrosado
  artificialmente, distinto del diseño. Para tipografías propias con varios pesos reales
  (ej. Avenir Roman / Medium / Heavy, cada una subida como familia separada, §7), el patrón
  correcto es: **elegir el peso subiendo el nombre de familia correcto por rol, y dejar
  `weight_style` en `400`**. Reservar `weight_style` numérico distinto de 400 para roles que
  usan una fuente de verdad multi-peso (Google Font vía CDN, o fuente de sistema como Verdana).

## 9. Estado en el dev de Nordés Ancín

`ssh -i ~/.ssh/id_ed25519_new nordesancin@nordesancin.invbit.systems`

Fuente propia Avenir subida (licencia del cliente, kit generado con transfonter.org a partir de
Avenir Roman/Medium/Heavy), tres familias independientes porque BeTheme no soporta múltiples
pesos bajo un mismo nombre de fuente propia (§5):

| Campo | Valor | Ficheros |
|---|---|---|
| `font-custom` | `Avenir` (peso Roman/400) | `uploads/2026/08/fonts/Avenir-Roman.{woff,ttf}` |
| `font-custom2` | `Avenir Medium` (peso 500) | `Avenir-Medium.{woff,ttf}` |
| `font-custom3` (slot dinámico, `font-custom-fields=1`) | `Avenir Heavy` (peso ~800) | `Avenir-Heavy.{woff,ttf}` |

Asignación por rol, según los 21 estilos de texto del `🎨 Style Guide` de Figma
(`getLocalTextStylesAsync()` — no había CSS estático que inspeccionar, los pesos reales viven en
los Text Styles del archivo):

| Campo (rol) | Valor | Motivo |
|---|---|---|
| `font-content` / `font-lead` | `Verdana` (fuente de sistema, ya en el catálogo) | `p-M`/`p-S`/`p-XL` del Style Guide son Verdana Regular |
| `font-menu` / `font-title` / `font-headings-small` / `font-blockquote` | `Avenir` (Roman; sin `#`, ver §3) | `a-nav`, `h-featured-large`, `h5`/`h6` son Avenir Roman |
| `font-headings` (h1–h4) | `Avenir Medium` | h1/h2/h3 son Avenir Medium; h4 es Roman — compromiso porque el theme agrupa h1–h4 en un único selector, sin granularidad por nivel |
| `font-decorative` | `Avenir Heavy` | cifras de impacto (`h-project-intro`) usan Avenir Heavy |

Además, `font-size-h1`…`font-size-h6` tenían `weight_style` en `700`/`600` (herencia de cuando
la familia era Montserrat vía Google, con múltiples pesos reales). Se han puesto a `400` para
evitar el fake-bold del navegador sobre las caras Avenir recién subidas (ver trampa de arriba).

`google-font-mode` y `static-css` siguen vacíos (CDN de Google + CSS de tipografía inline, sin
la trampa de `static.css` desactualizado) — el cambio de familia se ve en caliente sin forzar
regeneración.

Nota aparte: existe un `uploads/betheme/css/static.css` (67 KB) en disco, resto de cuando
`static-css` estuvo activo. Con la opción actualmente en vacío no se sirve (el theme comprueba
la opción viva en cada carga, `functions/theme-head.php:634`), pero si alguien reactiva
`static-css` sin volver a guardar Theme Options desde el admin, ese fichero **desactualizado**
es el que se serviría hasta forzar `_static_CSS(true)`.
