"""Teste de aplicação da skill em um story QP; cria entrega local editável e rastreável."""
import hashlib,html,json,pathlib,shutil
R=pathlib.Path(__file__).resolve().parents[1];S=R/'skills/qp-brandbook';O=R/'validacao/metas-viagem'
def main():
 O.mkdir(parents=True,exist_ok=True);(O/'assets').mkdir(exist_ok=True)
 A={a['id']:a for a in json.loads((S/'references/assets-index.json').read_text())['assets']}
 P=next(p for p in json.loads((S/'references/social/familias.json').read_text())['profiles']if p['id']=='qp-metas-viagem')
 used=[]
 def copy(id,name):
  a=A[id];source=S/a['path'];target=O/'assets'/name;shutil.copyfile(source,target)
  used.append({'id':id,'source_path':a['path'],'delivery_path':'assets/'+name,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()});return 'assets/'+name
 def image(id,name,style,kind):
  src=copy(id,name);return f'<img data-asset="{id}" data-kind="{kind}" src="{src}" alt="{html.escape(A[id]["name"])}" style="position:absolute;{style}">'
 fonts=[]
 for family,matcher,filename,weight,style in [('Sora',lambda a:'sora' in a['name'].lower(),'sora.ttf','100 800','normal'),('Bacalar Expanded',lambda a:a.get('css_family')=='Bacalar Expanded','bacalar.otf','600','normal'),('Instrument Serif',lambda a:'instrumentserif-italic' in a['name'].lower(),'instrument-serif-italic.ttf','400','italic')]:
  a=next(a for a in A.values()if a.get('font')and matcher(a));src=copy(a['id'],filename);fonts.append(f"@font-face{{font-family:'{family}';src:url('{src}');font-weight:{weight};font-style:{style};font-display:block;}}")
  # Preservar os avisos de distribuição dos arquivos de fonte utilizados.
  for license in (S/a['path']).parent.glob('*.txt'):
   if any(t in license.name.lower()for t in ['ofl','license','origem']):shutil.copyfile(license,O/'assets'/(filename+'-'+license.name))
 (O/'fontes.css').write_text('\n'.join(fonts)+'\n')
 body=image(P['pattern_id'],'trama.svg','left:0;top:-209px;','trama')
 matrix=','.join(str(n)for n in P['path_transform'])
 body+=f'<div data-kind="percurso" style="position:absolute;left:0;top:0;transform-origin:0 0;transform:matrix({matrix})">'+image(P['path_id'],'percurso.svg','','percurso')+'</div>'
 body+='''<section class="balloon" data-kind="balao"><div class="intro" data-check>Minhas metas de</div><div class="headline" data-check>VIAGEM</div></section>'''
 body+=image(P['sticker_ids'][0],'chinelos.svg','left:117px;top:195px;','sticker')
 body+=image(P['sticker_ids'][1],'coco.png','left:805px;top:278px;','sticker')
 for i,field in enumerate(P['fields']):
  y=570+220*i
  body+=f'''<section class="goal" data-kind="meta" style="top:{y}px"><div class="goal-title" data-check>{html.escape(field['title'])}</div><div class="goal-copy" data-check><span>{html.escape(field['prefix'])} </span><em>{html.escape(field['emphasis'])}</em></div><div class="answer" data-answer="{i+1}" role="textbox" aria-label="Preencher meta {i+1}: {html.escape(field['emphasis'])}" contenteditable="true" spellcheck="false"></div></section>'''
 body+='''<button type="button" id="begin" data-check data-kind="botao" aria-label="Preencher minhas metas">@queropassagem</button>'''
 css='''*{box-sizing:border-box}body{margin:0;background:#e6edf3;color:#0d2240;font:300 15px/1.6 Sora,sans-serif}header{max-width:1080px;margin:0 auto;padding:22px 16px}header p{margin:4px 0}header strong{font-weight:600}header button{font:400 14px Sora;padding:8px 14px;border:1px solid #c6d2df;border-radius:6px;background:white;color:#0d2240;cursor:pointer}.stage{position:relative;max-width:1080px;margin:auto;overflow:hidden;--scale:1;height:calc(1920px * var(--scale))}.story{position:relative;width:1080px;height:1920px;overflow:hidden;background:#0D2240;transform:scale(var(--scale));transform-origin:0 0}.balloon{position:absolute;left:96px;top:235px;width:834px;height:217px;background:#fff;border:2px solid #0D2240;border-radius:68px 136px 68px 68px;text-align:center;padding:30px 20px 16px}.intro{font:400 48px/1.12 Sora;color:#0D2240}.headline{font:600 86px/1.15 'Bacalar Expanded';color:#0066C6;letter-spacing:0}.goal{position:absolute;left:86px;width:912px;height:136px;color:white}.goal-title{width:430px;font:600 53px/1.16 'Bacalar Expanded'}.goal-copy{position:absolute;left:0;top:60px;width:435px;white-space:nowrap;font:300 34px/1.45 Sora}.goal-copy em{font:italic 400 47px/1.15 'Instrument Serif';color:#399AE6}.answer{position:absolute;left:454px;top:26px;width:457px;height:98px;border-bottom:3px solid #399AE6;font:300 37px/1.3 Sora;color:white;padding:28px 5px 6px;white-space:nowrap;overflow:hidden;outline:none}.answer:focus{background:#16396B80;box-shadow:0 3px 0 #FFCC00}.answer[aria-invalid=true]{border-color:#FFCC00}#begin{position:absolute;left:343px;top:1596px;width:394px;height:73px;background:#0D25B0;color:white;border:1px solid #0D2240;border-radius:25px 65px 33px 25px;font:300 32px/1 Sora;cursor:pointer}img{display:block}[data-check]{font-synthesis:none}@media print{header{display:none}.stage{--scale:1!important;margin:0}.story{transform:none}@page{size:1080px 1920px;margin:0}}'''
 script='''const stage=document.querySelector('.stage');new ResizeObserver(()=>stage.style.setProperty('--scale',Math.min(stage.clientWidth/1080,1))).observe(stage);const answers=[...document.querySelectorAll('[data-answer]')];document.getElementById('begin').onclick=()=>answers[0].focus();document.getElementById('clear').onclick=()=>answers.forEach(e=>{e.textContent='';e.removeAttribute('aria-invalid')});for(const e of answers)e.addEventListener('input',()=>e.setAttribute('aria-invalid',String(e.scrollWidth>e.clientWidth)));'''
 doc='<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Metas de viagem · teste local QP</title><link rel="stylesheet" href="fontes.css"><style>'+css+'</style><header><strong>Teste local · Story de metas de viagem</strong><p>Clique nas linhas para preencher. A assinatura leva ao primeiro campo. O PNG é uma arte base; não cria interação nativa no Instagram.</p><button id="clear" type="button">Limpar campos</button></header><div class="stage"><main class="story" aria-label="Minhas metas de viagem">'+body+'</main></div><script>'+script+'</script></html>'
 (O/'story.html').write_text(doc)
 report={'brief':P['brief'],'mode':'teste-local-sem-publicacao','profile':P['id'],'family':P['family'],'reference_ids':P['reference_ids'],'format':P['format'],'photo_required':False,'background':'#0D2240, escolha explícita do estudo; a referência original é transparente.','assets':used,'adaptations':['Texto novo de cabeçalho e rótulos com fontes locais reais.','Bacalar Expanded 600 do pacote no lugar da variante Semi Expanded registrada na referência.','Fundo marinho para leitura do texto branco.','Quatro campos preenchíveis somente na prova HTML; PNG não contém widget nativo de rede social.'],'copy_is_new':True,'source_image_used_as_background':False,'github_updated':False}
 (O/'producao.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('Prova HTML e assets locais preparados em validacao/metas-viagem')
if __name__=='__main__':main()
