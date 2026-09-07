<?php
// Runs the actual compiler; filesystem and metadata stay in memory.
define('ABSPATH', '/__muffin_test__/');
$metadata = []; $files = [];
class MemoryFilesystem {
    public function put_contents($path, $content, $mode = null) {
        $GLOBALS['files'][$path] = $content; return true;
    }
}
$wp_filesystem = new MemoryFilesystem();
function WP_Filesystem() { return true; }
function wp_upload_dir() { return ['basedir' => '/__muffin_test__/uploads']; }
function wp_normalize_path($path) { return $path; }
function wp_mkdir_p($path) { return true; }
function get_post_meta($id, $key, $single = true) { return ''; }
function get_post_type($id) { return 'page'; }
function update_post_meta($id, $key, $value) { $GLOBALS['metadata'][$key] = $value; }
function delete_post_meta($id, $key) { unset($GLOBALS['metadata'][$key]); }
function apply_filters($tag, $value) { return $value; }
require __DIR__ . '/../../betheme/functions/admin/class-mfn-helper.php';
$input = json_decode(stream_get_contents(STDIN), true, 512, JSON_THROW_ON_ERROR);
$result = Mfn_Helper::preparePostUpdate($input, 42);
echo json_encode(['styles' => $result, 'metadata' => $metadata, 'files' => $files], JSON_THROW_ON_ERROR);
