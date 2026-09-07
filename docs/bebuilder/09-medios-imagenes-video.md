# 09 — Medios: imágenes y vídeo (Figma → `assets/` → WordPress → JSON)

> Actualización: el flujo verificable, las excepciones por ruta y las precisiones sobre transformaciones, medios y perfiles están en [10-flujo-verificable.md](10-flujo-verificable.md). Las pruebas del código prevalecen sobre reglas históricas.
Flujo obligatorio para que **toda** imagen y **todo** vídeo del diseño acaben en la Media Library
del sitio destino y referenciados en el JSON de forma que el theme los renderice con `srcset`,
`alt`, dimensiones y poster. Evidencia en el código del theme al final de cada apartado.

Resumen en una línea: **inventariar en Figma → descargar a `proyectos/<cliente>/assets/` →
subir a WordPress → `assets/manifest.json` con `id` + `url` → referenciar como `URL#ID`**.

Ningún JSON se entrega con imágenes apuntando a Figma, a `localhost`, a rutas locales o a URLs
inventadas. Si un medio no se ha podido subir, se dice, no se disimula con un placeholder.

---

## 1. Inventario: qué medios hay en el diseño

Antes de trocear en secciones, listar los medios. Fuentes, por orden:

1. **`get_metadata(fileKey, nodeId)`** sobre el frame de la página: árbol con nombres, tipos y
   tamaños. Sirve para localizar frames-sección y nodos grandes con fill de imagen.
2. **`get_design_context(fileKey, nodeId)`** por sección (no toda la página: recorta el
   contexto): devuelve el código de referencia con las URLs de los assets que usa y la captura.
   En el código, cada `<img src="...">` o `background-image: url(...)` es un medio a recoger.
3. **`download_assets(fileKey, nodeId)`** por sección: `export` (render del nodo entero),
   `rawImages` (las imágenes originales subidas a Figma como fill, formato real en `format`) y
   `svgAssets` (vectores que conviene servir como SVG: iconos, logos, ilustraciones simples).

Clasificar cada medio por lo que **es**, no por cómo lo pintó Figma:

| Medio en el diseño | Tipo | Formato a guardar | Dónde acaba en el JSON |
|---|---|---|---|
| Foto, render, textura | ráster | el original de `rawImages` (jpg/png/webp) | `image.src`, fondo de sección/wrap/item |
| Logo, icono, ilustración plana | vector | `svgAssets` → `.svg` | `image.src` (logos), pack de iconos (doc 07) si va a un `icon_box`/`list` |
| Composición que solo existe montada en Figma (foto + formas + degradado) | ráster compuesto | `export` del nodo a 2x (`defaultScale: 2`) | `image.src` o fondo |
| Rectángulo con *video fill* o frame "vídeo" | vídeo | `.mp4` — **no lo da la API**, ver §4.1 | `bg_video_mp4` o item `video` |
| Animación de timeline / prototipo | vídeo | `export_video` → `.mp4` | ídem |
| Embed de YouTube/Vimeo | enlace | no se descarga | item `video` con `video` = ID |

Límites del MCP que condicionan cómo se pide: `rawImages` y `svgAssets` van **capados a 20 por
nodo** — pedir por sección, no por página. Las URLs devueltas son **temporales**: descargar en la
misma sesión, nunca guardarlas en el script.

---

## 2. Descargar a `proyectos/<cliente>/assets/`

- Nombres **kebab-case descriptivos por función**: `hero-portada.jpg`, `logo-cliente-blanco.svg`,
  `sector-logistico.jpg`. Nunca el nombre de capa de Figma (`Rectangle 12.png`, `image 3.png`).
  WordPress sanea el nombre al subir, y ese nombre es el que verá el cliente en la Media Library.
- Extensión = formato real (`format` de `rawImages`). Un PNG renombrado a `.jpg` sube, pero el
  theme y el navegador lo tratan por el MIME real y el `srcset` sale raro.
- Tamaño: hero y fondos a pantalla completa, máximo **2560 px de ancho** (por encima WordPress
  genera `-scaled.jpg` y sirve ese). Tarjetas y galerías, el doble del tamaño de diseño (2x).
  Iconos y logos, SVG sin rasterizar.
- Fotos PNG sin transparencia → convertir a JPG/WebP antes de subir (pesan 5-10x):
  `sips -s format jpeg in.png --out out.jpg` (macOS) o `cwebp -q 82 in.png -o out.webp`.
- Un medio, un fichero. Si el diseño usa la misma foto en dos sitios, se sube **una vez**.

Descarga (URLs temporales del MCP):

```bash
cd proyectos/<cliente>/assets
curl -sSL -o hero-portada.jpg "<url temporal rawImages>"
curl -sSL -o logo-cliente.svg "<url temporal svgAssets>"
file *          # comprobar que el tipo real coincide con la extensión
```

---

## 3. Subir a WordPress y construir `manifest.json`

El objetivo es obtener, por fichero, el **ID de adjunto** y la **URL real** en `uploads/`.
Ambos van a `proyectos/<cliente>/assets/manifest.json`, que es lo que lee el script.

### 3.1 Por SSH + wp-cli (preferido: da IDs, alt y título en un paso)

```bash
# 1. subir los ficheros al servidor
scp -i ~/.ssh/<clave> proyectos/<cliente>/assets/*.{jpg,png,webp,svg,mp4} <user>@<host>:/tmp/assets/

# 2. en el servidor, desde la raíz de WordPress
cd ~/public_html
ADMIN=<login-admin>          # imprescindible para SVG, ver trampa §6
for f in /tmp/assets/*; do
  id=$(wp media import "$f" --user="$ADMIN" --porcelain \
         --title="$(basename "${f%.*}" | tr '-' ' ')")
  url=$(wp eval "echo wp_get_attachment_url($id);")
  printf '%s\t%s\t%s\n' "$(basename "$f")" "$id" "$url"
done | tee /tmp/assets/subidos.tsv
```

`--porcelain` devuelve solo el ID. Añadir `--alt="texto"` a las imágenes con contenido (foto de
producto, equipo, sede); a las decorativas se les deja vacío y en el JSON se pone `alt: ""`.

Convertir el TSV en manifest (en local):

```bash
python3 - proyectos/<cliente>/assets/subidos.tsv <<'EOF'
import json, sys
rows = [l.rstrip("\n").split("\t") for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
man = {f: {"id": int(i), "url": u} for f, i, u in rows}
out = sys.argv[1].rsplit("/", 1)[0] + "/manifest.json"
json.dump(man, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(out, len(man), "medios")
EOF
```

Ficheros grandes (vídeo por encima de `upload_max_filesize`): copiarlos ya a
`wp-content/uploads/YYYY/MM/` y registrarlos sin volver a copiar:

```bash
wp eval 'echo size_format(wp_max_upload_size());'      # límite del servidor
wp media import wp-content/uploads/2026/08/hero.mp4 --skip-copy --porcelain --user="$ADMIN"
```

### 3.2 Por REST (sin SSH: usuario + application password)

```bash
curl -sS -u '<login>:<app password>' \
  -H 'Content-Disposition: attachment; filename="hero-portada.jpg"' \
  -H 'Content-Type: image/jpeg' \
  --data-binary @proyectos/<cliente>/assets/hero-portada.jpg \
  https://<sitio>/wp-json/wp/v2/media | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["id"], d["source_url"])'
```

El `alt` se pone con `POST /wp-json/wp/v2/media/<id>` y `{"alt_text": "..."}`. La REST respeta
el mismo filtro de MIME que el admin: SVG solo con un usuario que tenga `edit_theme_options`.

### 3.3 Formato del manifest

```json
{
  "hero-portada.jpg":   { "id": 1409, "url": "https://cliente.com/wp-content/uploads/2026/08/hero-portada.jpg", "alt": "Fachada de la sede" },
  "logo-cliente.svg":   { "id": 1410, "url": "https://cliente.com/wp-content/uploads/2026/08/logo-cliente.svg" },
  "hero-fondo.mp4":     { "id": 1411, "url": "https://cliente.com/wp-content/uploads/2026/08/hero-fondo.mp4" },
  "hero-fondo-poster.jpg": { "id": 1412, "url": "https://cliente.com/wp-content/uploads/2026/08/hero-fondo-poster.jpg" }
}
```

`id` y `url` obligatorios; `alt` y `node` (id del nodo Figma de origen) opcionales. El manifest
se commitea junto al script: es la prueba de que los medios existen en el destino.

---

## 4. Referenciar en el JSON: siempre `URL#ID`

El export real del Visual Builder escribe **`URL#ID`** en todos los campos `upload`:
`examples/example2/home.json:39` (`bg_video_mp4`), `:475` (`image.src`), `:759`
(`css_advanced_background_img`). Ese es el formato a generar. Con `tools/mfn.py`:

```python
from mfn import load_manifest, media
MAN = load_manifest(HERE / "assets" / "manifest.json")

item("image", {"src": media(MAN, "hero-portada.jpg"), "alt": "Fachada de la sede", "size": "full"})
```

`media()` lanza `KeyError` si el fichero no está en el manifest: un medio sin subir se sube, no
se inventa una URL.

### 4.1 Por qué el `#ID` (evidencia)

`sc_image()` — `betheme/functions/theme-shortcodes.php:8116-8180`:

- Si `src` contiene `#` toma el número tras él como ID de adjunto y llama a
  `mfn_get_attachment($id, $size, $lazy_load, ['alt' => $alt])`
  (`theme-functions.php:2218-2270`), que devuelve `wp_get_attachment_image()`: **`srcset` +
  `sizes` + `alt` de la Media Library + `width`/`height` reales**, y respeta el campo `size`
  (`full`, `large`, tamaños custom del theme).
- Sin `#ID`, intenta `attachment_url_to_postid($src)` (`theme-functions.php:2280-2292`): una
  consulta a BD **por imagen y por render**, que además devuelve 0 si la URL no coincide letra por
  letra con la guardada (http/https, dominio de desarrollo vs producción, sufijo `-scaled`, sufijo
  de tamaño `-300x200`).
- Si eso devuelve 0, cae al bloque `else` de `theme-shortcodes.php:8160`: `<img src="URL">`
  crudo, **sin `srcset`, ignorando `size`, con `width`/`height` vacíos** y `alt` solo si venía
  en el JSON. Se ve, pero es la peor versión posible de la imagen.

Fondos (`css_advanced_background_image` de sección, `css_advanced_background_img` de Advanced,
`css_queryloop_item_bg_image`): el helper envuelve el valor en `url(...)` tal cual
(`class-mfn-helper.php:432-440`), sin quitar el fragmento; el navegador ignora `#ID` al pedir el
fichero. Se mantiene el mismo formato por coherencia con el export.

### 4.2 Imagen como item `image`

```json
{
  "type": "image", "uid": "itm000001",
  "size": "1/2", "tablet_size": "1/2", "mobile_size": "1/1",
  "attr": {
    "src": "https://cliente.com/wp-content/uploads/2026/08/equipo.jpg#1420",
    "alt": "Equipo técnico en el taller",
    "size": "full",
    "image_height": "custom",
    "css_image_cover_height": {
      "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .image_frame.mfn-coverimg .image_wrapper img",
      "style": "height", "val": { "desktop": "520px", "mobile": "320px" }
    }
  }
}
```

- `alt` del JSON manda sobre el de la Media Library (`theme-shortcodes.php:8120-8123`). Si se
  deja vacío y la imagen tiene alt en WordPress, sale ese; si no, el título del adjunto.
- Altura fija del diseño → `image_height: "custom"` + `css_image_cover_height` (añade
  `.mfn-coverimg`, `object-fit: cover`). Ancho fijo → `css_image_frame_width`.
- Logos e iconos SVG: siempre con `css_image_frame_width` (o `width`); sin ancho el theme añade
  la clase `svg` y el SVG se estira al contenedor (`theme-shortcodes.php:8185`).
- `lazy_load`: `""` sigue Theme Options; `"disable"` para la imagen del hero (LCP).
- `stretch: "1"` cuando la imagen debe llenar la columna; de lo contrario respeta su tamaño
  natural y se alinea con `align`.

### 4.3 Imagen de fondo

Sección: `background_switcher: "default"` + `css_advanced_background_image` con valor por
breakpoint cuando el diseño recorta distinto en móvil (subir un segundo fichero, no confiar en
`background-position`):

```json
"background_switcher": "default",
"css_advanced_background_image": {
  "selector": ".mcb-section-mfnuidelement", "style": "background-image",
  "val": { "desktop": "https://cliente.com/wp-content/uploads/2026/08/hero-portada.jpg#1409",
           "mobile":  "https://cliente.com/wp-content/uploads/2026/08/hero-portada-movil.jpg#1413" }
},
"css_advanced_background_size":     { "selector": ".mcb-section-mfnuidelement", "style": "background-size",     "val": { "desktop": "cover" } },
"css_advanced_background_position": { "selector": ".mcb-section-mfnuidelement", "style": "background-position", "val": { "desktop": "center center" } },
"css_advanced_background_overlay_background_color": { "selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "background-color", "val": "rgba(0,0,0,0.45)" }
```

Wrap/item: mismos campos con prefijo `css_advanced_background_*` sobre `.mcb-wrap-inner` /
`.mcb-column-inner` (fichas `_wrap.md`, `_advanced.md`). Un fondo de sección sin
`background_switcher` explícito no muestra sus controles en el panel (trampa 19).

Tarjeta de query loop con foto de fondo: `css_queryloop_item_bg_image` en el wrap, o
`{featured_image}` como `src` de un `image` (el helper lo traduce a `var(--mfn-featured-image)`,
`class-mfn-helper.php:469`).

---

## 5. Vídeo

### 5.1 De dónde sale el `.mp4`

| Caso en Figma | Cómo obtenerlo |
|---|---|
| Rectángulo/frame con **video fill** (Figma de pago) | **La API y el MCP no devuelven el fichero de vídeo**: `download_assets` solo lista imágenes. Pedir el `.mp4` original al diseñador/cliente (o el enlace de descarga) y anotarlo en el manifest. El fotograma que Figma muestra **sí** se descarga (`export` del nodo) y sirve de poster. |
| Animación de **timeline**/prototipo que el cliente quiere como vídeo | `export_video(fileKey, nodeId)` con el **frame de primer nivel** que posee el timeline (no una capa interna). Si responde `status: "processing"`, repetir con `{fileKey, jobId}` cada 10-15 s. Parámetros: `quality: "high"`, `constraint: {type: "WIDTH", value: 1920}` para fondos, `fps` si el diseño lo fija. La URL caduca (`availableUntil`): descargar de inmediato. |
| Marco con captura de YouTube/Vimeo + botón play | No hay fichero: item `video` con el ID del vídeo (`video: "WoJhnRczeNg"`). |
| Vídeo que no existe aún (placeholder "aquí irá un vídeo") | Maquetar la sección con fondo de color + `bg_video_mp4` vacío y avisar de que falta el medio. Nunca un vídeo de stock sin permiso. |

Antes de subir, un vídeo de fondo se optimiza (sin audio, ≤1080p, `faststart` para que arranque
antes de descargar entero):

```bash
ffmpeg -i original.mp4 -an -vf "scale=1920:-2" -c:v libx264 -crf 28 -preset slow \
       -movflags +faststart -pix_fmt yuv420p hero-fondo.mp4
ffmpeg -i hero-fondo.mp4 -vframes 1 -q:v 3 hero-fondo-poster.jpg     # poster del primer frame
```

Objetivo: < 8-10 MB para un fondo en loop. Subir `.mp4` y poster al manifest como cualquier otro
medio (§3; con `--skip-copy` si supera `upload_max_filesize`).

### 5.2 Vídeo de fondo de sección

```json
"background_switcher": "video",
"bg_video_mp4": "https://cliente.com/wp-content/uploads/2026/08/hero-fondo.mp4#1411",
"bg_video_dots": "",
"css_advanced_background_color": { "selector": ".mcb-section-mfnuidelement", "style": "background-color", "val": "#1D242C" },
"css_advanced_background_overlay_background_color": { "selector": ".mcb-section-mfnuidelement .mcb-background-overlay", "style": "background-color", "val": "rgba(29,36,44,0.5)" }
```

Qué hace el theme (`class-mfn-builder-front.php:593-598` y `:921-953`):

- Con `bg_video_mp4` no vacío añade la clase `has-video` a la sección y pinta
  `<div class="section_video"><div class="mask"></div><video autoplay loop muted playsinline>
  <source type="video/mp4" src="URL#ID"></video></div>` antes del overlay. Reproduce también en
  móvil (`playsinline`, `muted`).
- **El poster solo sale del campo deprecado `bg_image`** (`front.php:928`). En JSON nuevo no se
  usa `bg_image` (el front lo vuelca como estilo inline, E021), así que el respaldo mientras carga
  el vídeo es `css_advanced_background_color` — poner el color dominante del vídeo, no negro por
  defecto.
- `bg_video_dots: "1"` superpone la trama de puntos (disimula vídeos de baja resolución,
  oscurece). Por defecto vacío.
- En el Visual Builder el `<video>` va comentado dentro de `.mfn-vb-video-lazy` (`front.php:933`):
  que no se vea en el editor no significa que falte.
- El patrón completo (100vh, título arriba, card abajo) está en
  `builder-elements/GUIA-MAQUETACIONES.md` §1.

### 5.3 Vídeo como item (`video`)

HTML5 autoalojado:

```json
{
  "type": "video", "uid": "itm000002",
  "size": "1/1", "tablet_size": "1/1", "mobile_size": "1/1",
  "attr": {
    "video": "",
    "mp4": "https://cliente.com/wp-content/uploads/2026/08/proceso.mp4#1430",
    "placeholder": "https://cliente.com/wp-content/uploads/2026/08/proceso-poster.jpg#1431",
    "html5_parameters": "a;;l;m;i",
    "object_fit": { "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-video", "style": "object-fit", "val": "cover" },
    "css_video_width":  { "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-video", "style": "width",  "val": { "desktop": "100%" } },
    "css_video_height": { "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-video", "style": "height", "val": { "desktop": "560px", "mobile": "240px" } }
  }
}
```

- **`video: ""` es obligatorio.** El campo trae default `n7-F-FMzM7Q` (ficha `video.md`) y
  `sc_video()` hace `if ($video) { iframe } elseif ($mp4) { html5 }`
  (`theme-shortcodes.php:12960-13020`): con el default sin vaciar sale un YouTube ajeno en lugar
  del MP4 del cliente. Trampa 25.
- `placeholder` = poster (`<video poster="…">`, `:13008-13011`); también es lo que se ve en
  móviles que bloquean el autoplay.
- `html5_parameters` es un código, no una lista libre: `a;;l;m;i` = autoplay + loop + muted +
  playsinline (fondo decorativo); `;c;;;p` = controles + playsinline (vídeo que el usuario
  reproduce). Tabla completa en `builder-elements/video.md`.
- `object_fit: cover` y `object_position` solo tienen efecto si van **los dos** `css_video_width`
  y `css_video_height` (`sc_video()` L18: el `style` inline del vídeo solo se compone con ambos).
- YouTube/Vimeo: `video` = ID (`WoJhnRczeNg` o `62954028`), `parameters` = `autoplay=1&mute=1&loop=1`.
  Vimeo puede bloquear parámetros según el autor.

---

## 6. Trampas de medios

| # | Trampa | Evidencia |
|---|---|---|
| M1 | `src` sin `#ID` → `attachment_url_to_postid()` por render; si la URL no coincide exactamente, `<img>` crudo sin `srcset` ni tamaño | `theme-shortcodes.php:8116-8180`, `theme-functions.php:2280` |
| M2 | Item `video` con `video` sin vaciar → pinta el YouTube por defecto, no el MP4 | `theme-shortcodes.php:12960`, ficha `video.md` |
| M3 | Poster del vídeo de sección solo desde `bg_image` (deprecado) → sin poster en JSON nuevo; usar color de fondo | `front.php:928` |
| M4 | SVG: la subida solo la permite `mfn_mimes_support()` a usuarios con `edit_theme_options` y con `svg-allow` no desactivado en Theme Options → Advanced → Disable. `wp media import` sin `--user=` corre sin usuario y **falla** con "Sorry, you are not allowed to upload this file type" | `theme-functions.php:265-283` |
| M5 | Imagen > 2560 px → WordPress crea `-scaled` y `wp_get_attachment_url()` devuelve esa; con `#ID` da igual, sin él la URL "bonita" no existe como adjunto | WP `big_image_size_threshold` |
| M6 | URLs del MCP de Figma (`figma.com/...` temporales o `localhost:3845/assets/...` del MCP de escritorio) dentro del JSON → funcionan en la sesión y mueren después | `download_assets`/`get_design_context` |
| M7 | Dominio de desarrollo en el manifest y entrega en producción: el `#ID` sigue resolviendo la imagen (mismo adjunto tras migrar), pero los fondos `url(...)` conservan el dominio viejo. Migrar con `wp search-replace` o regenerar el manifest en el destino final | `class-mfn-helper.php:432` |
| M8 | Vídeo mayor que `upload_max_filesize` → REST/admin fallan en silencio o con 413. `scp` + `wp media import --skip-copy` | `wp_max_upload_size()` |
| M9 | `object_fit: cover` en item `video` sin `css_video_width` **y** `css_video_height` → no aplica | `theme-shortcodes.php` `sc_video()` L18 |

---

## 7. Checklist de medios antes de entregar

- [ ] Todos los medios del diseño inventariados (fotos, logos, iconos, vídeo) y descargados a
      `proyectos/<cliente>/assets/` con nombre descriptivo y formato real.
- [ ] Todos subidos al sitio destino; `assets/manifest.json` con `id` + `url` de cada uno.
- [ ] `grep -c "figma.com\|localhost:3845\|/Users/\|placeholders/image.svg" salida.json` → 0.
- [ ] Todo `src`, `bg_video_mp4`, `mp4`, `placeholder` y fondo `url` con sufijo `#ID`.
- [ ] `alt` con contenido en imágenes informativas; `""` en decorativas.
- [ ] Item `video` HTML5 con `video: ""`, `placeholder` y `html5_parameters` elegidos.
- [ ] Sección con vídeo: `background_switcher: "video"` + color de fondo de respaldo + overlay si
      hay texto encima.
- [ ] Vídeo optimizado (sin audio si es fondo, ≤1080p, `faststart`, < 10 MB).
- [ ] Si algún medio no se ha conseguido (video fill sin fichero, foto en baja), está listado en
      la entrega como pendiente, no sustituido en silencio.

---

## 8. Ficheros del theme implicados

| Fichero | Qué hace |
|---|---|
| `betheme/functions/theme-shortcodes.php:8060-8215` | `sc_image()`: resolución de `src` (`#ID` → ID → URL cruda), `alt`, `svg`, `mfn-coverimg` |
| `betheme/functions/theme-shortcodes.php:12877-13025` | `sc_video()`: iframe YouTube/Vimeo vs `<video>` HTML5, poster, `html5_parameters` |
| `betheme/functions/theme-functions.php:2218-2270` | `mfn_get_attachment()`: `wp_get_attachment_image()` con `size`, lazy load, WPML |
| `betheme/functions/theme-functions.php:2280-2292` | `mfn_get_attachment_id_url()`: quita `#…` y hace `attachment_url_to_postid()` |
| `betheme/functions/theme-functions.php:2300-2350` | `mfn_get_attachment_data()`: alt/título/width/height del adjunto |
| `betheme/functions/theme-functions.php:265-283` | `mfn_mimes_support()`: permiso de subida de SVG/ICO/TTF/WOFF/JSON |
| `betheme/functions/builder/class-mfn-builder-front.php:593-598`, `:921-953` | Vídeo de fondo de sección (`has-video`, `.section_video`, poster desde `bg_image`) |
| `betheme/functions/admin/class-mfn-helper.php:432-440` | `background-image` → `url(valor)` sin tocar el fragmento |
| `builder-elements/image.md`, `video.md`, `_section.md`, `_advanced.md` | Fichas con todos los campos de medios |
