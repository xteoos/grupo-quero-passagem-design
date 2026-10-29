"""Valida integridade, referências e dependências sem publicar ou corrigir arquivos."""
import argparse, hashlib, json, pathlib, re, shutil, sys, urllib.parse, xml.etree.ElementTree as ET, zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1];SK=ROOT/"skills/qp-brandbook"
def inspect_file(p,expected=None):
    if not p.is_file():return "missing"
    with p.open("rb")as f:prefix=f.read(100)
    if prefix.startswith(b"version https://git-lfs.github.com/spec/v1"):return "lfs-pointer"
    if not p.stat().st_size:return "empty"
    if expected:
        with p.open("rb")as f:digest=hashlib.file_digest(f,"sha256").hexdigest()
        if digest!=expected:return "hash-mismatch"
    return None
def validate(root=ROOT):
    sk=root/"skills/qp-brandbook";errors=[];warnings=[];index=json.loads((sk/"references/assets-index.json").read_text());ids=set()
    for a in index["assets"]:
        if a["id"]in ids:errors.append(a["id"]+": duplicate-id")
        ids.add(a["id"])
        if not a.get("path"):
            warnings.append(a["id"]+": preview indisponível na coleta; consultar origem");continue
        p=(sk/a["path"]).resolve()
        if not p.is_relative_to(sk.resolve()):errors.append(a["id"]+": path-outside-skill");continue
        result=inspect_file(p,a.get("sha256"))
        if result:errors.append(a["id"]+": "+result);continue
        if p.suffix.lower()==".svg":
            try:ET.parse(p)
            except ET.ParseError:errors.append(a["id"]+": invalid-svg")
        if p.suffix.lower() in [".pptx",".docx"]:
            try:
                with zipfile.ZipFile(p)as z:
                    if z.testzip():errors.append(a["id"]+": corrupt-office-zip")
                    if "[Content_Types].xml"not in z.namelist():errors.append(a["id"]+": invalid-office-package")
            except zipfile.BadZipFile:errors.append(a["id"]+": invalid-office-zip")
        if a.get("font",{}).get("missing_glyphs"):warnings.append(a["id"]+": glifos ausentes: "+str(a["font"]["missing_glyphs"]))
        if re.search("bacalartest|trial|demo",a["name"],re.I)and a["category"]=="fontes":errors.append(a["id"]+": trial-font-in-production")
    for doc in sk.rglob("*.md"):
        for link in re.findall(r"\]\(([^)]+)\)",doc.read_text()):
            if re.match(r"[a-z]+:|#",link,re.I):continue
            path=urllib.parse.unquote(link.split("#")[0])
            if path and not(doc.parent/path).exists():errors.append(str(doc.relative_to(sk))+": broken-link "+link)
    font_names=" ".join(str(a.get("font",{}).get("names",{}))for a in index["assets"]).lower()
    for family,pattern in [("Bacalar Expanded","bacalar"),("Mauren","mauren"),("All Round Gothic","all round")]:
        if pattern not in font_names:warnings.append(family+" completa pendente para os templates que a exigem.")
    if not shutil.which("git-lfs"):warnings.append("Git LFS não encontrado neste ambiente; instalar antes de adicionar os originais ao Git.")
    return {"integrity_pass":not errors,"errors":errors,"warnings":warnings,"assets":len(index["assets"]),"local":sum(a.get("availability")=="local"for a in index["assets"])}
def main():
    p=argparse.ArgumentParser();p.add_argument("--strict",action="store_true");a=p.parse_args();r=validate();print(json.dumps(r,ensure_ascii=False,indent=2));sys.exit(1 if r["errors"]else 2 if a.strict and r["warnings"]else 0)
if __name__=="__main__":main()
