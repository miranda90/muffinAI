"""Offline roundtrip and region geometry comparison; no claim of pixel fidelity."""
import argparse
import json
from contracts import read_json


def normalize(document):
    if isinstance(document,list): return [normalize(x) for x in document]
    if not isinstance(document,dict): return document
    result={}
    for key,value in document.items():
        if key=='uid': continue
        if key=='attr' and isinstance(value,dict):
            value={k:v for k,v in value.items() if k not in ('vb','vb_postid','rwd')}
        result[key]=normalize(value)
    return result


def differences(left,right,path='$'):
    if type(left)!=type(right): return [{'path':path,'before':left,'after':right}]
    if isinstance(left,dict):
        out=[]
        for key in sorted(set(left)|set(right)):
            if key not in left or key not in right:
                out.append({'path':path+'.'+key,'missing':'before' if key not in left else 'after'})
            else: out.extend(differences(left[key],right[key],path+'.'+key))
        return out
    if isinstance(left,list):
        if len(left)!=len(right): return [{'path':path,'length_before':len(left),'length_after':len(right)}]
        return [d for i,(a,b) in enumerate(zip(left,right)) for d in differences(a,b,'%s[%d]'%(path,i))]
    return [] if left==right else [{'path':path,'before':left,'after':right}]


def parse_renames(pairs):
    """'origen=destino' explícitos; sin adivinar emparejamientos."""
    renames={}
    for pair in pairs or ():
        if '=' not in pair: raise ValueError('rename requiere ORIGEN=DESTINO: '+pair)
        source,target=pair.split('=',1)
        if not source or not target: raise ValueError('rename con clave vacía: '+pair)
        if source in renames: raise ValueError('rename duplicado: '+source)
        renames[source]=target
    if len(set(renames.values()))!=len(renames): raise ValueError('Varias regiones renombradas al mismo destino')
    return renames


def geometry(reference,actual,tolerance=2,renames=None):
    if reference.get('viewport')!=actual.get('viewport'):
        raise ValueError('Viewports distintos: comparación no válida')
    if not reference.get('fonts_ready') or not actual.get('fonts_ready'):
        raise ValueError('Esperar carga de fuentes antes de comparar')
    renames=dict(renames or {})
    expected={x['key']:x for x in reference['nodes']};found={x['key']:x for x in actual['nodes']}
    missing=[k for k in renames if k not in expected]
    if missing: raise ValueError('rename de regiones inexistentes en la referencia: '+', '.join(missing))
    expected={renames.get(k,k):v for k,v in expected.items()}
    if len(expected)!=len(reference['nodes']): raise ValueError('rename colisiona con una región existente')
    issues=[]
    for key in sorted(set(expected)|set(found)):
        if key not in expected or key not in found:
            issues.append({'path':key,'reason':'region missing'});continue
        for dimension in ('x','y','width','height'):
            delta=found[key]['box'][dimension]-expected[key]['box'][dimension]
            if abs(delta)>tolerance: issues.append({'path':key,'property':dimension,'delta_px':delta})
        for prop in ('text','media','style'):
            issues.extend(differences(expected[key].get(prop),found[key].get(prop),key+'.'+prop))
    if actual.get('overflow'): issues.append({'path':'document','reason':'horizontal overflow'})
    return issues


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('mode',choices=['roundtrip','geometry']);p.add_argument('before');p.add_argument('after')
    p.add_argument('--tolerance',type=float,default=2)
    p.add_argument('--rename',action='append',default=[],metavar='ORIGEN=DESTINO',help='geometry: emparejar una región de la referencia con otra clave del resultado (repetible)')
    args=p.parse_args()
    if args.tolerance<0: p.error('tolerance debe ser no negativa')
    if args.rename and args.mode!='geometry': p.error('--rename solo aplica a geometry')
    left,right=read_json(args.before),read_json(args.after)
    issues=differences(normalize(left),normalize(right)) if args.mode=='roundtrip' else geometry(left,right,args.tolerance,parse_renames(args.rename))
    print(json.dumps({'accepted':not issues,'mode':args.mode,'issues':issues},ensure_ascii=False,indent=2))
    return int(bool(issues))


if __name__=='__main__': raise SystemExit(main())
