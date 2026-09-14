"""API compacta (el/wr/nw/sec): normalización, switchers y equivalencia con un encargo real."""
import json
from pathlib import Path
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import mfn
from mfn import A, el, wr, nw, sec
from validate_bebuilder_json import validate


def strip(node):
    if isinstance(node, dict):
        return {k: strip(v) for k, v in node.items() if k != 'uid'}
    if isinstance(node, list):
        return [strip(x) for x in node]
    return node


class CompactApiTests(unittest.TestCase):
    def test_spacing_px_to_rem_and_mobile(self):
        val = A('section', padding=(80, 0))['css_advanced_padding']['val']
        self.assertEqual(val['desktop'], {'top': '5rem', 'right': '0px', 'bottom': '5rem', 'left': '0px'})
        self.assertEqual(val['mobile'], val['desktop'])
        with mfn.BuildContext(profile={'root_font_px': 10}):
            self.assertEqual(A('section', padding='20px')['css_advanced_padding']['val']['desktop']['top'], '2rem')
        val = A('item', 'heading', margin={'desktop': {'bottom': '2rem'}, 'mobile': {'bottom': '1rem'}})['css_advanced_margin']['val']
        self.assertEqual(val, {'desktop': {'bottom': '2rem'}, 'mobile': {'bottom': '1rem'}})

    def test_shorthand_dimensions_and_units(self):
        attr = A('item', 'button', button_border_radius=8, button_border_width='1px 0', button_gap=16, icon='icon-x')
        self.assertEqual(attr['css_button_border_radius']['val'], {'desktop': '8px 8px 8px 8px'})
        self.assertEqual(attr['css_button_border_width']['val'], {'desktop': '1px 0 1px 0'})
        self.assertEqual(attr['css_button_gap']['val'], {'desktop': '16px'})

    def test_typography_and_font_size_get_mobile(self):
        attr = A('item', 'heading', typography={'font-size': '68px'})
        self.assertEqual(attr['css_typography']['val']['mobile'], {'font-size': '68px'})
        self.assertEqual(attr['css_typography']['selector'], mfn.S_TITLE)

    def test_conditions_declared(self):
        attr = A('wrap', background_color='#fff', height='100%', grid_columns='repeat(3, 1fr)')
        self.assertEqual(attr['background_switcher'], 'default')
        self.assertEqual(attr['height_switcher'], 'custom')
        self.assertEqual(attr['grid'], 'grid')
        self.assertEqual(attr['grid_columns_switcher'], '')
        self.assertEqual(A('section', max_width='1728px')['width_switcher'], 'custom')
        self.assertEqual(A('item', 'image', image_cover_height=320)['image_height'], 'custom')
        # el valor explícito gana sobre la condición
        self.assertEqual(A('section', background_switcher='gradient', background_color='#fff')['background_switcher'], 'gradient')

    def test_legacy_plain_keys_do_not_shadow(self):
        self.assertIn('selector', A('wrap', padding=0)['css_advanced_padding'])
        self.assertEqual(A('item', 'button', title='x')['title'], 'x')

    def test_unknown_key_suggests(self):
        with self.assertRaisesRegex(ValueError, 'button_padding'):
            A('item', 'button', button_paddng=1)

    def test_prebuilt_css_passthrough_and_alias(self):
        built = mfn.css(mfn.S_TITLE, 'typography', {'desktop': {'font-size': '1px'}, 'mobile': {'font-size': '1px'}})
        self.assertIs(A('item', 'heading', typography=built)['css_typography'], built)
        with mfn.BuildContext():
            node = el('column', content='<p>x</p>')
        self.assertEqual(node['type'], mfn.catalog().canonical('column'))

    def test_cols_and_labels(self):
        with mfn.BuildContext():
            node = el('heading', title='x', cols=('1/3', '1/2'), label='Titular')
            self.assertEqual((node['size'], node['tablet_size'], node['mobile_size'], node['title']), ('1/3', '1/2', '1/1', 'Titular'))
            section = sec(wr(node, cols='1/2'), label='Hero')
            self.assertEqual(section['attr']['width_switcher'], 'full')
            self.assertEqual(section['wraps'][0]['size'], '1/2')
            with self.assertRaises(ValueError):
                nw(nw(node))

    def test_page_accepted_strict(self):
        manifest = {'hero': {'id': 7, 'url': 'https://sitio.example/wp-content/uploads/hero.jpg'}}
        with mfn.BuildContext(manifest=manifest) as ctx:
            page = [sec(
                wr(el('heading', title='Hola', header_tag='h1', color='#fff', typography={'font-size': '68px', 'line-height': '1'}, margin=0),
                   el('button', title='Ver', link='/x', icon='icon-right-thin', button_color='#fff', button_background_color='#123',
                      button_padding=(10, 24), button_border_radius=0, button_gap=16, margin=0, cols=('1/3', '1/2')),
                   el('image', src=ctx.media('hero'), alt='Hero', image_cover_height=320, margin=0), cols='1/2', padding=(0, 16)),
                wr(*[nw(el('plain_text', content='x', margin=0), background_color='#fff', height='100%', padding=24) for _ in range(3)],
                   grid_columns={'desktop': 'repeat(3, 1fr)', 'tablet': 'repeat(2, 1fr)', 'mobile': '1fr'}, grid_columns_gap='1.5rem', grid_rows_gap='1.5rem'),
                padding=(80, 0), max_width='1728px', background_color='#111', label='Hero')]
        result = validate(page, strict=True, manifest=manifest)
        self.assertTrue(result['accepted'], [x for x in result['issues'] if x['level'] != 'info'])


class RealProjectEquivalence(unittest.TestCase):
    """Bloques del encargo We Are Testers reescritos con la API compacta = mismo JSON."""
    FROZEN = ROOT / 'proyectos/we-are-testers/we-are-testers-casos-de-exito.json'
    MEDIA = 'https://wearetesters.com/wp-content/uploads/2026/08/'

    def find(self, title):
        stack = list(json.loads(self.FROZEN.read_text()))
        while stack:
            node = stack.pop(0)
            if node.get('title') == title:
                return strip(node)
            stack.extend(node.get('wraps', []) + node.get('items', []))
        raise AssertionError(title)

    def test_eyebrow(self):
        eyebrow = {'font-size': '24px', 'line-height': '1.1', 'letter-spacing': '-0.48px', 'font-weight': '600', 'text-transform': 'uppercase'}
        eyebrow_m = {'font-size': '18px', 'line-height': '1.1', 'letter-spacing': '-0.36px', 'font-weight': '600', 'text-transform': 'uppercase'}
        with mfn.BuildContext():
            node = wr(
                el('image', src=self.MEDIA + 'eyebrow-cuadrado.svg', alt='', width_switcher='inline', hover='disable',
                   image_frame_width='10px', margin={'desktop': (0, '1.125rem', 0, 0), 'mobile': (0, '0.75rem', 0, 0)},
                   cols=('1/6', '1/6', '1/6'), label='Eyebrow — cuadrado'),
                el('heading', title='Casos de éxito', header_tag='p', width_switcher='inline', color='#221C3D',
                   typography={'desktop': eyebrow, 'mobile': eyebrow_m}, margin=0,
                   cols=('5/6', '5/6', '5/6'), label='Eyebrow — texto'),
                align_items='center', margin={'desktop': {'bottom': '2rem'}, 'mobile': {'bottom': '1.25rem'}},
                label='Eyebrow — Casos de éxito')
        self.assertEqual(strip(node), self.find('Eyebrow — Casos de éxito'))

    def test_pill(self):
        t = {'font-size': '12px', 'line-height': '1.3', 'font-weight': '500', 'text-transform': 'uppercase'}
        tm = dict(t, **{'font-size': '11px'})
        with mfn.BuildContext():
            node = el('button', title='Comunidades online', link='', icon='', button_style='', width_switcher='inline',
                      button_color='#000000', button_background_color='transparent', button_border_style='solid',
                      button_border_width=1, button_border_color='#C5C7C8', button_border_radius=2000,
                      button_padding=(6, 12), button_typography={'desktop': t, 'mobile': tm},
                      button_background_hover='#F4F7F9', button_color_hover='#000000',
                      margin=(0, '0.75rem', 0, 0), cols=('1/4', '1/4', '1/2'), label='Etiqueta — Comunidades online')
        reference = self.find('Etiqueta — Comunidades online')
        # El script congelado omitió el switcher del hover (W050 en el validador); la API lo declara sola.
        reference['attr']['background_switcher_hover'] = 'default'
        self.assertEqual(strip(node), reference)


if __name__ == '__main__':
    unittest.main()
