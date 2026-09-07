<?php
/**
 * Harness de extracción: ejecuta Mfn_Builder_Fields real con stubs de WordPress
 * y vuelca todas las definiciones de campos a JSON.
 */

error_reporting(E_ERROR | E_PARSE); // silenciar warnings de claves indefinidas

define('ABSPATH', '/tmp/');

$opts = getopt('', ['theme:', 'stdout', 'check']);
$THEME = realpath($opts['theme'] ?? (__DIR__ . '/../../betheme'));
if (!$THEME || !is_file($THEME . '/functions/builder/class-mfn-builder-fields.php')) {
    fwrite(STDERR, "Theme no encontrado\n"); exit(3);
}

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
    $tokens = token_get_all($src);
    for ($i = 0; $i < count($tokens); $i++) {
        if (!is_array($tokens[$i]) || $tokens[$i][0] !== T_FUNCTION) continue;
        $j = $i + 1;
        while (isset($tokens[$j]) && is_array($tokens[$j]) && $tokens[$j][0] === T_WHITESPACE) $j++;
        if (!isset($tokens[$j]) || !is_array($tokens[$j]) || $tokens[$j][1] !== $name) continue;
        $code = ''; $depth = 0; $started = false;
        for (; $i < count($tokens); $i++) {
            $token = $tokens[$i];
            $code .= is_array($token) ? $token[1] : $token;
            if ($token === '{') { $depth++; $started = true; }
            if ($token === '}' && --$depth === 0 && $started) return $code;
        }
    }
    throw new RuntimeException('Función requerida no encontrada: ' . $name);
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

$source_files = [
    'functions/builder/class-mfn-builder-fields.php',
    'functions/builder/class-mfn-builder-items.php',
    'functions/builder/class-mfn-builder-helper.php',
    'functions/admin/class-mfn-helper.php',
    'muffin-options/theme-options.php',
    'visual-builder/assets/js/scripts.js',
];
$out['source_hashes'] = [];
foreach ($source_files as $file) $out['source_hashes'][$file] = hash_file('sha256', $THEME . '/' . $file);
$out['theme_version'] = null; // Partial reference may have no style.css; never infer from asset names.
if (is_file($THEME . '/style.css') && preg_match('/^Version:\s*(.+)$/mi', file_get_contents($THEME . '/style.css'), $match)) {
    $out['theme_version'] = trim($match[1]);
}
$items_source = file_get_contents($THEME . '/functions/builder/class-mfn-builder-items.php');
preg_match_all('/function\s+item_(\w+)\s*\(/', $items_source, $matches);
$out['render_types'] = $matches[1]; sort($out['render_types']);
$json = json_encode($out, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
if (isset($opts['check'])) {
    $old = json_decode(file_get_contents(__DIR__ . '/../_elements.json'), true, 512, JSON_THROW_ON_ERROR);
    $same = true;
    $current = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
    foreach (['section','wrap','advanced','items','inline_shortcodes','animations','source_hashes','render_types'] as $key) {
        if (($old[$key] ?? null) !== $current[$key]) { fwrite(STDERR, "Diferencia: " . $key . "\n"); $same = false; }
    }
    exit($same ? 0 : 1);
}
if (isset($opts['stdout'])) { echo $json; exit(0); }
$tmp = tempnam(__DIR__, '.fields-');
if (file_put_contents($tmp, $json) === false || !rename($tmp, __DIR__ . '/fields-dump.json')) {
    throw new RuntimeException('No se pudo publicar fields-dump.json');
}
echo "OK items=" . count($out['items']) . " bytes=" . strlen($json) . "\n";
