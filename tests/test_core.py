import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import mfn
from contracts import strict_loads, validate_manifest
from validate_bebuilder_json import Schema, Validator, validate


def page():
    with mfn.BuildContext():
        return [mfn.section({"width_switcher": "full"}, [mfn.wrap({}, [mfn.item("heading", {"title": "Prueba"})])])]


class CoreTests(unittest.TestCase):
    def setUp(self):
        self.doc = page()
        self.it = self.doc[0]["wraps"][0]["items"][0]

    def codes(self, **kwargs):
        return {x["code"] for x in validate(self.doc, **kwargs)["issues"]}

    def test_valid(self):
        self.assertTrue(validate(self.doc, strict=True)["accepted"])

    def test_malformed(self):
        mutations = [("size", []), ("size", {}), ("tablet_size", []), ("type", []), ("attr", [])]
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                doc = page(); doc[0]["wraps"][0]["items"][0][key] = value
                self.assertFalse(validate(doc)["accepted"])
        self.it.update(type="", item_is_wrap=1, items=1)
        self.assertIn("E012", self.codes())

    def test_aliases(self):
        for alias, target in mfn.catalog().aliases.items():
            self.it["type"] = alias
            self.assertIn("E018", self.codes())
            self.assertEqual(mfn.item(alias, {})["type"], mfn.catalog().canonical(target))

    def test_plain_css(self):
        for value in ("red", {"desktop": "red"}, 42):
            self.it["attr"]["css_color"] = value
            self.assertIn("E034", self.codes())

    def test_plain_styled_select_export(self):
        # El VB exporta un select de estilo sin tocar como su `std` plano (examples/example1).
        self.it["type"] = self.it["jsclass"] = "video"
        self.it["attr"] = {"video": "", "mp4": "https://sitio.example/a.mp4#5", "object_position": "center center"}
        self.assertIn("E034", self.codes())
        codes = [x["code"] for x in validate(self.doc, origin="export")["issues"]]
        self.assertNotIn("E034", codes); self.assertIn("I034", codes)
        self.it["attr"]["object_position"] = "top nonsense"
        self.assertIn("E034", [x["code"] for x in validate(self.doc, origin="export")["issues"]])

    def test_bad_style_types(self):
        for value in ([], {}, False, None):
            self.it["attr"]["css_color"] = {"selector": mfn.S_TITLE, "style": value, "val": "red"}
            self.assertIn("E030", self.codes())

    def test_selector_semantics(self):
        self.assertNotEqual(Validator.norm_selector(".a > .b"), Validator.norm_selector(".a .b"))
        self.assertEqual(Validator.norm_selector(".a|hover"), Validator.norm_selector(".a:hover"))
        self.it["attr"]["css_color"] = mfn.css(mfn.S_TITLE + ":hover", "color", "red")
        result = validate(self.doc, fix=True)
        self.assertNotIn("E031", {x["code"] for x in result["issues"]})
        self.assertEqual(result["document"], self.doc)

    def test_nested(self):
        self.it.pop("type"); self.it.update(item_is_wrap=True, items=[], attr={})
        self.assertNotIn("E009", self.codes())
        self.assertTrue(validate(self.doc, strict=True)["accepted"])
        self.assertFalse(validate(self.doc, strict=True, editor="classic")["accepted"])
        self.assertEqual(validate(self.doc, fix=True)["document"][0]["wraps"][0]["items"][0]["item_is_wrap"], 1)

    def test_grid_location(self):
        self.doc[0]["wraps"][0]["grid"] = "grid"
        self.assertIn("E017", self.codes())

    def test_fix_copy_identity_idempotence(self):
        for key in ("icon", "title", "jsclass", "uid"): self.it.pop(key)
        original = copy.deepcopy(self.doc)
        result = validate(self.doc, fix=True)
        self.assertEqual(self.doc, original)
        repaired = result["document"][0]["wraps"][0]["items"][0]
        self.assertEqual(repaired["jsclass"], "heading")
        self.assertEqual(repaired["icon"], "heading")
        self.assertEqual(validate(result["document"], fix=True)["fixes"], [])

    def test_uid_collision_with_generated(self):
        path = "$[0].wraps[0].items[0]"
        self.doc[0]["uid"] = Validator.gen_uid(path)
        self.it.pop("uid")
        result = validate(self.doc, fix=True)
        self.assertNotEqual(result["document"][0]["uid"], result["document"][0]["wraps"][0]["items"][0]["uid"])

    def test_policy_exports(self):
        self.it["attr"]["vb"] = "1"
        self.assertIn("E020", self.codes())
        self.assertFalse(validate(self.doc)["accepted"])
        self.assertTrue(validate(self.doc, origin="export")["accepted"])

    def test_no_structural_exception(self):
        self.it["size"] = "nonsense"
        self.assertFalse(validate(self.doc, ignore=["E008"])["accepted"])
        self.assertFalse(validate(self.doc, exceptions=[{"code":"E008", "path":"$[0].wraps[0].items[0].size", "reason":"test"}])["accepted"])

    def test_repeater_html(self):
        self.it.update(type="tabs", attr={"tabs":[{"title":"A", "content":"<b style='color:red'>X</b>"}]})
        self.assertIn("E023", self.codes())

    def test_css_builder_and_transform(self):
        self.it["attr"]["css_advanced_transform"] = mfn.style_field("item", "css_advanced_transform", {"desktop": mfn.transform(x=12, rotate=25)}, itype="heading")
        self.assertNotIn("E040", self.codes())
        self.it["attr"]["css_advanced_transform"]["val"]["desktop"]["string"] = "matrix(1,0,0,1,0,0)"
        self.assertIn("E040", self.codes())

    def test_context_independence(self):
        self.assertEqual(page(), page())
        attr = {"title":"A"}; item = mfn.item("heading", attr); attr["title"]="B"
        self.assertEqual(item["attr"]["title"], "A")
        self.assertEqual(mfn.m0("2rem", 0)["val"]["mobile"]["bottom"], "0px")
        self.assertIn("mobile", mfn.typo(mfn.S_TITLE, {"font-size":"16px"})["val"])

    def test_manifest(self):
        for entry in ({"id":0,"url":"https://site.test/x.png"}, {"id":1,"url":"http://localhost/x.png"}, {"id":1,"url":"https://site.test/x.png#2"}):
            with self.assertRaises(ValueError): mfn.media({"x":entry}, "x")
        man = {"x":{"id":1,"url":"https://site.test/x.png"}}
        self.it.update(type="image", attr={"src":mfn.media(man,"x")})
        self.assertTrue(validate(self.doc, manifest=man)["accepted"])
        self.assertFalse(validate(self.doc, manifest={})["accepted"])
        self.it["attr"]["src"]="http://localhost:3845/x.png"
        self.assertIn("E071", self.codes())

    def test_strict_json(self):
        for text in ('{"x":1,"x":2}', '[NaN]', '[1e999]', '[' * 100 + '0' + ']' * 100):
            with self.assertRaises(ValueError): strict_loads(text)

    def test_dictionary_fields(self):
        self.assertIn("test", mfn.catalog()._index({"group":{"id":"test", "type":"text"}}))

    def test_cli(self):
        for args in (["--fix"], ["--fix","--json"], ["--json"], ["--schema","/missing/schema.json","--json"]):
            result=subprocess.run([sys.executable,str(ROOT/"tools/validate_bebuilder_json.py"),"-"]+args,
                                  input=json.dumps(self.doc),text=True,capture_output=True)
            parsed=json.loads(result.stdout)
            self.assertNotIn("Traceback", result.stderr)
            if "--schema" in args: self.assertEqual(result.returncode,3)
        with tempfile.TemporaryDirectory() as folder:
            dest=Path(folder)/"output.json"; dest.write_text('"previous"')
            result=subprocess.run([sys.executable,str(ROOT/"tools/validate_bebuilder_json.py"),"-","--fix","-o",str(dest)],input="[]",text=True,capture_output=True)
            self.assertNotEqual(result.returncode,0)
            self.assertEqual(dest.read_text(),'"previous"')


if __name__ == "__main__": unittest.main()
