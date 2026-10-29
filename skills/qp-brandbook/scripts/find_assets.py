"""Busca offline no acervo; executar a partir de qualquer diretório."""
import argparse,json,pathlib
SK=pathlib.Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser();p.add_argument("--brand");p.add_argument("--category");p.add_argument("--usage");p.add_argument("--id");p.add_argument("--query",default="");p.add_argument("--limit",type=int,default=20);a=p.parse_args()
    rows=json.loads((SK/"references/assets-index.json").read_text())["assets"]
    rows=[r for r in rows if all(not v or r.get(k)==v for k,v in [("brand",a.brand),("category",a.category),("usage",a.usage),("id",a.id)])and a.query.lower()in(str(r.get("name",""))+" "+" ".join(r.get("tags",[]))).lower()]
    print(json.dumps({"total":len(rows),"path_base":str(SK),"assets":[{k:v for k,v in r.items()if k in ["id","name","brand","category","usage","path","availability","source_url","source_width","source_height","review_note","canonical_id"]}for r in rows[:a.limit]]},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
