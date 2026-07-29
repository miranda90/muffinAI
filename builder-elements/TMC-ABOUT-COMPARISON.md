# Comparación: diseño real (about-us.json) vs BeBuilder generado (tmc-about-bebuilder.json)

Este documento resume las diferencias entre la estructura **exportada por el diseño real** de la página About Us (`examples/example1/about-us.json`) y la estructura **generada para BeBuilder** (`tmc-about-bebuilder.json`), para mejorar futuras conversiones diseño → BeBuilder.

**Ver también:** Para patrones concretos de maquetación (hero con video, grid de categorías, card CTA, estadísticas con counter, etc.) según el diseño real del Home y About, ver **[GUIA-MAQUETACIONES.md](./GUIA-MAQUETACIONES.md)** (basada en `examples/example2/home.json` y example1).

---

## 1. Estructura de nivel raíz

| Aspecto | Diseño real (about-us.json) | BeBuilder generado (tmc-about-bebuilder.json) |
|--------|------------------------------|-----------------------------------------------|
| Raíz | Array de secciones `[{ section }, ...]` | Igual: array de secciones |
| Secciones | Muchas secciones (barra naranja, hero, valores, innovación, CTA, etc.) | Menos secciones (hero, values, innovation, cta) |

**Conclusión:** El formato de raíz es correcto. La reducción de secciones es intencional (resumen del diseño).

---

## 2. Estructura de cada Section

### Diseño real

Cada sección incluye campos que vienen del **Muffin Builder / BeTheme**:

- `icon`: `"section"`
- `uid`: string alfanumérico (ej. `"7q1cp5yg"`)
- `jsclass`: `"section"`
- `title`: `"Section"`
- `attr`: objeto con **atributos avanzados** (ver siguiente tabla)
- `ver`: `"default"`
- Opcional: `mfn_global_section_id`
- `wraps`: array de wraps

### Atributos de sección en el diseño real

Los estilos no se aplican con nombres simples sino con **bloques CSS avanzados**:

```json
"css_advanced_background_color": {
  "selector": ".mcb-section-mfnuidelement",
  "style": "background-color",
  "val": "#1D242C"
},
"css_advanced_padding": {
  "selector": ".mcb-section-mfnuidelement",
  "style": "padding",
  "val": {
    "desktop": { "top": "12px", "right": "2rem", "bottom": "12px", "left": "2rem" },
    "mobile": { "right": "1rem", "left": "1rem" }
  }
},
"css_advanced_background_image": { "val": { "desktop": "url(...)" }, "selector": "...", "style": "background-image" },
"css_advanced_background_size": { "val": { "desktop": "contain" }, ... },
"css_advanced_background_position": { "val": { "desktop": "top center" }, ... },
"css_advanced_background_overlay_background_color": { "val": "#1D242C85", ... },
"width_switcher": "full"
```

También aparecen: `scroll-visibility`, `closeable-x`, `tabber_*`, `query_*`, `background_switcher*`, `vb_postid`, `vb`, `rwd`.

### BeBuilder generado

Secciones con atributos **simplificados**:

- `uid`: legible (ej. `"sec-hero"`)
- `attr`: **`width_switcher`**: `"full"` (obligatorio para que la opción de ancho en la UI no quede en "default"), `padding_top`, `padding_bottom`, `style` (`"full-width"`), `bg_image`, `bg_position`, `bg_color`
- `wraps`: array de wraps
- **No** se incluyen: `icon`, `jsclass`, `title`, `ver`, ni bloques `css_advanced_*`

**Mejora para el futuro:**  
Si el backend/BeBuilder acepta ambos formatos, mantener el simplificado reduce tamaño y mantenibilidad. Si en algún momento se requiere **paridad total** con el diseño real (por ejemplo re-importar en el Visual Builder), habría que mapear:

- `padding_top` / `padding_bottom` → `css_advanced_padding.val.desktop.top` / `bottom`
- `bg_color` → `css_advanced_background_color`
- `bg_image` → `css_advanced_background_image`
- Añadir `icon`, `jsclass`, `title`, `ver` en secciones y wraps.

---

## 3. Wraps: anidamiento y atributos

### Diseño real

- **Wraps anidados:** Un wrap puede tener `"item_is_wrap": 1` y sus `items` son **otros wraps**. Así se consiguen layouts en grid de varios niveles (ej. hero: wrap exterior con grid `1.5fr auto`, dentro un wrap con altura `80vh` y contenido alineado abajo, y otro wrap con las 3 columnas de texto).
- Cada wrap tiene:
  - `icon`: `"wrap"`
  - `uid`, `size`, `tablet_size`, `mobile_size`, `laptop_size`, `tablet_resized`
  - `jsclass`: `"wrap"`
  - `title`: `"Wrap"`
  - `attr`: grid (ej. `grid`, `grid_columns_switcher`, `css_grid_columns_custom`), `width_switcher`, `css_advanced_flex` (width), `height_switcher`, `css_advanced_height`, `css_advanced_align_items`, `css_advanced_align_content`, `css_advanced_justify_content`, `css_advanced_margin`, `custom_id`, `visibility`, etc.
  - `items`: array de items (que pueden ser wraps si `item_is_wrap: 1`)

Ejemplo de grid en wrap:

```json
"grid": "grid",
"grid_columns_switcher": "custom",
"css_grid_columns_custom": {
  "val": { "desktop": "1.5fr auto", "tablet": "1fr" },
  "selector": ".mcb-section .mcb-wrap-grid.mcb-wrap-grid-col-custom.mcb-wrap-mfnuidelement > .mcb-wrap-inner",
  "style": "grid-template-columns"
},
"width_switcher": "custom",
"css_advanced_flex": { "val": { "desktop": "1580px", "tablet": "100%" }, "selector": "...", "style": "width" }
```

### BeBuilder generado

- **Un solo nivel de wraps:** Cada sección tiene wraps que contienen directamente items (heading, column, call_to_action). No hay wraps anidados.
- Wraps con: `uid`, `size`, `tablet_size`, `mobile_size`, `attr` (a menudo `{}`).

**Mejora para el futuro:**  
Para diseños más fieles al real (por ejemplo hero con título a la izquierda y 3 columnas a la derecha en una sola fila), conviene:

1. Revisar si el builder soporta **wraps anidados** (`item_is_wrap: 1`) y grids custom.
2. Si se genera solo un nivel de wraps, documentar que el layout puede quedar “aplanado” (p. ej. título y columnas en secuencia vertical en móvil) y que el diseño real usa grids y alturas (ej. `80vh`, `align-content: flex-end`) para alinear el contenido.

---

## 4. Items: nombres de atributos por tipo

### Heading

| Diseño real | BeBuilder generado |
|-------------|--------------------|
| `attr.title` = texto (puede llevar `<br>`, `<b>`) | `attr.content` = texto |
| `attr.header_tag` = `"h1"` \| `"h2"` \| `"h3"` | `attr.tag` = `"h1"` \| `"h2"` |
| Estilos: `css_color`, `css_typography` (font-size, line-height, font-weight por desktop/mobile), `css_advanced_margin`, `width_switcher`, `css_advanced_flex` | `attr.color`, `attr.align`, `attr.style` |

**Mejora para el futuro:**  
Comprobar en el código del builder qué nombres usa realmente. Si el backend espera el formato “real”, mapear:

- `content` → `title`
- `tag` → `header_tag`

Y, si se quiere paridad visual, añadir bloques `css_typography` y `css_advanced_margin` con `desktop`/`tablet`/`mobile`.

### Column

| Diseño real | BeBuilder generado |
|-------------|--------------------|
| `attr.content` = HTML del contenido | Igual: `attr.content` |
| Sin `attr.title` como “título del bloque” | `attr.title` usado como etiqueta (ej. "Intro", "Video") |
| Estilos: `css_column_attr_color`, `css_column_attra_color`, `css_column_attr_typography`, `css_advanced_padding`, `css_advanced_border_*`, `width_switcher`, `css_advanced_flex` | Sin estilos avanzados; a veces estilos inline en el HTML de `content` |

**Conclusión:** En column la diferencia principal es la cantidad de CSS avanzado; el uso de `content` es correcto. El `title` en nuestro JSON es solo identificador/etiqueta.

### Button / Call to Action

- **Diseño real:** Usa ítems `type: "button"` con `attr.title` (texto del botón), `attr.link`, `attr.class` (ej. `"arrow-button arrow-button-hover-white"`), `attr.target`, y estilos `css_button_*`.
- **BeBuilder generado:** Usa `type: "call_to_action"` para el CTA final, con `title`, `title_tag`, `button_title`, `link`. No se usa `type: "button"` en el CTA.

**Mejora para el futuro:**  
Si se quiere replicar exactamente el diseño (mismo aspecto y clases), considerar generar un ítem `button` con `title`, `link`, `class` y los estilos necesarios en lugar de (o además de) `call_to_action`, según lo que el builder espere.

---

## 5. Elementos que aparecen en el diseño real y no en nuestro JSON

- **list** (List Basic): ítems con `icon`, `title`, `title_tag`, `content` para valores (“Spanish-built mulchers”, “Engineered for intensive work”, etc.).
- **image**: con `src`, `size`, `mask_shape_*`, y estilos (`css_image_frame_width`, `css_advanced_position`, etc.).
- **html**: bloques HTML con `height_switcher`, `css_advanced_height`, `css_advanced_margin`.
- **video**: con `mp4`, `object_position`, `object_fit`, `css_advanced_border_radius`, `css_advanced_flex` (width).

En nuestro JSON se sustituyeron por columnas con HTML embebido (placeholders, texto, enlaces). Para acercarse más al diseño real habría que usar estos tipos nativos cuando el builder los soporte.

---

## 6. Responsive y CSS avanzado

- **Diseño real:** Casi todo el estilo va en atributos con estructura `{ "selector": "...", "style": "...", "val": { "desktop": ..., "tablet": ..., "mobile": ... } }`. Permite control fino por breakpoint.
- **BeBuilder generado:** Se usan `size`, `tablet_size`, `mobile_size` en wraps e items (correcto), pero no se rellenan bloques `css_advanced_*` ni `css_typography` con variantes por dispositivo.

**Mejora para el futuro:**  
Para layouts y tipografía más fieles, habría que generar (o documentar) el mapeo de:

- Padding/margin por breakpoint.
- Tipografía (tamaño, line-height) por desktop/tablet/mobile.
- Grid columns por breakpoint (`css_grid_columns_custom.val`).

---

## 7. Resumen de buenas prácticas para futuras conversiones

1. **Wraps:** Mantener siempre `size`, `tablet_size`, `mobile_size` (y `laptop_size` si el builder lo usa). Sin `size`, el front no renderiza los items del wrap (ya documentado en README).
2. **Nombres de atributos:** Confirmar en el código del builder si heading usa `title` + `header_tag` o `content` + `tag`, y unificar en la generación.
3. **Layout complejo:** Si el diseño tiene grids o columnas con proporciones fijas (ej. `1.5fr auto`, `20rem 1fr`), valorar wraps anidados y `grid_columns_switcher`/`css_grid_columns_custom` en lugar de solo columnas 1/2, 1/3.
4. **Estilos:** Si el objetivo es exportar/importar en el Visual Builder, incluir `icon`, `jsclass`, `title`, `ver` y bloques `css_advanced_*`/`css_typography` según el diseño real; si el objetivo es solo contenido y estructura mínima, el formato simplificado es suficiente.
5. **Tipos de ítems:** Preferir tipos nativos (`heading`, `column`, `button`, `image`, `video`, `list`, `html`) cuando el diseño los use, en lugar de empaquetar todo en columnas con HTML.
6. **UIDs:** El diseño real usa UIDs cortos alfanuméricos; nuestro uso de UIDs legibles (`item-hero-title`) es válido si el builder no los rechaza.

---

## 8. Referencia rápida: atributos por nivel

| Nivel   | Diseño real (campos típicos) | BeBuilder generado |
|--------|------------------------------|--------------------|
| Section | icon, uid, jsclass, title, attr (css_advanced_*), ver, wraps | uid, attr (padding_*, style, bg_*), wraps |
| Wrap   | icon, uid, size, tablet_size, mobile_size, laptop_size, jsclass, title, attr (grid, css_advanced_*), items, item_is_wrap | uid, size, tablet_size, mobile_size, attr, items |
| Item   | type, jsclass, title, icon, attr, uid, size, tablet_size, laptop_size, mobile_size, table_resized, be_classes | type, uid, size, tablet_size, mobile_size, attr |

Con esta comparación se puede ajustar la generación de JSON (o la documentación) para acercarse más al diseño real cuando haga falta, y mantener el formato simplificado cuando prioridad sea claridad y mantenimiento.
