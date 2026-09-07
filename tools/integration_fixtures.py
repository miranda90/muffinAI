"""Generate native fixtures for a future WordPress roundtrip. No remote writes.
Pass a real destination manifest and resource keys to include image/video cases.
"""
import argparse
from pathlib import Path
from contracts import atomic_json, read_json
from mfn import BuildContext, section, wrap, item, nested, pad, media
from recipes import hero, heading, grid, card, image, video


def fixtures(manifest=None, image_key=None, mp4_key=None, poster_key=None, menu_id=None):
    result={}
    with BuildContext():
        result['page']=[hero('Prueba de importación',spacing=pad({'top':'2rem'}))]
    with BuildContext():
        result['cards']=[section({'width_switcher':'full'},[grid([card([heading('Tarjeta %d'%i)],background='#eee',equal_height=True) for i in range(3)])])]
    with BuildContext():
        result['query']=[section({'width_switcher':'full'},[wrap({'type':'query','query_type':'posts','query_post_type':'post'},[nested({},[item('heading',{'title':'{title}'})])])])]
    if image_key:
        with BuildContext(): result['image']=[section({'width_switcher':'full'},[wrap({},[image(media(manifest,image_key),alt='Imagen de prueba')])])]
    if mp4_key and poster_key:
        with BuildContext(): result['video']=[section({'width_switcher':'full'},[wrap({},[video(media(manifest,mp4_key),media(manifest,poster_key))])])]
    if menu_id:
        if not str(menu_id).isdigit() or int(menu_id)<1: raise ValueError('menu-id debe ser positivo')
        with BuildContext(): result['header']=[section({'width_switcher':'full'},[wrap({},[item('header_menu',{'menu':str(menu_id)})])])]
        with BuildContext(): result['sidemenu']=[section({'width_switcher':'full'},[wrap({},[item('sidemenu_menu',{'tabs':[{'title':'Menu','menu':str(menu_id)}]})])])]
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--manifest');p.add_argument('--image');p.add_argument('--mp4');p.add_argument('--poster');p.add_argument('--menu-id')
    args=p.parse_args();manifest=read_json(args.manifest) if args.manifest else {}
    pages=fixtures(manifest,args.image,args.mp4,args.poster,args.menu_id)
    for name,document in pages.items(): atomic_json(args.output/(name+'.json'),document)
    atomic_json(args.output/'verification.json',{'wordpress_roundtrip':'not_run','visual_verification':'not_run',
       'fixtures':list(pages),'pending':[name for name in ('page','cards','query','image','video','header','sidemenu') if name not in pages],
       'note':'Usar solo un WordPress de pruebas; guardar, exportar, editar y comparar de nuevo.'})


if __name__=='__main__':main()
