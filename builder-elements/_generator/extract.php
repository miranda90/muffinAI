<?php
/**
 * Harness de extracción: ejecuta Mfn_Builder_Fields real con stubs de WordPress
 * y vuelca todas las definiciones de campos a JSON.
 */

error_reporting(E_ERROR | E_PARSE); // silenciar warnings de claves indefinidas

define('ABSPATH', '/tmp/');

$THEME = '/Users/invbit/Documents/Mis proyectos/muffinAI/betheme';

// ---------- Stubs WordPress ----------
function __($s, $d = null) { return $s; }
function _e($s, $d = null) { echo $s; }
function esc_html__($s, $d = null) { return $s; }
function esc_attr__($s, $d = null) { return $s; }
function esc_html($s) { return $s; }
function esc_attr($s) { return $s; }
function apply_filters($tag, $value) { return $value; }
function get_template_directory_uri() { return '{theme_uri}'; }
function get_theme_file_uri($p = '') { return '{theme_uri}' . $p; }
function get_site_option($k, $d = false) { return $d; }
function get_option($k, $d = false) { return $d; }
function get_current_user_id() { return 0; }
function mfn_opts_get($k, $d = null) { return $d; }
function wp_parse_args($args, $defaults) { return array_merge((array)$defaults, (array)$args); }
function get_post_types($a = [], $o = 'names') { return []; }
function get_taxonomies($a = [], $o = 'names') { return []; }
function get_terms($a = []) { return []; }
function get_posts($a = []) { return []; }
function get_categories($a = []) { return []; }
function wp_get_nav_menus() { return []; }
function get_intermediate_image_sizes() { return ['thumbnail','medium','medium_large','large']; }
function did_action($t) { return 0; }
function is_admin() { return true; }
function wp_json_encode($v, $f = 0) { return json_encode($v, $f); }
function sanitize_title($s) { return strtolower(preg_replace('/[^a-z0-9]+/i', '-', $s)); }
function shortcode_exists($s) { return false; }
function get_current_screen() { return null; }
function trailingslashit($s) { return rtrim($s, '/') . '/'; }
function home_url($p = '') { return '{home_url}' . $p; }
function admin_url($p = '') { return '{admin_url}' . $p; }
function wp_upload_dir() { return ['baseurl' => '{uploads}', 'basedir' => '/tmp']; }

// ---------- Extraer funciones mfna_* PURAS del theme-options.php real ----------
$src = file_get_contents($THEME . '/muffin-options/theme-options.php');

function extract_function($src, $name) {
    $pos = strpos($src, 'function ' . $name . '(');
    if ($pos === false) { return null; }
    $brace = strpos($src, '{', $pos);
    $depth = 0; $i = $brace;
    $len = strlen($src);
    do {
        $ch = $src[$i];
        if ($ch === '{') { $depth++; }
        elseif ($ch === '}') { $depth--; }
        $i++;
    } while ($depth > 0 && $i < $len);
    return substr($src, $pos, $i - $pos);
}

foreach (['mfna_bg_position', 'mfna_bg_size', 'mfna_utc', 'mfna_section_style', 'mfna_skin'] as $fn) {
    $code = extract_function($src, $fn);
    if ($code && !function_exists($fn)) { eval($code); }
}

// Dinámicas (listas de BD) — marcador
if (!function_exists('mfna_templates')) { function mfna_templates($t = false) { return ['' => '[dinamico: lista de la BD]']; } }
if (!function_exists('mfna_taxonomies')) { function mfna_taxonomies() { return ['' => '[dinamico: taxonomias del sitio]']; } }
if (!function_exists('mfna_menu')) { function mfna_menu() { return ['' => '[dinamico: menus del sitio]']; } }
if (!function_exists('mfna_cf7')) { function mfna_cf7() { return ['' => '[dinamico: formularios CF7]']; } }
if (!function_exists('mfn_get_categories')) { function mfn_get_categories($tax = 'category', $all = true) { return ['' => '[dinamico: terminos de ' . (is_string($tax) ? $tax : 'taxonomia') . ']']; } }
if (!function_exists('mfn_get_image_sizes')) { function mfn_get_image_sizes($full = false) { return ['' => '[dinamico: tamanos de imagen registrados]', 'thumbnail' => 'Thumbnail', 'medium' => 'Medium', 'large' => 'Large', 'full' => 'Full']; } }

// ---------- Cargar clases reales ----------
require $THEME . '/functions/builder/class-mfn-builder-helper.php';
require $THEME . '/functions/builder/class-mfn-builder-fields.php';

// vb=true: no fusiona advanced dentro de items (lo queremos separado)
$fields = new Mfn_Builder_Fields(true);

$ref = new ReflectionClass($fields);
$get = function ($prop) use ($ref, $fields) {
    $p = $ref->getProperty($prop);
    $p->setAccessible(true);
    return $p->getValue($fields);
};

$out = [
    'generated' => date('c'),
    'source' => 'class-mfn-builder-fields.php (ejecutado con stubs WP)',
    'section' => $get('section'),
    'wrap' => $get('wrap'),
    'advanced' => $get('advanced'),
    'items' => $get('items'),
    'inline_shortcodes' => Mfn_Builder_Fields::get_inline_shortcode(),
    'animations' => $get('animations'),
];

$json = json_encode($out, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PARTIAL_OUTPUT_ON_ERROR);
file_put_contents(__DIR__ . '/fields-dump.json', $json);

echo "OK items=" . count($out['items'])
    . " inline=" . count($out['inline_shortcodes'])
    . " section_fields=" . count($out['section'])
    . " wrap_fields=" . count($out['wrap'])
    . " advanced_fields=" . count($out['advanced'])
    . " bytes=" . strlen($json) . "\n";
