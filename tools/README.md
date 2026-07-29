# tools/ — Validador de JSON BeBuilder

`validate_bebuilder_json.py` comprueba que un JSON de BeBuilder (`mfn-page-items`) es
importable y se renderizará como se espera, **antes** de tocar WordPress.

No es un JSON Schema genérico: contrasta el documento contra el catálogo real de campos del
theme (`builder-elements/_elements.json`, volcado ejecutando el PHP de
`class-mfn-builder-fields.php`) y contra el comportamiento verificado de
`class-mfn-helper.php` (motor de CSS) y `class-mfn-builder-front.php` (render).

## Uso

```bash
python3 tools/validate_bebuilder_json.py pagina.json          # informe legible
python3 tools/validate_bebuilder_json.py pagina.json --strict  # warnings también fallan
python3 tools/validate_bebuilder_json.py pagina.json --json    # salida para CI/agentes
cat pagina.json | python3 tools/validate_bebuilder_json.py -

# corrige lo mecánico y escribe el resultado
python3 tools/validate_bebuilder_json.py pagina.json --fix -o pagina.ok.json
```

Opciones: `--level error|warning|info`, `--ignore E020,W058`, `--max-issues N`,
`--max-per-code N` (por defecto 5, para que un código repetido 130 veces no tape el resto),
`--no-hints`, `--no-color`, `--schema RUTA`, `--indent N`.

El informe legible termina siempre con un **resumen por código**, así que en un export real con
cientos de repeticiones se ve de un vistazo qué hay realmente.

Códigos de salida: `0` válido · `1` errores · `2` solo warnings con `--strict` ·
`3` JSON no parseable o schema no encontrado.

## Qué corrige `--fix`

Solo lo determinista, nunca lo que exige decidir:

| Corrección | Detalle |
|---|---|
| `attr.vb` / `vb_postid` / `rwd` | eliminados (basura de runtime del VB) |
| `border-width` / `border-radius` con objeto | convertidos a string shorthand (trampa 14) |
| `class` | migrado a `classes` (fusionando si ya existía) |
| Pseudo-clase `:hover` en `selector` | reescrita a `\|hover` (solo si el theme no la declara con `:`) |
| `tablet_size` / `mobile_size` ausentes | añadidos (`= size` y `1/1`) |
| `uid` ausente | generado (9 chars, determinista por ruta) |
| `icon` / `jsclass` / `title` ausentes | añadidos para paridad con el Visual Builder |
| Atributo legacy con valor vacío | eliminado |

No inventa `size`, `type` ni contenido: esos casos siguen siendo errores.

## Catálogo de comprobaciones

### Errores — el JSON se rompe o se degrada en silencio

| Código | Comprobación |
|---|---|
| E001 | La raíz no es un array de secciones |
| E002 | Array raíz vacío → `delete_post_meta` **borra la página** (`visual-builder.php:385`) |
| E003 | Sección / wrap / item que no es objeto |
| E004 | Sección sin `wraps` (y sin `mfn_global_section_id`) |
| E005 | `wraps` / `items` que no son array |
| E006 / E007 | Wrap / item sin `size` → no se renderiza, sin aviso (`front.php:1625`, `:2614`) |
| E008 | `size` / `tablet_size` / `mobile_size` fuera de la lista válida |
| E009 | Item sin `type` y sin `item_is_wrap: 1` |
| E010 | `type` inexistente → item ignorado en silencio (`front.php:2608`); sugiere el más cercano |
| E011 / E012 | `item_is_wrap` con `type`, o sin array `items` |
| E013 | `attr` que no es objeto |
| E020 | `attr.vb`, `vb_postid` o `rwd` (runtime del VB; altera dynamic data) |
| E021 | Atributo legacy con valor → el front lo vuelca como `style=""` inline |
| E022 | `custom_css` |
| E023 / E024 | `style=""`, `<style>` o `<link rel=stylesheet>` dentro del contenido HTML |
| E030 | `selector` y `val` presentes pero `style` vacío → el helper emite `":valor;"` y corrompe la regla |
| E031 | Pseudo-clase escrita con `:` en vez de `\|` (y el theme no la declara así) |
| E032 | `selector` con `{`, `}` o `;` |
| E035 | **Trampa 14**: `border-width` / `border-radius` con objeto por lado en vez de string shorthand |
| E036 | `gradient` / `transform` / `filter` sin subclave `string` → no emite nada |
| E037 | `val` mezcla claves de dispositivo con claves sueltas no reconocidas |
| E055 | Item `heading` con `content`/`tag` (del shortcode inline) en vez de `title`/`header_tag` |

### Warnings — degradación parcial, panel del VB roto o incumplimiento de las reglas del proyecto

| Código | Comprobación |
|---|---|
| W001 | Sección con `items` legacy en vez de `wraps` |
| W002 | Wrap o item sin `tablet_size` / `mobile_size` — **regla 5**: el responsive debe ser explícito |
| W003 / W004 | `uid` fuera de formato / duplicado |
| W005 | `item_is_wrap`: desactiva BeBuilder Blocks Classic y avisa en el builder clásico |
| W020 | `class` deprecado (usar `classes`) |
| W030 | Campo de estilo con `selector` o `val` vacío → no genera CSS |
| W031 | `selector` sin `mfnuidelement` → el estilo se aplica a toda la página |
| W032 / W033 | `selector` / `style` distintos de los declarados en el theme |
| W037 | Claves no-dispositivo a primer nivel en un campo responsive |
| W039 | `val` = `"0"` → PHP `empty()` lo descarta y no genera CSS (usar `"0px"`) |
| W040 | Valor fuera del enum declarado del campo (con sugerencia) |
| W041 | Propiedad tipográfica no reconocida |
| W042 | Color con formato no reconocido |
| W043 | Valor numérico sin unidad en un `style` que la exige |
| W044 / W045 | Lados desconocidos en un `dimensions`, o shorthand con nº de valores raro |
| W047 | Valor con `;` o `{}` que puede romper la regla generada |
| W050 / W051 | Subcampo presente sin su switcher explícito, o con el switcher en otro valor |
| W055 | Item `heading` sin `attr.title` |
| W056 / W057 | Animación o token de `visibility` desconocido |
| W058 | Clave `attr` no declarada para ese elemento → `shortcode_atts()` la descarta |
| W059 | `custom_id` que no es un id HTML válido |
| W060 | Shortcode de otro page builder dentro del contenido |
| W061 | `padding` / `margin` en `px`, `em` o `pt` — **regla 6**: van en `rem` (con la equivalencia calculada) |
| W062 | `padding` / `margin` / tipografía sin valor `mobile` — **regla 5**: generar siempre pensando en responsive |

### Reglas del proyecto que el validador impone

`W002`, `W061` y `W062` no vienen del theme sino de las reglas 5 y 6 de
`docs/bebuilder/05-reglas-y-trampas.md` §1:

- **Regla 5 — siempre responsive.** Todo wrap e item con `size`, `tablet_size` y `mobile_size`
  explícitos; todo espaciado y tipografía con valor `mobile` además del `desktop`.
- **Regla 6 — espaciados en `rem`.** `padding` y `margin` en `rem`; admitidos `0`, `auto`, `%`,
  unidades de viewport y `calc()`/`var()`. Bordes, radios y tamaños fijos pueden ir en `px`.

Al validar exports ajenos (no generados por nosotros) tiene sentido silenciarlas:
`--ignore W002,W061,W062`.

### Infos — convención del proyecto y matices de paridad con el VB

`I001`–`I006` (uid/icon/attr ausentes, sección global, wrap vacío), `I021` (legacy vacío),
`I032` (selector equivalente pero no idéntico), `I035`, `I037`/`I038` (ámbito desktop),
`I050` (sección sin `width_switcher` explícito), `I053` (grid sin `grid: "grid"`),
`I057`, `I060`.

## Mantenimiento

El validador no tiene reglas hardcodeadas sobre campos concretos: todo sale del catálogo.
Tras actualizar el theme hay que regenerarlo:

```bash
cd builder-elements/_generator && php extract.php && python3 generate_fichas.py
```

Verificación rápida de que el validador sigue calibrado (los exports reales del VB deben
salir sin errores estructurales, solo con la basura de runtime que el propio VB añade):

```bash
python3 tools/validate_bebuilder_json.py examples/example1/about-us.json --json
python3 tools/validate_bebuilder_json.py examples/example2/home.json --json
```
