"""Single offline maintenance command: python3 tools/check.py."""
import ast
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from contracts import read_json
from validate_bebuilder_json import load_schema, validate


def main():
    failures=[]
    def command(args):
        process=subprocess.run(args,cwd=ROOT)
        if process.returncode: failures.append(' '.join(map(str,args)))
    for path in [*ROOT.joinpath('tools').glob('*.py'),*ROOT.joinpath('proyectos').glob('*/*.py'),*ROOT.joinpath('builder-elements/_generator').glob('*.py')]:
        ast.parse(path.read_text(),str(path))
    command([sys.executable,'-m','unittest','discover','-s','tests','-v'])
    if shutil.which('php'):
        command(['php','-l','builder-elements/_generator/extract.php'])
        command(['php','builder-elements/_generator/extract.php','--check'])
    else: failures.append('PHP no disponible: contratos sin comprobar')
    if shutil.which('node'): command(['node','--check','tools/browser_capture.js'])
    command([sys.executable,'builder-elements/_generator/generate_fichas.py','--check'])
    for path in sorted(ROOT.joinpath('examples').glob('*/*.json')):
        result=validate(read_json(path),origin='export')
        if not result['accepted']:
            failures.append('%s: export real con %d errores'%(path.relative_to(ROOT),result['counts']['error']))
    schema=load_schema()
    for path in ROOT.joinpath('builder-elements').glob('*.md'):
        if not path.stem in schema.item_types: continue
        matches=re.findall(r'```json\s*(.*?)\s*```',path.read_text(),re.S)
        if not matches: continue
        node=json.loads(matches[0])
        doc=[{'attr':{},'wraps':[{'size':'1/1','attr':{},'items':[node]}]}]
        result=validate(doc,schema)
        errors=[x for x in result['issues'] if x['level']=='error']
        if errors: failures.append('%s: %s'%(path.name,errors))
    command([sys.executable,'tools/build.py','proyectos/_plantilla/build_plantilla.py','--check'])
    print(json.dumps({'accepted':not failures,'failures':failures},ensure_ascii=False,indent=2))
    return int(bool(failures))


if __name__=='__main__': raise SystemExit(main())
