#!/usr/bin/env python3
"""
Extract all builder elements and their attributes from class-mfn-builder-fields.php
Outputs JSON and can generate markdown docs.
"""
import re
import json
import sys
from pathlib import Path

FIELDS_FILE = Path(__file__).parent / "class-mfn-builder-fields.php"
OUTPUT_JSON = Path(__file__).resolve().parents[3] / "builder-elements" / "_elements.json"


def extract_php_string(s):
    """Extract string from __('...', 'mfn-opts') or '...' """
    if not s:
        return ""
    s = s.strip()
    # __('Title', 'mfn-opts') -> Title
    m = re.search(r"__\(\s*['\"]([^'\"]*)['\"]", s)
    if m:
        return m.group(1)
    # 'key' => 'value' or "key" => "value"
    m = re.search(r"['\"]([^'\"]*)['\"]\s*\)", s)
    if m:
        return m.group(1)
    m = re.search(r"=>\s*['\"]([^'\"]*)['\"]", s)
    if m:
        return m.group(1)
    return s


def parse_options_block(lines, start_idx):
    """Parse options array( 'a' => 'A', 'b' => 'B' ) return dict."""
    opts = {}
    depth = 0
    i = start_idx
    while i < len(lines):
        line = lines[i]
        if 'array(' in line or '[' in line:
            depth += line.count('array(') + line.count('[') - line.count(')') - line.count(']')
        if ')' in line or ']' in line:
            depth -= line.count(')') + line.count(']') - line.count('array(') - line.count('[')
        # Match 'key' => 'value' or 'key' => __('Val', ...)
        m = re.search(r"['\"]([a-z0-9_\.\-]+)['\"]\s*=>\s*(?:__\(['\"]([^'\"]*)['\"]|['\"]([^'\"]*)['\"]|(\d+))", line)
        if m:
            key = m.group(1)
            val = m.group(2) or m.group(3) or m.group(4) or ""
            opts[key] = val
        if depth <= 0 and (line.strip() == '),' or line.strip() == '],' or (line.strip().startswith(')') and 'array(' not in line)):
            break
        i += 1
    return opts, i


def parse_single_attr(lines, start_idx):
    """Parse one array( 'id' => ..., 'type' => ..., ... ) return dict and end index."""
    attr = {}
    depth = 0
    i = start_idx
    in_options = False
    options_start = 0
    while i < len(lines):
        line = lines[i]
        # Track nesting
        if 'array(' in line:
            depth += 1
        if ')' in line and 'array(' not in line:
            depth -= 1
        if '[' in line and '=>' in line:
            depth += 1
        if ']' in line:
            depth -= 1

        # 'id' => 'value'
        m = re.search(r"['\"]?(id|attr_id|old_id)['\"]?\s*=>\s*['\"]([^'\"]*)['\"]", line)
        if m and 'id' not in attr:
            attr['id'] = m.group(2)
        m = re.search(r"['\"]?type['\"]?\s*=>\s*['\"]([^'\"]*)['\"]", line)
        if m:
            attr['type'] = m.group(1)
        m = re.search(r"['\"]?title['\"]?\s*=>\s*(?:__\(['\"]([^'\"]*)['\"]|['\"]([^'\"]*)['\"])\s*", line)
        if m:
            attr['title'] = (m.group(1) or m.group(2) or "").strip()
        m = re.search(r"['\"]?desc['\"]?\s*=>\s*__\(['\"]([^'\"]*)['\"]", line)
        if m:
            attr['desc'] = m.group(1)
        m = re.search(r"['\"]?std['\"]?\s*=>\s*(?:['\"]([^'\"]*)['\"]|(\d+)|(\[\])|\]\s*\))", line)
        if m:
            attr['std'] = m.group(1) or m.group(2) or (m.group(3) if m.group(3) else "")
        if "'options' =>" in line or '"options" =>' in line:
            in_options = True
            options_start = i
        if in_options and depth <= 1 and (line.strip() == '),' or line.strip() == '],'):
            opts, _ = parse_options_block(lines, options_start)
            attr['options'] = opts
            in_options = False

        if depth == 0 and line.strip().startswith('),') and i > start_idx:
            break
        i += 1
    return attr, i


# Known builder element keys (main set_items + inline shortcodes)
ITEM_KEYS = {
    'accordion', 'alert', 'archive_blog_categories', 'archive_content', 'archive_heading',
    'archive_image', 'archive_portfolio_categories', 'archive_read_more', 'article_box',
    'banner_box', 'before_after', 'blockquote', 'blog', 'blog_news', 'blog_slider', 'blog_teaser',
    'breadcrumbs', 'button', 'call_to_action', 'cart_cross_sells', 'cart_table', 'cart_totals',
    'cf7', 'chart', 'checkout', 'clients', 'clients_slider', 'code', 'column', 'contact_box',
    'content', 'content_link', 'countdown', 'countdown_2', 'countdown_inline', 'counter',
    'counter_inline', 'divider', 'divider_2', 'dropcap', 'fancy_divider', 'fancy_heading',
    'fancy_link', 'faq', 'feature_box', 'feature_list', 'flat_box', 'footer_logo', 'footer_menu',
    'google_font', 'header_burger', 'header_currency_switcher', 'header_icon', 'header_language_switcher',
    'header_logo', 'header_menu', 'header_promo_bar', 'header_search', 'heading', 'helper',
    'highlight', 'hotspot', 'hover_box', 'hover_color', 'how_it_works', 'hr', 'html', 'icon',
    'icon_2', 'icon_bar', 'icon_block', 'icon_box', 'icon_box_2', 'idea', 'image', 'image_gallery',
    'info_box', 'list', 'list_2', 'livesearch', 'lorem', 'lottie', 'map', 'map_basic', 'megamenu_menu',
    'offer', 'offer_thumb', 'opening_hours', 'order_steps', 'our_team', 'our_team_list', 'payment_methods',
    'photo_box', 'placeholder', 'plain_text', 'popup', 'popup_exit', 'portfolio', 'portfolio_grid',
    'portfolio_photo', 'portfolio_slider', 'post_author', 'post_blog_categories', 'post_blog_related',
    'post_blog_tags', 'post_comments', 'post_content', 'post_date', 'post_excerpt', 'post_heading',
    'post_image', 'post_love', 'post_portfolio_categories', 'post_portfolio_related', 'pricing_item',
    'product_additional_information', 'product_breadcrumbs', 'product_cart_button', 'product_content',
    'product_images', 'product_meta', 'product_price', 'product_rating', 'product_related',
    'product_reviews', 'product_short_description', 'product_stock', 'product_tabs', 'product_title',
    'product_upsells', 'progress_bars', 'progress_icons', 'promo_box', 'quick_fact', 'readmore',
    'share', 'shop', 'shop_cat_bottom_desc', 'shop_cat_desc', 'shop_cat_top_desc', 'shop_products',
    'shop_slider', 'shop_title', 'shop_categories', 'sidebar_widget', 'sidemenu_menu', 'slider',
    'slider_plugin', 'sliding_box', 'spacer', 'story_box', 'table_of_contents', 'tabs', 'tag_cloud',
    'testimonials', 'testimonials_list', 'thankyou_order', 'thankyou_overview', 'timeline', 'toggle',
    'tooltip', 'tooltip_image', 'trailer_box', 'video', 'visual', 'woo_alert', 'zoom_box',
}


def find_item_blocks(content):
    """Find all top-level item definitions: 'itemname' => array( ... ). Returns list of (name, start_line, end_line)."""
    lines = content.split('\n')
    item_start = re.compile(r"^(\s+)['\"]([a-z0-9_]+)['\"]\s*=>\s*array\s*\(")
    blocks = []
    i = 0
    while i < len(lines):
        m = item_start.search(lines[i])
        if m:
            indent = m.group(1)
            name = m.group(2)
            if name not in ITEM_KEYS:
                i += 1
                continue
            start = i
            close_pat = re.compile(r"^" + re.escape(indent) + r"\),\s*$")
            i += 1
            while i < len(lines):
                if close_pat.match(lines[i]):
                    i += 1
                    break
                i += 1
            blocks.append((name, start, i))
        else:
            i += 1
    return blocks, lines


def parse_attr_block(lines, attr_start, attr_end):
    """Parse a single attribute array in range [attr_start, attr_end). Return dict with id, type, title, options, std, desc."""
    attr = {}
    id_candidates = {}
    for i in range(attr_start, attr_end):
        line = lines[i]
        for key in ("id", "attr_id", "old_id"):
            m = re.search(r"['\"]?" + key + r"['\"]?\s*=>\s*['\"]([^'\"]*)['\"]", line)
            if m:
                id_candidates[key] = m.group(1)
                break
    if id_candidates:
        attr["id"] = id_candidates.get("id") or id_candidates.get("attr_id") or id_candidates.get("old_id")
    for i in range(attr_start, attr_end):
        line = lines[i]
        m = re.search(r"['\"]?type['\"]?\s*=>\s*['\"]([^'\"]*)['\"]", line)
        if m:
            attr["type"] = m.group(1)
        m = re.search(r"['\"]?title['\"]?\s*=>\s*__\(\s*['\"]([^'\"]*)['\"]", line)
        if m:
            attr["title"] = m.group(1)
        m = re.search(r"['\"]?desc['\"]?\s*=>\s*__\(\s*['\"]([^'\"]*)['\"]", line)
        if m:
            attr["desc"] = m.group(1)
        m = re.search(r"['\"]?std['\"]?\s*=>\s*['\"]?([^'\",)\]]+)['\"]?", line)
        if m:
            attr["std"] = m.group(1).strip()
        if "'options' =>" in line or '"options" =>' in line:
            # Parse next lines for key => value until ),
            opts = {}
            j = i + 1
            while j < attr_end:
                ol = lines[j]
                if re.match(r"\s*\),\s*$", ol) or re.match(r"\s*\],\s*$", ol):
                    break
                om = re.search(r"['\"]([a-z0-9_\.\-]+)['\"]\s*=>\s*(?:__\(\s*['\"]([^'\"]*)['\"]|['\"]([^'\"]*)['\"]|(\d+))", ol)
                if om:
                    opts[om.group(1)] = om.group(2) or om.group(3) or om.group(4) or ""
                j += 1
            if opts:
                attr["options"] = opts
    return attr


def extract_attrs_from_block(lines, start, end):
    """Within a block, find 'attr' => array( and parse each direct child array( by indent."""
    attrs = []
    i = start
    while i < end:
        line = lines[i]
        if re.search(r"['\"]?(attr|fields)['\"]?\s*=>\s*array\s*\(", line):
            i += 1
            # Find indent of first attribute array
            while i < end and not re.search(r"^\s*array\s*\(", lines[i]):
                i += 1
            if i >= end:
                break
            attr_indent = re.match(r"^(\s+)", lines[i])
            attr_indent = attr_indent.group(1) if attr_indent else ""
            while i < end:
                line = lines[i]
                if re.search(r"^\s*array\s*\(", line):
                    block_start = i
                    # Find closing ), at same indent
                    i += 1
                    while i < end:
                        if re.match(r"^" + re.escape(attr_indent) + r"\),\s*$", lines[i]):
                            i += 1
                            break
                        i += 1
                    attr = parse_attr_block(lines, block_start, i - 1)
                    if attr.get("id") or attr.get("type") in ("header", "subheader", "html", "info"):
                        attrs.append(attr)
                else:
                    i += 1
            break
        i += 1
    return attrs


def extract_element_meta(lines, start, end):
    """Extract type, title, size, cat from element block (only direct children before 'attr')."""
    meta = {}
    # Find indent of element's 'type' => line (first occurrence before 'attr')
    child_indent = None
    for i in range(start + 1, min(end, start + 30)):
        line = lines[i]
        if "'attr' =>" in line or "'fields' =>" in line:
            break
        if "'type' =>" in line:
            m = re.match(r"^(\s+)", line)
            if m:
                child_indent = m.group(1)
                break
    if not child_indent:
        child_indent = "\t"
    for i in range(start + 1, min(end, start + 25)):
        line = lines[i]
        if "'attr' =>" in line or "'fields' =>" in line:
            break
        if not line.startswith(child_indent):
            continue
        m = re.search(r"['\"]?(type|title|size|tablet_size|mobile_size|cat|tablet_resized)['\"]?\s*=>", line)
        if m:
            key = m.group(1)
            val_m = re.search(r"__\(\s*['\"]([^'\"]*)['\"]", line)
            if val_m:
                val = val_m.group(1)
            else:
                val_m = re.search(r"=>\s*['\"]([^'\"]*)['\"]", line)
                val = val_m.group(1) if val_m else ""
            meta[key] = val
    return meta


def main():
    content = FIELDS_FILE.read_text(encoding='utf-8', errors='replace')
    lines = content.split('\n')
    set_items_start = content.find("private function set_items()")
    if set_items_start == -1:
        set_items_start = content.find("$this->items = array(")
    get_inline_start = content.find("$shortcode_inline = array(")
    if set_items_start == -1:
        print("Could not find set_items")
        sys.exit(1)

    # Build line ranges: main items start at first line of set_items content
    set_items_line = content[:set_items_start].count('\n')
    inline_line = content[:get_inline_start].count('\n') if get_inline_start > 0 else len(lines)

    all_elements = {}
    blocks, _ = find_item_blocks(content)
    for name, start, end in blocks:
        if end - start < 5:
            continue
        meta = extract_element_meta(lines, start, end)
        attrs = extract_attrs_from_block(lines, start, end)
        # Prefer main builder definition (has size, cat) over inline if both exist
        if name not in all_elements or (meta.get('size') or meta.get('cat')):
            all_elements[name] = {
                'type': meta.get('type', name),
                'title': meta.get('title', name),
                'size': meta.get('size', ''),
                'tablet_size': meta.get('tablet_size', ''),
                'mobile_size': meta.get('mobile_size', ''),
                'tablet_resized': meta.get('tablet_resized', ''),
                'cat': meta.get('cat', ''),
                'attr': attrs,
            }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(all_elements, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Extracted {len(all_elements)} elements to {OUTPUT_JSON}")

    # Generate markdown docs for each element
    md_dir = OUTPUT_JSON.parent
    for name, data in all_elements.items():
        md_path = md_dir / f"{name}.md"
        lines = [
            f"# {data.get('title', name.replace('_', ' ').title())}",
            "",
            "## Element properties",
            "",
            "| Property | Value |",
            "|----------|--------|",
            f"| **Type** | `{data.get('type', name)}` |",
            f"| **Title** | {data.get('title', '')} |",
            f"| **Category** | `{data.get('cat', '')}` |",
            f"| **Size** | {data.get('size', '')} (desktop), {data.get('tablet_size', '')} (tablet), {data.get('mobile_size', '')} (mobile) |",
            f"| **Tablet resized** | {data.get('tablet_resized', '')} |",
            "",
            "## Attributes",
            "",
        ]
        for a in data.get("attr", []):
            aid = a.get("id", a.get("type", "-"))
            atype = a.get("type", "")
            atitle = a.get("title", "")
            adesc = a.get("desc", "")
            astd = a.get("std", "")
            opts = a.get("options", {})
            if atype in ("html", "header", "subheader", "info") and not aid:
                lines.append(f"### {atitle or atype}")
            else:
                lines.append(f"### `{aid}`")
            lines.append(f"- **Type**: `{atype}`")
            if atitle:
                lines.append(f"- **Title**: {atitle}")
            if opts:
                lines.append(f"- **Options**: {', '.join(f'`{k}` ({v})' for k, v in list(opts.items())[:20])}")
            if astd:
                lines.append(f"- **Default**: `{astd}`")
            if adesc:
                lines.append(f"- **Description**: {adesc}")
            lines.append("")
        # Usage example (structure)
        example_attr = {a.get("id"): a.get("std", "") for a in data.get("attr", []) if a.get("id")}
        lines.append("## Structure (JSON)")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps({"type": data.get("type", name), "attr": example_attr}, indent=2))
        lines.append("```")
        md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {len(all_elements)} markdown files in {md_dir}")
    return all_elements


if __name__ == "__main__":
    main()
