"""Exemplos HTML editáveis derivados da geometria dos modelos PPTX; não altera os originais."""
import hashlib, html, json, pathlib
from pptx import Presentation
from pptx.enum.dml import MSO_COLOR_TYPE
ROOT=pathlib.Path(__file__).resolve().parents[1];SK=ROOT/"skills/qp-brandbook";OUT=ROOT/"validacao/exemplos"
FONT_CSS="../../skills/qp-brandbook/assets/fonts.css"
def css_font(name):
    s=name or"Sora";weight=200 if"ExtraLight"in s else 300 if"Light"in s else 600 if"SemiBold"in s else 500 if"Medium"in s else 700 if"Bold"in s else 400
    family="Sora" if"Sora"in s else"Inter"if"Inter"in s else"Instrument Serif"if"Instrument"in s else s
    return family,weight
def rgb(color,default="#0D2240"):
    try:
        if color.type==MSO_COLOR_TYPE.RGB:return "#"+str(color.rgb)
    except (AttributeError,TypeError):pass
    return default
def text_style(run,pixel_scale=1):
    font=run.font;family,weight=css_font(font.name)
    return "font-family:'"+family+"';font-weight:"+str(700 if font.bold else weight)+";font-size:"+str(font.size.pt*96/72*pixel_scale if font.size else 24*pixel_scale)+"px;color:"+rgb(font.color)+";font-style:"+("italic"if font.italic else"normal")
def render_slide(prs,sl,texts,title):
    scale=960/prs.slide_width;parts=[];text_i=0
    try:bg=rgb(sl.background.fill.fore_color,"#FFFFFF")
    except:bg="#FFFFFF"
    for owner in [sl,sl.slide_layout,sl.slide_layout.slide_master]:
        blips=owner._element.xpath('./p:cSld/p:bg/p:bgPr/a:blipFill/a:blip')
        if blips:
            rid=blips[0].get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed');part=owner.part.related_part(rid)
            name=hashlib.sha256(part.blob).hexdigest()[:20]+pathlib.Path(str(part.partname)).suffix
            (OUT/'assets'/name).write_bytes(part.blob)
            parts.append(f'<img alt="Fundo original do modelo" src="assets/{name}" style="position:absolute;inset:0;width:100%;height:100%">');break
    for shape in sl.shapes:
        x,y,w,h=[v*scale for v in [shape.left,shape.top,shape.width,shape.height]];style=f"position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;"
        if getattr(shape,"image",None):
            image=shape.image;name=hashlib.sha256(image.blob).hexdigest()[:20]+"."+image.ext;p=OUT/"assets"/name;p.parent.mkdir(exist_ok=True);p.write_bytes(image.blob)
            l,t,r,b=shape.crop_left,shape.crop_top,shape.crop_right,shape.crop_bottom
            parts.append(f'<div style="{style}overflow:hidden"><img alt="Elemento original do template" src="assets/{name}" style="position:absolute;left:{-l/(1-l-r)*100}%;top:{-t/(1-t-b)*100}%;width:{100/(1-l-r)}%;height:{100/(1-t-b)}%"></div>');continue
        if shape.has_text_frame:
            if not shape.text.strip():continue
            value=texts[text_i]if text_i<len(texts)else shape.text;text_i+=1
            tf=shape.text_frame;paragraph=tf.paragraphs[0];runs=paragraph.runs;run=runs[0]if runs else None;align="center"if str(paragraph.alignment).startswith("CENTER")else"right"if str(paragraph.alignment).startswith("RIGHT")else"left"
            ts=text_style(run,960/(prs.slide_width/914400*96))if run else"font:400 24px Sora";mt=tf.margin_top*scale;ml=tf.margin_left*scale;mr=tf.margin_right*scale
            parts.append(f'<div class="editable" contenteditable="true" spellcheck="false" style="{style}{ts};text-align:{align};padding:{mt}px {mr}px 0 {ml}px;line-height:1.25;white-space:pre-wrap;overflow:visible">{html.escape(value)}</div>');continue
        try:
            if shape.fill.type is not None:parts.append(f'<div style="{style}background:{rgb(shape.fill.fore_color,"transparent")};"></div>')
        except (AttributeError,TypeError):pass
    return f'<section class="slide" aria-label="{html.escape(title)}" style="height:{prs.slide_height*scale}px;background:{bg}">'+''.join(parts)+"</section>"
def document(title,body,note):
    return f'<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>{html.escape(title)}</title><link rel="stylesheet" href="{FONT_CSS}"><style>*{{box-sizing:border-box}}body{{margin:0;background:#e7edf3;font-family:Inter,sans-serif;color:#0d2240}}header{{width:960px;padding:22px 0;margin:auto;font-size:14px;line-height:1.6}}.slide{{position:relative;width:960px;margin:0 auto 26px;overflow:hidden;background:white}}.editable:focus{{outline:2px solid #0066c6}}img{{display:block}}@media print{{body{{background:white}}header{{display:none}}.slide{{margin:0;break-after:page}}@page{{size:10in 5.625in;margin:0}}}}</style><header><strong>{html.escape(title)}</strong><br>{html.escape(note)}</header>{body}</html>'
def main():
    OUT.mkdir(parents=True,exist_ok=True);(OUT/"assets").mkdir(exist_ok=True)
    source=next((SK/"assets/templates/apresentacoes").glob("*modelo*"));prs=Presentation(source)
    selections=[(0,["Design","Clareza para criar." ]),(1,["Comece pelo público","Defina o objetivo, o canal e o formato.\nEscolha o modelo e os arquivos da marca.\nConfira a peça antes de compartilhar."]),(2,["Uma voz próxima","Clareza, cuidado e confiança."]),(3,["Cores com contexto","Escolha a paleta conforme a aplicação."])]
    deck="".join(render_slide(prs,prs.slides[i],texts,"Slide "+str(j+1))for j,(i,texts)in enumerate(selections))
    (OUT/"apresentacao-qp.html").write_text(document("Apresentação QP · exemplo local",deck,"Derivada do modelo oficial. Texto editável no navegador. Geometria importada do PPTX; validar diferenças de renderização antes de uso."),encoding="utf8")
    source_comm=next((SK/"assets/templates/recursos").glob("*comunicados*"));comm=Presentation(source_comm)
    text="Exemplo de comunicado interno.\n\nExplique a mudança e o próximo passo. Complete os detalhes com a área responsável antes de compartilhar."
    body=render_slide(comm,comm.slides[0],[text,"Um novo processo"],"Comunicado")
    (OUT/"comunicado-qp.html").write_text(document("Comunicado QP · exemplo local",body,"Modelo oficial preservado como referência. Não é anúncio de uma mudança real e não contém datas ou políticas inventadas."),encoding="utf8")
    index=json.loads((SK/"references/assets-index.json").read_text())["assets"]
    logo=next(a for a in index if a["provider"]=="figma"and a["category"]=="logos"and"COLOR"in a["name"]and"horizontal - color"in a["name"])
    photo=next(a for a in index if a["category"]=="fotografia"and a["path"].endswith(".png")and"jessy"in a["path"])
    lp="../../skills/qp-brandbook/"+logo["path"];pp="../../skills/qp-brandbook/"+photo["path"]
    post=f'<section class="slide" style="width:720px;height:900px;background:#0D2240"><div style="position:absolute;left:54px;top:54px;width:612px;height:500px;background:#0066C6;border-radius:30px;overflow:hidden"><img src="{pp}" alt="Recorte oficial do ensaio Jessy" style="width:100%;height:100%;object-fit:contain"></div><div class="editable" contenteditable="true" style="position:absolute;left:54px;top:610px;color:white;font:300 42px/1.25 Sora;width:600px">O que você quer<br><em style="font-family:Instrument Serif;font-weight:400;color:#FFCC00">te move.</em></div><img src="{lp}" alt="Quero Passagem" style="position:absolute;left:54px;bottom:40px;width:220px;filter:brightness(0) invert(1)"></section>'
    # Use an official negative logo instead of recoloring an image.
    neg=next(a for a in index if a["provider"]=="figma"and a["category"]=="logos"and"WHITE"in a["name"]and"qp - horizontal"in a["name"])
    post=post.replace(lp,"../../skills/qp-brandbook/"+neg["path"]).replace(";filter:brightness(0) invert(1)","")
    (OUT/"post-qp.html").write_text(document("Post QP · estudo com fundamentos",post,"Estudo de composição com Sora Light + Instrument Serif Italic, cores normativas e arquivos oficiais. Não é reprodução do frame QP 1:1759, que exige Bacalar e usa outras cores."),encoding="utf8")
    cases=[{"file":"apresentacao-qp.html","source":"drive:1r80HtAMd2PTflVlzT-HXWC1xjIuEff-A3lP8uknESHo","source_slides":[i+1 for i,_ in selections],"status":"render-required"},{"file":"comunicado-qp.html","source":"drive:19lgUrEMkv7sYomWGXFMwfuqQQKP6mKlI3aBxlS94Fao","source_slides":[1],"status":"render-required"},{"file":"post-qp.html","source":"paginas/fundamentos/tipografia.md","assets":[neg["id"],photo["id"]],"status":"render-required"}]
    for key,family,source_id in [("viajo-mucho","Mauren","1:3470"),("rodon","All Round Gothic","42:42")]:
        original=next(a for a in index if a.get("source_id")==source_id and a["provider"]=="figma");local="../../skills/qp-brandbook/"+original["path"]
        b=f'<section class="slide" style="height:900px;width:720px;background:#fff"><img src="{local}" alt="Referência oficial {key}" style="max-height:650px;max-width:100%;margin:auto"><div style="padding:30px;font:400 20px/1.6 Inter">Adaptação de texto preparada no briefing.<br>Arte final pendente da fonte completa {family}.</div></section>'
        (OUT/(key+".html")).write_text(document("Validação de dependência · "+key,b,"Referência original exibida para conferência. Nenhuma fonte de teste ou substituição foi usada para simular a peça nova."),encoding="utf8")
        cases.append({"file":key+".html","source":original["id"],"status":"blocked-font","missing_font":family,"brief":{"objective":"inspirar uma viagem de fim de semana","language":"es-MX"if key=="viajo-mucho"else"pt-BR","headline":"Tu próximo viaje empieza contigo."if key=="viajo-mucho"else"Seu próximo destino começa com você.","commercial_claims":[]}})
    (OUT/"casos.json").write_text(json.dumps(cases,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"examples":len(cases),"new_final_arts":False,"fonts_pending":["Mauren","All Round Gothic"]}))
if __name__=="__main__":main()
