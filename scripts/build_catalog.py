"""Reconstrói índice e catálogo a partir de snapshots locais e arquivos reais."""
import collections, hashlib, html, json, pathlib, re, shutil, subprocess, sys, xml.etree.ElementTree as ET
from PIL import Image, ImageOps, ImageDraw
ROOT=pathlib.Path(__file__).resolve().parents[1]; SK=ROOT/"skills/qp-brandbook"
def read(p,default=None):
    f=ROOT/p
    return json.loads(f.read_text()) if f.exists() else default
def brand(s):
    s=s.lower()
    for key,terms in [("viajo-mucho",["viajo"]),("la-terminal",["la terminal","la-terminal"]),("teletiquete",["teletiquete"]),("rodon",["rodon"]),("grupo-quero-passagem",["grupo quero","grupo-quero","qp - group","qp-group"]),("sala-vip",["sala vip","sala-vip"]),("rodoviaria-bh",["rodoviaria","rodoviária"]),("quero-mais",["quero+","quero +"])]:
        if any(t in s for t in terms):return key
    return "quero-passagem"
def inspect_font(p):
    import struct
    raw=p.read_bytes();num=struct.unpack_from(">H",raw,4)[0];tables={}
    for i in range(num):
        tag,_,off,length=struct.unpack_from(">4sIII",raw,12+i*16);tables[tag.decode("latin1")]=(off,length)
    names={}
    if "name" in tables:
        off,_=tables["name"];_,cnt,storage=struct.unpack_from(">HHH",raw,off)
        for i in range(cnt):
            plat,enc,lang,nid,ln,pos=struct.unpack_from(">HHHHHH",raw,off+6+12*i)
            if nid in [1,2,4,6]:
                try:
                    text=raw[off+storage+pos:off+storage+pos+ln].decode("utf-16-be" if plat in [0,3] else "mac_roman")
                    names[str(nid)]=text
                except UnicodeError:pass
    def glyph(cp):
        if "cmap" not in tables:return False
        off,_=tables["cmap"];cnt=struct.unpack_from(">H",raw,off+2)[0]
        for i in range(cnt):
            plat,enc,sub=struct.unpack_from(">HHI",raw,off+4+i*8)
            if plat not in [0,3]:continue
            p=off+sub;fmt=struct.unpack_from(">H",raw,p)[0]
            if fmt==12:
                n=struct.unpack_from(">I",raw,p+12)[0]
                for j in range(n):
                    lo,hi,g=struct.unpack_from(">III",raw,p+16+j*12)
                    if lo<=cp<=hi and g+cp-lo:return True
            elif fmt==4 and cp<=65535:
                seg=struct.unpack_from(">H",raw,p+6)[0]//2;end=p+14;start=end+seg*2+2;delta=start+seg*2;ro=delta+seg*2
                for j in range(seg):
                    lo=struct.unpack_from(">H",raw,start+j*2)[0];hi=struct.unpack_from(">H",raw,end+j*2)[0]
                    if lo<=cp<=hi:
                        d=struct.unpack_from(">h",raw,delta+j*2)[0];r=struct.unpack_from(">H",raw,ro+j*2)[0]
                        g=struct.unpack_from(">H",raw,ro+j*2+r+(cp-lo)*2)[0] if r else cp
                        if (g+d)%65536 if g else 0:return True
        return False
    accents="ÁÉÍÓÚÀÂÊÔÃÕÇáéíóúàâêôãõç¿ñ"
    axes={}
    if "fvar" in tables:
        off,_=tables["fvar"];axesoff,_,cnt,axis_size=struct.unpack_from(">HHHH",raw,off+4)
        for i in range(cnt):
            tag,minimum,default,maximum=struct.unpack_from(">4siii",raw,off+axesoff+i*axis_size)
            axes[tag.decode()]={"min":minimum/65536,"default":default/65536,"max":maximum/65536}
    return {"names":names,"missing_glyphs":[c for c in accents if not glyph(ord(c))],"variable":"fvar" in tables,"axes":axes}
def main():
    assets=[];drive=read("fontes-de-origem/drive-inventory.json",{}) or {};files={f["id"]:f for f in drive.get("files",[])}
    for q in read("fontes-de-origem/drive-files.json",[]):
        f=files[q["id"]];a={"id":"drive:"+f["id"],"name":f["title"],"provider":"drive","source_id":f["id"],"source_url":f["url"],"brand":brand(f["collectionPath"]+" "+f["title"]),"category":pathlib.PurePosixPath(q["path"]).parts[3],"path":str(pathlib.PurePosixPath(q["path"]).relative_to("skills/qp-brandbook")),"mime":f["mime_type"],"tags":f["collectionPath"].split("/"),"usage":"historico" if "antigas" in f["collectionPath"].lower() else "revisar" if q["path"].split("/")[3]=="fotografia" else "documentado"}
        assets.append(a)
    for f in read("fontes-de-origem/page-media.json",[]):
        assets.append({"id":f["id"],"name":"Exemplo: "+", ".join(f["pages"]),"provider":"brand-navigator","source_url":f["source_url"],"brand":"quero-passagem","category":"referencias-paginas","path":str(pathlib.PurePosixPath(f["path"]).relative_to("skills/qp-brandbook")),"usage":"referencia","tags":f["pages"]})
    for f in read("fontes-de-origem/figma-graphics.json",[])+read("fontes-de-origem/figma-previews.json",[]):
        ispreview=not f.get("isGraphic",True);category="templates" if ispreview else f["category"]
        a={"id":"figma:"+f["fileKey"]+":"+f["id"],"name":f["name"],"provider":"figma","source_id":f["id"],"source_url":"https://www.figma.com/design/"+f["fileKey"]+"?node-id="+f["id"].replace(":","-"),"brand":f["category"] if ispreview else brand(f["name"]),"category":category,"usage":"referencia-template" if ispreview else "referencia" if f.get("type")=="FRAME" else "documentado","tags":[f["category"],f.get("type","")],"source_width":f["width"],"source_height":f["height"],"node_type":f.get("type"),"error":f.get("error")}
        if f.get("path"):a["path"]=str(pathlib.PurePosixPath(f["path"]).relative_to("skills/qp-brandbook"))
        assets.append(a)
    seen_ids=set();unique=[]
    for a in assets:
        if a["id"] in seen_ids:continue
        seen_ids.add(a["id"]);unique.append(a)
    assets=unique+read("fontes-de-origem/local-assets.json",[]);byhash={};fonts=[];errors=[]
    for a in assets:
        if not a.get("path") or not (p:=SK/a["path"]).exists():a["availability"]="missing";continue
        try:
            with p.open("rb")as probe: prefix=probe.read(80)
            if prefix.startswith(b"version https://git-lfs.github.com/spec/"):a["availability"]="lfs-pointer";continue
            a["bytes"]=p.stat().st_size
            with p.open("rb")as stream:a["sha256"]=hashlib.file_digest(stream,"sha256").hexdigest()
            a["availability"]="local";sha=a["sha256"]
            if sha in byhash:a["canonical_id"]=byhash[sha]
            else:byhash[sha]=a["id"]
            if p.suffix.lower() in [".png",".jpg",".jpeg",".webp",".gif"]:
                with Image.open(p)as im:
                    a["width"],a["height"]=im.size;im=ImageOps.exif_transpose(im);im.thumbnail((420,300))
                    if im.mode=="P":im=im.convert("RGBA")
                    if im.mode!="RGB":
                        bg=Image.new("RGB",im.size,"#e7edf3")
                        if "A"in im.getbands():bg.paste(im,mask=im.getchannel("A"))
                        else:bg.paste(im)
                        im=bg
                    thumb=SK/"assets/previews"/(sha[:24]+".jpg");thumb.parent.mkdir(exist_ok=True)
                    if not thumb.exists():im.convert("RGB").save(thumb,quality=78,optimize=True)
                    a["preview_path"]=str(thumb.relative_to(SK))
            elif p.suffix.lower()==".svg":
                e=ET.parse(p).getroot();a["width"]=e.get("width");a["height"]=e.get("height");a["preview_path"]=a["path"]
            elif p.suffix.lower() in [".ttf",".otf"]:
                info=inspect_font(p);fonts.append({"path":a["path"],**info,**{k:a[k]for k in ["css_family","css_weight"]if k in a}});a["font"]=info
        except Exception as e:
            errors.append({"id":a["id"],"error":str(e)});a["inspection_error"]=str(e)
    overrides=read("fontes-de-origem/asset-reviews.json",{})
    for a in assets:
        if a["id"] in overrides:a.update(overrides[a["id"]])
    index={"schema_version":1,"collected_at":"2026-10-29","path_base":"skill-root","assets":assets}
    (SK/"references/assets-index.json").write_text(json.dumps(index,ensure_ascii=False,indent=2)+"\n")
    (SK/"references/fonts-index.json").write_text(json.dumps(fonts,ensure_ascii=False,indent=2)+"\n")
    # Relative URLs resolve from assets/fonts.css.
    css=[]
    for a in assets:
        if a.get("availability")!="local" or not a.get("font"):continue
        n=a["name"].lower();family="Instrument Serif" if "instrument" in n else "Sora" if "sora" in n else "Inter" if "inter" in n else "Work Sans" if "worksans" in n or "work-sans" in n else "Poppins" if "poppins" in n else "Lilita One" if "lilitaone" in n else "Nunito" if "nunito" in n else "Bacalar Expanded" if "bacalar" in n else None
        if "bacalar" in n:family=a.get("css_family") or a["font"]["names"].get("1")
        if not family:continue
        css.append("@font-face{font-family:'"+family+"';src:url('./"+a["path"].removeprefix("assets/")+"');font-style:"+("italic"if"italic"in n else"normal")+";font-weight:"+((str(int(a["font"]["axes"]["wght"]["min"]))+" "+str(int(a["font"]["axes"]["wght"]["max"])))if "wght"in a["font"]["axes"] else str(a.get("css_weight",400)))+";font-display:swap;}")
    (SK/"assets/fonts.css").write_text("\n".join(css)+"\n")
    payload=json.dumps(index,ensure_ascii=False).replace("</","<\\/")
    template=(ROOT/"scripts/catalog-template.html").read_text();(ROOT/"catalogo/index.html").write_text(template.replace("__ASSET_DATA__",payload))
    counts=dict(collections.Counter(a["category"] for a in assets));local=sum(a.get("availability")=="local"for a in assets)
    summary={"items":len(assets),"local":local,"categories":counts,"missing":[a["id"]for a in assets if a.get("availability")!="local"],"duplicates":sum("canonical_id"in a for a in assets),"inspection_errors":errors}
    (ROOT/"fontes-de-origem/coverage.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
    known={q["id"] for q in read("fontes-de-origem/drive-files.json",[])}
    excluded=[{"id":f["id"],"name":f["title"],"source_url":f["url"],"mime":f["mime_type"],"collection":f["collectionPath"],"reason":"fonte-demo-trial" if "BACALAR"in f["collectionPath"] else "atalho-nao-resolvido" if "shortcut"in f["mime_type"] else "video-ou-original-de-producao-externo"}for f in files.values()if f["id"]not in known and "folder"not in f["mime_type"]]
    (ROOT/"fontes-de-origem/external-assets.json").write_text(json.dumps(excluded,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(summary,ensure_ascii=False))
if __name__=="__main__":main()
