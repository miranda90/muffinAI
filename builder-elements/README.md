# Muffin Builder Elements Documentation

> ✅ **REGENERADO (2026-07)**: Las 167 fichas `.md` y `_elements.json` se regeneraron ejecutando el
> PHP real del theme (no regex): `_generator/extract.php` (stubs de WordPress + `Mfn_Builder_Fields`)
> → `_generator/generate_fichas.py`. Para regenerar tras una actualización del theme:
>
> ```bash
> cd builder-elements/_generator && php extract.php && python3 generate_fichas.py
> ```
>
> El antiguo `extract_builder_elements.py` (parser regex roto) queda obsoleto — no usarlo.
> Documentación conceptual (arquitectura, pipeline CSS, reglas): `docs/bebuilder/00-INDICE.md`.

This directory contains documentation for all Muffin Builder elements available in the BeTheme visual constructor.

**Contenido:**
- `<elemento>.md` — 149 items del builder (los 6 con variante inline la documentan en sección aparte) + 18 shortcodes solo-inline. Los alias (`archive_*`, `post_*`, `shop_cat_*`, `readmore`) remiten a su tipo base.
- `_advanced.md` — pestaña Advanced común a TODOS los items (margins, paddings, fondos, bordes, posición, visibilidad, animación, `classes`, `custom_id`).
- `_section.md` / `_wrap.md` — campos de sección y de wrap (grid, query loop, sticky...).
- `_elements.json` — volcado íntegro y fiel de todas las definiciones (items, inline, section, wrap, advanced).

**Source**: Attributes and structure are extracted from `betheme/functions/builder/class-mfn-builder-fields.php` executing the real PHP (see regeneration command above). This covers the main builder items (`set_items`, 149), inline shortcode elements (`get_inline_shortcode`, 24; 6 overlap) — **167 unique elements** — plus section/wrap/advanced shared fields.

## Structure

Each element has its own markdown file with the following information:
- Element name and description
- All available attributes and their types
- Default values
- Usage examples
- Categories and placement restrictions

When you generically work with **builder structures** (JSON/arrays for `mfn-page-items`) there are three levels:

- **Sections**: array of sections, each with `uid`, `attr` y `wraps`. En `attr` incluir **`width_switcher`**: `"full"` para ancho completo; si falta, la UI del builder muestra "default" y el ancho puede no aplicarse correctamente (no usar solo `style`: `"full-width"`).
- **Wraps**: dentro de cada sección, cada wrap debe incluir siempre `size`, `tablet_size`, `mobile_size`, además de `uid`, `attr` e `items`.  
  Si `size` falta o está vacío, el front de BeTheme hace `return` en `show_wraps()` y **no se renderiza ningún item de ese wrap**.
- **Items**: dentro de cada wrap, cada item tiene `type`, `size` (1/1, 1/2, 1/3, etc.), `tablet_size`, `mobile_size`, `uid` y `attr` con los campos propios del elemento.
- **Heading**: el shortcode `sc_heading` del tema usa **`attr.title`** para el texto visible y **`attr.header_tag`** para la etiqueta (h1, h2, etc.). Si usas `content` y `tag`, el título puede mostrarse vacío; en JSON usa siempre `title` y `header_tag`. Ver [heading.md](./heading.md).

Ten esto en cuenta si en el futuro generas contenido del builder por código o a partir de JSON (como en el caso de la página «Sostenibilidad»).

### Comparación diseño real vs BeBuilder generado

- **[TMC-ABOUT-COMPARISON.md](./TMC-ABOUT-COMPARISON.md)** – Comparación de `examples/example1/about-us.json` con `tmc-about-bebuilder.json` (secciones, wraps anidados, atributos `css_advanced_*`, nombres de campos en heading/column/button, buenas prácticas).

### Guía de maquetaciones (cómo se construyen los layouts en el diseño real)

- **[GUIA-MAQUETACIONES.md](./GUIA-MAQUETACIONES.md)** – Patrones de maquetación extraídos de `examples/example2/home.json` y `examples/example1/about-us.json`: hero con video, barra naranja con grid custom, grid de categorías (query), card CTA sobre imagen, bloque partner + estadísticas (counter), CTA final con overlay en degradado, imagen en posición absoluta, estilos de botón. Incluye checklist para generar JSON fiel al diseño.

## Element Categories

### WooCommerce Elements (28 elements)
- thankyou_overview
- thankyou_order
- checkout
- cart_table
- cart_totals
- cart_cross_sells
- order_steps
- woo_alert
- shop_products
- shop_categories
- shop_title
- product_title
- product_images
- product_price
- product_cart_button
- product_reviews
- product_rating
- product_stock
- product_meta
- product_breadcrumbs
- product_short_description
- product_additional_information
- product_upsells
- product_related
- product_content
- product_tabs
- shop
- shop_slider

### Content Elements (66 elements)
- accordion
- article_box
- before_after
- blockquote
- blog
- blog_news
- blog_slider
- blog_teaser
- call_to_action
- chart
- clients
- clients_slider
- code
- column
- contact_box
- content
- countdown_2
- countdown
- counter
- faq
- feature_box
- feature_list
- flat_box
- heading
- helper
- hover_box
- hover_color
- how_it_works
- icon_2
- icon_box
- icon_box_2
- image
- image_gallery
- info_box
- list_2
- list
- livesearch
- lottie
- payment_methods
- photo_box
- plain_text
- placeholder
- portfolio
- portfolio_grid
- portfolio_photo
- portfolio_slider
- pricing_item
- progress_bars
- promo_box
- quick_fact
- sidebar_widget
- slider
- slider_plugin
- sliding_box
- story_box
- table_of_contents
- tabs
- tag_cloud
- testimonials
- testimonials_list
- timeline
- toggle
- trailer_box
- video
- visual
- zoom_box

### Layout Elements (5 elements)
- divider_2
- divider
- fancy_divider
- fancy_heading
- spacer

### Interactive Elements (6 elements)
- button
- map_basic
- map
- hotspot
- banner_box
- html

### Header Elements (9 elements)
- header_logo
- footer_logo
- header_menu
- header_icon
- header_burger
- header_search
- header_promo_bar
- header_language_switcher
- header_currency_switcher

### Navigation Elements (5 elements)
- sidemenu_menu
- popup_exit
- footer_menu
- megamenu_menu
- breadcrumbs

### Post Elements (3 elements)
- post_comments
- share
- post_content

### Form Elements (1 elements)
- cf7

### Location Elements (3 elements)
- opening_hours
- offer
- offer_thumb

## Complete Element List (132 elements)

- [accordion](./accordion.md)
- [article_box](./article_box.md)
- [banner_box](./banner_box.md)
- [before_after](./before_after.md)
- [blockquote](./blockquote.md)
- [blog](./blog.md)
- [blog_news](./blog_news.md)
- [blog_slider](./blog_slider.md)
- [blog_teaser](./blog_teaser.md)
- [breadcrumbs](./breadcrumbs.md)
- [button](./button.md)
- [call_to_action](./call_to_action.md)
- [cart_cross_sells](./cart_cross_sells.md)
- [cart_table](./cart_table.md)
- [cart_totals](./cart_totals.md)
- [cf7](./cf7.md)
- [chart](./chart.md)
- [checkout](./checkout.md)
- [clients](./clients.md)
- [clients_slider](./clients_slider.md)
- [code](./code.md)
- [column](./column.md)
- [contact_box](./contact_box.md)
- [content](./content.md)
- [countdown](./countdown.md)
- [countdown_2](./countdown_2.md)
- [counter](./counter.md)
- [divider](./divider.md)
- [divider_2](./divider_2.md)
- [fancy_divider](./fancy_divider.md)
- [fancy_heading](./fancy_heading.md)
- [faq](./faq.md)
- [feature_box](./feature_box.md)
- [feature_list](./feature_list.md)
- [flat_box](./flat_box.md)
- [footer_logo](./footer_logo.md)
- [footer_menu](./footer_menu.md)
- [header_burger](./header_burger.md)
- [header_currency_switcher](./header_currency_switcher.md)
- [header_icon](./header_icon.md)
- [header_language_switcher](./header_language_switcher.md)
- [header_logo](./header_logo.md)
- [header_menu](./header_menu.md)
- [header_promo_bar](./header_promo_bar.md)
- [header_search](./header_search.md)
- [heading](./heading.md)
- [helper](./helper.md)
- [hotspot](./hotspot.md)
- [hover_box](./hover_box.md)
- [hover_color](./hover_color.md)
- [how_it_works](./how_it_works.md)
- [html](./html.md)
- [icon_2](./icon_2.md)
- [icon_box](./icon_box.md)
- [icon_box_2](./icon_box_2.md)
- [image](./image.md)
- [image_gallery](./image_gallery.md)
- [info_box](./info_box.md)
- [list](./list.md)
- [list_2](./list_2.md)
- [livesearch](./livesearch.md)
- [lottie](./lottie.md)
- [map](./map.md)
- [map_basic](./map_basic.md)
- [megamenu_menu](./megamenu_menu.md)
- [offer](./offer.md)
- [offer_thumb](./offer_thumb.md)
- [opening_hours](./opening_hours.md)
- [order_steps](./order_steps.md)
- [our_team](./our_team.md)
- [our_team_list](./our_team_list.md)
- [payment_methods](./payment_methods.md)
- [photo_box](./photo_box.md)
- [placeholder](./placeholder.md)
- [plain_text](./plain_text.md)
- [popup_exit](./popup_exit.md)
- [portfolio](./portfolio.md)
- [portfolio_grid](./portfolio_grid.md)
- [portfolio_photo](./portfolio_photo.md)
- [portfolio_slider](./portfolio_slider.md)
- [post_comments](./post_comments.md)
- [post_content](./post_content.md)
- [pricing_item](./pricing_item.md)
- [product_additional_information](./product_additional_information.md)
- [product_breadcrumbs](./product_breadcrumbs.md)
- [product_cart_button](./product_cart_button.md)
- [product_content](./product_content.md)
- [product_images](./product_images.md)
- [product_meta](./product_meta.md)
- [product_price](./product_price.md)
- [product_rating](./product_rating.md)
- [product_related](./product_related.md)
- [product_reviews](./product_reviews.md)
- [product_short_description](./product_short_description.md)
- [product_stock](./product_stock.md)
- [product_tabs](./product_tabs.md)
- [product_title](./product_title.md)
- [product_upsells](./product_upsells.md)
- [progress_bars](./progress_bars.md)
- [promo_box](./promo_box.md)
- [quick_fact](./quick_fact.md)
- [share](./share.md)
- [shop](./shop.md)
- [shop_categories](./shop_categories.md)
- [shop_products](./shop_products.md)
- [shop_slider](./shop_slider.md)
- [shop_title](./shop_title.md)
- [sidebar_widget](./sidebar_widget.md)
- [sidemenu_menu](./sidemenu_menu.md)
- [slider](./slider.md)
- [slider_plugin](./slider_plugin.md)
- [sliding_box](./sliding_box.md)
- [spacer](./spacer.md)
- [story_box](./story_box.md)
- [table_of_contents](./table_of_contents.md)
- [tabs](./tabs.md)
- [tag_cloud](./tag_cloud.md)
- [testimonials](./testimonials.md)
- [testimonials_list](./testimonials_list.md)
- [thankyou_order](./thankyou_order.md)
- [thankyou_overview](./thankyou_overview.md)
- [timeline](./timeline.md)
- [toggle](./toggle.md)
- [trailer_box](./trailer_box.md)
- [video](./video.md)
- [visual](./visual.md)
- [woo_alert](./woo_alert.md)
- [zoom_box](./zoom_box.md)

## Usage

Each element documentation includes:
1. **Description** - What the element does
2. **Element Properties** - Basic configuration
3. **Attributes** - All available options with types and defaults
4. **Usage Examples** - JSON structure examples
5. **Notes** - Special considerations and limitations

## Categories Explained

- **WooCommerce**: Elements specific to e-commerce functionality
- **Content**: General content display elements
- **Layout**: Structural and spacing elements
- **Interactive**: Elements that require user interaction
- **Header**: Elements used in website headers
- **Navigation**: Menu and navigation elements
- **Post**: Blog and post-related elements
- **Form**: Form and input elements
- **Location**: Location and business-specific elements
