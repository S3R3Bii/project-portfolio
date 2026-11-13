"""Download pinned public inputs; never require API keys or remote code execution."""
from pathlib import Path
from urllib.request import urlopen, Request
from datetime import datetime, timezone
import hashlib, json

ROOT=Path(__file__).resolve().parent
DATA_COMMIT='57ec275d8078af65b7731c2a98be812d844a6d6b'
MODEL_COMMIT='1110a243fdf4706b3f48f1d95db1a4f5529b4d41'
sources={
 'data/raw/train.csv':f'https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets/{DATA_COMMIT}/banking_data/train.csv',
 'data/raw/test.csv':f'https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets/{DATA_COMMIT}/banking_data/test.csv',
 'data/raw/LICENSE_BANKING77.txt':f'https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets/{DATA_COMMIT}/LICENSE',
 'data/raw/README_BANKING77.md':f'https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets/{DATA_COMMIT}/README.md',
 'data/models/tokenizer.json':f'https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/{MODEL_COMMIT}/tokenizer.json',
 'data/models/model.onnx':f'https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/{MODEL_COMMIT}/onnx/model.onnx',
 'data/models/README_MODEL.md':f'https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/{MODEL_COMMIT}/README.md',
}
def main():
    manifest=[]
    for rel,url in sources.items():
        p=ROOT/rel; p.parent.mkdir(parents=True,exist_ok=True)
        if not p.exists():
            temp=p.with_suffix(p.suffix+'.part')
            with urlopen(Request(url,headers={'User-Agent':'BankingIntentAtlas/1.0 (public reproducibility study)'}),timeout=90) as response,temp.open('wb') as f:
                while chunk:=response.read(1024*1024): f.write(chunk)
            temp.replace(p)
        h=hashlib.sha256(p.read_bytes()).hexdigest()
        manifest.append({'path':rel,'url':url,'bytes':p.stat().st_size,'sha256':h})
        print(rel,p.stat().st_size,h,flush=True)
    (ROOT/'outputs').mkdir(exist_ok=True)
    (ROOT/'outputs/source_manifest.json').write_text(json.dumps({'retrieved_utc':datetime.now(timezone.utc).isoformat(),'sources':manifest},indent=2),encoding='utf-8')
if __name__=='__main__': main()
