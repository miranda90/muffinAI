"""Benchmark parsing/index load separately from warm validation and CLI startup."""
import argparse
import json
from pathlib import Path
import statistics
import subprocess
import sys
import time
from contracts import read_json
from validate_bebuilder_json import load_schema, validate


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('files',nargs='+');p.add_argument('--runs',type=int,default=5)
    args=p.parse_args()
    if args.runs<1:p.error('runs debe ser positivo')
    start=time.perf_counter();schema=load_schema();catalog_ms=(time.perf_counter()-start)*1000
    results=[]
    for filename in args.files:
        doc=read_json(filename);warm=[];cold=[]
        for _ in range(args.runs):
            start=time.perf_counter();result=validate(doc,schema);warm.append((time.perf_counter()-start)*1000)
            start=time.perf_counter();subprocess.run([sys.executable,str(Path(__file__).with_name('validate_bebuilder_json.py')),filename,'--json'],stdout=subprocess.DEVNULL,check=False);cold.append((time.perf_counter()-start)*1000)
        results.append({'file':filename,'warm_median_ms':statistics.median(warm),'cli_median_ms':statistics.median(cold),'stats':result['stats'],'bytes':Path(filename).stat().st_size})
    print(json.dumps({'catalog_load_ms':catalog_ms,'runs':args.runs,'results':results},indent=2))


if __name__=='__main__':main()
