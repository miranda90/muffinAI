# `payment_methods` — Payment methods

- **Categoría:** other
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 13

## Campos
- **`dynamic_items`** (dynamic_items) — Payment methods
  - Valor: String
  - Opciones: `var` {"predefined": "Predefined", "custom": "Custom"} · `add_button` false · `preview` img · `options` {"predefined": {"type": "select-img", "label": "Predefined", "options": {"Affirm": "{theme_uri}/images/payment-methods/Affirm.svg", "Alipay": "{theme_uri}/images/payment-methods/Alipay.svg", "AmazonPay": "{theme_uri}/images/payment-methods/AmazonPay.svg", "Amex": "{theme_uri}/images/payment-methods/Amex.svg", "ApplePay": "{theme_uri}/images/payment-methods/ApplePay.svg", "Bancontact": "{theme_uri}/images/payment-methods/Bancontact.svg", "Bitcoin": "{theme_uri}/images/payment-methods/Bitcoin.svg", "BitcoinCash": "{theme_uri}/images/payment-methods/BitcoinCash.svg", "Bitpay": "{theme_uri}/images/payment-methods/Bitpay.svg", "Citadele": "{theme_uri}/images/payment-methods/Citadele.svg", "DinersClub": "{theme_uri}/images/payment-methods/DinersClub.svg", "Discover": "{theme_uri}/images/payment-methods/Discover.svg", "Elo": "{theme_uri}/images/payment-methods/Elo.svg", "Etherium": "{theme_uri}/images/payment-methods/Etherium.svg", "FacebookPay": "{theme_uri}/images/payment-methods/FacebookPay.svg", "Forbrugsforeningen": "{theme_uri}/images/payment-methods/Forbrugsforeningen.svg", "Giropay": "{theme_uri}/images/payment-methods/Giropay.svg", "GooglePay": "{theme_uri}/images/payment-methods/GooglePay.svg", "Ideal": "{theme_uri}/images/payment-methods/Ideal.svg", "Interac": "{theme_uri}/images/payment-methods/Interac.svg", "JCB": "{theme_uri}/images/payment-methods/JCB.svg", "Klarna": "{theme_uri}/images/payment-methods/Klarna.svg", "Lightcoin": "{theme_uri}/images/payment-methods/Lightcoin.svg", "Maestro": "{theme_uri}/images/payment-methods/Maestro.svg", "Mastercard": "{theme_uri}/images/payment-methods/Mastercard.svg", "PayPal": "{theme_uri}/images/payment-methods/PayPal.svg", "Payoneer": "{theme_uri}/images/payment-methods/Payoneer.svg", "Paysafe": "{theme_uri}/images/payment-methods/Paysafe.svg", "Poli": "{theme_uri}/images/payment-methods/Poli.svg", "Qiwi": "{theme_uri}/images/payment-methods/Qiwi.svg", "SEPA": "{theme_uri}/images/payment-methods/SEPA.svg", "ShopPay": "{theme_uri}/images/payment-methods/ShopPay.svg", "Skrill": "{theme_uri}/images/payment-methods/Skrill.svg", "Sofort": "{theme_uri}/images/payment-methods/Sofort.svg", "Stripe": "{theme_uri}/images/payment-methods/Stripe.svg", "UnionPay": "{theme_uri}/images/payment-methods/UnionPay.svg", "Venmo": "{theme_uri}/images/payment-methods/Venmo.svg", "Verifone": "{theme_uri}/images/payment-methods/Verifone.svg", "Visa": "{theme_uri}/images/payment-methods/Visa.svg", "WeChat": "{theme_uri}/images/payment-methods/WeChat.svg", "Webmoney": "{theme_uri}/images/payment-methods/Webmoney.svg", "Yandex": "{theme_uri}/images/payment-methods/Yandex.svg"}}, "custom": {"type": "upload", "label": "Custom"}}
- **`greyscale`** (switch) — Grayscale
  - Valor: String
  - Opciones: 
  - Default: `0`
- **`invert`** (switch) — Invert
  - Valor: String
  - Opciones: 
  - Default: `0`

### Items

- **`css_payment-methods-list_justify_content`** (select) — Alignment
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .payment-methods-list", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `flex-start` Left · `center` Center · `flex-end` Right · `space-between` Space between · `space-around` Space around
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_payment-methods-listliimg_width`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .payment-methods-list li img", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_payment-methods-listli_opacity`** (sliderbar) — Opacity
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .payment-methods-list li", "style": "opacity", "val": "valor"}`
  - Default: `1`
- **`css_payment-methods-listli_background_color`** (color) — Background
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .payment-methods-list li", "style": "background-color", "val": "valor"}`
- **`css_payment-methods-listli_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .payment-methods-list li", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_payment-methods-listli_margin`** (dimensions) — Margin
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .payment-methods-list li", "style": "margin", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_payment-methods-listli_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .payment-methods-list li", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_payment-methods-listli_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .payment-methods-list li", "style": "border-color", "val": "valor"}`
  - Visible si: `border_style_paymet` isnt `none`
- **`css_payment-methods-listli_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .payment-methods-list li", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `border_style_paymet` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_payment-methods-listli_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .payment-methods-list li", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "payment_methods",
  "uid": "itm000001",
  "icon": "payment_methods",
  "jsclass": "payment_methods",
  "title": "Payment methods",
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