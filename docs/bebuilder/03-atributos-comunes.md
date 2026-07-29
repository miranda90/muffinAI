# 03 — Atributos comunes: Advanced, sección, wrap, switchers

Fuente: `class-mfn-builder-fields.php` — `set_section()` L181 (209 campos), `set_wrap()` L3497 (179 campos),
`set_advanced()` L66752 (pestaña común a todos los items).

## 1. Pestaña Advanced (TODOS los items la tienen)

Selectores base usados por estos campos:
- externa: `.mcb-section .mcb-wrap .mcb-item-mfnuidelement`
- interna: `.mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner` (+ `|hover` para variantes hover)

### Dimensiones y espaciado

| Clave attr | Tipo | style / notas | Responsive |
|---|---|---|---|
| `width_switcher` | select | `""` (default) \| `"inline"` \| `"custom"` | no |
| `css_advanced_flex` | text | `width` (helper emite `flex:0 0 X`); activo con `width_switcher: "custom"` | sí |
| `height_switcher` | select | `""` \| `"custom"` | no |
| `css_advanced_height` | text | `height` (caja interna) | sí |
| `css_advanced_padding` | dimensions **separated-fields** | `padding` sobre `.mcb-column-inner`; `val.{device}.{top,right,bottom,left}` | sí |
| `css_advanced_margin` | dimensions **separated-fields** | `margin` sobre `.mcb-column-inner`; objeto por lado | sí |

⚠️ El objeto `{top,right,bottom,left}` es **exclusivo de `margin` y `padding`** (los únicos `dimensions`
con `version: "separated-fields"`). El resto de `dimensions` — `border-width`, `border-radius` — usa
**string shorthand**. Ver §"Formatos por tipo de campo" y `05-reglas-y-trampas.md`.

📏 **Reglas del proyecto para el espaciado** (`05-reglas-y-trampas.md` §1, reglas 5 y 6):

- Valores en **`rem`** siempre (`"1.5rem"`, `"5rem"`), nunca `px` ni `em`. Se admiten `0`, `auto`,
  `%`, unidades de viewport y `calc()`/`var()`.
- Siempre **con valor `mobile`** además del `desktop`; `tablet`/`laptop` cuando el diseño lo pida.
  Un padding de `6rem` en desktop es casi siempre excesivo en móvil.

```json
"css_advanced_margin": {
  "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mcb-column-inner",
  "style": "margin",
  "val": {
    "desktop": { "bottom": "1.5rem" },
    "mobile":  { "bottom": "1rem" }
  }
}
```

### Posicionamiento

| Clave | Tipo | Notas |
|---|---|---|
| `css_advanced_position` | select | `""`\|`"relative"`\|`"absolute"`… ; `absolute` añade clase `mfn-column-absolute` |
| `css_advanced_top` / `_bottom` / `_left` / `_right` | text | activos si position ≠ `""` |
| `css_advanced_z_index` | text number | no responsive |
| `css_advanced_order` | text number | `order` flex, responsive |

### Fondo (normal y hover)

| Clave | Tipo | Notas |
|---|---|---|
| `background_switcher` | switch | `"default"` \| `"gradient"` — decide qué subcampos aplican |
| `css_advanced_background_color` | color | `background-color` caja interna |
| `css_advanced_gradient` | gradient | requiere `val.string` |
| `css_advanced_background_img` | upload | URL; helper envuelve en `url()` |
| `css_advanced_background_repeat` / `_position` (+`_position_v2`) / `_attachment` / `_size` (+`_size_v2`) | select/text | `_v2` activos con valor `"custom"` |
| `css_advanced_backdrop_filter` | backdrop_filter | requiere `val.string` |
| `css_advanced_transition` | sliderbar | `transition` (ms) |
| Variantes `*_hover` de todo lo anterior | | selector interna`\|hover` |

### Borde y sombra

| Clave | Tipo | Notas |
|---|---|---|
| `css_advanced_border_style` | select | si ≠ `none` activa color y width |
| `css_advanced_border_color` | color | |
| `css_advanced_border_width` | dimensions (sin `version`) | **string shorthand** `"top right bottom left"`, p. ej. `{"desktop": "1px 1px 1px 0px"}`. Responsive. NUNCA objeto por lado |
| `css_advanced_border_radius` | dimensions (sin `version`) | **string shorthand** `"top-left top-right bottom-right bottom-left"`, p. ej. `{"desktop": "8px 8px 8px 8px"}`. Responsive |
| `css_advanced_box_shadow` | box_shadow | string `"inset x y blur spread color"` |
| `css_advanced_overflow` | select | |

### Responsive / visibilidad

| Clave | Formato | Notas |
|---|---|---|
| `visibility` | string tokens con espacio inicial | `" hide-desktop hide-laptop hide-tablet hide-mobile"` (los que apliquen) |
| `custom-responsive` | `"hide"` (std) \| `"show"` | activa uno de los dos siguientes |
| `css_advanced_hide_under_custom` / `_show_under_custom` | sliderbar 400–1920 | media query dinámica |

### Animación

| Clave | Valores |
|---|---|
| `animate` | `""`, `fadeIn`, `fadeInUp/Down/Left/Right(+Large)`, `zoomIn(+Up/Down/Left/Right)(+Large)`, `bounceIn(+Up/Down/Left/Right)` |
| `css_advanced_animation_delay` | sliderbar 0–3000 ms |

### Transform

| Clave | Notas |
|---|---|
| `css_advanced_transform` (+`_hover`) | requiere `val.string` (o `val.{device}.string`) |
| `css_advanced_transform_origin` | select |

### Otros

| Clave | Tipo | Notas |
|---|---|---|
| `conditions` | logic | lógica condicional de visualización (en sección/wrap se llama `conditional_logic`) |
| `classes` | pills → `"clase-a clase-b"` | **usar este**, no `class` (deprecated) |
| `custom_id` | text | atributo `id` en el DOM (anclas) |
| `custom_css` | textarea | CSS crudo inline — **NO usar en JSON generado** |

## 2. Campos de SECCIÓN (no `css_*`)

- **Layout**: `width_switcher` (`""`\|`"full"`\|`"custom"`), `height_switcher` (`""`\|`"full-screen"`\|`"custom"`), `reverse_order`, `navigation`, `hide`, `collapse`, `style` (legacy).
- **Fondo/vídeo**: `background_switcher` (`"default"`\|`"gradient"`\|`"video"`), `bg_video_mp4` (URL), `bg_video_dots`, `background_switcher_hover`, `background_switcher_scroll`, `background_overlay_switcher` (`"default"`\|`"gradient"`).
- **Decoración**: `shape_divider_type_top/_bottom` + `_flip_`/`_invert_`/`_bring_front_`, `divider`, `decor_top`, `decor_bottom`.
- **Header templates**: `scroll-visibility`, `closeable`, `closeable-time`, `closeable-x`.
- **Query loop** (sección repetidora): `type: "query"`, `query_type` (`""` posts \| `"terms"`), `query_post_type`, `query_post_orderby/order/per_page/offset/pagination`, `query_terms_taxonomy`, `query_terms_includes_*/excludes_*`, `query_terms_orderby/order/hide_empty/number`, `query_display` (`""`\|`"slider"`), `query_display_style` (`"masonry"`), `query_slider_*` (columns, autoplay, speed, arrows, dots, …).
- **Identidad**: `section_id` (legacy) / `custom_id`, `classes`, `conditional_logic`, `global_sections(_select)`.
- **Legacy inline (prohibidos)**: `bg_color`, `bg_image`, `bg_position`, `bg_size`, `padding_top`, `padding_bottom`, `padding_horizontal`, `custom_css`.

`css_*` de sección más usados: `css_advanced_background_color/_image/_size/_position`,
`css_advanced_padding/_margin`, `css_advanced_height`, `css_advanced_align_items/_justify_content/_align_content`
(sobre `.section_wrapper`), `css_advanced_background_overlay_background_color` (overlay),
`css_advanced_overlay_gradient` (con `val.string`).

## 3. Campos de WRAP (no `css_*`)

- **Grid**: `grid: "grid"` (activa modo grid), `grid_columns_switcher` (`""` defined \| `"custom"`):
  - `""` → `css_grid_columns` (switch `1fr` … `repeat(6,1fr)`, std `repeat(3, 1fr)`; style `grid-template-columns` sobre `.mcb-wrap-inner`)
  - `"custom"` → `css_grid_columns_custom` (texto libre, ej. `"35rem 1fr"`)
  - gap: `css_grid_columns_gap` (`column-gap`, default px)
- **Layout**: `width_switcher` (`""`\|`"custom"` → `css_advanced_flex`), `height_switcher`, `vertical_align`, `column_margin`, `reverse_order`, `move_up` (legacy), `sticky` + `sticky_offset` (por dispositivo).
- **Query loop**: bloque `query_*` idéntico al de sección.
- **Identidad/estado**: `visibility`, `custom-responsive`, `classes`, `custom_id`, `animate`, `conditional_logic`, `global_wraps(_select)`.
- **Legacy inline (prohibidos)**: `padding`, `bg_color`, `bg_image`, `bg_position`, `bg_size`, `style`, `custom_css`.

Alineación de contenido del wrap: `css_advanced_align_items`, `css_advanced_justify_content`,
`css_advanced_align_self` (ej. `"flex-end"` para pegar abajo), sobre el wrap o su inner.

## 4. Switchers: cómo funcionan

Los switchers se guardan en `attr` como string plano (`"width_switcher": "custom"`). Si se omiten,
aplica su `std`, pero **escribirlos explícitamente** cuando se active el subcampo correspondiente:
el editor los usa para mostrar/ocultar controles (el CSS se genera igual desde los `css_*`).

| Switcher | Ámbito | Valores | Activa |
|---|---|---|---|
| `width_switcher` | sección | `""`, `"full"`, `"custom"` | custom → ancho custom |
| `width_switcher` | wrap/item | `""`, (`"inline"` item), `"custom"` | custom → `css_advanced_flex` |
| `height_switcher` | sección | `""`, `"full-screen"`, `"custom"` | custom → `css_advanced_height` |
| `grid_columns_switcher` | wrap (con `grid:"grid"`) | `""`, `"custom"` | ver §3 |
| `background_switcher*` | todos | `"default"`, `"gradient"` (+`"video"` en sección) | color+img vs gradient |
| `background_overlay_switcher` | sección/wrap | `"default"`, `"gradient"` | overlay color vs gradiente |
| `custom-responsive` | wrap/item | `"hide"`, `"show"` | hide/show_under_custom |

Los `condition` del panel apuntan al `attr_id` del campo controlador (no a su `id`); una misma
clave (`width_switcher`) tiene `attr_id` distinto por contexto (`sect_`/`wrap_`/`item_width_switcher_adv`).

## 5. Formatos de valor por tipo de campo (resumen)

| Tipo de campo | Valor en JSON |
|---|---|
| text / textarea / select / color / icon / upload | string (`"#fff"`, `"icon-basket"`, URL) |
| switch single | string clave de opción |
| switch multiple (`visibility`) | tokens separados por espacio, **con espacio inicial** |
| checkbox | `"1"` / `""` |
| pills (`classes`) | `"clase-a clase-b"` |
| sliderbar | `"24px"` (número+unidad) |
| upload_multi | `"12,45,88"` (IDs adjuntos) |
| dimensions **con `version: "separated-fields"`** (solo `margin` / `padding`) | objeto `{top,right,bottom,left}` (por dispositivo si responsive) |
| dimensions **sin `version`** (`border-width`, `border-radius`) | **string shorthand** de 4 valores separados por espacios: `"1px 1px 1px 1px"` (por dispositivo si responsive) |
| typography_vb | objeto por dispositivo con font-size, line-height, etc. |
| gradient / transform / filters | objeto; **obligatoria subclave `string`** |
| tabs | array de objetos según esquema del campo (`options` define subcampos); formato propio — ver `ajax.php:1046-1060` |
| order | string CSV (`"image,title,price,button"`) |
| hotspots | estructura anidada especial (`class-mfn-helper.php:315`) |
