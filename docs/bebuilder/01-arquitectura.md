# 01 — Arquitectura del JSON y ciclo de vida

## 1. Jerarquía

```
[ sección, sección, ... ]            ← raíz: SIEMPRE array de secciones
  sección.wraps = [ wrap, ... ]
    wrap.items  = [ item, ... ]
      item.items = [ item, ... ]     ← solo si item.item_is_wrap = 1 (nested wrap)
```

`attr` en cada nivel es un **objeto plano `id_de_campo → valor`**. Los ids y formatos de valor
los define `class-mfn-builder-fields.php` (ver docs 03 y 04).

## 2. Esqueleto completo (paridad Visual Builder)

```json
[
  {
    "icon": "section", "uid": "a1b2c3d4e", "jsclass": "section", "title": "Section",
    "ver": "default",
    "attr": { "width_switcher": "full", "css_advanced_padding": { "...": "..." } },
    "wraps": [
      {
        "icon": "wrap", "uid": "b2c3d4e5f", "jsclass": "wrap", "title": "Wrap",
        "size": "1/1", "tablet_size": "1/1", "mobile_size": "1/1",
        "attr": {},
        "items": [
          {
            "type": "heading", "jsclass": "heading", "title": "Heading", "icon": "heading",
            "uid": "c3d4e5f6a", "size": "1/1", "tablet_size": "1/1", "mobile_size": "1/1",
            "attr": { "title": "Hola", "header_tag": "h2" }
          }
        ]
      }
    ]
  }
]
```

## 3. Campos obligatorios REALES por nivel (verificado en código)

| Campo | Nivel | ¿Obligatorio? | Evidencia |
|---|---|---|---|
| `wraps` | sección | Sí de facto (sin él la sección sale vacía) | legacy `section.items` se autoconvierte: `visual-builder-class.php:951` |
| `size` | **wrap** | **SÍ — sin él el wrap NO SE RENDERIZA** (return silencioso) | `front.php:1625-1627` |
| `size` | **item** | **SÍ — sin él el item NO SE RENDERIZA** | `front.php:2614-2616` |
| `type` | item | **SÍ**, salvo `item_is_wrap: 1` | `front.php:2606-2608` |
| `type` inexistente | item | Item ignorado en silencio (`method_exists`) | `front.php:2608` |
| `uid` | todos | No — se regenera SIEMPRE al importar | `helper.php:232-292` |
| `attr` | todos | No (fallback `[]`), pero sin él no hay estilos | `front.php:2620` |
| `tablet_size`/`mobile_size`/`laptop_size` | wrap/item | No — fallbacks: `tablet_size=size`, `mobile_size='1/1'`, `laptop_size=size` | `front.php:1554-1562` |
| `icon`, `jsclass`, `title` | todos | No — los regenera `loadExistedElements()` al abrir el VB | `visual-builder-class.php:1036-1067` |
| `ver` | sección | No; solo relevante en templates de header (`header-sticky`/`header-mobile`) | `front.php:448-450` |

**Valores válidos de `size`** (`front.php:37-51`): `1/6`, `1/5`, `1/4`, `1/3`, `2/5`, `1/2`, `3/5`, `2/3`, `3/4`, `4/5`, `5/6`, `1/1` y `divider` (solo wrap). Cualquier otro valor → warning PHP + layout roto.

## 4. Nested wraps (`item_is_wrap`)

Un item con `"item_is_wrap": 1` es un **wrap anidado**: no lleva `type`, lleva `size` + `items[]` propios.
Es estructura canónica y soportada:

- `front.php:2569-2572` — `show_items()` delega a `show_wraps()` ANTES de leer `type`. Sin error.
- `helper.php:263-276` — `unique_ID_reset()` recorre sus hijos.
- `visual-builder-class.php:1005-1012` — el VB le inyecta `jsclass/title/icon` de wrap.

**UN SOLO NIVEL.** El render (`show_items` → `show_wraps`) recurre sin límite, pero las tres rutinas
de la ruta de import se paran en el primer nivel: `unique_ID_reset` (`helper.php:246-282`),
`loadExistedElements` (`visual-builder-class.php:1005`) y `MfnLocalCssCompability::nested_wrap`
(`local-css-compability.php:365-371`). Un wrap anidado dentro de otro wrap anidado degrada en
silencio: uid sin regenerar, bloque ausente del panel y `css_*` sin normalizar. Detalle y
alternativas de maquetación en `05-reglas-y-trampas.md` trampa 16; el validador lo bloquea (E014).

**Limitaciones reales** (no error 500):
- El **builder clásico admin** (formulario antiguo) genera warnings PHP 8 con nested wraps (`admin.php:833` sin guard) — puede parecer un 500 con `display_errors` activo.
- **BeBuilder Blocks Classic se autodesactiva** si detecta `item_is_wrap` o `type: "query"` en la página (`admin.php:1637-1646`).
- Conclusión práctica: nested wraps OK para el Visual Builder; evitarlos si la página debe editarse con el builder clásico/Blocks Classic.

## 5. Ciclo de vida

### 5.1 Import

| Vía | Endpoint | Código |
|---|---|---|
| Visual Builder (pegar JSON) | `wp_ajax_importdata` | `visual-builder.php:1044-1077` |
| VB clipboard | `wp_ajax_importfromclipboard` | `visual-builder.php:1315` |
| Builder clásico | `wp_ajax_mfn_builder_import` | `ajax.php:1175` |

- Espera `json_decode` → array de secciones. Validación mínima: nonce + `is_array`. **Sin validación de esquema**: JSON incompleto se acepta y se degrada en silencio al renderizar.
- `unique_ID_reset()` **sobrescribe todos los `uid`** (sección/wrap/item/nested de primer nivel). Los uid del JSON de entrada son irrelevantes; no construir referencias cruzadas por uid.

Cadena real de `wp_ajax_importdata` (`visual-builder.php:1046-1077`):

```
mfnvb_import_data()
  └ MfnLocalCssCompability->render($items)   normaliza css_* legacy (1 nivel de anidamiento)
  └ mfnvb_renderView($items, $id)            visual-builder.php:1513
      ├ new MfnVisualBuilder()               ← instancia una clase de CPT según el post EDITADO
      ├ unique_ID_reset()                    regenera uid
      ├ $front->show_sections()              renderiza el HTML de vuelta
      └ loadExistedElements()                construye el formulario del panel
```

**El paso que más 500 provoca es el primero de `renderView`**, y no depende del JSON: `MfnVisualBuilder`
elige la clase de post type con `get_post_type($post_id)` y la instancia sin `class_exists()`
(`visual-builder-class.php:52`). Si ese CPT está desactivado en Theme Options, su clase no se ha
cargado (`functions.php:118-146`) y el import muere con un fatal. Ver `05-reglas-y-trampas.md`
trampa 15 — es el primer sitio donde mirar ante un 500 al importar.

### 5.2 Export

- **Visual Builder**: 100% JS (`scripts.js prepareForm.get()`), exporta el objeto en memoria → incluye `jsclass`, `title`, `icon`, `ver`, `laptop_size`, `used_fonts`. Puede llevar basura de runtime `attr.vb`, `attr.vb_postid`, `attr.rwd` — **no generarla nunca** (puede alterar dynamic data vía `front.php:2638-2640`).
- **Builder clásico**: `ajax.php:942-1173`, reconstruye desde `$_POST`; NO emite `icon/jsclass/title/ver` ni sizes responsive.

### 5.3 Guardado en BD

| Meta key | Contenido |
|---|---|
| `mfn-page-items` | Estructura del builder (fuente de verdad). **Nunca JSON**: array serializado por WP, o `base64_encode(serialize())` si opción `builder-storage = encode` |
| `mfn-page-object` | Array PLANO `{jsclass, uid, attr}` usado para recalcular CSS local |
| `mfn-page-local-style` | JSON de estilos locales calculados |
| `mfn-page-fonts` | Fuentes usadas (para encolar Google Fonts) |
| `mfn-page-items-seo` | Texto plano para Yoast/RankMath |
| `mfn-builder-preview*` | Datos de preview |
| `mfn-builder-revision-*` | Hasta 10 revisiones |

Lectura canónica en todo el theme:
```php
if ( ! is_array($mfn_items) ) {
    $mfn_items = unserialize( base64_decode($mfn_items), ['allowed_classes' => false] );
}
```

### 5.4 Flujo de guardado del VB (`wp_ajax_updatevbview`, `visual-builder.php:236-390`)

1. `$_POST['sections']` (árbol) + `$_POST['obj']` (array plano para CSS).
2. `Mfn_Helper::preparePostUpdate($obj, $post_id)` → genera `uploads/betheme/css/post-{ID}.css` + fuentes.
3. Serializa según `builder-storage` → `mfn-page-items`.
4. **Si `sections` llega vacío → `delete_post_meta('mfn-page-items')`**: un JSON malformado que decodifique a `[]` BORRA la página (`visual-builder.php:385`).

### 5.5 Punto crítico: el CSS NO se genera solo con el meta

Escribir `mfn-page-items` directamente (SQL/WP-CLI/importer propio) **no** genera el CSS local.
Hay que invocar además:

```php
Mfn_Helper::preparePostUpdate( $array_plano_de_{jsclass,uid,attr}, $post_id );
```

(así lo hacen `admin.php:3320` y `visual-builder.php:353-354`). Alternativa práctica: importar por
el endpoint del VB o abrir y guardar la página en el VB una vez — regenera todo.

## 6. Render front (camino de un item hasta HTML)

```
mfn-page-items → Mfn_Builder_Front::show() (front.php:269)
  └ show_sections() :406 → <section class="section mcb-section mcb-section-{uid} ...">
      └ .section_wrapper.mcb-section-inner-{uid} :1004
         └ show_wraps() :1523 → <div class="wrap mcb-wrap mcb-wrap-{uid} column_1_1 ...">
             └ .mcb-wrap-inner-{uid} :2099
                └ show_items() :2556 → <div class="column mcb-column mcb-item-{uid} column_{type}">
                    └ .mcb-column-inner-{uid} :2782
                       └ Mfn_Builder_Items::item_{type}($item['attr'], $vb) :2819
                           └ sc_{type}($fields) en theme-shortcodes.php → HTML final
```

`Mfn_Builder_Items` pasa el `attr` COMPLETO a `sc_*()`, que hace `extract(shortcode_atts([...], $attr))`:
las claves de `attr` **son** los parámetros del shortcode; las no declaradas se descartan en silencio.

Wraps/secciones tipo `query` (`attr.type = "query"`): repiten sus wraps por cada resultado de
`WP_Query`/`get_terms` (loops dinámicos), con soporte slider (Swiper) y masonry. Ver campos `query_*` en doc 03.

Dos detalles del render dentro de un loop, ambos con consecuencias al editar:

- Cada iteración se envuelve en `.mfn-queryloop-item-wrapper` (`:1230`/`:2310` para términos,
  `:2489` para posts).
- **Solo la iteración 0 es editable**: `:2793` `if( $vb && !$w_iterate )` es lo que añade `vb-item`,
  `data-uid` y la barra del módulo. Combinado con `iframe.css:1544` (`pointer-events: none` en las
  demás), en el VB solo se puede tocar la primera tarjeta. Trampas 18 y 20 de la doc 05.
