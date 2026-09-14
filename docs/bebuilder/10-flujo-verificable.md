# 10 — Generación verificable de muffinAI

Este documento actualiza el flujo de los scripts nuevos. Los scripts y JSON entregados permanecen congelados. Betheme se consulta, no se modifica.

## Construir y entregar

1. Copiar `proyectos/_plantilla/build_plantilla.py` al directorio del cliente.
2. Completar `PROFILE`, `SOURCE`, `TOKENS` y `build(context)` con la API compacta de `tools/mfn.py`
   (`el`/`wr`/`nw`/`sec`/`bg`: cada kwarg es un campo del catálogo; selector, style, `rem`, valor
   `mobile` y switchers se resuelven solos; detalle en `tools/README.md`). Campos por tipo:
   `python3 tools/fields.py <tipo>`. `--check` imprime solo veredicto e incidencias (`--full` para
   el informe completo).
3. Registrar diseño y decisiones responsive con `context.bind()`. Un bloque medido, inferido o pendiente conserva su procedencia en el sidecar; no se añaden campos propios al JSON de BeBuilder. Vincular una sección cubre sus descendientes, pero no justifica omisiones del diseño: cada bloque fuente debe asignarse o tener excepción.
4. Resolver medios y dependencias. Las URLs locales o temporales no son entregables.
5. Ejecutar desde cualquier directorio, utilizando rutas correctas al script:

```bash
python3 tools/build.py proyectos/_plantilla/build_plantilla.py --check
python3 tools/build.py proyectos/cliente/build_pagina.py --profile proyectos/cliente/profile.json
```

`--check` no escribe los artefactos. El módulo Python debe ser confiable y no tener efectos secundarios al importarse: `build(context)` devuelve la página y toda escritura la realiza el punto común de entrega. Los scripts históricos sin esa función se rechazan antes de importarlos.

Sin `--check`, se publican JSON, `.report.json`, `.design.json` y `.profile.json` junto al script. Cada fichero se reemplaza atómicamente; el JSON se publica al final. Una validación rechazada no sobrescribe la entrega anterior. `--draft` permite conservar una propuesta rechazada con sufijo `.draft.json` (y su `.draft.report.json` con `accepted: false`); si la propuesta se acepta, `--draft` no cambia nada y se publica normalmente.

Un informe aceptado localmente no acredita fidelidad visual: `visual_verification` y `wordpress_roundtrip` permanecen `not_run` hasta realizar esas pruebas.

## Contratos públicos

- `validate(document, schema=None, origin="generated", editor="visual", strict=False, fix=False, ignore=(), exceptions=(), manifest=None, profile=None)`: no modifica la entrada. Devuelve documento, incidencias, correcciones, `valid`, `structurally_valid`, `accepted` y `exit_code`.
- `BuildContext`: UID independientes, tokens, manifest, perfil, excepciones y mapa de diseño.
- `style_field(scope, key, value, itype=None, selector=None)`: recupera selector y propiedad del catálogo. Rechaza ambigüedades.
- `transform(scale_x=1, scale_y=1, skew_x=0, skew_y=0, x=0, y=0, rotate=0)`: produce siete parámetros editables y su cadena CSV. No pasar `matrix(...)` como `string`.
- `recipes`: heading, button, image, video, counter, card, grid, band, hero, split y cta. No añaden contenido demo del theme ni adivinan recursos.

Ejemplo de estilo:

```python
from mfn import style_field, transform
attr = {
    "css_advanced_transform": style_field(
        "item", "css_advanced_transform",
        {"desktop": transform(x=12, rotate=25)}, itype="heading")
}
```

## Perfiles y excepciones

`--origin generated` aplica políticas del taller. `--origin export` permite analizar exports reales sin tratar atributos de runtime o CSS legacy como errores estructurales. El destino predeterminado es `--editor visual`; nested wraps generan información, no bloqueo. En `classic` mantienen el warning.

Con `--json`, stdout contiene un único objeto. `--fix --json` añade `document`; sin `--json`, el documento corregido ocupa stdout y el informe va a stderr. `--fix -o` requiere una ruta distinta al original y solo escribe si el resultado es aceptado. La corrección se realiza sobre copia y se revalida.

`valid` indica ausencia de errores, mientras `accepted` incluye `--strict`. Siempre consumir `accepted` y `exit_code` para automatizar una entrega. `--ignore` se conserva por compatibilidad y las incidencias suprimidas quedan en el informe; un error estructural ignorado sigue impidiendo aceptación.

Una excepción es concreta, revisable y no admite errores estructurales:

```json
[{"code":"W032","path":"$[0].wraps[0].items[0].attr.css_color.selector","reason":"Selector específico necesario para el componente; comprobar tras importar"}]
```

Perfil mínimo del destino:

```json
{
  "editor": "visual",
  "artifact_kind": "page",
  "root_font_px": 16,
  "media_domains": ["sitio.example"],
  "fonts": ["Arial"],
  "dependencies": {"menus": [6], "forms": [], "post_types": ["post"], "taxonomies": [], "templates": []},
  "global_styles": []
}
```

El perfil registra hechos del sitio, no demuestra por sí solo que sigan vigentes. Indicar en el encargo cómo y cuándo se comprobaron. Las fuentes pueden heredarse del theme si la familia y pesos por rol están documentados. La conversión a `rem` usa `root_font_px`; no asumir que toda instalación tiene raíz de 16 px. Laptop/tablet/mobile corresponden a 1440/959/767 px en esta referencia del theme.

## Medios

```bash
python3 tools/assets.py inventory proyectos/cliente/assets/hero.png --output proyectos/cliente/assets/inventory.json
python3 tools/assets.py register proyectos/cliente/assets/hero.png --manifest proyectos/cliente/assets/manifest.json --id 123 --url https://sitio.example/wp-content/uploads/hero.png
python3 tools/assets.py video proyectos/cliente/assets/original.mp4 --output proyectos/cliente/assets/hero.mp4 --background
```

Registrar exige un ID real previamente obtenido del destino; no sube ni comprueba recursos remotamente. El manifest conserva URL, ID, fichero local, hash, dimensiones disponibles y formato. Un ID debe ser positivo; la URL pública no lleva fragmento previo. `media()` añade `#ID` una sola vez. `--background` elimina audio al optimizar vídeo; la salida debe ser nueva y conserva el original. Requiere ffmpeg; ffprobe es opcional para inventario de dimensiones/duración.

Los consumidores no son equivalentes: `image.src` puede resolver un adjunto y generar `srcset`; un fondo CSS o un vídeo no obtiene `srcset` por añadir `#ID`. El recorte y las dimensiones se ajustan según el diseño. `alt: ""` debe comprobarse en el DOM: el theme puede heredar el alt del adjunto.

## Extraer las tres entradas

Las herramientas trabajan con snapshots locales y anotaciones. No necesitan ni almacenan credenciales de Figma/WordPress.

### Figma

Obtener un snapshot de nodos con las herramientas de diseño disponibles y congelarlo. Inventariar primero frames; solicitar después detalles por sección. Conservar Auto Layout, constraints, fixed/hug/fill, espaciados, variantes, textos, tipografía, fills, efectos y recortes. No repetir consultas de componentes sin cambios.

```bash
python3 tools/design.py figma proyectos/cliente/source/figma.json --reference archivo/frame --revision revision-real --output proyectos/cliente/design.json --cache proyectos/cliente/.cache/design
```

El adaptador admite un árbol `document` o un mapa `nodes` de documentos. Las URLs temporales del snapshot son evidencia de origen, nunca recursos de entrega. Un vídeo inaccesible queda pendiente. La caché combina tipo, referencia, revisión, opciones y hash del snapshot.

### HTML

Ejecutar `tools/browser_capture.js` en el navegador que tenga la referencia cargada y obtener `await muffinSnapshot()`. Espera fuentes e imágenes y recoge cajas, estilos calculados, pseudoelementos y medios. Con selectores explícitos se pueden comparar regiones equivalentes. Guardar el objeto como JSON y normalizar:

```bash
python3 tools/design.py html proyectos/cliente/source/html.json --reference pagina-original --revision hash-del-html --output proyectos/cliente/design.json
```

Capturar cada viewport y estado significativo. El script no pulsa controles ni modifica el contenido. Los wrappers técnicos del DOM no se convierten automáticamente en wraps de BeBuilder. Scripts y lógica de negocio se registran como dependencias, no se copian indiscriminadamente.

### Imagen

Registrar tamaño real de la captura, escala y bloques anotados con `id`, texto, geometría y propiedades conocidas. El adaptador exige `viewport` y `blocks`; no simula OCR. El agente revisa la imagen y completa las anotaciones. Lo no medible se marca `inferred`; lo pendiente, `pending`.

```bash
python3 tools/design.py image proyectos/cliente/source/anotaciones.json --reference diseno.png --revision sha256-imagen --output proyectos/cliente/design.json
```

No inferir enlaces, contenido oculto, animaciones o responsive como hechos observados. Una anotación de imagen solo acredita el viewport mostrado.

## Selección nativa y layout

| Bloque | Criterio |
|---|---|
| Título / texto / acción | heading / plain_text / button independientes cuando se editan por separado |
| Tarjeta | Componente nativo compuesto si cubre el contenido; en otro caso nested wrap de un solo nivel |
| Retícula con gap | Grid en `attr`; tamaños de celda controlados por columnas del grid |
| Cifras | counter solo si formato entero y animación encajan; conservar decimales y separadores con texto cuando sea necesario |
| Tabla | Elemento adecuado o HTML semántico limitado; no sacrificar filas/encabezados por una regla de estilo |
| Slider / galería | Confirmar si consume medios estáticos o posts/CPT; no elegirlo solo por su apariencia |
| Tabs / acordeón | Datos y comportamiento nativos; comprobar también el contenido de cada fila |
| Header / footer / sidemenu | Artefactos separados con menú, plantilla y destino registrados |

No añadir equal-height, CTA abajo o animación por defecto si el diseño no lo pide. Columnas hermanos tienen que caber después de márgenes y padding. `split()` es un patrón simple; para huecos medidos usar grid. Evitar coordenadas absolutas salvo superposiciones concretas. Comparar orden, visibilidad, recorte y alturas en responsive.

Priorizar edición nativa. Una limitación demostrada admite CSS específico o HTML semántico con excepción por campo/ruta; no convertir una página entera en HTML opaco. Mantener locales los estilos de un JSON autónomo. Si se usan Global Styles, entregar/importar también sus definiciones y comprobar `be_classes`; no deduplicarlos automáticamente porque altera especificidad y dependencias.

## Pruebas reales pendientes

Preparar fixtures sin tocar servidores:

```bash
python3 tools/integration_fixtures.py --output /tmp/muffin-fixtures
```

Para generar imagen/vídeo/header/sidemenu, aportar `--manifest`, claves `--image`, `--mp4`, `--poster` y `--menu-id` reales. No se inventan IDs.

En un WordPress desechable con el mismo theme: importar cada fixture, guardar, exportar, editar una propiedad de cada bloque, volver a guardar y exportar. Comprobar conservación de hijos y controles. El query necesita posts reales. Header/sidemenu se importan en plantillas del tipo correcto. Buscar un valor concreto del diseño en el CSS posterior a guardar: el import cambia UID.

```bash
python3 tools/compare.py roundtrip antes.json despues.json
python3 tools/compare.py geometry referencia-medidas.json resultado-medidas.json --tolerance 2
python3 tools/compare.py geometry referencia.json resultado.json --rename hero-title=sec1-heading --rename hero-cta=sec1-button
python3 tools/visual_report.py referencia.png resultado.png --output comparacion.html
```

La comparación estructural ignora únicamente identidad de nodos y los tres atributos de runtime indicados; el contenido se conserva. Revisar diferencias de metadatos del editor, no añadir ignorados indiscriminadamente. Para geometría, los snapshots deben compartir viewport y claves de regiones; `--rename ORIGEN=DESTINO` (repetible) empareja explícitamente una región de la referencia con la clave del resultado, sin adivinar correspondencias, y falla si la región no existe o colisiona con otra. El HTML de comparación permite superposición, diferencia absoluta y descarga de PNG. No decide aprobación automática por píxeles.

Revisar 767/768, 959/960 y 1440/1441 px, fuentes cargadas, ausencia de overflow, saltos de texto, recorte de imágenes y contenido dinámico estabilizado. Tolerancia geométrica inicial: 2 px en fixtures controlados. El antialiasing de texto no se evalúa por igualdad de píxeles.

## Mantenimiento y rendimiento

Python 3.10+ y PHP 8+ para las herramientas y pruebas; Node opcional para comprobación sintáctica del capturador. Sin paquetes Python obligatorios. La compatibilidad PHP del WordPress destino se comprueba aparte.

```bash
python3 tools/check.py   # tests, PHP, node --check del capturador, fichas, calibración de exports reales y plantilla
python3 tools/benchmark.py proyectos/nordes-ancin/nordes-ancin-portada.json --runs 5
php builder-elements/_generator/extract.php --check
php builder-elements/_generator/extract.php --theme /ruta/a/betheme --stdout
```

El benchmark separa catálogo, validación con índice cargado y arranque CLI. No comparar una validación antigua incompleta con otra más estricta como si hicieran el mismo trabajo. La reducción principal esperada es menos consultas repetidas y menos iteraciones; medir esos pasos durante encargos reales antes de publicar porcentajes.
