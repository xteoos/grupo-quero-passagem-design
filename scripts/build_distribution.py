"""Gera catálogo remoto e ZIP leve, excluindo o acervo binário da instalação."""
import hashlib,json,pathlib,subprocess,zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1];SK=ROOT/'skills/qp-brandbook';OUT=ROOT/'distribution'
def main():
    OUT.mkdir(exist_ok=True)
    refs={p.relative_to(SK).as_posix():p.read_text()for p in sorted((SK/'references').rglob('*'))if p.is_file()and p.suffix in ['.md','.json']}
    files={}
    indexed={a['path']:a for a in json.loads((SK/'references/assets-index.json').read_text())['assets']}
    allowed=set(indexed)|{a['preview_path']for a in indexed.values()if a.get('preview_path')}|{'assets/fonts.css'}
    for p in sorted((SK/'assets').rglob('*')):
        if not p.is_file():continue
        rel=p.relative_to(SK).as_posix()
        if rel not in allowed:continue
        a=indexed.get(rel)
        attr=subprocess.check_output(['git','check-attr','filter','--',str(p.relative_to(ROOT))],cwd=ROOT,text=True)
        files[rel]={'sha256':a['sha256']if a else hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'lfs':attr.rstrip().endswith(': lfs')}
    bundle={'schema_version':1,'repository':'xteoos/grupo-quero-passagem-design','references':refs,'files':files}
    (OUT/'brandbook-bundle.json').write_text(json.dumps(bundle,ensure_ascii=False,separators=(',',':'))+'\n')
    target=OUT/'qp-brandbook.zip'
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
        for p in sorted(SK.rglob('*')):
            rel=p.relative_to(SK)
            if p.is_file()and(rel.parts[0]in['references','agents','scripts']or str(rel)=='SKILL.md')and '__pycache__'not in rel.parts:
                info=zipfile.ZipInfo('qp-brandbook/'+rel.as_posix(),date_time=(2026,10,30,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;z.writestr(info,p.read_bytes())
    print(json.dumps({'zip_bytes':target.stat().st_size,'remote_files':len(files),'references':len(refs)}))
if __name__=='__main__':main()
