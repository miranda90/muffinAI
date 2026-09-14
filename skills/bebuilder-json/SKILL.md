---
name: bebuilder-json
description: Genera y valida JSON para BeTheme/Muffin Builder (BeBuilder) a partir de diseños, HTML o ideas. Usar cuando se cree o edite JSON de mfn-page-items, se convierta un diseño a builder JSON, o se mencione BeBuilder, Muffin Builder o builder JSON.
---

# BeBuilder JSON Expert

Jerarquía: **secciones → wraps → items** (raíz = array de secciones). El JSON no se escribe a
mano: lo genera un script Python con la API compacta de `tools/mfn.py` y lo entrega
`tools/build.py`, que valida contra el catálogo real del theme. Esta skill cabe en una lectura;
los docs largos se consultan solo cuando la tabla final lo indique.

## 1. Flujo de un encargo (en este orden)

1. `proyectos/<cliente>/build_<pagina>.py` copiado de `proyectos/_plantilla/build_plantilla.py`.
   Nada en la raíz ni en el CWD.
2. **Medios antes que maquetación** (doc 09): inventariar imágenes/logos/iconos/vídeos del diseño,
   descargar a `assets/`, subir al WordPress destino, registrar en `assets/manifest.json`
   (`python3 tools/assets.py register …`). En el script solo `context.media("nombre")` → `URL#ID`.
   Nunca URLs de Figma, `localhost` ni inventadas; lo no conseguido se lista como pendiente.
3. Tokens del diseño en el script (`TOKENS`, roles tipográficos `T` con valor mobile, `BTN`…).
4. Trocear el diseño: bandas → `sec()`, filas/columnas → `wr()`, tarjetas → `nw()`, bloques → `el()`.
   Registrar cada banda con `context.bind(id, nodo, evidence=…, responsive={…})`; `evidence` es
   `measured` (medido en Figma/HTML), `inferred` (spec textual, imagen, deducido) o `pending`.
5. Iterar `python3 tools/build.py proyectos/<cliente>/build_<pagina>.py --check` hasta
   `"accepted": true` (exit 0). Se corrige el script, nunca el JSON.
6. Publicar con el mismo comando sin `--check` (escribe JSON + `.report/.design/.profile.json`).
7. Entregar: importar por Export/Import del Visual Builder y **guardar una vez en el VB** (sin ese
   guardado no hay CSS: trampas 6 y 17). Comprobar
   `grep -c "figma.com\|localhost\|placeholders/image.svg" salida.json` → 0.

## 2. API compacta (`from mfn import el, wr, nw, sec, bg`)

Cada kwarg es un **campo del catálogo**, con o sin prefijo `css_` / `css_advanced_`. Selector y
style se copian del catálogo; el valor se normaliza según el tipo del campo; los switchers del
panel que condicionan el campo (`background_switcher`, `grid`, `image_height`, `full_width`,
`width_switcher`, `height_switcher`…) se declaran solos. Un campo inexistente lanza `ValueError`
con sugerencias. Campos por tipo: `python3 tools/fields.py <tipo>` (`--grep`, `--advanced`, `--types`).

```python
BTN = dict(button_background_color=T_PRIMARY, button_color="#fff", button_border_radius=0,
           button_padding=(12, 28), button_typography={"desktop": {...}, "mobile": {...}}, margin=0)

hero = sec(
    wr(el("heading", title="Titular", header_tag="h1", color="#fff", typography=T["h1"], margin=(0, 0, 24, 0)),
       el("plain_text", content="Texto", descdesca_color="#fff", desc_typography=T["p"], margin=(0, 0, 40, 0)),
       el("button", title="Empezar", link="/contacto/", **BTN, cols=("1/3", "1/2")),
       cols=("2/3", "1/1")),
    padding=(160, 36, 120, 36), max_width="1728px", background_color="#221C3D",
    **bg(context.media("hero")), name="Hero")

cards = sec(
    wr(*[nw(el("image", src=context.media(f), alt=t, image_cover_height=240, margin=(0, 0, 24, 0)),
            el("heading", title=t, header_tag="h3", typography=T["h3"], margin=(0, 0, 12, 0)),
            el("button", title="Ver", link=u, **BTN),
            background_color="#fff", padding=32, height="100%", align_content="space-between")
         for f, t, u in CARDS],
       grid_columns={"desktop": "repeat(3, 1fr)", "tablet": "repeat(2, 1fr)", "mobile": "1fr"},
       grid_columns_gap="2rem", grid_rows_gap="2rem"),
    padding=(120, 64), max_width="1728px", name="Servicios")

cifras = sec(wr(*[el("counter", number=n, label=suf, title=t, icon="", image="", cols=("1/3", "1/3")) for n, suf, t in KPI]),
             padding=(96, 36), background_color="#0B1B2B", name="Cifras")
cta = sec(wr(el("heading", title="¿Hablamos?", header_tag="h2", txt_align="center", typography=T["h2"]),
             el("button", title="Escríbenos", link="/contacto/", **BTN, text_align="center")),
          padding=(96, 36), background_color=T_PRIMARY, name="CTA")
```

| Valor que pasas | Campo | Resultado |
|---|---|---|
| `(80, 0)`, `"24px 0 0"`, `32`, `{"bottom": "2rem"}` | `padding` / `margin` (y `button_padding`…) | lados `top right bottom left`, **px → rem** con `root_font_px` del perfil, `0` → `"0px"`, `mobile` = desktop si no se da |
| `{"desktop": (80, 0), "mobile": (40, 0)}` | ídem | cada breakpoint normalizado; `laptop`/`tablet` opcionales |
| `8`, `"1px 0"` | `border_radius`, `border_width` | string shorthand `"8px 8px 8px 8px"` (trampa 14) |
| `{"font-size": "68px", ...}` o `{"desktop": …, "mobile": …}` | `typography`, `desc_typography`, `button_typography` | `mobile` replicado si falta |
| `16`, `"100%"`, `"center"` | campo responsive (`gap`, `height`, `image_cover_height`, `align_items`…) | `{"desktop": v}` + unidad del catálogo si es número |
| `"#fff"` | color | tal cual |
| `"0 4px 24px 0 rgba(0,0,0,.08)"` | `box_shadow`, `text_shadow` | string CSS tal cual |
| gradient / transform dicts | compuestos | tal cual (`transform()` de mfn para transform) |
| `120`, `1` | campos de contenido/switch (`number`, `full_width`…) | `"120"`, `"1"` (el theme guarda strings) |
| `css(...)`, `typo(...)`, `style_field(...)` | cualquiera | se respeta sin tocar |
| `cols="1/2"` / `cols=("1/3", "1/2", "1/1")` | `el`/`wr`/`nw` | `size` / `tablet_size` / `mobile_size` (mobile `1/1` por defecto) |
| `name="Hero"` | todos | `title` del nodo en el panel (`title`/`label` son campos de contenido: heading, button, counter) |
| `align="center"`, `bg_color=…` | legacy | `ValueError`: el front los vuelca como `style=""` inline; usar el `css_*` |
| campo con guion (`counternumber-wrappernumber_color`) | cualquiera | `**{"campo-con-guion": v}` |

Sizes válidos: `1/6 1/5 1/4 1/3 2/5 1/2 3/5 2/3 3/4 4/5 5/6 1/1`. `sec()` pone `width_switcher: full`
salvo `max_width=` (→ `custom`). Un dict de kwargs (`**BTN`) es la forma de compartir estilo.
Centrar dentro de su columna: botón `text_align="center"` (`css__text_align`), imagen
`image_text_align="center"`, título `txt_align="center"`; no `justify_content` en el wrap. Botón a ancho completo: `full_width=1`
(no es responsive; en desktop el ancho lo da `cols`). Enlace de texto suelto: `plain_text` con
`<a>` y `descdesca_color` (cubre `.desc a`). Icono suelto: `icon_2` con `size`/`color`.
Los helpers previos (`css`, `typo`, `pad`, `m0`, `item`, `wrap`, `nested`, `section`, `style_field`,
`recipes.py`) siguen disponibles y se mezclan sin problema.

## 3. Elegir el elemento por lo que el bloque ES

`python3 tools/fields.py --types` lista los 128 tipos. Título → `heading` (`title` + `header_tag`),
párrafo → `plain_text` (`content`), botón → `button`, imagen → `image` (`src` = `URL#ID`, `alt`),
lista con iconos → `list`, cifras → `counter` (entero pelado en `number`; `prefix`/`label` para
`+`/`%`; `icon=""` e `image=""`; separador solo `""`/`comma`/`space`), pestañas → `tabs`,
acordeón → `faq`, testimonio → `testimonial`, badge sobre imagen → `banner_box`, vídeo →
`video` con `video=""` obligatorio + `mp4` + `placeholder` + `html5_parameters="a;;l;m;i"`
(trampa 25). Nunca empaquetar columnas o título+texto en un `column` con HTML y clases grid.
Si un nativo cubre el bloque se usa aunque el mockup sea estático; degradar solo con motivo.

## 4. Layout: reglas que la API no puede decidir por ti

- **Fila de tarjetas con hueco medido → siempre grid**: `wr(*[nw(...)], grid_columns=…,
  grid_columns_gap=…)`. `gap` no existe fuera del grid (trampa 21). En cada tarjeta `nw()`:
  `height="100%"` para que el fondo llene la celda y `align_content="space-between"` si el botón
  va abajo. Hermanos `wr(cols="1/3")` solo para columnas de contenido suelto.
- **Nested wraps: un solo nivel** (`nw` dentro de `nw` lanza error; trampa 16). Solo para VB.
- **Query loop**: de sección contiene wraps; de wrap contiene **un** `nw()` con los items de la
  tarjeta (varios items directos se borran al guardar; E016, trampa 20). Con `grid` en el wrap del
  loop, la celda se estila con `queryloop_item_*` del wrap. CPT de BeTheme (`portfolio`, `client`,
  `offer`, `slide`, `testimonial`…) deben estar activos en Theme Options o el VB da 500 (trampa 15).
- **Anchos custom saltan de fila por px, no por `size`** (trampa 22): el bloque que deba ocupar
  fila propia va en `wr(cols="1/1")` sin `width`/`flex`; el ancho del diseño se logra con el
  `cols` del item (`2/5` ≈ 650px, `2/3` ≈ 1104px sobre 1656px) + `justify_content`.
- **Contenedor del diseño** (p. ej. 1728px): `sec(max_width=…)` + padding lateral del diseño;
  no simularlo con wraps de ancho custom.
- **Margen del item**: el theme pone 12px laterales y 40px abajo por defecto; `margin=0` o el
  margen del diseño en cada `el()`.
- Espaciados en `rem` (la API convierte px); bordes, radios, anchuras fijas y sombras en `px`.
- Anclas → `custom_id`; clases → `classes`. Nunca emitir `vb`, `vb_postid`, `rwd` ni `uid` cruzados.
- No añadir animación, equal-height ni CTA abajo si el diseño no lo pide.

## 5. Validación y entrega

`tools/build.py --check` devuelve `accepted`, `exit_code`, `counts` e `issues` (sin infos si hay
algo más grave; `--full` para el informe completo). Exit `0` entregable · `1` errores (el JSON se
degrada o rompe) · `2` warnings con `--strict` (cada uno es decisión consciente y escrita) · `3`
no ejecutable/JSON ilegible. Excepción concreta en `EXCEPTIONS`:
`{"code": "W032", "path": "$[0].wraps[0]…", "reason": "…"}`; los errores estructurales no se
suprimen. Códigos y evidencia en el PHP: `tools/README.md`. Un JSON suelto:
`python3 tools/validate_bebuilder_json.py fichero.json --strict` (`--origin export` para exports
reales, `--fix -o` para lo mecánico).

Al entregar avisar de: guardar una vez en el VB; en el VB solo la primera tarjeta de un loop es
interactiva (trampa 18); un guardado con secciones vacías borra la página (nunca `[]`); medios
pendientes; CPT que deben estar activos.

## 6. Documentación (leer solo lo que haga falta)

| Cuándo | Dónde |
|---|---|
| Campos de un tipo, opciones, condiciones | `python3 tools/fields.py <tipo>` (ficha completa: `builder-elements/<tipo>.md`) |
| Runner, perfiles, `context.bind`, extracción Figma/HTML/imagen, comparación | `docs/bebuilder/10-flujo-verificable.md` |
| Medios: inventario, subida, manifest, vídeo | `docs/bebuilder/09-medios-imagenes-video.md` |
| Trampas verificadas 14–25 y checklist final | `docs/bebuilder/05-reglas-y-trampas.md` |
| Patrones de layout reales (hero vídeo, grid, counters, CTA overlay) | `builder-elements/GUIA-MAQUETACIONES.md` |
| Formato `css_*`, placeholders, breakpoints (≤1440/≤959/≤767) | `docs/bebuilder/02-css-pipeline.md` |
| Estructura JSON, nested wraps, ciclo import/export | `docs/bebuilder/01-arquitectura.md` |
| Iconos, tipografías/fuentes, Global Styles, animaciones | docs 07, 08, 06 y skill `bebuilder-animations` |
| Exports reales de referencia | `examples/example2/home.json`, `examples/example1/about-us.json` |

Scripts anteriores a `tools/mfn.py` (nordes, maderas, wat) están congelados: no migrarlos ni
ejecutarlos con `tools/build.py`. Si se rehace una página, script nuevo.
