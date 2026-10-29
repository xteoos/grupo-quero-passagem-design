"""Materializa URLs temporárias fornecidas pelos conectores; nunca versionar a fila."""
import argparse, concurrent.futures, hashlib, json, os, pathlib, sys, time, urllib.request, urllib.error
ROOT=pathlib.Path(__file__).resolve().parents[1]
def download(item):
    out=ROOT/item["path"]
    try:
        if not out.resolve().is_relative_to(ROOT): raise ValueError("Caminho fora do repositório")
        out.parent.mkdir(parents=True,exist_ok=True)
        existing_valid=out.is_file() and out.stat().st_size>0 and (not item.get("size") or out.stat().st_size==int(item["size"]))
        if existing_valid:
            with out.open("rb")as probe:existing_valid=not probe.read(80).startswith(b"version https://git-lfs.github.com/spec/v1")
        if not existing_valid:
            error=None
            for attempt in range(3):
                try:
                    req=urllib.request.Request(item["download_url"],headers={"User-Agent":"QP-Brandbook-Local/1.0"})
                    with urllib.request.urlopen(req,timeout=180) as r, open(str(out)+".part","wb") as w:
                        while chunk:=r.read(1024*1024): w.write(chunk)
                    if item.get("size") and pathlib.Path(str(out)+".part").stat().st_size!=int(item["size"]): raise ValueError("Tamanho divergente")
                    if not pathlib.Path(str(out)+".part").stat().st_size:raise ValueError("Resposta vazia")
                    os.replace(str(out)+".part",out);error=None;break
                except Exception as e:
                    error=str(e).split("?")[0]
                    if isinstance(e,urllib.error.HTTPError)and e.code in [401,403]:break
                    time.sleep(attempt+1)
            if error: raise RuntimeError(error)
        return {"id":item["id"],"path":item["path"],"status":"downloaded","bytes":out.stat().st_size,"sha256":hashlib.file_digest(open(out,"rb"),"sha256").hexdigest()}
    except Exception as e: return {"id":item["id"],"path":item["path"],"status":"error","error":str(e).split("?")[0]}
def main():
    p=argparse.ArgumentParser();p.add_argument("--queue",default=".cache/transfers.json");p.add_argument("--workers",type=int,default=8);a=p.parse_args()
    items=json.loads((ROOT/a.queue).read_text());results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:
        futures=[pool.submit(download,item)for item in items]
        for i,future in enumerate(concurrent.futures.as_completed(futures),1):
            r=future.result()
            results.append(r)
            if i%20==0 or r["status"]=="error": print(i,len(items),r["status"],r["id"],flush=True)
    (ROOT/(".cache/"+pathlib.Path(a.queue).stem+"-results.json")).write_text(json.dumps(results,ensure_ascii=False,indent=2))
    print(json.dumps({"total":len(results),"downloaded":sum(r["status"]=="downloaded" for r in results),"errors":[r for r in results if r["status"]=="error"]},ensure_ascii=False))
    if any(r["status"]=="error"for r in results):sys.exit(1)
if __name__=="__main__": main()
