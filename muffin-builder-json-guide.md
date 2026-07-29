## Muffin Builder JSON Authoring Guide

This guide explains how to handcraft Muffin Builder JSON from a design (Figma/HTML/spec) and import it in WordPress.

### Top-level Structure
- The document is a JSON array of sections.
- Hierarchy: sections → wraps → items.
- Item `type` determines available fields and rendering.

```json
[
  {
    "icon": "section",
    "uid": "unique-section-id",
    "jsclass": "section",
    "title": "Section",
    "attr": { /* section fields */ },
    "ver": "default",
    "wraps": [
      {
        "icon": "wrap",
        "uid": "unique-wrap-id",
        "size": "1/1",
        "tablet_size": "1/1",
        "mobile_size": "1/1",
        "jsclass": "wrap",
        "attr": { /* wrap fields */ },
        "title": "Wrap",
        "items": [
          {
            "type": "heading",
            "jsclass": "heading",
            "title": "Heading",
            "icon": "heading",
            "attr": { /* item fields */ },
            "uid": "unique-item-id",
            "size": "1/1",
            "tablet_size": "1/1",
            "laptop_size": "1/1",
            "mobile_size": "1/1"
          }
        ]
      }
    ]
  }
]
```

### Import/Export Behavior
- Import expects the above JSON array (AJAX import decodes JSON and resets UIDs).
- Export builds the same structure and prints JSON.
- Page save stores serialized base64 or raw arrays internally; you only need the JSON for manual import.

### Attribute Conventions

#### 1) Simple fields
- Stored directly in `attr` as scalars.
- If responsive, the exported JSON commonly nests values under a `val` map. You can mirror that shape.

Example (text-align on desktop):
```json
"css_txt_align": {
  "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title",
  "style": "text-align",
  "val": { "desktop": "center" }
}
```

Example (grid columns on wrap):
```json
"css_grid_columns": {
  "selector": ".mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement .mcb-wrap-inner",
  "style": "grid-template-columns",
  "val": { "desktop": "repeat(3, 1fr)" }
}
```

#### 2) CSS-advanced fields (recommended)
- Keys usually start with `css_`.
- Must be an object with: `selector`, `style`, `val`.
- `val` can be a single string or a per-device map. Composite values (e.g., padding object) are allowed inside each device.

Example (section padding):
```json
"css_advanced_padding": {
  "selector": ".mcb-section-mfnuidelement",
  "style": "padding",
  "val": {
    "desktop": { "top": "5rem", "bottom": "5rem" },
    "tablet":  { "top": "3rem", "bottom": "3rem" },
    "mobile":  { "top": "2rem", "bottom": "2rem" }
  }
}
```

Rendering: Muffin generates local CSS from these entries, mapping the `selector` and `style` with transformed values.

#### 3) How responsive folding works internally
- Admin UI folds fields with device suffixes into `attr[key].val[device]` for `css_*` fields, or under `attr[key][device]` for some simple fields.
- For authoring JSON, prefer the `css_*` object form with `val` device maps.

### Common Attributes by Level

#### Section
- **Width/Height**: Use **`width_switcher`: `"full"`** for full-width sections; the builder UI reads this attribute (if missing, it shows "default"). Do not rely on `style: "full-width"` alone. `height_switcher`: `"custom"` | `"full-screen"`.
- **Background**: `css_advanced_background_color` or other `css_*` with `selector`/`style`/`val`.
- **Spacing**: `css_advanced_padding`, `css_advanced_margin`.
- **Flex alignment**: `css_advanced_align_items`, `css_advanced_justify_content`, `css_advanced_align_content` targeting `.section_wrapper`.
- **IDs**: `custom_id` for DOM anchors.

#### Wrap
- **Grid**: `css_grid_columns` → `grid-template-columns` on `.mcb-wrap-inner`.
- **Height**: `css_advanced_height`, `css_advanced_min_height`.
- **Visibility**: `custom-responsive` (e.g., `hide`).

#### Items (type-driven)
- `heading`: `title`, `header_tag`, `css_txt_align`, `css_typography`.
- `column`: `content` (HTML/shortcodes), plus bg/margin/padding fields if needed.
- Other item types follow the same `attr` pattern; `css_*` for styles.

Example heading typography:
```json
"css_typography": {
  "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title",
  "style": "typography",
  "val": {
    "desktop": { "font-size": "70px", "line-height": "1.3rem", "letter-spacing": "1rem" },
    "mobile":  { "font-size": "2rem",  "letter-spacing": "0.2rem" },
    "text-transform": "uppercase"
  }
}
```

Example column content with shortcode:
```json
"content": "<div class=\"mainMenuCover\">[menu menu=\"main-menu\"]</div>"
```

### Unique IDs
- `uid` can be any unique string. Import will regenerate missing/duplicate IDs.
- Readable UIDs help debugging.

### Practical Authoring Flow (Figma/HTML → JSON)
1. Split layout into sections (bands), wraps (rows/containers), items (content blocks).
2. Build the skeleton: sections with empty `wraps`, wraps with empty `items`.
3. Map styling to `css_*` attributes with `selector`, `style`, `val` (per device if needed).
4. Add responsive values only where necessary (`desktop`, `laptop`, `tablet`, `mobile`).
5. Use `column` items for raw HTML/shortcodes.
6. Add `custom_id` and readable `uid`s as needed.
7. Import the JSON array into Muffin Builder.

### Ready-to-use Scaffolds

Empty black section, centered content, responsive padding:
```json
[
  {
    "icon": "section",
    "uid": "sec-hero",
    "jsclass": "section",
    "title": "Section",
    "attr": {
      "css_advanced_background_color": {
        "selector": ".mcb-section-mfnuidelement",
        "style": "background-color",
        "val": "#000000"
      },
      "css_advanced_padding": {
        "selector": ".mcb-section-mfnuidelement",
        "style": "padding",
        "val": {
          "desktop": { "top": "5rem", "bottom": "5rem" },
          "mobile":  { "top": "2rem", "bottom": "2rem" }
        }
      },
      "css_advanced_align_items": {
        "selector": ".mcb-section-mfnuidelement .section_wrapper",
        "style": "align-items",
        "val": { "desktop": "center" }
      },
      "css_advanced_justify_content": {
        "selector": ".mcb-section-mfnuidelement .section_wrapper",
        "style": "justify-content",
        "val": { "desktop": "center" }
      }
    },
    "ver": "default",
    "wraps": []
  }
]
```

Add a 3-column wrap with centered H2:
```json
{
  "icon": "wrap",
  "uid": "wrap-3col",
  "size": "1/1",
  "tablet_size": "1/1",
  "mobile_size": "1/1",
  "jsclass": "wrap",
  "attr": {
    "css_grid_columns": {
      "selector": ".mcb-section .mcb-wrap-grid.mcb-wrap-mfnuidelement .mcb-wrap-inner",
      "style": "grid-template-columns",
      "val": { "desktop": "repeat(3, 1fr)" }
    }
  },
  "title": "Wrap",
  "items": [
    {
      "type": "heading",
      "jsclass": "heading",
      "title": "Heading",
      "icon": "heading",
      "attr": {
        "title": "Title here",
        "header_tag": "h2",
        "css_txt_align": {
          "selector": ".mcb-section .mcb-wrap .mcb-item-mfnuidelement .title",
          "style": "text-align",
          "val": { "desktop": "center" }
        }
      },
      "uid": "h2-title",
      "size": "1/1",
      "tablet_size": "1/1",
      "laptop_size": "1/1",
      "mobile_size": "1/1"
    }
  ]
}
```

### What I need from you to generate JSON fast
- Section list with backgrounds/spacing/width/height
- For each section: wraps and grid (columns) per breakpoint
- For each item: `type`, text/content, alignment, typographic constraints, and any HTML/shortcodes
- Any special IDs or classes you want to target later