# 05 — Reglas de oro, trampas verificadas y checklist

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
9. **Elementos nativos primero**: `heading` (`title`+`header_tag`), `button`, `image`, `list`,
   `counter`, `plain_text`… antes que HTML en `column`.
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

## 3. Correcciones a documentación previa del proyecto

- **FALSO: "item con `item_is_wrap` sin `type` → error 500 en import admin-ajax".**
  El nested wrap sin `type` es la forma canónica y está soportada en front (`front.php:2569`),
  helper y VB. El origen del mito: warnings PHP 8 del **builder clásico admin** (formulario viejo)
  que con `display_errors` parecen un 500. Regla real: nested wraps OK para VB; evitarlos solo si
  la página debe editarse con builder clásico/Blocks Classic.
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
- [ ] Nested wraps (`item_is_wrap`) solo si el destino es Visual Builder.
- [ ] Paridad VB deseada → incluir `icon`, `jsclass`, `title`, `ver` (opcionales pero exportables).
- [ ] Sin `attr.vb`, `attr.vb_postid`, `attr.rwd`.

## 5. Patrones de maquetación

Ver `builder-elements/GUIA-MAQUETACIONES.md` (validada): hero con video, barra sólida + grid custom,
grid de categorías con query, card sobre imagen, partner + counters, CTA con overlay degradado,
imagen en posición absoluta "saliendo" del bloque.
