"""Create a standalone image overlay/diff report from two local PNG/JPEG/WebP files."""
import argparse
import base64
from pathlib import Path
import json


def report(reference, actual):
    def data(path):
        path=Path(path)
        mime={'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp'}.get(path.suffix.lower())
        if not mime: raise ValueError('Formato admitido: PNG, JPEG o WebP')
        return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()
    return '''<!doctype html><html lang="es"><meta charset="utf-8"><title>muffinAI · Comparación visual</title>
<style>body{font:16px system-ui;margin:24px;background:#f4f4f4;color:#222}canvas{max-width:100%;background:white;border:1px solid #bbb}label,button{margin-right:16px}#status{margin:16px 0}</style>
<h1>Comparación visual</h1><p>Las diferencias de píxeles orientan la revisión; no acreditan por sí solas fidelidad ni editabilidad.</p>
<label>Opacidad del resultado <input id="opacity" type="range" min="0" max="1" step="0.01" value="0.5"></label>
<label><input id="diff" type="checkbox">Diferencia absoluta</label><button id="save" disabled>Guardar PNG</button>
<p id="status">Cargando imágenes…</p><canvas id="canvas"></canvas>
<script>
const urls=URLS;
const canvas=document.getElementById('canvas'),ctx=canvas.getContext('2d');
const opacity=document.getElementById('opacity'),diff=document.getElementById('diff'),save=document.getElementById('save');
Promise.all(urls.map(url=>new Promise((resolve,reject)=>{const img=new Image();img.onload=()=>resolve(img);img.onerror=reject;img.src=url;}))).then(([a,b])=>{
 if(a.naturalWidth!==b.naturalWidth||a.naturalHeight!==b.naturalHeight)throw Error('Las capturas deben tener las mismas dimensiones y viewport.');
 canvas.width=a.naturalWidth;canvas.height=a.naturalHeight;
 const temp=document.createElement('canvas');temp.width=canvas.width;temp.height=canvas.height;const t=temp.getContext('2d');
 t.drawImage(a,0,0);const p=t.getImageData(0,0,temp.width,temp.height);t.clearRect(0,0,temp.width,temp.height);t.drawImage(b,0,0);const q=t.getImageData(0,0,temp.width,temp.height);
 const delta=t.createImageData(temp.width,temp.height);let sum=0;
 for(let i=0;i<p.data.length;i+=4){for(let c=0;c<3;c++){const d=Math.abs(p.data[i+c]-q.data[i+c]);delta.data[i+c]=d;sum+=d;}delta.data[i+3]=255;}
 document.getElementById('status').textContent=`${canvas.width} × ${canvas.height}; diferencia RGB media: ${(sum/(canvas.width*canvas.height*3)).toFixed(2)}/255. Revisar texto, recorte, alineación y contenido.`;
 function draw(){ctx.globalAlpha=1;ctx.clearRect(0,0,canvas.width,canvas.height);if(diff.checked)ctx.putImageData(delta,0,0);else{ctx.drawImage(a,0,0);ctx.globalAlpha=+opacity.value;ctx.drawImage(b,0,0);ctx.globalAlpha=1;}}
 opacity.oninput=draw;diff.onchange=draw;draw();save.disabled=false;
 save.onclick=()=>{const link=document.createElement('a');link.download=diff.checked?'diferencias.png':'superposicion.png';link.href=canvas.toDataURL();link.click();};
}).catch(error=>document.getElementById('status').textContent=String(error));
</script></html>'''.replace('URLS',json.dumps([data(reference),data(actual)]))


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('reference');p.add_argument('actual');p.add_argument('--output',required=True,type=Path)
    args=p.parse_args();args.output.write_text(report(args.reference,args.actual),encoding='utf-8')


if __name__=='__main__':main()
