# 04 — Inventario completo de elementos (167 IDs)

Fuente: `class-mfn-builder-fields.php` — `set_items()` L6507 (**149 elementos**) y
`get_inline_shortcode()` L65386 (**24 shortcodes inline**). 6 IDs existen en ambos
(`blockquote`, `button`, `code`, `divider`, `heading`, `image`): **como item del builder manda la
definición de `set_items()`** (la inline es una versión mínima para el editor de texto).

Todos los items reciben además la pestaña **Advanced** completa (doc 03 §1). Aquí se listan solo
los campos PROPIOS (los `css_*` propios se resumen; formato siempre `{selector,style,val}` — copiar
selector/style del PHP). `L` = línea en `class-mfn-builder-fields.php`.

## 1. Contenido y tipografía

| ID | L | Campos propios clave |
|---|---|---|
| `heading` | 40008 | `title` (texto visible, admite `<br>`, `<b>`), `header_tag` (h1–h6), `link`, `target`, `link_title`, `onclick`. CSS: `css_txt_align`, `css_color(_hover)`, `css_typography`, `css_text_shadow`, `css_line_clamp`, `css_bg_img(_pos)`, `css_stroke_width/_color` |
| `column` (Column Text) | 36303 | `content` (HTML limpio), `title`. CSS: `css_column_attr_text_align`, `css_column_attr_color`, `css_column_attra_color(_hover)` (links), `css_column_attr_text_shadow`, `css_column_attr_typography`. Deprecated (no usar): `align`, `align-mobile`, `column_bg`, `bg_image`, `bg_position`, `bg_size`, `margin_bottom`, `padding`, `class`, `style` |
| `visual` (Visual Editor) | 65028 | `content` (editor WP; aplica `be_dynamic_data()` + `do_shortcode()`) |
| `plain_text` | 50712 | `content`, `shortcodes_parser` (`"1"` para ejecutar shortcodes) |
| `blockquote` | 29151 | `content`, `icon`, `author`, `icon_author`, `link`, `target`, `link_title` |
| `button` | 33496 | `title`, `link`, `target`, `link_title`, `icon`, `icon_position`, `size`, `full_width`, `button_style`, `button_function` (+`_copy_to_clipboard(_tooltip/_copied_tooltip)`, `_read_more_title/_icon`, `_go_to`, `_popupid`), `button_id`, `download`, `rel`, `onclick`, `align`. CSS: `css__text_align`, `css_button_justify_content/_padding/_gap/_typography`, `css_button_border_style/_width/_radius`, `css_button_box_shadow`, `css_button_color/_icon_color/_icon_size/_border_color/_background_color/_gradient/_transition` + familia `*_hover` |
| `image` | 43714 | `src`, `size`, `stretch`, `lazy_load`, `link_type`, `popup_id`, `link_image`, `link`, `rel`, `target`, `link_title`, `hover`, `onclick`, `alt`, `caption`, `mask_shape_type/_size/_position`, `align`, `width`, `height`, `image_height(_style)`, `greyscale`, `product_badge_onsale_position`. CSS: `css_image_frame_width`, `css_image_cover_height`, `css_image_border_*`, `css_image_caption_*` |
| `image_gallery` | 44728 | `ids` (upload_multi CSV), `size`, `style`, `layout`, `columns`, `greyscale`, `image_height`, `image_caption_style` |
| `code` | 36252 | `content` (ace) |
| `html` | 42093 | `content` (ace) |
| `content` (Content WP) | 36803 | sin campos (vuelca el contenido del post) |
| `fancy_heading` | 38274 | `title`, `h1`, `content`, `style`, `icon`, `slogan` |
| `readmore` | 55034 | alias de `button`, sin campos propios |

## 2. Cajas (boxes)

| ID | L | Campos propios clave |
|---|---|---|
| `banner_box` | 27071 | (el más grande: 117 campos) `style`, `image`, `size`, `overlay`, `hover_effect`, `title(_tag)`, `subtitle(_tag)`, `bb_excerpt`, `cta`, `cta_icon`, `cta_image`, `cta_hover_effect`, `link_type`, `popup_id`, `link`, `target`, `order`, `hidden_elements_mobile`, `bb_badge(_pos)`, `image_height` |
| `article_box` | 26634 | `image`, `slogan`, `title(_tag)`, `link`, `target`, `link_title` |
| `flat_box` | 39667 | `image`, `title(_tag)`, `content`, `icon`, `icon_image`, `link`, `target`, `link_title`, `background` |
| `feature_box` | 39082 | `image`, `title(_tag)`, `content`, `link_type`, `popup_id`, `link`, `target`, `link_title`, `background` |
| `photo_box` | 50392 | `title(_tag)`, `image`, `content`, `link`, `target`, `link_title`, `greyscale`, `align` |
| `promo_box` | 54468 | `image`, `title(_tag)`, `content`, `btn_text`, `btn_link`, `target`, `link_title`, `position`, `border` |
| `story_box` | 59540 | `image`, `style`, `title(_tag)`, `content`, `link`, `target`, `link_title` |
| `sliding_box` | 59335 | `image`, `title(_tag)`, `link`, `target`, `link_title` |
| `trailer_box` | 63295 | `image`, `orientation`, `slogan`, `title(_tag)`, `link_type`, `popup_id`, `link`, `target`, `link_title`, `style` |
| `hover_box` | 40611 | `image`, `image_hover`, `link_type`, `popup_id`, `link`, `target`, `link_title` |
| `zoom_box` | 65080 | `image`, `content_image`, `content`, `link_type`, `popup_id`, `link`, `target`, `link_title`, `bg_color` |
| `before_after` | 29003 | `image_before`, `image_after`, `size`, `label_before`, `label_after` |
| `icon_2` (Icon) | 42138 | `icon`, `link_type`, `popup_id`, `link`, `target`, `link_title`, `hover` |
| `icon_box_2` (Icon Box) | 42434 | `title(_tag)`, `content`, `icon`, `icon_position`, `icon_align`, `image`, `label`, `link_type` (+`_read_more_title/_icon`), `popup_id`, `link`, `target`, `link_title`, `hover` |
| `icon_box` (Icon Box Basic) | 43233 | `title(_tag)`, `content`, `icon`, `icon_position`, `image`, `link`, `target`, `link_title`, `border` |
| `counter` | 37675 | `title(_tag)`, `icon`, `image`, `prefix`, `number`, `label`, `duration`, `thousands_separator`, `type` (`"vertical"`…), `color` |
| `quick_fact` | 55042 | `heading(_tag)`, `title(_tag)`, `content`, `number`, `prefix`, `label`, `align` |
| `chart` | 35295 | `title(_tag)`, `percent`, `label`, `icon`, `image`, `color`, `line_width` |
| `progress_bars` | 54118 | `title(_tag)`, `tabs`, `content` |
| `countdown_2` | 36836 | `date`, `timezone`, `show`, `align`, `separator(_sign)`, `mobile_orientation/_align/_separator`, `order` |
| `countdown` (Basic) | 37357 | `date`, `title_tag`, `timezone`, `show` |
| `spacer` | 26030 | solo altura vía CSS propio |
| `placeholder` | 26007 | interno (sin Advanced) |

## 3. Bloques (blocks)

| ID | L | Campos propios clave |
|---|---|---|
| `accordion` | 26074 | `title(_tag)`, `tabs` (título+contenido por panel), `icon`, `icon_active`, `open1st`, `openAll`, `style` |
| `faq` | 38611 | `title(_tag)`, `tabs`, `open1st`, `openAll`, `style` |
| `toggle` | 62082 | `tabs`, `tag`, `type`, `starting`, `divider`, `open_first`, `open_all`, `open_more`, `icon`, `active_icon`, `icon_animation` (72 css propios) |
| `tabs` | 59868 | `title(_tag)`, `tabs`, `type` (horizontal/vertical), `padding` |
| `list_2` (List) | 45353 | `tabs`, `type`, `starting`, `align`, `valign`, `divider`, `icon`, `image`, `background_switcher` |
| `list` (List Basic) | 45874 | `icon`, `image`, `title(_tag)`, `content`, `style`, `link`, `target` |
| `helper` | 40281 | `title(_tag)`, `title1/content1/link1/target1/class1`, `title2/…`, `link_type(_2)`, `popup_id(_2)` |
| `table_of_contents` | 61523 | `title(_tag)`, `tags_anchors`, `marker_view`, `icon`, `url_format`, `allow_hide`, `text_show`, `text_hide` |
| `slider` | 58759 | `category`, `orderby`, `order`, `style`, `title_tag`, `navigation` (post type Slides) |
| `tag_cloud` | 60294 | `category`, `reference`, `orderby`, `order`, `design` |

## 4. Elementos (elements)

| ID | L | Campos propios clave |
|---|---|---|
| `call_to_action` | 34127 | `title(_tag)`, `icon`, `content`, `link_type`, `popup_id`, `button_title`, `link`, `target`, `link_title` |
| `contact_box` | 36556 | `title(_tag)`, `address`, `telephone(_2)`, `fax`, `email`, `www`, `image` |
| `feature_list` | 39401 | `tabs`, `content`, `columns` |
| `fancy_divider` | 38196 | `style`, `color_top`, `color_bottom` |
| `hover_color` | 40722 | `content`, `link_type`, `popup_id`, `link`, `target`, `link_title`, `align`, `padding`, `background(_hover)`, `border(_hover)`, `border_width`, `style` |
| `how_it_works` | 41090 | `title(_tag)`, `image`, `number`, `content`, `border`, `style`, `link`, `target`, `link_title` |
| `hotspot` | 41527 | `image`, `marker_animation`, `content_animation`, `style`, `hotspots` (repetidor especial), `img_height(_style)` |
| `info_box` | 45119 | `title(_tag)`, `tabs`, `content`, `image` |
| `map` (Advanced) | 46337 | `lat`, `lng`, `latlng`, `info_window`, `zoom`, `type`, `controls`, `draggable`, `border`, `icon`, `color`, `styles`, `tabs`, `title`, `content`, `telephone`, `email`, `www`, `style`, `height` |
| `map_basic` | 46247 | `iframe`, `address`, `zoom`, `height` |
| `opening_hours` | 47809 | `title(_tag)`, `tabs`, `content`, `image` |
| `our_team` | 48288 | `heading(_tag)`, `image`, `title(_tag)`, `subtitle`, `phone`, `content`, `email`, `facebook`, `twitter`, `linkedin`, `vcard`, `blockquote`, `style`, `link_type`, `popup_id`, `link`, `target`, `link_title` |
| `our_team_list` | 49154 | como `our_team` sin `heading`/`style` |
| `lottie` | 49907 | `source_switcher` (`file`/`url`), `file`, `src`, `trigger`, `loop`, `speed`, `viewport`, `frame_start/_end`, `direction`, `link` |
| `share` | 55530 | `copy_link(_icon/_label)`, `facebook(_icon/_label)`, `twitter(_icon/_label)`, `linkedin(_icon/_label)` |
| `timeline` | 61785 | `tabs` |
| `video` | 63602 | `video` (ID YouTube/Vimeo; **`""` obligatorio para HTML5**, default `n7-F-FMzM7Q` — trampa 25), `parameters`, `mp4` (`URL#ID`), `ogv`, `placeholder` (poster, `URL#ID`), `html5_parameters` (código, p. ej. `a;;l;m;i`), `object_fit`, `object_position`, `mask_shape_type/_size/_position` |
| `divider_2` | 25416 | `type`, `align`, `addon`, `label`, `image`, `icon` |
| `divider` (legacy) | 25905 | `height`, `style`, `line`, `color`, `themecolor` |
| `breadcrumbs` | 33306 | `separator`, `breadcrumb_home` |
| `livesearch` | 46168 | `min_characters`, `container_height`, `featured_image` (uno por página) |

## 5. Loops (contenido dinámico)

| ID | L | Campos propios clave |
|---|---|---|
| `blog` | 29555 | (108 campos) `count`, `style`, `columns`, `title_tag`, `images`, `category(_multi)`, `orderby`, `order`, `sticky_posts`, `exclude_id`, `related`, `filters`, `excerpt`, `more`, `pagination`, `load_more`, `greyscale`, `margin`, `events` |
| `blog_news` | 31150 | `title(_tag)`, `items_title_tag`, `featured_title_tag`, `count`, `style`, `category(_multi)`, `orderby`, `order`, `sticky_posts`, `excerpt`, `link` |
| `blog_slider` | 31772 | `style`, `title(_tag)`, `count`, `category(_multi)`, `orderby`, `order`, `sticky_posts`, `one_post_per_slide`, `excerpt`, `more`, `navigation` |
| `blog_teaser` | 32825 | `title`, `heading_tag`, `title_tag`, `category(_multi)`, `orderby`, `order`, `sticky_posts`, `margin` |
| `portfolio` | 50826 | (93 campos) `title_tag`, `count`, `style`, `columns`, `category(_multi)`, `orderby`, `order`, `portfolio-link`, `exclude_id`, `related`, `filters`, `pagination`, `load_more`, `excerpt_hide`, `greyscale` |
| `portfolio_grid` | 52135 | `count`, `category(_multi)`, `orderby`, `order`, `greyscale` |
| `portfolio_photo` | 52509 | `title_tag`, `count`, `category(_multi)`, `orderby`, `order`, `target`, `greyscale`, `margin` |
| `portfolio_slider` | 52928 | `count`, `category(_multi)`, `orderby`, `order`, `arrows`, `size`, `scroll` |
| `clients` | 35525 | `in_row`, `style`, `size`, `category`, `orderby`, `order`, `greyscale` |
| `clients_slider` | 35777 | `title(_tag)`, `category`, `orderby`, `order`, `per_slide`, `scroll`, `navigation` |
| `testimonials` | 60575 | `title_tag`, `category`, `orderby`, `order`, `style`, `hide_photos` |
| `testimonials_list` | 61176 | `title_tag`, `category`, `orderby`, `order`, `style` |
| `offer` | 46803 | `category`, `align` |
| `offer_thumb` | 47304 | `category`, `style`, `align` |
| `pricing_item` | 53140 | `image`, `title(_tag)`, `price`, `currency`, `currency_pos`, `period`, `subtitle`, `content`, `tabs`, `link_type`, `popup_id`, `icon`, `link`, `target`, `link_title`, `style`, `featured` |

## 6. WooCommerce

| ID | L | Campos propios clave |
|---|---|---|
| `shop` | 56580 | `limit`, `columns`, `type`, `category`, `orderby`, `order`, `paginate`, `load_more`, `product_badge_onsale_position` |
| `shop_slider` | 57573 | `title(_tag)`, `count`, `show`, `out_of_stock`, `add_to_cart_button`, `category`, `orderby`, `order` |
| `shop_products` | 18492 | (107 campos) `products`, `layout`, `ordering`, `description`, `button`, `title_tag`, `equal_heights`, `load_more`, `shop-list-*`, `order`, `product_badge_onsale_position` |
| `shop_categories` | 56153 | `columns`, `display`, `category`, `subcategory`, `empty`, `image`, `title`, `count`, `title_tag`, `order` |
| `shop_title` | 19973 | `title_tag` |
| `shop_cat_desc` / `shop_cat_top_desc` / `shop_cat_bottom_desc` | 20074+ | alias de `plain_text` |
| `product_title` | 20292 | `title_tag` |
| `product_images` | 20392 | `zoom`, `thumbnail_arrows`, `product_badge_onsale_position` |
| `product_price` | 20943 | — |
| `product_cart_button` | 21058 | `cart_button_text`, `variations-label` |
| `product_breadcrumbs` | 21562 | `breadcrumb_delimiter`, `breadcrumb_home` |
| `product_reviews` | 21698 | 30 css propios |
| `product_rating` / `product_stock` / `product_short_description` | 22173+ | — |
| `product_meta` | 22361 | `layout` |
| `product_tabs` | 22645 | `nav` (29 css propios) |
| `product_content` | 23098 | `content` |
| `product_additional_information` | 23153 | `title(_tag)` |
| `product_related` / `product_upsells` | 23343 / 24393 | `heading_tag`, `products`, `columns`, `button`, `description`, `order`, `title_tag` |
| `cart_table` | 8575 | `update_cart_label`, `coupon_code_placeholder`, `apply_coupon_label`, `background_switcher_inactive` |
| `cart_totals` | 9370 | `cart_totals_heading`, `proceed_checkout_label`, `continue_shopping_string` |
| `cart_cross_sells` | 9923 | `heading(_tag)`, `columns`, `products`, `button`, `description`, `title_tag`, `order` |
| `checkout` | 7407 | `layout` (81 css propios) |
| `order_steps` | 10718 | `cart_label`, `checkout_label`, `order_label` |
| `thankyou_overview` | 6513 | solo css propios |
| `thankyou_order` | 6830 | solo css propios |
| `woo_alert` | 20109 | solo css (no se renderiza sin notices fuera del builder) |

## 7. Header / Footer / Menús / Templates

| ID | L | Campos propios clave |
|---|---|---|
| `header_logo` | 14263 | `image`, `link` |
| `header_menu` | 14334 | `menu_display`, `animation`, `separator`, `submenu_display`, `submenu_icon_*`, `icon_align/_animation`, `dropdown_pointer/_alignment` |
| `header_burger` | 15570 | (111 campos) `icon`, `image`, `desc`, `link_title`, `sidebar_type`, `menu_display`, `menu_pos`, `animation`, `icon_position/_align`, `items_align`… |
| `header_icon` | 17216 | `type`, `icon`, `image`, `desc`, `cart_total`, `count(_if_zero)`, `link`, `target`, `icon_count_posv/_posh` |
| `header_search` | 18041 | `placeholder`, `icon` |
| `header_promo_bar` | 18342 | `tabs`, `slider_speed` |
| `header_language_switcher` | 63950 | `style`, `flags`, `dropdown_icon(_html/_image)` |
| `header_currency_switcher` | 64378 | `style`, `flags`, `dropdown_icon(_html)` |
| `footer_logo` | 12971 | `image`, `link` |
| `footer_menu` | 13026 | `menu_display`, `menu_style` |
| `megamenu_menu` | 13214 | `menu_display`, `menu_style`, `submenu_on`, `submenu_hori_on`, `icon_align/_animation`, `submenu(_animation)`, `submenu_icon(_animation)`, `decoration_icon` |
| `sidemenu_menu` | 11309 | `tabs`, `submenu(_on)`, `submenu_icon(_display/_animation)` (84 css propios) |
| `popup_exit` | 12733 | `label`, `icon`, `image` |
| `sidebar_widget` | 58709 | `sidebar` |
| `slider_plugin` | 59264 | `rev` (Revolution), `layer` (LayerSlider) |
| `payment_methods` | 50113 | `dynamic_items` (repetidor de logos), `greyscale`, `invert` |

## 8. Archive / Single post (templates dinámicos, mayoría alias)

`archive_heading` (→heading), `archive_image` (→image), `archive_read_more` (→button),
`archive_content` (→plain_text), `archive_blog_categories` / `archive_portfolio_categories` (→tag_cloud),
`post_heading`, `post_image`, `post_author` / `post_date` (→icon_box_2), `post_blog_related` (→blog),
`post_portfolio_related` (→portfolio), `post_blog_categories` / `post_portfolio_categories` /
`post_blog_tags` (→tag_cloud), `post_excerpt` (→plain_text), `post_love`, `post_comments`,
`post_content` (L11079–11255). Los alias usan los campos del tipo base.

## 9. Shortcodes inline (24) — para dentro de campos de texto

`alert`, `blockquote`, `button`, `code`, `content_link`, `countdown_inline`, `counter_inline`,
`divider`, `dropcap`, `fancy_link`, `google_font`, `heading` (usa `tag`/`content`/`align`/`color`/`style`/`color2` —
**NO confundir con el item `heading` del builder** que usa `title`/`header_tag`), `highlight`, `hr`,
`icon`, `icon_bar`, `icon_block`, `idea`, `image`, `popup`, `progress_icons`, `tooltip`,
`tooltip_image`, `lorem` (L65390–66714).

Se usan como shortcodes `[sc_xxx ...]` dentro de `content` de column/plain_text/visual, no como items.
