"""Freeze source snapshots and annotations without guessing unobserved design states."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from contracts import atomic_json, read_json


class SourceCache:
    def __init__(self, directory): self.directory = Path(directory)
    def key(self, *, kind, reference, revision, options=None):
        if not revision: raise ValueError('Cache requiere revisión explícita del origen')
        descriptor = {'version':1,'kind':kind,'reference':reference,'revision':revision,'options':options or {}}
        return hashlib.sha256(json.dumps(descriptor,sort_keys=True).encode()).hexdigest()
    def get(self, **descriptor):
        path=self.directory/(self.key(**descriptor)+'.json')
        return read_json(path) if path.exists() else None
    def put(self, value, **descriptor):
        atomic_json(self.directory/(self.key(**descriptor)+'.json'),value)


def from_figma(data, reference, revision):
    """Accept a saved Figma document/node tree. No API credentials or live requests."""
    blocks=[]
    def walk(node, parent=None):
        if not isinstance(node,dict) or node.get('visible') is False: return
        kind=node.get('type')
        if kind and node.get('id'):
            blocks.append({'id':str(node['id']), 'parent':parent, 'name':node.get('name',''),
                           'role':kind, 'text':node.get('characters',''),
                           'geometry':node.get('absoluteBoundingBox',{}),
                           'layout':{k:node[k] for k in ('layoutMode','layoutSizingHorizontal','layoutSizingVertical',
                                      'primaryAxisSizingMode','counterAxisSizingMode','constraints','itemSpacing',
                                      'paddingTop','paddingRight','paddingBottom','paddingLeft') if k in node},
                           'appearance':{k:node[k] for k in ('style','fills','strokes','effects','cornerRadius',
                                          'componentId','componentProperties','styles') if k in node},
                           'evidence':'measured','uids':[],'responsive':{},'exception':None})
        for child in node.get('children',[]): walk(child,node.get('id',parent))
    if 'nodes' in data:
        for entry in data['nodes'].values():
            if entry: walk(entry.get('document',{}))
    else: walk(data.get('document',data))
    if not blocks: raise ValueError('Snapshot Figma sin nodos identificables')
    return {'source':{'kind':'figma','reference':reference,'revision':revision},'blocks':blocks,
            'pending':['Asignar nodos BeBuilder, medios locales y decisiones responsive por bloque']}


def from_html(snapshot, reference, revision):
    if not isinstance(snapshot.get('nodes'),list) or not snapshot.get('viewport'):
        raise ValueError('Usar el snapshot de browser_capture.js con viewport y nodes')
    blocks=[]
    for node in snapshot['nodes']:
        blocks.append({'id':node['key'],'role':node['tag'],'text':node.get('text',''),
                       'geometry':node['box'],'appearance':node.get('style',{}),
                       'pseudo':node.get('pseudo',{}),'media':node.get('media',{}),
                       'evidence':'measured','uids':[],'responsive':{},'exception':None})
    return {'source':{'kind':'html','reference':reference,'revision':revision,
                      'viewport':snapshot['viewport'],'fonts_ready':snapshot.get('fonts_ready',False)},
            'blocks':blocks,'pending':['Inspeccionar otros viewports y estados interactivos']}


def from_image(annotations, reference, revision):
    if not annotations.get('viewport') or not isinstance(annotations.get('blocks'),list):
        raise ValueError('Imagen requiere anotaciones con viewport y blocks; no se inventa OCR')
    blocks=[]
    for block in annotations['blocks']:
        if not block.get('id'): raise ValueError('Anotación sin id')
        blocks.append({**block,'evidence':block.get('evidence','inferred'),'uids':[],
                       'responsive':block.get('responsive',{}),'exception':block.get('exception')})
    return {'source':{'kind':'image','reference':reference,'revision':revision,'viewport':annotations['viewport']},
            'blocks':blocks,'pending':['Confirmar texto, fuentes y assets; responsive no observado es inferido']}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('kind',choices=['figma','html','image']);p.add_argument('snapshot',type=Path)
    p.add_argument('--reference',required=True);p.add_argument('--revision',required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--cache',type=Path)
    args=p.parse_args()
    data=read_json(args.snapshot)
    descriptor=dict(kind=args.kind,reference=args.reference,revision=args.revision,
                    options={'snapshot_sha256':hashlib.sha256(args.snapshot.read_bytes()).hexdigest()})
    cache=SourceCache(args.cache) if args.cache else None
    result=cache.get(**descriptor) if cache else None
    if result is None:
        result={'figma':from_figma,'html':from_html,'image':from_image}[args.kind](data,args.reference,args.revision)
        if cache: cache.put(result,**descriptor)
    atomic_json(args.output,result)


if __name__=='__main__': main()
