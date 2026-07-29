# `lorem` — Lorem ipsum (shortcode inline)

Shortcode **inline** para usar dentro de `content` (column, plain_text, visual). NO es un item del builder: no lleva `type`/`size`/`uid`.

## Campos
- **`type`** (switch) — Type of listing
  - Valor: String
  - Opciones: `paragraphs` Paragraphs · `lists` Lists
  - Default: `paragraphs`
- **`rows_amount`** (text) — Amount
  - Valor: String
  - Default: `3`
- **`min_words_amount`** (text) — Minimal words amount
  - Valor: String
  - Default: `10`
- **`max_words_amount`** (text) — Maximal words amount
  - Valor: String
  - Default: `15`

*Generado desde `class-mfn-builder-fields.php` (`get_inline_shortcode()`) — no editar a mano.*