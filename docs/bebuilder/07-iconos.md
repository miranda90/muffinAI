# 07 — Iconos: packs personalizados (CPT `icons`)

Cómo BeTheme registra, almacena, carga y borra los packs de iconos, y cómo gestionarlos
íntegramente por SSH sin pasar por el wp-admin. Todo verificado leyendo el código del theme
y ejecutándolo en el dev de Nordés Ancín.

## 1. Las tres fuentes de iconos del theme

| Fuente | Origen | Clases | Dónde se define |
|---|---|---|---|
| Muffin icons | Fuente incrustada en el theme | `icon-*` | `muffin-options/icons.php:10` (`class Mfn_Icons`), listado en `get_icons()` L2097 |
| Font Awesome | Librería externa que carga el theme | `fas fa-*`, `far fa-*`, `fab fa-*` | `Mfn_Icons::get_icons()` L2097 (clave `fa`) |
| **Packs personalizados** | Post type `icons` + ficheros en uploads | `{prefijo}-{nombre}` | `functions/post-types/class-mfn-post-type-icons.php` |

Este documento cubre la tercera. Las dos primeras son estáticas y no se tocan.

## 2. Ficheros implicados

| Fichero | Rol |
|---|---|
| `functions/post-types/class-mfn-post-type-icons.php` | Registro del CPT, creación de directorios, carga del CSS, borrado, lectura del listado |
| `muffin-options/fields/upload_icon/field_upload_icon.php` | Campo `upload_icon`: descomprime el zip, valida, renombra clases, escribe las meta |
| `muffin-options/fields/upload_icon/field_upload_icon.js` | UI del campo (media uploader) |
| `visual-builder/partials/modal-icons.php` | Modal "Select an icon" del Visual Builder |
| `muffin-options/icons.php:2128` (`the_modal()`) | Mismo modal para el builder clásico / theme options |

## 3. El CPT `icons`

Registrado en `class-mfn-post-type-icons.php:132` (`register()` L102):

```php
'public'        => false,
'show_ui'       => true,
'show_in_menu'  => apply_filters('betheme_dynamic_slug', 'betheme'),  // solo si current_user_can('edit_theme_options')
'supports'      => array('title'),
'capabilities'  => array( 'create_posts', 'edit_posts', 'publish_posts' => 'edit_theme_options' ),
'map_meta_cap'  => true,
```

Consecuencias prácticas:

- No tiene front propio (`public => false`), no hay permalink ni plantilla.
- Solo administradores con `edit_theme_options` lo ven o lo editan.
- Solo se guarda el `title`; **todo lo demás vive en post meta**.
- Un pack solo cuenta si su `post_status` es `publish` (los queries de lectura filtran por él).

El constructor (L25) además:

- `init` → `make_dir()` (L139): crea `uploads/betheme/` y `uploads/betheme/icons/` si no existen.
- `trashed_post` → `single_post_remove()` (L155): borrado del pack, ver §7.
- `wp_footer` y `admin_footer` (prioridad 1) → `load_icons()` (L174): imprime el `<link>` del CSS.

## 4. Post meta: el contrato completo

| Meta | Contenido | Quién la consume |
|---|---|---|
| `mfn-icon-name` | Nombre visible, sin parsear (`Nordés Ancín`) | Selector de iconos (nombre del grupo), `set_icons_name()` |
| `mfn-icon-name-parsed` | Nombre saneado = **nombre de la carpeta** (`NordesAncin`) | `load_icons()` (id del `<link>`), `single_post_remove()` (**qué carpeta borrar**) |
| `mfn-icon-prefix` | Prefijo de las clases CSS, sin guion final (`nordes`) | Composición de la clase `{prefijo}-{icono}` |
| `mfn-icon-upload` | **Ruta absoluta** al directorio del pack | Check de "hay pack" en `load_icons()`; valor del campo en el admin |
| `mfn-icon-url` | **URL pública** al directorio del pack | `href` del `<link>` que carga `style.css` |
| `mfn-icon-titles-array` | Array serializado: `[0]` nombre, `[1]` prefijo, `[2…]` nombres de iconos | `get_list_of_icons()` → selector del builder |

`mfn-icon-titles-array` es la **única** fuente del selector de iconos. Si falta, el pack se carga
en el front (el CSS sí se imprime) pero no aparece en el modal para elegirlo.

## 5. Flujo de subida por el admin (referencia)

`field_upload_icon.php::render()` L207 detecta `$_GET['message']` tras guardar y llama a
`upload_icons()` L46, que hace:

1. Lee `mfn-icon-name`, `mfn-icon-prefix` y el fichero subido. Si falta cualquiera de los tres, **return** silencioso.
2. `sanitize_file_name()` + `validate_file()` sobre el nombre; si detecta path traversal, `wp_die()`.
3. Mueve el zip a `uploads/betheme/icons/{nombre_parseado}.zip`.
4. `unzip_file()` L93 en `uploads/betheme/icons/{nombre_parseado}/`.
5. Recorre el resultado y **borra todo fichero** cuya extensión no esté en
   `svg, ttf, woff, woff2, eot, json, css`.
6. Borra el zip.
7. `add_prefix_on_upload()` L13: `preg_replace('/icon-/', $prefijo.'-', style.css)`.
   → **El zip debe venir de IcoMoon con el prefijo por defecto `icon-`**; si trae otro, las clases no se reescriben.
8. Escribe las meta (L81-84, L113) y llama a `set_icons_name()` L122, que lee `selection.json`
   y guarda `mfn-icon-titles-array`.

La previsualización del admin (`draw_icons_svg()` L151) **no usa la fuente**: dibuja `<svg>` leyendo
`icons[].icon.paths` de `selection.json`, con `viewBox="-100 -100 1200 1200"`.

## 6. Estructura del pack en disco

```
wp-content/uploads/betheme/icons/{NombreParseado}/
├── style.css          @font-face + reglas .{prefijo}-{icono}:before { content: "\eXXX" }
├── selection.json     formato IcoMoon
└── fonts/
    ├── {prefijo}.eot
    ├── {prefijo}.ttf
    ├── {prefijo}.woff
    └── {prefijo}.svg
```

De `selection.json` el theme solo lee dos cosas:

- `icons[].properties.name` → nombre del icono (`set_icons_name()`, L122)
- `icons[].icon.paths` → previsualización SVG en el admin (`draw_icons_svg()`, L151)

Rejilla estándar IcoMoon: `height: 1024`, paths en coordenadas SVG (y hacia abajo) dentro de la caja 0–1024.

## 7. Cómo se carga y se consume

**CSS.** `load_icons()` L174 recorre todos los posts `icons` publicados y, si `mfn-icon-upload` no
está vacío, imprime en `wp_footer` y `admin_footer`:

```html
<link rel="stylesheet" id="mfn-custom-icons-{name-parsed}" href="{mfn-icon-url}/style.css" media="all">
```

Sin `wp_enqueue_style`, sin versionado y sin caché intermedia: cualquier cambio en disco o en meta
se ve al recargar. Un plugin de "próximamente" que corte la salida del tema también corta este `<link>`.

**Selector.** `get_list_of_icons()` L202 devuelve un array de arrays `mfn-icon-titles-array`.
Lo consumen `visual-builder/partials/modal-icons.php:11` y `muffin-options/icons.php:2135`.
El modal (L41-49) genera cada opción como:

```php
data-rel="{prefijo}-{icono}"   // esto es lo que se guarda como valor del campo icon en el JSON del builder
```

**Borrado.** `single_post_remove()` L155 se engancha a `trashed_post`: borra
`uploads/betheme/icons/{mfn-icon-name-parsed}` recursivamente y después hace
`wp_delete_post($id, true)`. La papelera nunca conserva nada, porque los ficheros ya no existen.

## 8. Gestión por SSH (wp-cli)

Todo el sistema es post meta + ficheros. No hay transients, opciones ni CSS compilado. Por tanto se
puede crear, editar y borrar packs entera y exclusivamente por consola.

### Crear un pack

```bash
cd ~/public_html
NAME="Mi Pack"; PARSED="MiPack"; PREFIX="mipack"
DIR="wp-content/uploads/betheme/icons/$PARSED"

# 1. ficheros
mkdir -p "$DIR" && unzip -o /ruta/pack.zip -d "$DIR"
find "$DIR" -type f ! -regex '.*\.\(svg\|ttf\|woff\|woff2\|eot\|json\|css\)$' -delete
sed -i "s/icon-/${PREFIX}-/g" "$DIR/style.css"      # solo si el zip trae el prefijo por defecto

# 2. post + meta
ID=$(wp post create --post_type=icons --post_status=publish --post_title="$NAME" --porcelain)
wp post meta update $ID mfn-icon-name        "$NAME"
wp post meta update $ID mfn-icon-name-parsed "$PARSED"
wp post meta update $ID mfn-icon-prefix      "$PREFIX"
wp post meta update $ID mfn-icon-upload      "$PWD/$DIR"
wp post meta update $ID mfn-icon-url         "$(wp option get home)/$DIR"

# 3. listado de iconos desde selection.json
wp post meta update $ID mfn-icon-titles-array \
  "$(wp eval "\$j=json_decode(file_get_contents('$DIR/selection.json'),true);
     \$a=['$NAME','$PREFIX'];
     foreach(\$j['icons'] as \$i){\$a[]=\$i['properties']['name'];}
     echo json_encode(\$a);")" --format=json
```

`--format=json` hace que wp-cli serialice el array igual que lo haría WordPress.

### Comprobar

```bash
wp eval '
$l = Mfn_Post_Type_Icons::get_list_of_icons();
foreach($l as $p){ echo $p[0]." | prefijo ".$p[1]." | ".(count($p)-2)." iconos\n"; }
ob_start(); Mfn_Post_Type_Icons::load_icons(); echo ob_get_clean()."\n";
'
```

### Editar

| Cambio | Qué tocar |
|---|---|
| Añadir/quitar iconos | Sustituir ficheros del directorio + regenerar `mfn-icon-titles-array` |
| Cambiar prefijo | `sed -i "s/viejo-/nuevo-/g" style.css`, meta `mfn-icon-prefix`, y elemento `[1]` del array. **Además** hay que reemplazar la clase antigua en el JSON de las páginas ya maquetadas |
| Renombrar carpeta | Renombrar el directorio + `mfn-icon-name-parsed` + `mfn-icon-upload` + `mfn-icon-url` |
| Mover de servidor | Actualizar `mfn-icon-upload` (ruta absoluta) y `mfn-icon-url` (dominio) |

### Borrar

```bash
wp post delete $ID          # SIN --force: pasa por trash y el hook borra carpeta y post
```

Verificar `mfn-icon-name-parsed` antes: es la meta que decide qué carpeta se borra.

## 9. Generar un pack desde SVG sueltos (sin IcoMoon)

Método usado para el pack `Nordés Ancín` a partir de un frame de Figma. Node ≥ 18.

```bash
npm i svgpath svgicons2svgfont svg2ttf ttf2woff ttf2eot
```

1. **Normalizar los SVG a rejilla 1024.** Cada icono debe quedar dentro de la caja `0 0 1024 1024`
   con las mismas proporciones. Con `svgpath`: `.translate(-x,-y).scale(1024/tamañoOriginal)`.
   Si los iconos vienen de un export único (un frame con varios), calcular `x`/`y` desde la rejilla
   del frame, no desde el bounding box del path — el bounding box rompe el padding y descuadra tamaños.
2. **Construir la fuente**: `svgicons2svgfont` con `fontHeight: 1024`, `descent: 0`, `normalize: false`
   → fuente SVG → `svg2ttf` → `ttf2woff` / `ttf2eot`. Códigos desde `0xe900` (convención IcoMoon).
3. **`style.css`** con el prefijo ya aplicado (no hace falta el `sed`, ese paso solo existe para
   los zips de IcoMoon).
4. **`selection.json`** con `height: 1024` y, por icono, `properties.name` + `icon.paths`.
   El resto de campos IcoMoon son decorativos para el theme, pero conviene mantenerlos por si
   alguien reabre el pack en IcoMoon.
5. **Verificar visualmente** renderizando la fuente en un HTML antes de subir: un flip de eje Y o
   un `fill-rule` mal resuelto solo se detecta mirando.

El script completo que generó el pack de Nordés Ancín está en `proyectos/nordes-ancin/icons/` del repo
(SVG sueltos, pack montado y zip subible por admin).

## 10. Trampas verificadas

- **`mfn-icon-upload` con ruta de otro servidor** (típico tras migrar): el front sigue bien porque el
  `<link>` usa `mfn-icon-url`, pero la pantalla de edición del pack muestra el formulario de subida y
  el error *"This is not the Icomoon zip file"* — `is_icon_uploaded()` L185 busca `selection.json` en
  esa ruta absoluta y no lo encuentra. Arreglo: actualizar la meta a la ruta real.
- **Reabrir y guardar el post en el admin** vuelve a disparar `upload_icons()` (`render()` L207 depende
  de `$_GET['message']`). Con el pack ya montado por SSH no hay fichero que mover, pero conviene no
  guardar el post desde el admin sin necesidad.
- **El zip debe traer el prefijo `icon-`**. `add_prefix_on_upload()` L13 hace un `preg_replace` literal
  de `icon-`; con cualquier otro prefijo, las clases del CSS quedan sin reescribir y colisionan con
  la fuente de Muffin icons.
- **Prefijos cortos son peligrosos.** El bloque `[class^="{prefijo}-"]` fuerza `font-family !important`
  sobre cualquier clase que empiece igual. Usar un prefijo específico del proyecto, no dos letras.
- **Sin `mfn-icon-titles-array` el pack es invisible** en el selector aunque el CSS cargue.
- **Nombres duplicados** dentro de un pack: el último gana en el CSS. Al generar desde diseño hay que
  desduplicar antes (ver §9).
- **`post_status` distinto de `publish`** = pack inexistente para el theme.
- **Actualizar un pack existente (mismo nombre de carpeta) no se ve para nadie que ya lo hubiera
  cargado antes.** `load_icons()` (L194) imprime `<link href="{mfn-icon-url}/style.css">` **sin
  querystring de versión**, y `uploads/` suele servir con cabeceras de caché muy largas
  (`Cache-Control: max-age` de meses/años vía `mod_expires` o similar). Si sobreescribes
  `style.css`/`fonts/*` en la misma URL, el servidor tiene el contenido nuevo (verificable con
  `curl -sI`, mirar `Last-Modified`) pero el navegador de cualquiera que ya visitó el sitio sigue
  usando su copia cacheada — los iconos que ya existían antes se ven bien (mismos códigos, ya en
  caché), los nuevos códigos añadidos no aparecen hasta recarga forzada (Cmd/Ctrl+Shift+R) o hasta
  que expire la caché. No hay forma de invalidarlo desde el servidor sin cambiar la URL (renombrar
  la carpeta del pack, o añadir un parámetro de versión al `<link>` si se parchea el theme).
  Diagnóstico rápido: `curl -s https://sitio/…/style.css | grep nombre-clase-nueva` — si aparece
  en la respuesta directa pero no en el navegador, es caché, no el pack.

## 11. Estado en el dev de Nordés Ancín

`ssh -i ~/.ssh/id_ed25519_new nordesancin@nordesancin.invbit.systems`

| Post | Pack | Prefijo | Carpeta | Iconos |
|---|---|---|---|---|
| 72 | Témini | `temini` | `Tmini` | 17 |
| 123 | Nordés Ancín | `nordes` | `NordesAncin` | 33 |

Pendiente: el post 72 tiene `mfn-icon-upload` apuntando a `/home/pmini/public_html/...` (resto de una
migración). Front OK, admin del pack roto. Arreglo:

```bash
wp post meta update 72 mfn-icon-upload "$HOME/public_html/wp-content/uploads/betheme/icons/Tmini"
```
