# `countdown_inline` — Countdown Inline (shortcode inline)

Shortcode **inline** para usar dentro de `content` (column, plain_text, visual). NO es un item del builder: no lleva `type`/`size`/`uid`.

## Campos
- **`date`** (text) — Launch date
  - month/day/year hour:minute:second
  - Valor: String
  - Default: `12/30/2022 12:00:00`
- **`timezone`** (select) — Timezone
  - Valor: String
  - Opciones: `-12` -12:00 · `-11` -11:00 Pago Pago · `-10` -10:00 Papeete, Honolulu · `-9.5` -9:30 · `-9` -9:00 Anchorage · `-8` -8:00 Los Angeles, Vancouver, Tijuana · `-7` -7:00 Phoenix, Calgary, Ciudad Juárez · `-6` -6:00 Chicago, Guatemala City, Mexico City, San José, San Salvador, Winnipeg · `-5` -5:00 New York, Lima, Toronto, Bogotá, Havana, Kingston · `-4` -4:00 Caracas, Santiago, La Paz, Manaus, Halifax, Santo Domingo · `-3.5` -3:30 St. John's · `-3` -3:00 Buenos Aires, Montevideo, São Paulo · `-2` -2:00 · `-1` -1:00 Praia · `0` ±0:00 Accra, Casablanca, Dakar, Dublin, Lisbon, London · `+1` +1:00 Berlin, Lagos, Madrid, Paris, Rome, Tunis, Vienna, Warsaw · `+2` +2:00 Athens, Bucharest, Cairo, Helsinki, Jerusalem, Johannesburg, Kiev · `+3` +3:00 Istanbul, Moscow, Nairobi, Baghdad, Doha, Minsk, Riyadh · `+3.5` +3:30 Tehran · `+4` +4:00 Baku, Dubai, Samara, Muscat · `+4.5` +4:30 Kabul · `+5` +5:00 Karachi, Tashkent, Yekaterinburg · `+5.5` +5:30 Delhi, Colombo · `+5.75` +5:45 Kathmandu · `+6` +6:00 Almaty, Dhaka, Omsk · `+6.5` +6:30 Yangon · `+7` +7:00 Jakarta, Bangkok, Krasnoyarsk, Ho Chi Minh City · `+8` +8:00 Beijing, Hong Kong, Taipei, Singapore, Kuala Lumpur, Perth, Manila, Denpasar, Irkutsk · `+8.5` +8:30 Pyongyang · `+8.75` +8:45 · `+9` +9:00 Seoul, Tokyo, Ambon, Yakutsk · `+9.5` +9:30 Adelaide · `+10` +10:00 Port Moresby, Brisbane, Vladivostok, Sydney · `+10.5` +10:30 · `+11` +11:00 Nouméa · `+12` +12:00 Auckland, Suva · `+12.75` +12:45 · `+13` +13:00 Apia, Nukuʻalofa · `+14` +14:00
  - Default: `0`
- **`show`** (select) — Show
  - Valor: String
  - Opciones: `""` days hours minutes seconds · `dhm` days hours minutes · `dh` days hours · `d` days

*Generado desde `class-mfn-builder-fields.php` (`get_inline_shortcode()`) — no editar a mano.*