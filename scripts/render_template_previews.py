from pathlib import Path
import json,subprocess
from PIL import Image
root=Path.cwd();sk=root/"skills/qp-brandbook";records=json.load(open('fontes-de-origem/local-assets.json'));reviews=json.load(open('fontes-de-origem/asset-reviews.json'))
for r in records:
    if not r['path'].endswith('.pdf'):continue
    src=sk/r['path'];dest=sk/"assets/previews"/(r['source_id']+"-pdf")
    subprocess.run(['pdftoppm','-f','1','-singlefile','-scale-to','720','-jpeg',str(src),str(dest)],check=True)
    thumb=str(dest.relative_to(sk))+".jpg"
    reviews[r['id']]={'preview_path':thumb};reviews.setdefault('drive:'+r['source_id'],{}).update({'preview_path':thumb})
Path('fontes-de-origem/asset-reviews.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2)+'\n')
