---
name: bebuilder-json
description: Generates and validates JSON structures for BeTheme/Muffin Builder (BeBuilder). Use when creating or editing page JSON for mfn-page-items, converting designs to builder JSON, or when the user mentions BeBuilder, Muffin Builder, builder JSON, or mfn-page-items.
---

# BeBuilder JSON Expert

Generates JSON structures for BeTheme/Muffin Builder import. Hierarchy: **sections → wraps → items**. Root = array of sections.

## Generation workflow (mandatory)

0. **Validate before delivering (mandatory).** Write the JSON to a file and run
   `python3 tools/validate_bebuilder_json.py salida.json --strict`. Exit 0 = deliverable,
   1 = errors (fix and re-run), 2 = warnings only, 3 = unparseable. `--fix -o ok.json`
   repairs the mechanical issues. Codes and evidence: `tools/README.md`.
   The authoritative docs are `docs/bebuilder/01..06` and `.claude/skills/bebuilder-json/SKILL.md`.

Before generating JSON:

1. **Resolve target:** If the user wants re-import into Visual Builder or pixel-perfect match → use **VB parity** (full format: `icon`, `jsclass`, `title`, `ver`, and `css_advanced_*` with `selector`/`style`/`val`). If the goal is content/structure only → simplified `attr` is acceptable.
2. **Prefer simple wraps for robustness:** For page-content imports (`mfn-page-items` vía backend), priorizar estructuras simples: varias `sections`, y dentro de cada sección **wraps hermanos** con `size` (`1/1`, `1/2`, `2/3`, `1/3`, etc.) y items estándar. Reservar `grid`, `css_grid_columns_*` e `item_is_wrap` solo para casos donde el diseño lo requiera explícitamente o haya un ejemplo real equivalente.
3. **Match layout to pattern:** If the design matches a pattern in `builder-elements/GUIA-MAQUETACIONES.md`, use that pattern’s structure and attributes. Map: hero with video → §1; solid bar + custom grid → §2; category/product grid → §3; image bg + centered card → §4; partner + stats → §5; CTA with gradient overlay → §6; image breaking out → §7.
3b. **Always responsive (project rule):** Generate the JSON contemplating the four breakpoints
   from the start, never as an afterthought. Every wrap and item carries explicit `size`,
   `tablet_size` and `mobile_size`; every spacing (`css_advanced_padding` / `_margin`) and every
   typography value carries a `mobile` value alongside `desktop` (`tablet`/`laptop` only when the
   design calls for it). A JSON styled only for `desktop` is not finished.
3c. **Spacing in `rem` (project rule):** `padding` and `margin` values are always written in `rem`
   (`"1.5rem"`, `"5rem"`), never `px` or `em`. Also accepted: `0`, `auto`, `%`, viewport units,
   `calc()`/`var()`. Borders, radii, fixed widths and shadows may stay in `px`.
4. **Prefer native items:** Use `heading` (with `attr.title` and `attr.header_tag`), `button`, `image`, `list`, `plain_text`, `counter` when the design has those elements; do not pack everything into a single `column` with HTML.

**Never:** Put multiple columns, title+text, or title+menu (e.g. footer blocks) inside a single `column` item with HTML and CSS classes (grid/flex). That does not work in the builder. **Always:** Use wraps or the wrap’s grid option to create columns, then place one item per column: `heading` for titles, `column` or `plain_text` for body text, menu/shortcode items for navigation, etc. Each logical column = its own wrap (with `size` e.g. `"1/3"`) or one row with grid and one wrap per cell.

When in doubt, consult `builder-elements/TMC-ABOUT-COMPARISON.md` for real vs generated attribute names and `reference.md` for the decision tree.

## Root structure

```json
[
  {
    "icon": "section",
    "uid": "unique-section-id",
    "jsclass": "section",
    "title": "Section",
    "attr": { },
    "ver": "default",
    "wraps": [ ]
  }
]
```

- **Sections:** Required at minimum: `uid`, `attr`, `wraps`. For full parity with Visual Builder export also include `icon`, `jsclass`, `title`, `ver`.
- **Wraps:** Always include `size`, `tablet_size`, `mobile_size` (e.g. `"1/1"`). If missing, the front does not render the wrap's items. Also: `uid`, `attr`, `items`. Optional: `laptop_size`, `tablet_resized`.
- **Items:** Required: `type`, `uid`, `size`, `tablet_size`, `mobile_size`, `attr`. Optional: `icon`, `jsclass`, `title`.

## Attribute conventions

### CSS-advanced (recommended for styling)

Keys usually `css_*`. Object shape: `selector`, `style`, `val`.

- `val`: string or per-device map `{ "desktop": "...", "tablet": "...", "mobile": "..." }`.
- Composite values (e.g. padding): `"val": { "desktop": { "top": "5rem", "bottom": "5rem" } }`.

Examples:

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
    "desktop": { "top": "5rem", "bottom": "5rem" },
    "mobile": { "top": "2rem", "bottom": "2rem" }
  }
}
```

### Section (attr)

- **Width (obligatorio para ancho de sección):** Usar **`width_switcher`**: `"full"` para sección a ancho completo. La UI del builder muestra "default" si falta; **no** confiar solo en `style`: `"full-width"` (ese no controla la opción en el panel). Valores típicos: `"full"` (full width), `"default"` o `"custom"` con `css_advanced_flex` para ancho fijo.
- **Height:** `height_switcher`: `"custom"` | `"full-screen"`.
- **Background (recomendado):** Usar siempre `css_advanced_background_color` y resto de `css_advanced_*` (`css_advanced_background_image`, `css_advanced_background_size`, `css_advanced_background_position`, `css_advanced_background_overlay_background_color`). Evitar fijar `bg_color` en secciones nuevas, porque bloquea la opción de fondo del UI y hace que los cambios de color no se guarden como esperas.
- **Padding (recomendado):** No usar nuevos campos `padding_top`, `padding_bottom`, `padding_horizontal` en secciones generadas, porque se convierten en estilos inline difíciles de sobreescribir desde el UI. Para definir el padding inicial, usar `css_advanced_padding` sobre `.mcb-section-mfnuidelement`, o dejar que el usuario lo ajuste sólo desde el builder.
- **Video hero:** `background_switcher`: `"video"`, `bg_video_mp4`: URL (e.g. `"https://.../file.mp4#ID"`), overlay as above, `css_advanced_height`: `{ "val": { "desktop": "100vh" } }`.
- **Overlay gradient:** `background_overlay_switcher`: `"gradient"`, `css_advanced_overlay_gradient` with `val.string` (e.g. `"linear-gradient(0deg, rgba(29,36,44,0) 0%, #1D242C 100%)"`).
- **Spacing/alignment:** `css_advanced_padding`, `css_advanced_margin`; `css_advanced_align_items`, `css_advanced_justify_content`, `css_advanced_align_content` on `.section_wrapper`.
- **Anchor:** `custom_id`.

### Wrap (attr)

- **Basic layout (recomendado):** Para la mayoría de páginas estáticas, usar varios wraps hermanos con distintos `size` (p. ej. `2/3` + `1/3` para contenido + tarjeta lateral) en lugar de grids avanzados. Esto es lo más compatible con imports vía backend.
- **Grid (avanzado):** `grid`: `"grid"`, `grid_columns_switcher`: `"custom"`, `css_grid_columns_custom`: `{ "val": { "desktop": "1.5fr 1fr", "mobile": "1fr" } }` or `css_grid_columns` with `style`: `"grid-template-columns"`. Usar solo cuando exista un patrón real equivalente o se necesite un grid responsive más complejo.
- **Width:** `width_switcher`: `"custom"`, `css_advanced_flex`: `{ "val": { "desktop": "1580px", "tablet": "100%" } }`.
- **Alignment:** `css_advanced_align_items`, `css_advanced_justify_content`, `css_advanced_align_self` (e.g. `"flex-end"` for bottom-aligned content).
- **Query loop (categories/cards):** `type`: `"query"`, `query_type`: `"terms"`, `query_terms_taxonomy`: `"product_cat"` (or other), plus query include/order options; use `css_grid_columns` per breakpoint.
- **Nested wraps (grid of cards):** Items with `item_is_wrap`: `1` are sub-wraps; each has its own `items` (sin `type` — es la forma canónica, soportada por front/helper/VB; NO produce error 500). **Limitación real:** el builder clásico admin genera warnings PHP 8 con nested wraps y BeBuilder Blocks Classic se autodesactiva si detecta `item_is_wrap` o `type: "query"`. Usar nested wraps solo si el destino es el Visual Builder; para compatibilidad con el builder clásico, aplanar en wraps hermanos (p. ej. 3 columnas = 3 wraps con `size` 1/3).

### Item types and key attributes

- **heading:** Design real uses `attr.title` (text, can include `<br>`, `<b>`), `attr.header_tag` (`h1`–`h6`). Typography: `css_typography` with `val.desktop`/`val.mobile` (font-size, line-height, font-weight). Color: `css_color` (selector/style/val). Align: `css_txt_align`. Simplified form may use `content`, `tag`—prefer `title` + `header_tag` for VB parity.
- **column:** `attr.content` (HTML/shortcodes). **Do not use inline `style` attributes here.** All visual styling (color, typography, spacing, alignment) must go through the element options: `css_column_attr_color`, `css_column_attra_color` (links), `css_column_attr_typography`, `css_advanced_padding`, `css_advanced_margin`, etc. The HTML in `content` should stay as clean as possible (semantic tags, links, lists).
- **button:** `attr.title`, `attr.link`, `attr.target` (`0`|`_blank`), `attr.class` (e.g. `"arrow-button"`, `"arrow-button arrow-button-white"`). Styles: `css_button_background_color`, `css_button_color`, `css_button_border_color`, and `*_hover` variants.
- **image:** `attr.src`, `attr.link`, `attr.target`. Optional: `image_height`: `"custom"`, `css_image_cover_height`; position: `css_advanced_position`: `"absolute"`, `css_advanced_right`/`left`/`bottom` (e.g. negative values for “breaking out”); `visibility`: `" hide-mobile"`.
- **counter:** `type`: `"vertical"`, `number`, `label` (e.g. `"+"`, `"%"`), `title_tag`: `"h3"`, `duration`: `1000`.
- **call_to_action:** `title`, `title_tag`, `button_title`, `link` when a single CTA block is needed; for pixel-perfect button styling prefer `button` item with `class` and `css_button_*`.
- **plain_text:** Raw HTML/shortcodes; `shortcodes_parser`: `"1"` if shortcodes must run.
- **list:** `content` (HTML list), `title`, `title_tag` for value lists.

Sizes: `size`, `tablet_size`, `mobile_size` (e.g. `"1/1"`, `"1/2"`, `"1/3"`).

## Layout patterns (from real designs)

1. **Hero full-screen with video:** Section: `background_switcher`: `"video"`, `bg_video_mp4`, overlay, `height_switcher`: `"custom"`, `css_advanced_height` 100vh. Two wraps: first = margin-top + heading; second = `css_advanced_align_self`: `"flex-end"` + plain_text/shortcode (e.g. product carousel).
2. **Solid bar + custom grid:** Section background color. Wrap: `grid`, `grid_columns_switcher`: `"custom"`, `css_grid_columns_custom` (e.g. `35rem 1fr`), `width_switcher`: `"custom"`, `css_advanced_flex`: `"1580px"`.
3. **Category/product grid:** Wrap with `type`: `"query"`, `query_type`: `"terms"`, taxonomy + `css_grid_columns` (e.g. repeat(4, 1fr) desktop, repeat(2, 1fr) tablet, 1fr mobile). Each cell = nested wrap (`item_is_wrap`: 1) with image + button + heading.
4. **Image background + centered card:** Section: custom height, background image, overlay, align/justify center. Wrap: white bg, padding, border-radius, custom width; inner wrap with heading + column + buttons.
5. **Partner + stats:** Section dark bg. First wrap: grid 1.5fr 1fr (heading + image | column + button). Second wrap: grid 4 cols (or 2+2 mobile), each cell = nested wrap with counter + column.
6. **CTA with gradient overlay:** Section: background image, `background_overlay_switcher`: `"gradient"`, `css_advanced_overlay_gradient` (linear-gradient string in val).
7. **Image breaking out:** Item image with `css_advanced_position`: `"absolute"`, negative `css_advanced_right`/`left`, `css_advanced_bottom`, custom width; `visibility`: `" hide-mobile"` if needed.

## Pattern checklists (minimum required)

Use these so required attrs are not omitted. Full details in `builder-elements/GUIA-MAQUETACIONES.md`.

- **Hero video (GUIA §1):** Section: `background_switcher`: `"video"`, `bg_video_mp4`, `height_switcher`: `"custom"`, `css_advanced_height` with `val.desktop`: `"100vh"`, overlay color. Each wrap: `size`, `tablet_size`, `mobile_size`. Wrap 2: `css_advanced_align_self`: `"flex-end"` if content at bottom.
- **Solid bar + grid (GUIA §2):** Section: `css_advanced_background_color`. Wrap: `grid`: `"grid"`, `grid_columns_switcher`: `"custom"`, `css_grid_columns_custom`, `width_switcher`: `"custom"`, `css_advanced_flex` (e.g. 1580px). Every wrap: `size`, `tablet_size`, `mobile_size`. **Para imports sencillos se puede sustituir por varios wraps hermanos con `size` apropiado.**
- **Category/product grid (GUIA §3):** Wrap: `type`: `"query"`, `query_type`: `"terms"`, taxonomy + `css_grid_columns` per breakpoint. Cells = items with `item_is_wrap`: 1, each with own `items` (e.g. image, heading, button). Sizes on every wrap and item. **Evitar `item_is_wrap` en páginas estáticas si no es estrictamente necesario.**
- **CTA with gradient overlay (GUIA §6):** Section: background image, `background_overlay_switcher`: `"gradient"`, `css_advanced_overlay_gradient` with linear-gradient string in `val`.

## Checklist before output

- [ ] **Every section** has `attr.width_switcher`: `"full"` (or `"custom"` / `"default"` when needed) so the section width option in the builder UI shows correctly; do not rely on `style`: `"full-width"` alone.
- [ ] Every wrap has `size`, `tablet_size`, `mobile_size`.
- [ ] Heading: use `attr.title` and `attr.header_tag` for VB parity (not only content/tag). Aplicar un `margin-bottom` consistente (1.5rem) mediante opciones del elemento (`css_advanced_margin`) en vez de estilos inline.
- [ ] Column text / visual editor: usar `column` o `visual_editor` con `attr.content` limpio y configurar un `margin-bottom` de 1rem mediante opciones del elemento (`css_advanced_margin` o ajustes equivalentes), nunca via `style` inline.
- [ ] Use native types (`heading`, `column`, `button`, `image`, `counter`, `list`, `plain_text`) instead of putting everything in column HTML when the design matches.
- [ ] Para la mayoría de layouts usar wraps hermanos con `size` (sin `grid` ni `item_is_wrap`). Solo usar `grid`/`item_is_wrap` cuando se copie un patrón real del tema o sea imprescindible.
- [ ] No introducir nuevos `padding_top`, `padding_bottom` ni `padding_horizontal` en secciones generadas; preferir `css_advanced_padding` o dejar que el padding se controle únicamente desde el UI.
- [ ] No fijar `bg_color` en secciones generadas salvo que se quiera un valor “hardcoded”; preferir `css_advanced_background_color` o dejar que el color de fondo se defina desde el UI.
- [ ] Multi-column / footer (title+text, title+menu): use separate wraps or wrap grid for columns, and one item per column (heading, column, menu, etc.). Never a single column with HTML + grid/flex classes.
- [ ] Responsive: add `val.desktop`/`tablet`/`mobile` in `css_*` only where needed.
- [ ] UIDs: any unique string; readable (e.g. `sec-hero`, `wrap-3col`) helps debugging.

## Reference

- **Documentación maestra (fuente principal, verificada contra el código):** `docs/bebuilder/00-INDICE.md` → arquitectura, pipeline CSS, atributos comunes (pestaña Advanced completa), inventario de los 167 elementos, reglas y trampas.
- **Element list and attributes:** Fichas `builder-elements/*.md` regeneradas (2026-07) ejecutando el PHP real — fiables. Incluyen `_advanced.md` (pestaña Advanced común), `_section.md`, `_wrap.md` y `_elements.json` íntegro. Regenerar: `cd builder-elements/_generator && php extract.php && python3 generate_fichas.py`.
- **Authoring guide:** Project root `muffin-builder-json-guide.md`.
- **Layout patterns (Spanish):** `builder-elements/GUIA-MAQUETACIONES.md`.
- **Real vs generated comparison:** `builder-elements/TMC-ABOUT-COMPARISON.md`.
- **Real JSON examples:** `examples/example2/home.json` (full VB export), `examples/example1/about-us.json`; `builder-elements/tmc-about-bebuilder.json` (simplified).

When generating new JSON, apply the **Generation workflow** above: prefer the full format with `css_advanced_*` and `selector`/`style`/`val` for VB parity; use simplified section attributes only when the target is minimal/content-only. Use **reference.md** for the decision tree and selector list.
