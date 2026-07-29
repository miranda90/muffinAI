# `google_font` — Google Font (shortcode inline)

Shortcode **inline** para usar dentro de `content` (column, plain_text, visual). NO es un item del builder: no lleva `type`/`size`/`uid`.

## Campos
- **`font`** (text) — Font
  - Google font name<br><b>Important</b>: Works only with Google Fonts loaded from Google or Local for fonts selected in Theme Options
  - Valor: String
  - Default: `Open Sans`
- **`size`** (text) — Size
  - Font size in px
  - Valor: String
- **`weight`** (select) — Weight
  - Font weight (some fonts only)
  - Valor: String
  - Opciones: `100` 100 · `200` 200 · `300` 300 · `400` 400 · `500` 500 · `600` 600 · `700` 700 · `800` 800
  - Default: `400`
- **`italic`** (switch) — Italic
  - Font style: italic (some fonts only)
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`letter_spacing`** (text) — Letter Spacing
  - Letter spacing in px
  - Valor: String
- **`color`** (color) — Color
  - Color of font
  - Valor: String
  - Default: `#626262`
- **`subset`** (text) — Subset
  - Subset for font (multiple separate with comma)
  - Valor: String
- **`content`** (textarea) — Content
  - Valor: String

*Generado desde `class-mfn-builder-fields.php` (`get_inline_shortcode()`) — no editar a mano.*