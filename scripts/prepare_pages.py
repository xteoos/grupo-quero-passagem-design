"""Converte o snapshot oficial para referências legíveis e prepara mídias públicas."""
import concurrent.futures, hashlib, html, json, pathlib, re, urllib.parse, urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1];SK=ROOT/"skills/qp-brandbook"
def walk(v):
    if isinstance(v,dict):
        for k,x in v.items():
            if isinstance(x,str): yield k,x
            elif isinstance(x,(dict,list)): yield from walk(x)
    elif isinstance(v,list):
        for x in v: yield from walk(x)
def main():
    snap=json.loads((ROOT/"fontes-de-origem/brand-navigator.json").read_text()); media={};pages=[]
    for a in snap["areas"]:
        for p in a["pages"]:
            lines=["# "+p["title"],"",f"Fonte: Brand Navigator /{a['slug']}/{p['slug']}. Atualização na origem: {p['updated_at']}.","","> Transcrição da página publicada. Exemplos de interface e dados ilustrativos permanecem exemplos; não são políticas comerciais.",""]
            for b in p["blocks"]:
                lines+=["",f"<!-- bloco {b['sort_order']} · {b['id']} · {b['type']} -->",""]
                for k,s in walk(b["content"]):
                    if k=="html":lines += [s,""]
                    elif k in ("title","text","caption","label","alt") and s.strip():lines += [s,""]
                    if s.startswith(snap["source"]+"/storage/") and re.search(r"\.(png|jpe?g|webp|svg|gif)(\?|$)",s,re.I):
                        uid=hashlib.sha256(s.encode()).hexdigest()[:20];ext=pathlib.PurePosixPath(urllib.parse.urlparse(s).path).suffix.lower()
                        path=f"skills/qp-brandbook/assets/referencias-paginas/{uid}{ext}"
                        media.setdefault(s,{"id":"page-"+uid,"path":path,"download_url":s,"pages":[]})
                        if p["slug"] not in media[s]["pages"]:media[s]["pages"].append(p["slug"])
                        if k in ("url","src"):lines += [f"![Exemplo visual da página](../../../assets/referencias-paginas/{uid}{ext})",""]
                    elif s.startswith("http") and k in ("url","href"):lines += [f"[Recurso na origem]({s})",""]
            dest=SK/"references/paginas"/a["slug"]/(p["slug"]+".md");dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text("\n".join(lines),encoding="utf8")
            pages.append({"area":a["slug"],"slug":p["slug"],"title":p["title"],"blocks":len(p["blocks"]),"path":str(dest.relative_to(ROOT))})
    queue=list(media.values());(ROOT/".cache/page-transfers.json").write_text(json.dumps(queue))
    (ROOT/"fontes-de-origem/page-media.json").write_text(json.dumps([{k:v for k,v in x.items() if k!="download_url"}|{"source_url":u} for u,x in media.items()],ensure_ascii=False,indent=2))
    (ROOT/"fontes-de-origem/pages-index.json").write_text(json.dumps(pages,ensure_ascii=False,indent=2))
    index=["# Páginas oficiais extraídas",""]+[f"- [{p['title']}]({p['area']}/{p['slug']}.md) — {p['area']}" for p in pages]
    (SK/"references/paginas/INDEX.md").write_text("\n".join(index)+"\n")
    print(json.dumps({"pages":len(pages),"images":len(media)}))
if __name__=="__main__":main()
