# 02 — Pipeline CSS: de `css_*` en el JSON a hoja de estilos

**Regla absoluta del proyecto: el JSON nunca lleva CSS inline ni genera archivos CSS a mano.**
Todo estilo se expresa como atributo `css_*` con `{selector, style, val}`; el theme genera
`wp-content/uploads/betheme/css/post-{ID}.css` automáticamente.

## 1. El motor real

`betheme/functions/builder/class-mfn-builder-styles.php` es **código muerto** (legacy Muffin Builder 2,
solo entiende `bg_color`/`padding_top`, nunca se instancia). Ignorarlo.

Motor real: `betheme/functions/admin/class-mfn-helper.php`

```
preparePostUpdate($obj_plano, $post_id)   L41   ← recorre attr de cada {jsclass, uid, attr}
  └ mfnLocalStyle($selector,$style,$val,$uid)  L404  ← placeholders + normalización
      └ generate_css($styles,$post_id)         L479  ← escribe uploads/betheme/css/post-{ID}.css
```

El front lo encola en `front.php:185 enqueue_local_style()` (o inline en `<head>` si la opción
del theme `local-styles-location = inline`).

## 2. Qué atributos se reconocen como estilo

**Criterio estructural, no de prefijo** (`class-mfn-helper.php:195-198`): el valor del atributo
debe ser un array con `selector`, `style` y `val` no vacíos. Por convención los ids empiezan por `css_`.
Un `css_*` "plano" (string) NO genera CSS. Única excepción con trato especial: clave `hotspots`.

Formato canónico — copiar `selector` y `style` **literalmente** de la definición del campo en
`class-mfn-builder-fields.php`:

```json
"css_advanced_padding": {
  "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner",
  "style": "padding",
  "val": {
    "desktop": { "top": "20px", "right": "", "bottom": "20px", "left": "" },
    "mobile":  { "top": "10px" }
  }
}
```

## 3. Placeholders del selector (`class-mfn-helper.php:404-428`)

| Placeholder en JSON | Sustitución |
|---|---|
| `mfnuidelement` | uid real del bloque (9 chars) |
| `.mcb-section-mfnuidelement` | además se prefija etiqueta → `section.mcb-section-{uid}` |
| `mcb-section-inner` | `mcb-section-inner-{uid}` |
| `section_wrapper` | `mcb-section-inner-{uid}` |
| `mcb-wrap-inner` | `mcb-wrap-inner-{uid}` |
| `mcb-column-inner` | `mcb-column-inner-{uid}` |
| `\|` (pipe) | `:` → pseudo-clases: escribir `\|hover`, `\|before`, `\|after` (NUNCA `:hover` en el selector) |

Selectores base por nivel:

| Nivel | Selector |
|---|---|
| Sección | `.mcb-section-mfnuidelement` |
| Sección interior (flex/align) | `.mcb-section-mfnuidelement .section_wrapper` |
| Overlay sección | `.mcb-section-mfnuidelement .mcb-background-overlay` |
| Wrap | `.mcb-section .mcb-wrap-mfnuidelement` |
| Wrap interior | `.mcb-section .mcb-wrap-mfnuidelement .mcb-wrap-inner` |
| Wrap grid | `.mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement .mcb-wrap-inner` |
| Item (caja externa) | `.mcb-section .mcb-wrap .mcb-item-mfnuidelement` |
| Item (caja interna) | `.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner` |

Clases reales en el DOM: `.mcb-section-{uid}`, `.mcb-section-inner-{uid}`, `.mcb-wrap-{uid}`,
`.mcb-wrap-inner-{uid}`, `.mcb-item-{uid}`, `.mcb-column-inner-{uid}`.

**uid**: 9 caracteres `[0-9a-f]` (openssl) o `[0-9a-z]` (fallback) — `helper.php:197-224`.

## 4. Breakpoints (`class-mfn-helper.php:505-565`)

| Clave en `val` | Media query |
|---|---|
| `desktop` | ninguna (base) |
| `laptop` | `@media(max-width:1440px)` |
| `tablet` | `@media(max-width:959px)` |
| `mobile` | `@media(max-width:767px)` |

- Solo esas 4 claves son dispositivos. La "herencia" es cascada CSS normal: lo declarado en
  `desktop` aplica también abajo salvo que se sobrescriba.
- **Trampa**: una clave de primer nivel de `val` que NO sea dispositivo se interpreta como
  sub-propiedad y va a desktop: `{"style":"padding","val":{"top":"10px"}}` → `padding-top:10px` SOLO desktop.
- El motor despacha por clave de dispositivo **siempre**, aunque la definición del campo no lleve
  `responsive: true` (eso solo gobierna el panel del VB). Usar breakpoints nunca es un fallo.

### Regla del proyecto: generar siempre pensando en responsive

Un JSON con estilos solo en `desktop` no se considera terminado. Como mínimo, todo espaciado
(`padding`/`margin`) y toda tipografía llevan además valor `mobile`; `laptop` y `tablet` se añaden
cuando el diseño lo pida. Detalle en `05-reglas-y-trampas.md` §1 regla 5.

```json
"css_advanced_padding": {
  "selector": ".mcb-section-mfnuidelement",
  "style": "padding",
  "val": {
    "desktop": { "top": "6rem", "bottom": "6rem" },
    "tablet":  { "top": "4rem", "bottom": "4rem" },
    "mobile":  { "top": "2.5rem", "bottom": "2.5rem" }
  }
}
```

### Regla del proyecto: `rem` en márgenes y paddings

Los valores de `padding` y `margin` se escriben en `rem` (`"1.5rem"`, `"5rem"`), nunca en `px`
ni `em`: escalan con la raíz del documento y mantienen el ritmo vertical coherente entre bloques
y entre breakpoints. Admitidos además: `0`, `auto`, `%`, unidades de viewport y `calc()`/`var()`.
Bordes, radios, anchuras fijas y sombras pueden seguir en `px`.

## 5. Estilos compuestos y especiales

| `style` | Forma de `val` | Salida |
|---|---|---|
| `padding` / `margin` (dimensions con `version: "separated-fields"`) | `{device: {top,right,bottom,left}}` | `padding-top: …; padding-right: …` (por lado) |
| `border-width` / `border-radius` (dimensions **sin** `version`) | `{device: "1px 1px 1px 1px"}` | `border-width: 1px 1px 1px 1px` |
| cualquier dimensions con string | `{device: "20px 10px"}` | `padding: 20px 10px` |

⚠️ **Nunca objeto por lado en `border-width` / `border-radius`.** La expansión por lado de
`class-mfn-helper.php:260` es ciega — concatena `$style_name.'-'.$v` — y produce
`border-width-top: 1px`, propiedad CSS inexistente que el navegador descarta: el borde no se ve.
Con `padding` el resultado (`padding-top`) sí es una propiedad válida, de ahí la asimetría.
Detalle completo y síntomas en el panel del VB: `05-reglas-y-trampas.md` §3.
| `typography` | `{device: {font-family, font-size, line-height, font-weight, letter-spacing, text-transform, font-style, text-decoration, color}}` | propiedades sueltas; `font-family` se registra en `mfn-page-fonts` y se entrecomilla |
| `gradient` | objeto con `type, angle, color, location, color2, location2` y **`string`** | SOLO `string` se emite, como `background-image` |
| `transform` | `{device: {…, "string": "matrix(…)"}}` | SOLO `string` |
| `filter` / `backdrop-filter` | `{device: {…, "string": "blur(10px)"}}` | SOLO `string` |
| `background-image` | `"https://…/img.jpg"` | se envuelve en `url(…)` automáticamente |
| `box-shadow` | string `"inset x y blur spread color"` | tal cual |
| `text-shadow` | string `"x y blur color"` | tal cual |
| `flex` (ancho custom de item/wrap) | `"1580px"` / `"50%"` | se prefija `0 0 ` → `flex:0 0 1580px` |
| `background-position_v2` / `background-size_v2` | string libre | el sufijo `_v2` se elimina |
| `hide_under_custom` / `show_under_custom` | `"768"` | media query dinámica display none/block |
| `--mfn-*` / `--swiper-*` | string | variable CSS tal cual |

Valores que NO generan regla: vacío, `"custom"`, `"cover-ultrawide"`, `background-attachment: "parallax"`
(estos tres últimos se traducen a clases/comportamiento en PHP).

## 6. `css_*` que además tocan PHP (clases/comportamiento)

| Clave | Efecto |
|---|---|
| `css_advanced_background_attachment` = `parallax` | activa parallax JS (`data-parallax` + `<img class="mfn-parallax">`) |
| `css_advanced_background_size` = `cover-ultrawide` | clase `bg-cover-ultrawide` |
| `css_advanced_background_image` con `{featured_image}` | inline necesario en query loops; fuera de loops → `var(--mfn-featured-image)` |
| `css_advanced_position` = `absolute` (desktop) | clase `mfn-column-absolute` |
| `css_advanced_transform(_hover)` | clase `mfn-transformed` |
| `css_line_clamp` | clase `mfn-line-clamp` |
| `css_queryloop_item_margin` | espaciado Swiper (`data-space_*`) |

## 7. Atributos LEGACY que generan estilo inline — PROHIBIDOS en JSON nuevo

Estos campos existen por compatibilidad y el front los vuelca a `style="…"` inline. **No usarlos.**

| Nivel | Atributos legacy (inline) | Código |
|---|---|---|
| Sección | `padding_top`, `padding_bottom`, `padding_horizontal`, `bg_color`, `bg_image`, `bg_position`, `bg_size`, `custom_css` | `front.php:690-741` |
| Wrap | `padding`, `bg_color`, `move_up`, `bg_image`, `bg_position`, `style` (CSS crudo concatenado), `custom_css` | `front.php:1839-1888, 2029-2052` |
| Item | `custom_css`; en `column`: `align`, `margin_bottom`, `padding`, `column_bg`, `bg_image`… (marcados `mfn-deprecated`) | `front.php:2736` |
| Todos | ids legacy formato `style:SELECTOR:propiedad` (formato pre-`css_*`) | migrados por `MfnLocalCssCompability` |

Equivalencias modernas:

| Legacy | Moderno |
|---|---|
| `padding_top/bottom/horizontal` (sección) | `css_advanced_padding` sobre `.mcb-section-mfnuidelement` |
| `bg_color` | `css_advanced_background_color` |
| `bg_image`/`bg_position`/`bg_size` | `css_advanced_background_image/_position/_size` |
| `padding` (wrap) | `css_advanced_padding` sobre `.mcb-wrap-inner` |
| `style` crudo | campos `css_*` específicos |
| `class` (campo deprecated de items) | `classes` (pestaña Advanced, tipo pills) |
