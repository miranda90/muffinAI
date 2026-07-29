# `fancy_link` — Fancy Link (shortcode inline)

Shortcode **inline** para usar dentro de `content` (column, plain_text, visual). NO es un item del builder: no lleva `type`/`size`/`uid`.

## Campos
- **`title`** (text) — Link text
  - Valor: String
- **`link`** (text) — Link (with https://)
  - Valor: String
- **`target`** (select) — Target
  - Link target
  - Valor: String
  - Opciones: `0` Default · `_blank` New tab or window
- **`style`** (select) — Style
  - Style of fancy link
  - Valor: String
  - Opciones: `1` Brackets · `2` Block flipping · `3` Border bottom · `4` Border clone · `5` Background shift · `6` Color and border shift · `7` Border position change · `8` Borders to cross · `9` Icon below link
  - Default: `1`
- **`font`** (font_select) — Font family
  - Valor: String
- **`font_size`** (text) — Font size
  - Valor: String
- **`margin`** (text) — Margin
  - Valor: String
- **`icon`** (icon) — Icon
  - for style <b>Icon below link</b> only
  - Valor: String
- **`class`** (text) — Class
  - CSS classess
  - Valor: String
- **`popup`** (text) — Popup ID
  - Valor: String
- **`download`** (text) — Download
  - Enter the new filename (if click on button downloads a file)
  - Valor: String

*Generado desde `class-mfn-builder-fields.php` (`get_inline_shortcode()`) — no editar a mano.*