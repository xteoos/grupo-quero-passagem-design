> Revisão inicial independente. Os achados de faixa da Sora, CLI ausente e prévias com marca d’água foram corrigidos nesta entrega; consulte RELATORIO.md e os resultados atuais.

# Validação independente da skill qp-brandbook

Escopo: leitura somente da pasta da skill, sem depender do Brand Navigator original. Não editei o repositório. Avaliação feita durante coleta; não considerei contagens parciais do catálogo como defeitos.

## Pedido 1: post de fim de semana, Bacalar, foto oficial, HTML editável + PNG, destino indefinido

Comportamento permitido e correto:
- Quero Passagem / Brasil / português; público de viajantes; objetivo de inspiração, sem inventar destino, preço ou roteiro.
- Posso desenvolver mensagem genérica: “SEU FIM DE SEMANA PEDE UMA VIAGEM”, apoio “Inspire-se para sair da rotina.” Esses textos seriam propostas da peça, nunca slogans aprovados.
- Selecionar família de inspiração de viagem e conferir geometria: frame 63:12 da fonte Figma EyJUWysTaFKnJewVXFz0u0 é 1080x1920, apesar do nome [FEED]. Abri preview: há viajante, foto e composição tipográfica. O frame 63:34 é apenas fundo fotográfico e 63:89 é branco; não são boas bases de hierarquia por si sós. A skill alerta para esse caso.
- Foto candidata: drive:1bJ41mpP-7ar0JoPIOzwu8HBE1xtD4w6K, QP (30).jpg, ensaio Irineu DEZ-2025. Preview mostra pessoa em espera, mala e telefone; não exige um destino. Revisão visual inicial favorável. Antes de final usar o original e conferir recorte e marcas em dimensão final.
- Não consigo declarar o título em Bacalar atendido: SKILL.md:28 é explícito sobre arquivo completo pendente e proíbe Demo/Trial. Sem concordância para Sora, a entrega permanece rascunho pendente de tipografia. É correto perguntar pelo arquivo completo autorizado; não é correto exportar fallback silencioso e chamar de fiel.
- Não é necessário forçar uma pergunta sobre destino, pois o pedido pode ser atendido como inspiração genérica. A peça final precisará de formato/canal compatível; o frame escolhido pode orientar uma proposta story 1080x1920 explicitada ao usuário.
- HTML editável deve conservar texto como texto, logo como asset oficial e fontes/imagens locais; PNG só depois de conferir fontes efetivas, render e recorte. Estas regras estão presentes.

Risco visual demonstrado: drive:1Ey_zpcgReX_0FbHdBydWm6gy01TH-T2i, Jessica1188.jpg, possui a inscrição “© Vini Level PRÉVIA” no arquivo de 1366x2048, não somente no preview. O índice diz usage:revisar; eu rejeitaria para arte final e buscaria original sem marca d'água. Sugeri regra explícita contra uso de prévias com marca d'água.

## Pedido 2: comunicado interno, mudança de processo, briefing + seleção, sem inventar datas

Entrega possível sem inventar o processo:

**Briefing**
- Marca: Quero Passagem. Comunicação interna aos colaboradores afetados (equipes exatas a confirmar).
- Objetivo: explicar uma mudança de processo e orientar a ação esperada.
- Tom: objetivo, próximo e prático.
- Conteúdo a coletar: processo atual; o que muda; motivo; equipes afetadas; ação necessária; data de início, se houver; responsável/canal de dúvidas.
- Campos não informados: manter pendentes, sem preencher por suposição. Nem mesmo a data atual deve virar vigência.
- Estrutura sugerida: título da mudança; resumo; o que muda; o que fazer; início da mudança [a confirmar]; dúvidas [responsável/canal a confirmar].

**Seleção**
- Template drive:19lgUrEMkv7sYomWGXFMwfuqQQKP6mKlI3aBxlS94Fao, “Template comunicados - Quero Passagem”, PPTX local em assets/templates/recursos.
- Inspecionei o ZIP OOXML: 2 slides, título e corpo com lorem ipsum, Sora Light e Sora SemiBold, quatro imagens locais e nenhuma relação externa. É template editável, não comunicado preenchido.
- Usar assinatura e hierarquia presentes no modelo; sem adicionar foto ou decoração sem função. Reutilizar imagens internas do template e Sora disponível, conferindo correspondência dos estilos na etapa de edição/render.
- Esta entrega é briefing e seleção; não requer fingir que foi produzida uma arte ou um PPTX validado. Se o contexto for comunicação do grupo e não QP, esclarecer marca antes de trocar logo.

## Portabilidade e referências

- Todos os links Markdown relativos encontrados resolvem dentro da pasta atual.
- Nenhum caminho `path`/`preview_path` do índice escapa da raiz da skill ou é absoluto.
- Nenhum symlink depende do repositório pai.
- Cinco fontes referenciadas por assets/fonts.css existem localmente.
- PPTX de comunicados não tem imagens/fontes externas referenciadas por relações OOXML.
- Links Figma originais são dependências autenticadas opcionais e a skill esclarece que previews não são arquivo .fig nem garantem edição offline. Não tratei isso como defeito.
- Há um vídeo remoto na transcrição da página marca.md; é referência, não dependência essencial do fluxo local.

## Defeito real encontrado

assets/fonts.css:5 declarava Sora com font-weight:100 900, mas a tabela fvar do TTF empacotado possui wght 100..800. Inter possui wght 100..900. Isto contradiz a promessa de pesos reais em references/tipografia.md:16. O agente principal foi informado e está corrigindo o gerador.

No momento da primeira leitura, SKILL.md:18 apontava scripts/find_assets.py inexistente. O agente principal confirmou que esse CLI estava em preparação; não considerei defeito final sem revalidar após geração.

## Limites desta validação

Não produzi HTML/PNG final: o pedido de Bacalar não pode ser integralmente atendido com o arquivo completo pendente e não houve concordância com substituição. Não renderizei o PPTX, pois o pedido 2 requer somente briefing/seleção. A inspeção OOXML não é alegação de conformidade visual. Não tentei acessar contas externas nem publiquei material.
