# `divider_2` — &bull; Divider

- **Categoría:** other
- **Size por defecto:** 1/1 · tablet 1/1 · mobile 1/1 · tablet_resized 0
- **Campos propios:** 27

## Campos
- **`type`** (select) — Type
  - Valor: String
  - Opciones: `""` Empty · `#optgroup-border` Border · `border-solid` Solid · `border-dotted` Dotted · `border-dashed` Dashed · `border-double` Double · `#optgroup-border-end`  · `#optgroup-pattern` Pattern · `pattern-star` Star · `pattern-triangle` Triangle · `pattern-plus` Plus · `pattern-tree` Tree · `pattern-heart` Heart · `pattern-question` Question · `pattern-gear` Gear · `pattern-parquet` Parquet · `pattern-sun` Sun · `pattern-fence` Fence · `pattern-flower` Flower · `#optgroup-pattern-end`  · `#optgroup-lines` Lines · `pattern-line-wave` Waves · `pattern-line-zigzag` Zig Zag · `pattern-line-zigzag2` Zig Zag 2 · `pattern-line-hearts` Hearts · `pattern-line-triangles` Triangles · `pattern-line-circles` Circles · `pattern-line-circles2` Circles 2 · `pattern-line-circles3` Circles 3 · `pattern-line-stars` Stars · `pattern-line-rhombus` Rhombus · `pattern-line-figures` Figures · `pattern-line-loopline` Loopline · `#optgroup-lines-end` 
- **`align`** (switch) — Alignment
  - Valor: String
  - Opciones: `start` Start · `center` Center · `end` End
  - Default: `center`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Gap

- **`css_divider_gap_top`** (sliderbar) — Gap top
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "--mfn-divider-gap-top", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `20px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_divider_gap_bottom`** (sliderbar) — Gap bottom
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "--mfn-divider-gap-bottom", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Default: `20px`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Addon

- **`addon`** (select) — Addon
  - Valor: String
  - Opciones: `""` None · `label` Label · `image` Image · `icon` Icon
- **`label`** (text) — Label
  - Valor: String
  - Visible si: `divider-2-addon` is `label`
- **`image`** (upload) — Image
  - Valor: String
  - Visible si: `divider-2-addon` is `image`
- **`icon`** (icon) — Icon
  - Valor: String
  - Visible si: `divider-2-addon` is `icon`

### Container

- **`css_divider-inner_width`** (text) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)

### Divider

- **`css_divider_height`** (sliderbar) — Pattern height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "--mfn-divider-height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `divider-2-type` is `pattern-star,pattern-triangle,pattern-plus,pattern-tree,pattern-heart,pattern-question,pattern-gear,pattern-parquet,pattern-sun,pattern-fence,pattern-flower,pattern-line-wave,pattern-line-zigzag,pattern-line-zigzag2,pattern-line-hearts,pattern-line-triangles,pattern-line-circles,pattern-line-circles2,pattern-line-circles3,pattern-line-stars,pattern-line-rhombus,pattern-line-figures,pattern-line-loopline`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_divider_pattern_color`** (color) — Pattern color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "--mfn-divider-pattern-color", "val": "valor"}`
  - Visible si: `divider-2-type` is `pattern-star,pattern-triangle,pattern-plus,pattern-tree,pattern-heart,pattern-question,pattern-gear,pattern-parquet,pattern-sun,pattern-fence,pattern-flower,pattern-line-wave,pattern-line-zigzag,pattern-line-zigzag2,pattern-line-hearts,pattern-line-triangles,pattern-line-circles,pattern-line-circles2,pattern-line-circles3,pattern-line-stars,pattern-line-rhombus,pattern-line-figures,pattern-line-loopline`
- **`css_divider_border_width`** (sliderbar) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "--mfn-divider-border-width", "val": "valor"}`
  - Visible si: `divider-2-type` is `border-solid,border-dotted,border-dashed,border-double`
- **`css_divider_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "--mfn-divider-border-color", "val": "valor"}`
  - Visible si: `divider-2-type` is `border-solid,border-dotted,border-dashed,border-double`

### Addon

- **`css_divider_spacing`** (sliderbar) — Spacing
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "--mfn-divider-spacing", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_divider-innerdivider-iconi_font_size`** (sliderbar) — Icon size
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner .divider-icon i", "style": "font-size", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `divider-2-addon` is `icon`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_divider_icon_color`** (color) — Icon color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "--mfn-divider-icon-color", "val": "valor"}`
  - Visible si: `divider-2-addon` is `icon`
- **`css_divider-innerdivider-imageimg_height`** (sliderbar) — Image height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner .divider-image img", "style": "height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `divider-2-addon` is `image`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_divider-innerdivider-label_color`** (color) — Text color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner .divider-label", "style": "color", "val": "valor"}`
  - Visible si: `divider-2-addon` is `label`
- **`css_divider-innerdivider-label_typography`** (typography_vb) — Typography
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner .divider-label", "style": "typography", "val": {"desktop": {"font-size": "...", "line-height": "...", "font-weight": "...", ...}, "tablet": ..., "mobile": ...}}`
  - Visible si: `divider-2-addon` is `label`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_divider-innerdivider-addon_background_color`** (color) — Background color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner .divider-addon", "style": "background-color", "val": "valor"}`
- **`css_divider-innerdivider-label_padding`** (dimensions) — Padding
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner .divider-label", "style": "padding", "val": {"desktop": {"top": "...", "right": "...", "bottom": "...", "left": "..."}, "tablet": ..., "mobile": ...}}`
  - Visible si: `divider-2-addon` is `label`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_divider_addon_width`** (sliderbar) — Width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "--mfn-divider-addon-width", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `divider-2-addon` isnt `label`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_divider_addon_height`** (sliderbar) — Height
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner", "style": "--mfn-divider-addon-height", "val": {"desktop": "valor", "tablet": ..., "mobile": ...}}`
  - Visible si: `divider-2-addon` isnt `label`
  - Responsive: sí (`val` por dispositivo: desktop/laptop/tablet/mobile)
- **`css_divider-innerdivider-addon_border_style`** (select) — Border style
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner .divider-addon", "style": "border-style", "val": "valor"}`
  - Opciones: `none` None · `solid` Solid · `dashed` Dashed · `dotted` Dotted · `double` Double
- **`css_divider-innerdivider-addon_border_color`** (color) — Border color
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner .divider-addon", "style": "border-color", "val": "valor"}`
  - Visible si: `divider-2-addon-border` isnt `none`
- **`css_divider-innerdivider-addon_border_width`** (dimensions) — Border width
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner .divider-addon", "style": "border-width", "val": "1px 1px 1px 1px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top right bottom left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)
  - Visible si: `divider-2-addon-border` isnt `none`
- **`css_divider-innerdivider-addon_border_radius`** (dimensions) — Border radius
  - Valor: Objeto CSS: `{"selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .mfn-divider-inner .divider-addon", "style": "border-radius", "val": "8px 8px 8px 8px"}`
  - ⚠️ Shorthand: string con los 4 valores separados por espacios (`top-left top-right bottom-right bottom-left`), **nunca** objeto `{top,right,bottom,left}` (ese formato es exclusivo de margin/padding)

## Ejemplo mínimo

```json
{
  "type": "divider_2",
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