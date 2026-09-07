# Guía de maquetaciones – Diseño real BeTheme/Muffin Builder

> Actualización: el flujo verificable, las excepciones por ruta y las precisiones sobre transformaciones, medios y perfiles están en [10-flujo-verificable.md](../docs/bebuilder/10-flujo-verificable.md). Las pruebas del código prevalecen sobre reglas históricas.
Esta guía describe **cómo se construyen en el diseño real** las maquetaciones más habituales, tomando como referencia:

- **`examples/example2/home.json`** – Home TMC (hero con video, sección naranja, catálogo, estadísticas, CTA final).
- **`examples/example1/about-us.json`** – About Us (hero con imagen, columnas, valores, innovación).

Objetivo: tener patrones claros para replicar o aproximar estos layouts al generar JSON para el builder y perfeccionar el estilo.

---

## 1. Hero a pantalla completa con video de fondo

**Diseño:** Sección que ocupa 100vh, fondo con video MP4 y overlay oscuro, título grande a la izquierda y (opcional) un bloque tipo “card” abajo a la derecha (p. ej. carrusel de producto).

**Sección (attr):**

- `background_switcher`: `"video"`.
- `bg_video_mp4`: URL del vídeo en la Media Library del destino con sufijo `#ID` (p. ej. `"https://.../archivo.mp4#1406"`). Flujo de descarga/subida y optimización en `docs/bebuilder/09-medios-imagenes-video.md` §5.
- `height_switcher`: `"custom"`.
- `css_advanced_height`: `{ "selector": ".mcb-section-mfnuidelement", "style": "height", "val": { "desktop": "100vh", "tablet": "auto" } }`.
- `css_advanced_background_color`: color de respaldo (ej. `#1D242C`). Es lo único que se ve mientras carga el vídeo: el poster solo existe vía `bg_image` (deprecado), así que elegir el color dominante del vídeo.
- `css_advanced_background_overlay_background_color`: overlay (ej. `"rgba(29,36,44,0.5)"`).

**Estructura de wraps:**

- **Wrap 1:** margen superior (`css_advanced_margin.val.desktop.top`: `"10rem"`) y un item **heading** (h1, texto blanco, tipografía grande con `css_typography` desktop/mobile).
- **Wrap 2:** mismo grid por defecto; en **attr** del wrap: `css_advanced_align_self` → `"flex-end"` para pegar el contenido abajo. Dentro, un item **plain_text** con shortcode (ej. `[homepage_product_carousel]`) y `shortcodes_parser`: `"1"`. La “card” blanca se consigue con estilos en el plain_text: `css_advanced_background_color`, `css_advanced_border_radius`, `css_advanced_padding` en el selector del column-inner.

**Resumen:** Hero con video = sección con `background_switcher: "video"` + `height_switcher: "custom"` + 100vh; contenido en dos wraps (título arriba, card/shortcode abajo con `align-self: flex-end`).

---

## 2. Barra o bloque con color sólido (ej. naranja) y grid custom

**Diseño:** Sección con fondo color sólido (ej. naranja #F08018), ancho limitado (ej. 1580px) centrado, y dentro un grid con columnas en medidas fijas + flex (ej. 35rem + 1fr).

**Sección (attr):**

- `css_advanced_background_color`: color (ej. `#F08018`).
- `width_switcher`: `"full"`.
- `css_advanced_justify_content`: centro en `.section_wrapper`.
- Opcional: `css_advanced_background_position` / `css_advanced_background_size` si se usa imagen de fondo parcial (ej. `top right`, `custom` + `css_advanced_background_size_v2`: `"100rem"`).

**Wrap principal:**

- `grid`: `"grid"`.
- `grid_columns_switcher`: `"custom"`.
- `css_grid_columns_custom`: p. ej. `{ "desktop": "35rem 1fr", "mobile": "1fr" }` (columna fija + resto flexible).
- `width_switcher`: `"custom"`.
- `css_advanced_flex`: ancho del wrap (ej. `"1580px"` desktop, `"100%"` tablet).
- `css_advanced_align_items`: p. ej. `"center"` (laptop) para centrar verticalmente.
- `css_advanced_margin`: márgenes por breakpoint (ej. bottom 4rem desktop, 2rem tablet).

**Items típicos:** En la primera columna un **heading** (título grande, mayúsculas, color oscuro). En la segunda, una **image** con ancho custom y opcionalmente `visibility: " hide-mobile"` y posición absoluta en tablet para que la imagen “salga” del bloque.

**Resumen:** Sección color sólido + wrap con `grid_columns_switcher: "custom"` y `css_grid_columns_custom` (ej. `35rem 1fr`) + `width_switcher: "custom"` y `css_advanced_flex` para ancho máximo.

---

## 3. Grid de categorías / productos (query loop)

**Diseño:** Varias tarjetas (imagen + título + botón/icono) en grid 4 columnas desktop, 2 tablet, 1 móvil. Los datos pueden venir de términos de taxonomía (ej. `product_cat`).

**Wrap (attr):**

- `grid`: `"grid"`.
- `type`: `"query"`.
- `query_type`: `"terms"`.
- `query_terms_taxonomy`: `"product_cat"` (o la taxonomía que sea).
- `query_terms_includes_product_cat` (o equivalente): array de `{ "key": "ID", "value": "Nombre" }`.
- `css_grid_columns`: por breakpoint, ej. `{ "desktop": "repeat(4, 1fr)", "tablet": "repeat(2, 1fr)", "mobile": "1fr" }`.
- `width_switcher`: `"custom"`, `css_advanced_flex`: `"1580px"`.
- `css_grid_columns_gap` / `css_grid_rows_gap` si hace falta.

**Items del wrap:** Son **wraps anidados** (`item_is_wrap`: `1`). Cada sub-wrap representa una tarjeta y contiene:

- **image:** `src`: `"{featured_image}"`, enlace `"{permalink}"`, altura custom (`image_height`: `"custom"`, `css_image_cover_height`), border-radius.
- **button:** Estilo “icono” (transparent, imagen de fondo con SVG, posición absoluta abajo-derecha, hover con `css_advanced_transform_hover` translateX).
- **heading:** Título de categoría con `link`: `"{permalink}"`, tipografía y margen.

**Resumen:** Grid de tarjetas = wrap con `type: "query"` y `query_type: "terms"` + `css_grid_columns` responsive; cada celda es un wrap anidado con image + button + heading.

---

## 3.bis Fila de tarjetas estáticas (grid + subwraps) — patrón por defecto

**Diseño:** N tarjetas idénticas en fila (icono/imagen + título + texto + botón), con un hueco
definido entre ellas (ej. 36px) y todas a la misma altura, con el botón alineado abajo.

**Por qué grid y no N wraps hermanos `1/4`:** el `gap` no existe fuera del grid —
`css_grid_columns_gap`/`css_grid_rows_gap` están condicionados a `wrap_grid is grid` y su selector
exige `.mcb-wrap-grid` (`class-mfn-builder-fields.php:3582-3600`,
`class-mfn-builder-front.php:1528`). Con hermanos, el hueco es el gutter del theme (~2%) y solo se
modula con márgenes, que además comen ancho de columna. Ver trampa 21 en `docs/bebuilder/05`.

**Wrap contenedor (`1/1`):**

- `grid`: `"grid"`, `grid_columns_switcher`: `""`.
- `css_grid_columns`: `{ "desktop": "repeat(4, 1fr)", "tablet": "repeat(2, 1fr)", "mobile": "1fr" }`.
- `css_grid_columns_gap` / `css_grid_rows_gap`: el hueco del diseño, con valor por breakpoint.

**Cada tarjeta = subwrap (`item_is_wrap: 1`), `size` `1/1` en los tres breakpoints** (el reparto lo
hace el grid, no el `size`):

- Fondo/borde/radio de la tarjeta en `.mcb-wrap-inner` (`css_advanced_background_color`,
  `css_advanced_border_radius`, `css_advanced_padding`) + `background_switcher: "default"`.
- `height_switcher: "custom"` + `css_advanced_height` `{"desktop": "100%"}`: sin esto el fondo no
  llena la celda estirada y las tarjetas se ven de distinta altura aunque el grid sí lo esté.
- `css_advanced_align_content: "space-between"` para clavar el botón abajo.
- Dentro, items normales: `image` (icono con `css_image_frame_width`), `heading`, `plain_text`,
  `button`.

**Lo que sobra con este patrón:** `classes: "equal-height-wrap"` en la sección y el `margin-bottom`
por tarjeta — los cubre el propio grid y `css_grid_rows_gap`.

**Compatibilidad:** nested wrap es información en el perfil visual; W005 bloquea con strict únicamente en classic.

**Resumen:** tarjetas con gap definido → wrap `1/1` grid + un `item_is_wrap` por tarjeta con
`height: 100%` y `align-content: space-between`.

---

## 3.ter Fila de cifras animadas (counter)

**Diseño:** 3-5 cifras grandes con una descripción corta debajo (“+1.000 profesionales en
plantilla”), normalmente centradas.

**Elemento:** `counter` si el formato y la animación encajan con el diseño; texto para formatos no soportados. Anima de 0 al valor al entrar en viewport
(`js/scripts.js:1425-1465`, waypoint + `data-to`) y ya trae la estructura del bloque:
`.number-wrapper` (`.prefix` + `.number` + `.postfix`) + `.title`, cada parte con sus propios campos
de color y tipografía.

**Campos clave:**

- `prefix` (“+”, “€”), `number` (**entero pelado**: el JS hace `Math.floor` sobre `data-to`),
  `label` (sufijo: “%”, “k”), `title` (la descripción) + `title_tag`.
- `icon`: `""` **y** `image`: `""` — el default es `icon-lamp` y si no se vacía se pinta un icono
  que el diseño no tiene (`theme-shortcodes.php:7770`).
- `thousands_separator`: `""` | `"comma"` | `"space"`. **No hay opción de punto**: para el formato
  español (`1.000`) la aproximación correcta es `"space"` (`1 000`, que es lo que recomienda la RAE);
  si el cliente exige el punto, entonces sí toca `plain_text` estático y se pierde la animación.
- `duration` en ms (ej. `"1500"`), `type`: `"vertical"`.

**Aviso:** la animación puede estar apagada globalmente en Theme Options
(`math-animations-disable`, `theme-shortcodes.php:7728`). Si las cifras salen fijas, mirar ahí antes
que al JSON.

**Resumen:** cifras = `counter` con `prefix`/`number`/`label`/`title`, `icon` e `image` vacíos y
`thousands_separator: "space"` para miles en español.

---

## 4. Sección con imagen de fondo y card centrada (CTA catálogo)

**Diseño:** Sección altura fija (ej. 80rem), imagen de fondo cover y overlay; una card blanca centrada con título, texto y dos botones.

**Sección (attr):**

- `height_switcher`: `"custom"`.
- `css_advanced_height`: ej. `{ "desktop": "80rem" }`.
- `css_advanced_background_image`, `css_advanced_background_size`: `"cover"`, `css_advanced_background_position`: `"center"`.
- `css_advanced_background_overlay_background_color`: overlay (ej. `rgba(29,36,44,0.2)`).
- `css_advanced_align_items` y `css_advanced_justify_content`: `"center"` en `.section_wrapper`.

**Wrap (attr):**

- Grid 2 columnas (o 1 en tablet) con **gap** (ej. `css_grid_columns_gap`: 4rem).
- Fondo blanco en el wrap inner: `css_advanced_background_color`: `"#FFFFFF"`, `css_advanced_padding`, `css_advanced_border_radius`.
- `width_switcher`: `"custom"`, `css_advanced_flex`: `"1580px"` (y 100% tablet).
- `css_advanced_align_self`: `"flex-end"` si se quiere la card más abajo; o centrado con align/justify en section.

**Contenido del wrap:** Un **wrap anidado** (`item_is_wrap`: 1) con:

- **heading** (h2).
- **column** (texto descriptivo).
- Dos **button** (ej. “Discover the catalog” y “Visit our Youtube channel”) con `classes`: `"arrow-button"`, enlaces y márgenes responsive.

**Resumen:** Imagen de fondo + card = sección con height custom + background image + overlay; wrap con fondo blanco, padding y border-radius; contenido en wrap anidado (heading + column + botones).

---

## 5. Bloque “Partner” + estadísticas (2 columnas + 4 números)

**Diseño:** Fondo oscuro (#1D242C); primera fila en dos columnas (título grande a la izquierda, texto + botón a la derecha); segunda fila con 4 estadísticas (número grande + texto).

**Sección (attr):**

- `css_advanced_background_color`: `#1D242C`.
- `width_switcher`: `"full"`, contenido centrado con `css_advanced_justify_content`.

**Primer wrap (2 columnas):**

- `grid_columns_switcher`: `"custom"`.
- `css_grid_columns_custom`: `{ "desktop": "1.5fr 1fr", "mobile": "1fr" }`.
- `width_switcher`: `"custom"`, `css_advanced_flex`: `"1580px"`.
- `css_grid_columns_gap`: ej. 6rem desktop.

**Items del primer wrap:**

- Columna 1: puede incluir una **image** con posición absoluta (derecha, abajo 70%) para efecto visual, y un **wrap anidado** con un **heading** (texto blanco).
- Columna 2: **wrap anidado** con **column** (texto blanco, `css_column_attr_color`: `#FFFFFF`) y **button** (estilo outline blanco: `css_button_border_color`, `css_button_background_color`: transparent, clase `arrow-button arrow-button-white`).

**Segundo wrap (4 estadísticas):**

- `css_grid_columns`: `{ "desktop": "repeat(4, 1fr)", "mobile": "repeat(2, 1fr)" }` (sin `grid_columns_switcher` custom, o con custom si se quiere algo tipo `1.5fr 1fr`).
- En el diseño real se usa también `css_grid_columns_custom` con `"desktop": "1.5fr 1fr"` para el wrap de estadísticas (dos columnas de proporción fija).
- Cada celda es un **wrap anidado** con:
  - **counter:** `type`: `"vertical"`, `number`, `label` (ej. "+", "%", "X"), `title_tag`: `"h3"`, `duration`: `1000`.
  - **column:** texto descriptivo en blanco.

**Resumen:** Partner + stats = un wrap en grid 1.5fr 1fr (heading + image opcional | column + button) y otro wrap en grid 4 columnas (o 2+2 en móvil) de counter + column por celda.

---

## 6. CTA final con imagen de fondo y overlay en degradado

**Diseño:** Sección con imagen de fondo a ancho completo, overlay en degradado (de transparente abajo a sólido arriba), altura fija; a veces solo impacto visual sin contenido en wraps, o un pequeño CTA centrado.

**Sección (attr):**

- `height_switcher`: `"custom"`, `css_advanced_height`: ej. `{ "desktop": "70rem" }`.
- `background_switcher_scroll`: por defecto; `background_overlay_switcher`: `"gradient"`.
- `css_advanced_background_image`, `css_advanced_background_size`: `"cover"`, `css_advanced_background_position`: `"center"`.
- `css_advanced_overlay_gradient`:  
  `"val": { "color": "#1D242C", "string": "linear-gradient(0deg, rgba(29,36,44,0) 0%, #1D242C 100%)", "color2": "rgba(29,36,44,0)", "location2": "100%" }`.
- `css_advanced_align_items`: `"flex-start"`, `css_advanced_justify_content` y `css_advanced_align_content`: `"center"` para centrar contenido si hay wraps.

Si hay contenido (ej. “Have any doubts? Contact us!”), suele ir en un wrap con ancho limitado y uno o dos items (heading + button o call_to_action).

**Resumen:** CTA final = sección con imagen de fondo + `background_overlay_switcher`: `"gradient"` y `css_advanced_overlay_gradient` para el degradado; altura custom; opcionalmente un wrap con CTA centrado.

---

## 7. Imagen que “sale” del bloque (posición absoluta)

**Uso:** En secciones con color sólido (ej. naranja), una imagen del producto que se solapa con la siguiente sección o con el borde.

**En el item image (attr):**

- `width_switcher`: `"custom"`.
- `css_advanced_flex`: ancho (ej. `"55rem"` en tablet).
- `css_advanced_position`: `"absolute"`.
- `css_advanced_right` o `css_advanced_left`: ej. `"-28rem"` (desktop), `"-20rem"` (tablet).
- `css_advanced_bottom`: ej. `"70%"`.
- `visibility`: `" hide-mobile"` si solo se muestra en desktop/tablet.

**Resumen:** Imagen “flotante” = item image con posición absoluta y valores negativos en right/left/bottom y ancho custom; opcionalmente oculta en móvil.

---

## 8. Botones con estilo “arrow” (TMC)

En el diseño real se usan clases y estilos concretos:

- **Sólido (fondo blanco, texto negro):** `classes`: `"arrow-button"`.
- **Outline blanco (fondo transparente, borde y texto blanco):** `class`: `"arrow-button arrow-button-white"`; en attr: `css_button_background_color`: transparent, `css_button_border_color` y `css_button_color`: `#FFFFFF`; hover con `css_button_background_hover`: `#ffffff`, `css_button_color_hover`: `#1d242c`.
- **Enlace externo:** `target`: `"1"` (o `"_blank"` según tema), `link`: URL.

**Resumen:** Mantener `class` y los `css_button_*` / `css_button_*_hover` para fidelidad visual con el sitio TMC.

---

## 9. Checklist para generar JSON fiel al diseño

- [ ] **Secciones:** Incluir `icon`, `jsclass`, `title`, `ver` si el import lo requiere; si no, al menos `uid`, `attr`, `wraps`.
- [ ] **Wraps:** Siempre `size`, `tablet_size`, `mobile_size` (y `laptop_size`, `tablet_resized` si existen en el real). Para layouts en grid: `grid`, `grid_columns_switcher`, `css_grid_columns_custom` con val desktop/tablet/mobile.
- [ ] **Heading:** En diseño real `attr.title` y `attr.header_tag`; tipografía con `css_typography.val` (desktop, mobile) y color con `css_color`.
- [ ] **Column:** `attr.content` (HTML); colores de texto con `css_column_attr_color` (y `css_column_attra_color` para enlaces).
- [ ] **Hero con video:** `background_switcher`: `"video"`, `bg_video_mp4`, overlay, height 100vh; segundo wrap con `align-self`: flex-end para card abajo.
- [ ] **Card sobre imagen:** Wrap con fondo blanco, padding, border-radius, ancho custom; contenido en wrap anidado.
- [ ] **Estadísticas:** Item **counter** (nunca `plain_text` estático) con `type`: `"vertical"`,
      `prefix`/`number` entero/`label`/`title`, `icon` e `image` vacíos y `thousands_separator`
      (`"space"` para miles en español). Ver §3.ter.
- [ ] **Fila de tarjetas con gap del diseño:** wrap `1/1` en `grid` + un `item_is_wrap` por tarjeta
      con `height: 100%`, no N wraps hermanos `1/4` (no admiten `gap`). Ver §3.bis.
- [ ] **Overlay degradado:** `background_overlay_switcher`: `"gradient"` y `css_advanced_overlay_gradient` con `string` del linear-gradient.

---

## Referencia de archivos

| Archivo | Contenido |
|---------|-----------|
| `examples/example2/home.json` | Home: hero video, barra naranja, categorías (query), catálogo CTA, partner + counters, CTA final. |
| `examples/example1/about-us.json` | About: hero imagen, columnas con enlaces, valores (heading + list/column), innovación, CTA. |
| `builder-elements/TMC-ABOUT-COMPARISON.md` | Comparación diseño real vs JSON generado (About) y buenas prácticas. |

Con esta guía se puede revisar cómo está hecha cada maquetación en el JSON real y replicar o simplificar de forma coherente al generar nuevo contenido para el builder.
