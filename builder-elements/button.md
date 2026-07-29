# `button` — Button

- **Categoría:** typography
- **Size por defecto:** 1/4 · tablet 1/4 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 48

## Campos
- **`title`** (text) — Title
  - Valor: String
  - Default: `Click here`
- **`link`** (text) — Link
  - Valor: String
- **`target`** (select) — Link target
  - Valor: String
  - Opciones: `0` Default \| _self · `1` New tab or window \| _blank · `lightbox` Lightbox (image or embed video)
- **`link_title`** (text) — Link title
  - Valor: String

### Icon

- **`icon`** (icon) — Icon
  - Valor: String
- **`icon_position`** (switch) — Position
  - Valor: String
  - Opciones: `left` Left · `right` Right
  - Default: `left`

### Style

- **`size`** (switch) — Size
  - Valor: String
  - Opciones: `1` Small · `2` Default · `3` Large · `4` XL
  - Default: `2`
- **`full_width`** (switch) — Width
  - Valor: String
  - Opciones: `""` Default · `1` Full width
- **`css_button_justify_content`** (select) — Horizontal align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button.button_full_width", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Left · `flex-end` Right · `center` Center · `space-between` Space between
  - Visible si: `full_width` is `1`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`button_style`** (switch) — Style
  - Valor: String
  - Opciones: `""` Default · `button_theme` Highlighted · `action_button` Action

### Advanced

- **`button_function`** (select) — Functional button
  - Read more doesn't support inner wraps.
  - Valor: String
  - Opciones: `""` None · `exit-mfn-popup` Close popup · `open-mfn-popup` Open popup · `mfn-go-to` Go to Section · `mfn-read-more` Read more · `mfn-copy-to-clipboard` Copy to clipboard
- **`button_function_copy_to_clipboard`** (text) — Copy to clipboard text
  - Valor: String
  - Visible si: `button_function` is `mfn-copy-to-clipboard`
- **`button_function_copy_to_clipboard_tooltip`** (text) — Tooltip text
  - Text on the tooltip. Leave this field empty to not display the tooltip.
  - Valor: String
  - Default: `Copy to clipboard`
  - Visible si: `button_function` is `mfn-copy-to-clipboard`
- **`button_function_copy_to_clipboard_copied_tooltip`** (text) — Confirmation text
  - Valor: String
  - Default: `Copied`
  - Visible si: `button_function` is `mfn-copy-to-clipboard`
- **`button_function_read_more_title`** (text) — Button title after expand
  - Valor: String
  - Visible si: `button_function` is `mfn-read-more`
- **`button_function_read_more_icon`** (icon) — Button icon after expand
  - Valor: String
  - Visible si: `button_function` is `mfn-read-more`
- **`button_function_go_to`** (select) — Section to go
  - Valor: String
  - Opciones: `""` Next · `last` Last · `prev` Prev
  - Visible si: `button_function` is `mfn-go-to`
- **`button_function_popupid`** (text) — Popup ID
  - Valor: String
  - Visible si: `button_function` is `open-mfn-popup`
- **`class`** (text) — Class
  - This option is useful when you want to use <b>scroll</b>
  - Valor: String
- **`button_id`** (text) — ID
  - This option is useful when you want to use <b>GTM</b>
  - Valor: String
- **`download`** (text) — Download
  - Enter the new filename for the downloaded file
  - Valor: String
- **`rel`** (text) — Rel
  - Valor: String
- **`onclick`** (text) — Onclick
  - Valor: String

### Deprecated

- **`align`** (switch) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Alignment
  - Valor: String
  - Opciones: `""` Left · `center` Center · `right` Right
- **`color`** (color) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Background color
  - For theme color button please enter <b>theme</b> in color filed
  - Valor: String
- **`font_color`** (color) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Text color
  - Valor: String

### Container

- **`css__text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Button

- **`css_button_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_gap`** (sliderbar) — Gap
  - Doesn't work with space between option.
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "gap", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `button_icon_select` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_icon_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button .button_icon", "style": "font-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `button_icon_select` isnt ``
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_button_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_button` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_button_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "color", "val": "valor"}`
- **`css_button_icon_color`** (color) — Icon color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button i", "style": "color", "val": "valor"}`
  - Visible si: `button_icon_select` isnt ``
- **`css_button_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_button` isnt `none`
- **`background_switcher`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_button_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "background-color", "val": "valor"}`
  - Visible si: `background_switcher_button` is `default`
- **`css_button_gradient`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_button` is `gradient`
- **`css_button_transition`** (sliderbar) — Transition duration
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button", "style": "transition", "val": "valor"}`
- **`css_button_color_hover`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button:hover", "style": "color", "val": "valor"}`
- **`css_button_icon_color_hover`** (color) — Icon color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button:hover i", "style": "color", "val": "valor"}`
  - Visible si: `button_icon_select` isnt ``
- **`css_button_border_color_hover`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button:hover", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_button` isnt `none`
- **`background_switcher_hover`** (switch) — Background type
  - Valor: String
  - Opciones: `default` Default · `gradient` Gradient
  - Default: `default`
- **`css_button_background_hover`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button:hover, .mcb-section .mcb-wrap .mcb-item-mfnuidelement .button:before", "style": "background", "val": "valor"}`
  - Visible si: `background_switcher_hover_button` is `default`
- **`css_button_gradient_hover`** (gradient) — Gradient
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .button:hover", "style": "gradient", "val": {..., "string": "linear-gradient(...)"} — solo string se emite}`
  - Visible si: `background_switcher_hover_button` is `gradient`

## Ejemplo mínimo

```json
{
  "type": "button",
  "uid": "itm000001",
  "size": "1/4",
  "tablet_size": "1/4",
  "mobile_size": "1/1",
  "attr": {
    "title": "Click here"
  }
}
```

## Variante shortcode inline (para `content` de column/plain_text/visual)

⚠️ Definición DISTINTA al elemento del builder — solo para el shortcode dentro de texto:
- **`title`** (text) — Button
  - Text on the button
  - Valor: String
  - Default: `Button`
- **`link`** (text) — Link
  - Link (with http://)
  - Valor: String
- **`target`** (select) — Target
  - Link target
  - Valor: String
  - Opciones: `0` Default · `_blank` New tab or window · `lightbox` Lightbox
  - Default: `0`
- **`align`** (switch) — Align
  - Button align
  - Valor: String
  - Opciones: `left` Left · `center` Center · `right` Right
- **`icon`** (icon) — Icon
  - To use a button with an icon, type the icon name here
  - Valor: String
- **`icon_position`** (switch) — Icon position
  - Icon position
  - Valor: String
  - Opciones: `left` Left · `right` Right
- **`color`** (color) — Button background color
  - Valor: String
- **`font_color`** (color) — Button text color
  - Valor: String
- **`size`** (switch) — Button Size
  - Valor: String
  - Opciones: `1` Small · `2` Default · `3` Large · `4` Very Large
  - Default: `2`
- **`full_width`** (switch) — Full Width
  - Stretch to the width of the column
  - Valor: String
  - Opciones: `""` No · `1` Yes
- **`class`** (pills) — Class
  - CSS Classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)
- **`button_id`** (text) — ID
  - This option is useful when you want to use <b>GTM</b>
  - Valor: String
- **`rel`** (text) — Rel
  - "Rel" attribute to the link
  - Valor: String
- **`download`** (text) — Download
  - Enter the new filename (if click on button downloads a file)
  - Valor: String
- **`onclick`** (text) — onclick
  - "Onclick" attribute to the link
  - Valor: String

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*