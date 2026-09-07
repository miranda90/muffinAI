import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import mfn
import recipes
from build import deliver
from validate_bebuilder_json import validate


class PipelineTests(unittest.TestCase):
    def test_recipes(self):
        with mfn.BuildContext():
            cells = [recipes.card([recipes.heading('Card'), recipes.button('Action', '/contact', background='#123456', color='#fff')], background='#fff', equal_height=True, cta_bottom=True) for _ in range(3)]
            doc = [recipes.band([recipes.grid(cells)], spacing=mfn.pad({'top':'2rem'}))]
        result = validate(doc, strict=True)
        self.assertTrue(result['accepted'], result['issues'])

    def test_delivery(self):
        ctx=mfn.BuildContext(design={'source':{'kind':'manual'},'blocks':[]})
        with ctx:
            hero=recipes.hero('Hola', spacing=mfn.pad({'top':'2rem'}))
            ctx.bind('hero',hero,responsive={'mobile':'single column'})
        with tempfile.TemporaryDirectory() as folder:
            output=Path(folder)/'page.json'
            result=deliver([hero],ctx,output,check=True)
            self.assertTrue(result['accepted'],result)
            self.assertFalse(output.exists())
            deliver([hero],ctx,output)
            previous=output.read_bytes()
            self.assertEqual(json.loads(output.with_suffix('.report.json').read_text())['visual_verification'],'not_run')
            deliver([],ctx,output)
            self.assertEqual(previous,output.read_bytes())
            draft=output.with_name('page.draft.json')
            deliver([],ctx,output,draft=True)
            self.assertEqual(previous,output.read_bytes())
            self.assertTrue(draft.exists())
            self.assertFalse(json.loads(draft.with_suffix('.report.json').read_text())['accepted'])
            draft.unlink()
            deliver([hero],ctx,output,draft=True)  # aceptada: se publica, no se degrada a borrador
            self.assertFalse(draft.exists())

    @unittest.skipUnless(shutil.which('php'), 'PHP no disponible')
    def test_real_php_css(self):
        attr = {
            'css_advanced_padding': mfn.style_field('item', 'css_advanced_padding', mfn.pad({'top':'2rem','left':'0'}),itype='heading'),
            'css_advanced_border_radius': mfn.style_field('item','css_advanced_border_radius',{'desktop':'4px 8px 12px 16px'},itype='heading'),
            'css_advanced_transform': mfn.style_field('item','css_advanced_transform',{'desktop':mfn.transform(x=12,rotate=25)},itype='heading'),
            'css_typography': mfn.style_field('item','css_typography',{'desktop':{'font-family':'Arial','font-size':'20px'},'mobile':{'font-size':'16px'}},itype='heading'),
        }
        node=mfn.item('heading',attr)
        process=subprocess.run(['php',str(ROOT/'tests/php/css_harness.php')],input=json.dumps([node]),text=True,capture_output=True)
        self.assertEqual(process.returncode,0,process.stderr)
        data=json.loads(process.stdout); css=''.join(data['files'].values())
        for fragment in ('padding-top:2rem', 'padding-left:0px', 'border-radius:4px 8px 12px 16px', 'transform:matrix(1,0,0,1,12,0) rotate(25deg)', '@media(max-width: 767px)', "font-family:'Arial'", 'font-size:16px'):
            self.assertIn(fragment,css)
        self.assertNotIn('mfnuidelement',css)
        self.assertEqual(json.loads(data['metadata']['mfn-page-fonts']),['Arial'])

    def test_template_check_from_other_cwd(self):
        process=subprocess.run([sys.executable,str(ROOT/'tools/build.py'),str(ROOT/'proyectos/_plantilla/build_plantilla.py'),'--check'],cwd='/tmp',text=True,capture_output=True)
        self.assertEqual(process.returncode,0,process.stderr+process.stdout)
        self.assertTrue(json.loads(process.stdout)['accepted'])


if __name__ == '__main__': unittest.main()
