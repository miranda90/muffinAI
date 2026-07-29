# BeBuilder JSON – Reference

## Decision tree

- **Goal = re-import in Visual Builder or pixel-perfect match** → Use **VB parity**: include `icon`, `jsclass`, `title`, `ver` on sections/wraps/items; use `css_advanced_*` (and `css_typography`, `css_color`, etc.) with `selector` / `style` / `val`; use `attr.title` and `attr.header_tag` for headings; prefer native item types (`heading`, `button`, `image`, `list`, `plain_text`, `counter`).
- **Goal = content/structure only** → Simplified format is fine: minimal `attr` (e.g. `padding_top`, `bg_color`), optional omission of `icon`/`jsclass`/`title`/`ver`; still require `size`, `tablet_size`, `mobile_size` on every wrap and item.

**Layout → GUIA section:** Hero with video → GUIA §1. Solid bar + custom grid → §2. Category/product grid → §3. Image bg + centered card → §4. Partner + stats → §5. CTA with gradient overlay → §6. Image breaking out → §7. When the design matches, copy structure and attrs from that section.

**Columns / footer:** Never use one `column` with HTML and grid/flex classes for multiple columns, title+text, or title+menu. Use wraps (with `size` e.g. 1/2, 1/3) or wrap grid to create columns; put one element per column (heading, column, menu, etc.).

## Project documentation (muffinAI)

| Doc | Path | Purpose |
|-----|------|--------|
| JSON authoring guide | `muffin-builder-json-guide.md` | Top-level structure, attr conventions, scaffolds |
| Builder elements index | `builder-elements/README.md` | 132 elements, categories, structure rules |
| Layout patterns (ES) | `builder-elements/GUIA-MAQUETACIONES.md` | Hero video, bars, grids, cards, counters, overlay CTA |
| Real vs generated | `builder-elements/TMC-ABOUT-COMPARISON.md` | Section/wrap/item attr naming, nested wraps, css_advanced |
| Element attributes | `builder-elements/<element>.md` | Per-element attrs (e.g. `heading.md`, `column.md`, `button.md`); many include a **Structure (JSON)** block as minimal valid example |
| Element schema (raw) | `builder-elements/_elements.json` | Full attr definitions from builder PHP |

## Example JSON

- `examples/example2/home.json` – Full Visual Builder export (hero video, orange bar, categories, CTA, counters).
- `examples/example1/about-us.json` – About page (hero, values, innovation, CTA).
- `builder-elements/tmc-about-bebuilder.json` – Simplified BeBuilder-oriented version.

## Selector patterns (css_*)

Use these consistently so generated CSS targets the right nodes. Replace `mfnuidelement` with the actual section/wrap/item UID when known; for hand-authored JSON the theme often accepts the generic form.

| Target | Selector |
|--------|----------|
| Section | `.mcb-section-mfnuidelement` or `.mcb-section-<uid>` |
| Section wrapper (flex/align) | `.mcb-section-mfnuidelement .section_wrapper` |
| Wrap (generic) | `.mcb-wrap-mfnuidelement` |
| Wrap grid inner | `.mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement > .mcb-wrap-inner` or `.mcb-section .mcb-wrap-grid.mcb-wrap-grid-col-custom.mcb-wrap-mfnuidelement > .mcb-wrap-inner` for custom columns |
| Heading text | `.mcb-section .mcb-wrap .mcb-item-mfnuidelement .title` |
| Column content | `.mcb-section .mcb-wrap .mcb-item-mfnuidelement .column_attr`; links: `... .column_attr a` |
| Button | `.mcb-section .mcb-wrap .mcb-item-mfnuidelement` (button item root) |
| Plain text / HTML block | Same as column when styled via wrapper; often `.mcb-item-mfnuidelement .column_attr` or item root |

## Responsive keys

Use inside `val`: `desktop`, `laptop`, `tablet`, `mobile`. Omit keys where default is enough.
