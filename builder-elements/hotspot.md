# `hotspot` — Hotspot

- **Categoría:** elements
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 40

## Campos
- **`image`** (upload) — Image
  - Valor: String

### General

- **`marker_animation`** (switch) — Marker animation
  - Valor: String
  - Opciones: `""` Default · `pulse` Pulse · `scale` Scale · `bounce` Bounce
- **`content_animation`** (switch) — Content animation
  - Valor: String
  - Opciones: `""` Default · `fadeIn` Fade In
- **`style`** (switch) — Points style
  - Valor: String
  - Opciones: `""` Default · `line` Line

### Hotspots

- **`hotspots`** (hotspot) — Hotspots
  - Valor: String

### Image

- **`img_height`** (switch) — Height
  - Valor: String
  - Opciones: `""` Default · `custom` Custom
- **`img_height_style`** (switch) — Image style
  - Valor: String
  - Opciones: `""` Default · `cover` Cover
  - Visible si: `img_height` is `custom`
- **`css_img_height`** (text) — Custom height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot-height .hotspot-image img", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `img_height` is `custom`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_image-hotspot_justify_content`** (switch) — Align
  - Doesn't work with Image Cover mode
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "justify-content", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_hotspot-image_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-image", "style": "background-color", "val": "valor"}`
- **`css_hotspot-image_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-image", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_hotspot-image_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-image", "style": "border-color", "val": "valor"}`
  - Visible si: `hotspot-border-img` isnt `none`
- **`css_hotspot-image_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-image", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `hotspot-border-img` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_hotspot-image_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-image", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_hotspot-image_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-image", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Marker

- **`css_hotspot_marker_default_bg`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-default-bg", "val": "valor"}`
- **`css_hotspot-marker_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-marker", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Default

- **`css_hotspot_marker_default_pulse_bg`** (color) — Pulse color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-default-pulse-bg", "val": "valor"}`
  - Visible si: `marker_animation` is `pulse`
- **`css_hotspot_marker_default_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-default-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Icon

- **`css_hotspot_marker_icon_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-icon-color", "val": "valor"}`
- **`css_hotspot_marker_icon_bg`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-icon-bg", "val": "valor"}`
- **`css_hotspot_marker_icon_pulse_bg`** (color) — Pulse color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-icon-pulse-bg", "val": "valor"}`
  - Visible si: `marker_animation` is `pulse`
- **`css_hotspot_marker_icon_size`** (sliderbar) — Size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-icon-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_hotspot_marker_icon_font_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-icon-font-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Text

- **`css_hotspot_marker_text_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-text-color", "val": "valor"}`
- **`css_hotspot_marker_text_bg`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-text-bg", "val": "valor"}`
- **`css_hotspot_marker_text_pulse_bg`** (color) — Pulse color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-marker-text-pulse-bg", "val": "valor"}`
  - Visible si: `marker_animation` is `pulse`
- **`css_marker_txt_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .marker-text", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_marker_txt_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .marker-text", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Box

- **`css_hotspot-content_text_align`** (switch) — Text align
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-content", "style": "text-align", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Opciones: `""` Default · `left` Left · `center` Center · `right` Right · `justify` Justify
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_hotspot-content_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-content", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_hotspot_content_bg`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-content-bg", "val": "valor"}`
- **`css_image-hotspothotspot-content_color`** (color) — Color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot .hotspot-content", "style": "color", "val": "valor"}`
- **`css_hotspot-content_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-content", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_hotspot_content_offset`** (sliderbar) — Offset
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-image-hotspot", "style": "--mfn-image-hotspot-content-offset", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_hotspot-content_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-content", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_hotspot-content_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-content", "style": "border-color", "val": "valor"}`
  - Visible si: `hotspot-border-content` isnt `none`
- **`css_hotspot-content_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-content", "style": "border-width", "val": {"desktop": "1px 1px 1px 1px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `hotspot-border-content` isnt `none`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_hotspot-content_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-content", "style": "border-radius", "val": {"desktop": "8px 8px 8px 8px", "tablet": ..., "mobile": ...}}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_hotspot-content_box_shadow`** (box_shadow) — Box shadow
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .hotspot-content", "style": "box-shadow", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

## Ejemplo mínimo

```json
{
  "type": "hotspot",
  "uid": "itm000001",
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