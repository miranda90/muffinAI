# `column` — Column Text

- **Categoría:** typography
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 18

## Campos
- **`content`** (visual) — Content
  - Valor: String

### Content

- **`title`** (text) — Label
  - This field is only used as label in the builder
  - Valor: String
- **`css_column_attr_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .column_attr", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_column_attr_color`** (color) — Color
  - May be overwritten by individual tags or inline CSS
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .column_attr", "style": "color", "val": "valor"}`
- **`css_column_attra_color`** (color) — Link color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .column_attr a", "style": "color", "val": "valor"}`
- **`css_column_attra_color_hover`** (color) — Link hover
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .column_attr a:hover", "style": "color", "val": "valor"}`
- **`css_column_attr_text_shadow`** (text_shadow) — Text shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .column_attr", "style": "text-shadow", "val": "valor"}`
- **`css_column_attr_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .column_attr", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Deprecated

- **`align`** (switch) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Text align
  - Valor: String
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
- **`align-mobile`** (switch) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Mobile text align
  - Valor: String
  - Opciones: `""` As above · `left` Left · `center` Center · `right` Right · `justify` Justify
- **`column_bg`** (color) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background color
  - Valor: String
- **`bg_image`** (upload) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background image
  - Valor: String
- **`bg_position`** (select) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background position
  - Valor: String
  - Opciones: `""` Default · `no-repeat;left top;;` Left Top \| no-repeat · `repeat;left top;;` Left Top \| repeat · `no-repeat;left center;;` Left Center \| no-repeat · `repeat;left center;;` Left Center \| repeat · `no-repeat;left bottom;;` Left Bottom \| no-repeat · `repeat;left bottom;;` Left Bottom \| repeat · `no-repeat;center top;;` Center Top \| no-repeat · `repeat;center top;;` Center Top \| repeat · `repeat-x;center top;;` Center Top \| repeat-x · `repeat-y;center top;;` Center Top \| repeat-y · `no-repeat;center;;` Center Center \| no-repeat · `repeat;center;;` Center Center \| repeat · `no-repeat;center bottom;;` Center Bottom \| no-repeat · `repeat;center bottom;;` Center Bottom \| repeat · `repeat-x;center bottom;;` Center Bottom \| repeat-x · `repeat-y;center bottom;;` Center Bottom \| repeat-y · `no-repeat;right top;;` Right Top \| no-repeat · `repeat;right top;;` Right Top \| repeat · `no-repeat;right center;;` Right Center \| no-repeat · `repeat;right center;;` Right Center \| repeat · `no-repeat;right bottom;;` Right Bottom \| no-repeat · `repeat;right bottom;;` Right Bottom \| repeat
  - Default: `center top no-repeat`
- **`bg_size`** (select) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background size
  - Valor: String
  - Opciones: `""` Default · `auto` Auto · `contain` Contain · `cover` Cover · `cover-ultrawide` Cover, on ultrawide screens only > 1920px
- **`margin_bottom`** (select) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Margin bottom
  - Valor: String
  - Opciones: `""` - Default - · `0px` 0px · `10px` 10px · `20px` 20px · `30px` 30px · `40px` 40px · `50px` 50px
- **`padding`** (text) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Padding
  - Use value with <b>px</b> or <b>%</b>. Example: <b>20px</b> or <b>20px 10px 20px 10px</b> or <b>20px 1%</b>
  - Valor: String
- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)
- **`style`** (textarea) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Column inline CSS
  - Example: <b>border: 1px solid #999;</b>
  - Valor: String

## Ejemplo mínimo

```json
{
  "type": "column",
  "uid": "itm000001",
  "icon": "column",
  "jsclass": "column",
  "title": "Column Text",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {
    "title": "Título de ejemplo"
  }
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*