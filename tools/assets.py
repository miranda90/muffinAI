"""Inventory local assets, register destination attachments, optimize video explicitly."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import struct
import subprocess
import xml.etree.ElementTree as ET
from contracts import atomic_json, read_json, validate_manifest


def inventory(path):
    path=Path(path);raw=path.read_bytes()
    record={'local':path.name,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'format':path.suffix.lower().lstrip('.')}
    if raw.startswith(b'\x89PNG\r\n\x1a\n') and len(raw)>=24:
        record['width'],record['height']=struct.unpack('>II',raw[16:24])
    elif path.suffix.lower()=='.svg':
        root=ET.fromstring(raw)
        record['viewBox']=root.get('viewBox')
        record['intrinsic_width']=root.get('width');record['intrinsic_height']=root.get('height')
    elif shutil.which('ffprobe'):
        process=subprocess.run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)],text=True,capture_output=True)
        if process.returncode==0:
            probe=json.loads(process.stdout)
            for stream in probe.get('streams',[]):
                if stream.get('codec_type')=='video':
                    record.update(width=stream.get('width'),height=stream.get('height'));break
            record['duration']=probe.get('format',{}).get('duration')
    return record


def optimize_video(source,output,background=False):
    source,output=Path(source).resolve(),Path(output).resolve()
    if source==output or output.exists():raise ValueError('La salida debe ser nueva; se conserva el original')
    if not shutil.which('ffmpeg'):raise ValueError('Instalar ffmpeg para optimizar vídeo')
    command=['ffmpeg','-nostdin','-n','-i',str(source),'-vf',"scale=w='min(1920,iw)':h='min(1080,ih)':force_original_aspect_ratio=decrease:force_divisible_by=2",'-c:v','libx264','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart']
    command+=['-an'] if background else ['-c:a','aac','-b:a','128k']
    subprocess.run(command+[str(output)],check=True)


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='action',required=True)
    inv=sub.add_parser('inventory');inv.add_argument('files',nargs='+');inv.add_argument('--output',required=True)
    reg=sub.add_parser('register');reg.add_argument('file',type=Path);reg.add_argument('--manifest',type=Path,required=True);reg.add_argument('--id',type=int,required=True);reg.add_argument('--url',required=True);reg.add_argument('--name')
    vid=sub.add_parser('video');vid.add_argument('file');vid.add_argument('--output',required=True);vid.add_argument('--background',action='store_true')
    args=p.parse_args()
    if args.action=='inventory':atomic_json(args.output,[inventory(x) for x in args.files])
    elif args.action=='register':
        manifest=read_json(args.manifest) if args.manifest.exists() else {}
        root=args.manifest.resolve().parent
        file=args.file.resolve()
        if not file.is_relative_to(root):raise ValueError('El asset debe estar dentro del directorio del manifest')
        record=inventory(file);record.update(local=str(file.relative_to(root)),id=args.id,url=args.url)
        manifest[args.name or file.name]=record
        validate_manifest(manifest,root=root);atomic_json(args.manifest,manifest)
    else:optimize_video(args.file,args.output,args.background)


if __name__=='__main__':main()
