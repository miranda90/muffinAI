# `countdown_2` — Countdown

- **Categoría:** boxes
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 36

## Campos
- **`date`** (text) — Launch date
  - month/day/year hour:minute:second<br />+7 = seven days (till midnight)<br />*24 = twenty four hours
  - Valor: String
  - Default: `12/30/2025 12:00:00`
- **`timezone`** (select) — Timezone (server)
  - Valor: String
  - Opciones: `-12` -12:00 · `-11` -11:00 Pago Pago · `-10` -10:00 Papeete, Honolulu · `-9.5` -9:30 · `-9` -9:00 Anchorage · `-8` -8:00 Los Angeles, Vancouver, Tijuana · `-7` -7:00 Phoenix, Calgary, Ciudad Juárez · `-6` -6:00 Chicago, Guatemala City, Mexico City, San José, San Salvador, Winnipeg · `-5` -5:00 New York, Lima, Toronto, Bogotá, Havana, Kingston · `-4` -4:00 Caracas, Santiago, La Paz, Manaus, Halifax, Santo Domingo · `-3.5` -3:30 St. John's · `-3` -3:00 Buenos Aires, Montevideo, São Paulo · `-2` -2:00 · `-1` -1:00 Praia · `0` ±0:00 Accra, Casablanca, Dakar, Dublin, Lisbon, London · `+1` +1:00 Berlin, Lagos, Madrid, Paris, Rome, Tunis, Vienna, Warsaw · `+2` +2:00 Athens, Bucharest, Cairo, Helsinki, Jerusalem, Johannesburg, Kiev · `+3` +3:00 Istanbul, Moscow, Nairobi, Baghdad, Doha, Minsk, Riyadh · `+3.5` +3:30 Tehran · `+4` +4:00 Baku, Dubai, Samara, Muscat · `+4.5` +4:30 Kabul · `+5` +5:00 Karachi, Tashkent, Yekaterinburg · `+5.5` +5:30 Delhi, Colombo · `+5.75` +5:45 Kathmandu · `+6` +6:00 Almaty, Dhaka, Omsk · `+6.5` +6:30 Yangon · `+7` +7:00 Jakarta, Bangkok, Krasnoyarsk, Ho Chi Minh City · `+8` +8:00 Beijing, Hong Kong, Taipei, Singapore, Kuala Lumpur, Perth, Manila, Denpasar, Irkutsk · `+8.5` +8:30 Pyongyang · `+8.75` +8:45 · `+9` +9:00 Seoul, Tokyo, Ambon, Yakutsk · `+9.5` +9:30 Adelaide · `+10` +10:00 Port Moresby, Brisbane, Vladivostok, Sydney · `+10.5` +10:30 · `+11` +11:00 Nouméa · `+12` +12:00 Auckland, Suva · `+12.75` +12:45 · `+13` +13:00 Apia, Nukuʻalofa · `+14` +14:00
  - Default: `0`
- **`show`** (select) — Show
  - Valor: String
  - Opciones: `""` -- Default -- · `dhms` days hours minutes seconds · `dhm` days hours minutes · `dh` days hours · `d` days · `hms` hours minutes seconds
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Settings

- **`align`** (switch) — Alignment
  - Valor: String
  - Opciones: `left` Left · `center` Center · `right` Right
  - Default: `center`
- **`separator`** (switch) — Separator
  - Valor: String
  - Opciones: `off` Disable · `""` Enable
- **`separator_sign`** (text) — Separator sign
  - Valor: String
  - Default: `:`

### Mobile Settings

- **`mobile_orientation`** (switch) — Orientation
  - Valor: String
  - Opciones: `""` Horizontal · `vertical` Vertical
- **`mobile_align`** (switch) — Alignment
  - Valor: String
  - Opciones: `left` Left · `center` Center · `right` Right
  - Default: `center`
- **`mobile_separator`** (switch) — Separator
  - Valor: String
  - Opciones: `off` Disable · `""` Enable
  - Visible si: `mobile_orientation` isnt `vertical`

### Order

- **`order`** (order) — Order
  - Valor: String
  - Default: `number,title`

### General

- **`css_countdown-spacing`** (sliderbar) — Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown", "style": "--mfn-countdown-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `15px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Countdown item

- **`css_countdown-item-spacing`** (sliderbar) — Number/Title Gap
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown", "style": "--mfn-countdown-countdown-item-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `10px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-item-padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-item", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-item-width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-item", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-item-height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-item", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-item-background-color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-item", "style": "background-color", "val": "valor"}`
- **`css_countdown-item-border-style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-item", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_countdown-item-border-color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-item", "style": "border-color", "val": "valor"}`
  - Visible si: `css_countdown-item-border-style` isnt `none`
- **`css_countdown-item-border-width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-item", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `css_countdown-item-border-style` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-item-border-radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-item", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-item-box-shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-item", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Number

- **`css_countdown-number-color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-number", "style": "color", "val": "valor"}`
- **`css_countdown-number_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-number", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-number-width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-number", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-number-height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-number", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-number-background-color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-number", "style": "background-color", "val": "valor"}`
- **`css_countdown-number-border-style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-number", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_countdown-number-border-color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-number", "style": "border-color", "val": "valor"}`
  - Visible si: `css_countdown-number-border-style` isnt `none`
- **`css_countdown-number-border-width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-number", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `css_countdown-number-border-style` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-number-border-radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-number", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-number-box-shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-number", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Title

- **`css_countdown-title-color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-title", "style": "color", "val": "valor"}`
- **`css_countdown-title-typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .counter-title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Separator

- **`css_countdown-separator-color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-separator.colon", "style": "color", "val": "valor"}`
- **`css_countdown-separator-typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-separator.colon", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_countdown-separator-offset`** (sliderbar) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-countdown .countdown-separator.colon", "style": "top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `0`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "countdown_2",
  "uid": "itm000001",
  "icon": "countdown_2",
  "jsclass": "countdown_2",
  "title": "Countdown",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "attr": {}
}
```

---
Todos los elementos admiten además la **pestaña Advanced** (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`): ver [_advanced.md](_advanced.md).
Formato de los campos `css_*` y pipeline CSS: `docs/bebuilder/02-css-pipeline.md`. Reglas y trampas: `docs/bebuilder/05-reglas-y-trampas.md`.

*Generado desde `class-mfn-builder-fields.php` por `_generator/` — no editar a mano.*