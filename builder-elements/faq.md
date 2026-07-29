# `faq` — FAQ

- **Categoría:** blocks
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 28

## Campos
- **`title`** (text) — Title
  - Valor: String
  - Default: `This is the title`
- **`title_tag`** (switch) — Title tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h4`
- **`tabs`** (tabs) — FAQ
  - <b>JavaScript</b> content like Google Maps and some plugins shortcodes do <b>not work</b> in tabs
  - Valor: Array de objetos (formato propio del campo tabs)
  - Opciones: `title` ["input", "Question", "Sample question"] · `content` ["textarea", "Answer", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."]
  - Default: `[{"title": "This is the 1st question", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."}, {"title": "This is the 2nd question", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu massa orci."}]`
- **`open1st`** (switch) — Open first
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`openAll`** (switch) — Open all
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`style`** (switch) — Style
  - Valor: String
  - Opciones: `accordion` Accordion · `toggle` Toggle
  - Default: `accordion`

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Title

- **`css_faqheading_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .heading", "style": "color", "val": "valor"}`
- **`css_faqheading_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .heading", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_faqheading_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .heading", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Bar

- **`css_faqquestion_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_faqquestionfaqquestiontitlebefore_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question .title:before", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_faqquestionfaqquestiontitlebefore_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question,.mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question .title:before", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_faqt` isnt `none`
- **`css_faqquestion_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_faqt` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_faqquestion_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_faqquestiontitle_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question .title", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_faq___mfn_faq_line`** (color) — Line color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq", "style": "--mfn-faq-line", "val": "valor"}`
- **`css_faqquestion_background`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question", "style": "background", "val": "valor"}`
- **`css_faqquestionactive_background`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question.active", "style": "background", "val": "valor"}`

### Title bar

- **`css_faqquestiontitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_faqquestiontitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question .title", "style": "color", "val": "valor"}`
- **`css_faqquestiontitlei_color`** (color) — Icon color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question .title i", "style": "color", "val": "valor"}`
- **`css_faqquestionactivetitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question.active .title", "style": "color", "val": "valor"}`
- **`css_faqquestionactivetitlei_color`** (color) — Icon color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question.active .title i", "style": "color", "val": "valor"}`

### Content

- **`css_faqquestionanswer_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question .answer", "style": "color", "val": "valor"}`
- **`css_faqquestionanswer_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question .answer", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Bar line

- **`css_simplefaqquestion_border_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".style-simple .mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question", "style": "border-color", "val": "valor"}`
- **`css_simplefaqquestionafter_background_color_active`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".style-simple .mcb-section .mcb-wrap .mcb-item-mfnuidelement .faq .question.active:after", "style": "background-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "faq",
  "uid": "itm000001",
  "size": "1/4",
  "tablet_size": "1/4",
  "mobile_size": "1/1",
  "attr": {
    "title": "This is the title"
  }
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*