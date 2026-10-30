"""Testa o ZIP leve contra a base local, sem GitHub e sem instalar a skill globalmente."""
import hashlib,json,pathlib,subprocess,sys,tempfile,zipfile
R=pathlib.Path(__file__).resolve().parents[1]
def main():
 package=R/'distribution/qp-brandbook.zip';bundle=json.loads((R/'distribution/brandbook-bundle.json').read_text());retired=json.loads((R/'fontes-de-origem/retirados-do-catalogo.json').read_text())
 assert all(a['path']not in bundle['files']for a in retired)
 with tempfile.TemporaryDirectory()as d:
  with zipfile.ZipFile(package)as z:
   assert not any('/assets/'in n for n in z.namelist());z.extractall(d)
  s=pathlib.Path(d)/'qp-brandbook'
  def run(*args):return json.loads(subprocess.check_output([sys.executable,str(s/'scripts/remote_assets.py'),*args],text=True))
  first=run('sync','--local-root',str(R));assert first['mode']=='local-review';assert run('sync')['mode']=='local-review'
  r=run('find','--brand','quero-passagem','--category','stickers','--query','Chinelos');assert r['total']==1;run('get','--id',r['assets'][0]['id'])
  assert run('find','--brand','quero-passagem','--category','fundos')['total']==0
  assert run('find','--brand','quero-passagem','--category','pranchas-de-elementos')['total']==0
  assert run('find','--brand','quero-passagem','--category','ilustracoes')['total']==6
  profiles=json.loads((s/'references/social/familias.json').read_text())['profiles'];assert profiles[0]['id']=='qp-metas-viagem'
  run('get','--path','assets/fonts.css');assert(s/'assets/fonts.css').exists()
  report={'mode':'local-review','network_required':False,'github_updated':False,'sync':first,'local_mode_preserved':True,'retired_files_absent_from_manifest':len(retired),'qp_stickers':run('find','--brand','quero-passagem','--category','stickers')['total'],'city_illustrations':6,'profile_available':True,'individual_sticker_loaded':True,'fonts_and_css_materialized':True,'zip_bytes':package.stat().st_size,'zip_sha256':hashlib.sha256(package.read_bytes()).hexdigest()}
  (R/'validacao/metas-viagem/package-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':main()
