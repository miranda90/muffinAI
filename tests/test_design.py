import copy
from pathlib import Path
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
from design import SourceCache,from_figma,from_html,from_image
from compare import differences,normalize,geometry,parse_renames
from integration_fixtures import fixtures
from validate_bebuilder_json import validate


class DesignTests(unittest.TestCase):
    def test_cache_revision(self):
        with tempfile.TemporaryDirectory() as folder:
            cache=SourceCache(folder);key=dict(kind='figma',reference='file/frame',revision='1')
            cache.put({'value':1},**key);self.assertEqual(cache.get(**key),{'value':1})
            self.assertIsNone(cache.get(**dict(key,revision='2')))
    def test_figma(self):
        result=from_figma({'document':{'id':'1:1','type':'FRAME','layoutMode':'HORIZONTAL','children':[{'id':'1:2','type':'TEXT','characters':'Hello'}]}},'file/frame','1')
        self.assertEqual(len(result['blocks']),2);self.assertEqual(result['blocks'][1]['text'],'Hello')
        self.assertEqual(result['blocks'][0]['uids'],[])
    def test_image_inference(self):
        result=from_image({'viewport':{'width':100,'height':200},'blocks':[{'id':'hero'}]},'shot.png','hash')
        self.assertEqual(result['blocks'][0]['evidence'],'inferred')
    def test_roundtrip(self):
        a=[{'uid':'aaa','attr':{'title':'Hello'}}];b=[{'uid':'bbb','attr':{'title':'Hello','vb':'1'}}]
        self.assertEqual(differences(normalize(a),normalize(b)),[])
        b[0]['attr']['title']='Changed';self.assertTrue(differences(normalize(a),normalize(b)))
    def test_geometry(self):
        a={'viewport':{'width':100,'height':100},'fonts_ready':True,'nodes':[{'key':'hero','box':{'x':0,'y':0,'width':90,'height':80}}]}
        b=copy.deepcopy(a);b['nodes'][0]['box']['x']=1;self.assertEqual(geometry(a,b),[])
        b['nodes'][0]['box']['x']=3;self.assertTrue(geometry(a,b))
        b['fonts_ready']=False
        with self.assertRaises(ValueError):geometry(a,b)
    def test_geometry_rename(self):
        a={'viewport':{'width':100,'height':100},'fonts_ready':True,'nodes':[{'key':'hero-title','box':{'x':0,'y':0,'width':90,'height':80}}]}
        b=copy.deepcopy(a);b['nodes'][0]['key']='sec1-heading'
        self.assertEqual(len(geometry(a,b)),2)  # sin rename: región ausente en ambos sentidos
        self.assertEqual(geometry(a,b,renames=parse_renames(['hero-title=sec1-heading'])),[])
        with self.assertRaises(ValueError):parse_renames(['hero-title'])
        with self.assertRaises(ValueError):parse_renames(['a=x','b=x'])
        with self.assertRaises(ValueError):geometry(a,b,renames={'missing':'sec1-heading'})
    def test_fixtures(self):
        for name,doc in fixtures().items():
            self.assertTrue(validate(doc)['structurally_valid'],name)


if __name__=='__main__':unittest.main()
