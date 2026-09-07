# `countdown` — Countdown Basic

- **Categoría:** boxes
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 20

## Campos
- **`date`** (text) — Launch date
  - month/day/year hour:minute:second
  - Valor: String
  - Default: `12/30/2024 12:00:00`
- **`title_tag`** (switch) — Label tag
  - Valor: String
  - Opciones: `h1` h1 · `h2` h2 · `h3` h3 · `h4` h4 · `h5` h5 · `h6` h6 · `p` p · `p.lead` p.lead · `span` span
  - Default: `h3`
- **`timezone`** (select) — Timezone
  - Valor: String
  - Opciones: `-12` -12:00 · `-11` -11:00 Pago Pago · `-10` -10:00 Papeete, Honolulu · `-9.5` -9:30 · `-9` -9:00 Anchorage · `-8` -8:00 Los Angeles, Vancouver, Tijuana · `-7` -7:00 Phoenix, Calgary, Ciudad Juárez · `-6` -6:00 Chicago, Guatemala City, Mexico City, San José, San Salvador, Winnipeg · `-5` -5:00 New York, Lima, Toronto, Bogotá, Havana, Kingston · `-4` -4:00 Caracas, Santiago, La Paz, Manaus, Halifax, Santo Domingo · `-3.5` -3:30 St. John's · `-3` -3:00 Buenos Aires, Montevideo, São Paulo · `-2` -2:00 · `-1` -1:00 Praia · `0` ±0:00 Accra, Casablanca, Dakar, Dublin, Lisbon, London · `+1` +1:00 Berlin, Lagos, Madrid, Paris, Rome, Tunis, Vienna, Warsaw · `+2` +2:00 Athens, Bucharest, Cairo, Helsinki, Jerusalem, Johannesburg, Kiev · `+3` +3:00 Istanbul, Moscow, Nairobi, Baghdad, Doha, Minsk, Riyadh · `+3.5` +3:30 Tehran · `+4` +4:00 Baku, Dubai, Samara, Muscat · `+4.5` +4:30 Kabul · `+5` +5:00 Karachi, Tashkent, Yekaterinburg · `+5.5` +5:30 Delhi, Colombo · `+5.75` +5:45 Kathmandu · `+6` +6:00 Almaty, Dhaka, Omsk · `+6.5` +6:30 Yangon · `+7` +7:00 Jakarta, Bangkok, Krasnoyarsk, Ho Chi Minh City · `+8` +8:00 Beijing, Hong Kong, Taipei, Singapore, Kuala Lumpur, Perth, Manila, Denpasar, Irkutsk · `+8.5` +8:30 Pyongyang · `+8.75` +8:45 · `+9` +9:00 Seoul, Tokyo, Ambon, Yakutsk · `+9.5` +9:30 Adelaide · `+10` +10:00 Port Moresby, Brisbane, Vladivostok, Sydney · `+10.5` +10:30 · `+11` +11:00 Nouméa · `+12` +12:00 Auckland, Suva · `+12.75` +12:45 · `+13` +13:00 Apia, Nukuʻalofa · `+14` +14:00
  - Default: `0`

### Options

- **`show`** (select) — Show
  - Valor: String
  - Opciones: `""` days hours minutes seconds · `dhm` days hours minutes · `dh` days hours · `d` days

### Deprecated

- **`class`** (pills) ⚠️ **DEPRECATED — no usar en JSON nuevo** — Element classes
  - Valor: String de clases separadas por espacio (ej. `"clase-a clase-b"`)

### Container

- **`css_downcount_fact_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact", "style": "background-color", "val": "valor"}`
- **`css_downcount_fact_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_downcount_fact_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_downcount_fact_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_downcount_fact_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_dcqf` isnt `none`
- **`css_downcount_fact_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_dcqf` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_downcount_fact_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Number

- **`css_downcount_factnumber-wrappernumber_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact .number-wrapper .number", "style": "color", "val": "valor"}`
- **`css_downcount_factnumber-wrapper_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact .number-wrapper", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_downcount_factnumber-wrapper_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact .number-wrapper", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Label

- **`css_downcount_facttitle_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact .title", "style": "color", "val": "valor"}`
- **`css_downcount_facttitle_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact .title", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_downcount_facttitle_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact .title", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Divider

- **`css_downcount_facthr_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact hr", "style": "width", "val": "valor"}`
- **`css_downcount_facthr_background_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .downcount .column .quick_fact hr", "style": "background-color", "val": "valor"}`

## Ejemplo mínimo

```json
{
  "type": "countdown",
  "uid": "itm000001",
  "icon": "countdown",
  "jsclass": "countdown",
  "title": "Countdown Basic",
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