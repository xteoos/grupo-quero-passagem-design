"""Acervo público sob demanda. Apenas biblioteca padrão; não exige Git/LFS."""
import argparse,concurrent.futures,hashlib,json,pathlib,re,tempfile,urllib.request,urllib.parse,sys
SK=pathlib.Path(__file__).resolve().parents[1]
REPO='xteoos/grupo-quero-passagem-design'
PREFIX='skills/qp-brandbook/'
STATE='.remote-state.json'
def request(url):
    req=urllib.request.Request(url,headers={'User-Agent':'qp-brandbook/1','Accept':'application/vnd.github+json' if 'api.github.com' in url else '*/*'})
    with urllib.request.urlopen(req,timeout=90)as response:return response.read()
def local(root,path):
    p=(root/path).resolve()
    if not p.is_relative_to(root.resolve())or pathlib.PurePosixPath(path).is_absolute():raise ValueError('Caminho fora da skill: '+path)
    return p
def raw(commit,path,lfs=False):
    host='https://media.githubusercontent.com/media/' if lfs else 'https://raw.githubusercontent.com/'
    return host+REPO+'/'+commit+'/'+urllib.parse.quote(path,safe='/')
def sync(root=SK):
    commit=json.loads(request('https://api.github.com/repos/'+REPO+'/commits/main'))['sha']
    if not re.fullmatch('[a-f0-9]{40}',commit):raise ValueError('Revisão GitHub inválida')
    bundle=json.loads(request(raw(commit,'distribution/brandbook-bundle.json')))
    if bundle.get('schema_version')!=1:raise ValueError('Atualize o pacote da skill: versão do catálogo incompatível')
    # Uma revisão por sessão: regras, catálogo e downloads vêm do mesmo commit.
    references=bundle['references']
    for name,content in references.items():
        if not name.startswith('references/')or not name.endswith(('.md','.json')):raise ValueError('Referência inválida')
        local(root,name)
    for name,content in references.items():
        p=local(root,name);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
    state={'commit':commit,'files':bundle['files']}
    local(root,STATE).write_text(json.dumps(state,ensure_ascii=False))
    return {'commit':commit,'references':len(references),'available_files':len(bundle['files'])}
def state(root):
    p=root/STATE
    if not p.exists():sync(root)
    return json.loads(p.read_text())
def fetch(path,root=SK,seen=None):
    seen=seen if seen is not None else set()
    if path in seen:return
    seen.add(path);s=state(root)
    if path not in s['files']:raise ValueError('Arquivo não catalogado: '+path)
    meta=s['files'][path];p=local(root,path)
    if not p.exists()or hashlib.sha256(p.read_bytes()).hexdigest()!=meta['sha256']:
        data=request(raw(s['commit'],PREFIX+path,meta['lfs']))
        if data.startswith(b'version https://git-lfs.github.com/spec/v1'):raise ValueError('GitHub retornou ponteiro LFS em vez do original: '+path)
        if len(data)!=meta['bytes']or hashlib.sha256(data).hexdigest()!=meta['sha256']:raise ValueError('Arquivo recebido não passou na integridade: '+path)
        p.parent.mkdir(parents=True,exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=p.parent,delete=False)as f:f.write(data);tmp=pathlib.Path(f.name)
        try:tmp.replace(p)
        finally:tmp.unlink(missing_ok=True)
    # Materializa dependências locais de HTML/CSS portáveis, sem reescrever os originais.
    if p.suffix in ['.html','.css']:
        text=p.read_text()
        deps=re.findall(r'(?:src|href)=[\"\']([^\"\']+)',text)if p.suffix=='.html'else re.findall(r'url\([\"\']?([^\"\')]+)',text)
        for url in deps:
            if urllib.parse.urlsplit(url).scheme or url.startswith(('#','//','data:')):continue
            dep=local(root,str(pathlib.PurePosixPath(path).parent/urllib.parse.unquote(url.split('?')[0])))
            fetch(dep.relative_to(root.resolve()).as_posix(),root,seen)
    return str(p)
def rows(root=SK):return json.loads((root/'references/assets-index.json').read_text())['assets']
def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('sync');find=sub.add_parser('find')
    for flag in ['brand','category','query']:find.add_argument('--'+flag,default='')
    find.add_argument('--limit',type=int,default=20)
    get=sub.add_parser('get');group=get.add_mutually_exclusive_group(required=True);group.add_argument('--id',action='append');group.add_argument('--path');group.add_argument('--preview')
    a=p.parse_args()
    try:
        if a.command=='sync':result=sync()
        elif a.command=='find':
            state(SK);r=[x for x in rows()if(not a.brand or x['brand']==a.brand)and(not a.category or x['category']==a.category)and a.query.lower()in json.dumps(x,ensure_ascii=False).lower()]
            result={'total':len(r),'assets':[dict(x,cached=local(SK,x['path']).exists())for x in r[:a.limit]]}
        else:
            state(SK);index={x['id']:x for x in rows()}
            paths=[a.path]if a.path else [index[a.preview]['preview_path']]if a.preview else[index[i]['path']for i in a.id]
            result={'commit':state(SK)['commit'],'files':[fetch(path)for path in paths]}
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except Exception as e:print('Não foi possível obter o acervo: '+str(e)+'. Verifique o acesso à internet/GitHub. Não substituir o material ausente.',file=sys.stderr);sys.exit(1)
if __name__=='__main__':main()
