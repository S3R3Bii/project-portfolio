"""Reproduce in a new directory without replacing the retained experiment."""
from pathlib import Path
import argparse, shutil, subprocess, sys

parser=argparse.ArgumentParser()
parser.add_argument('--output',required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parent
target=Path(args.output).resolve()
if target.exists():
    raise SystemExit('Choose a new output directory; existing results are never replaced.')
target.mkdir(parents=True)
for name in ['fetch_sources.py','pipeline.py','audit.py','build_artifacts.py','PROTOCOL.md','requirements.txt']:
    shutil.copy2(root/name,target/name)
for command in [['fetch_sources.py'],['pipeline.py','prepare'],['pipeline.py','train'],['pipeline.py','evaluate'],['audit.py'],['build_artifacts.py']]:
    subprocess.run([sys.executable,*command],cwd=target,check=True)
print(f'Reproduced artifacts: {target}')
