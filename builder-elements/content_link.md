# `content_link` — Content link (shortcode inline)

Shortcode **inline** para usar dentro de `content` (column, plain_text, visual). NO es un item del builder: no lleva `type`/`size`/`uid`.

## Campos
- **`title`** (text) — Title
  - Item title text
  - Valor: String
- **`icon`** (icon) — Icon
  - Valor: String
  - Default: `icon-lamp`
- **`link`** (text) — Link
  - Valor: String
- **`target`** (select) — Target
  - Link target
  - Valor: String
  - Opciones: `0` Default · `_blank` New tab or window
  - Default: `0`
- **`class`** (pills) — Class
  - CSS classess
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)
- **`download`** (text) — Download
  - Enter the new filename (if click on button downloads a file)
  - Valor: String

*Generado desde `class-mfn-builder-fields.php` (`get_inline_shortcode()`) — no editar a mano.*