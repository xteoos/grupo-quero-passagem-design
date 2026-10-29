---
name: qp-brandbook
description: Crie ou revise apresentações, posts, anúncios e comunicados da Quero Passagem, Viajo Mucho, Rodon e demais marcas do grupo usando regras, templates, fontes e assets oficiais. Use quando houver pedido de material dessas marcas; não confunda o acervo com autorização para publicar.
---

# Brandbook Quero Passagem

Crie materiais coerentes com a marca escolhida, preservando o conteúdo e o formato pedidos. Todos os caminhos abaixo são relativos a esta pasta; o pacote funciona sem o Brand Navigator original.

## Antes de compor
Identifique marca, público, objetivo, canal, idioma e formato de entrega a partir do pedido. Pergunte somente pelos dados importantes que faltarem. O formato não tem padrão obrigatório: pode ser PPTX, PDF, Google Slides, Figma, HTML, SVG ou imagem, conforme a necessidade e as ferramentas disponíveis.

Leia [marcas](references/marcas.md), [produção](references/producao.md) e [dependências](references/dependencias.md). Depois carregue apenas as referências pertinentes:
- Qualquer peça: [cores](references/cores.md), [tipografia](references/tipografia.md) e [linguagem](references/linguagem.md).
- Fotografias: [direção fotográfica](references/fotografia.md).
- Layouts, stickers e ilustrações: [composição](references/composicao.md) e [templates](references/templates.md).
- Dúvida sobre a norma: [páginas oficiais](references/paginas/INDEX.md).
- Encontrar arquivos: [índice do acervo](references/assets-index.json). Use `python3 scripts/find_assets.py --brand quero-passagem --category logos` se houver execução local. O índice registra caminhos relativos à raiz desta skill.

## Criar com o acervo
1. Selecione um template da marca e do formato. Abra o preview e consulte o original editável quando necessário; registre seu ID. Não use uma campanha isolada como regra geral.
2. Escolha os arquivos reais pelo catálogo. Confira marca, finalidade, dimensões, marca d’água e situação. Não usar prévias com marca d’água em artes finais nem remover a marca para reaproveitar a prévia. Um item histórico ou pendente de revisão não é automaticamente adequado para uma peça atual.
3. Importe fontes, logos e elementos oficiais. Nunca redesenhe um logo nem peça a um gerador de imagens para simulá-lo. Use texto real com a fonte carregada; o raster da peça pronta não substitui o editável quando ele foi pedido.
4. Faça variações controladas: altere conteúdo, fotos, proporção e organização conforme a família do template; preserve hierarquia, caráter, proporções e aplicações da marca.
5. Renderize o resultado no formato solicitado. Confira fontes efetivas, acentos, quebras, recortes, contraste, legibilidade, logos e relação com o template.

## Limites que afetam a entrega
A Bacalar Expanded completa está pendente. Não use BacalarTest/Demo/Trial em produção. Uma peça que exige Bacalar não pode ser declarada fiel com outra fonte. Se for útil preparar uma prova em Sora, obtenha concordância com essa adaptação e identifique-a; sem isso, entregue a composição como rascunho pendente de tipografia.

Se um arquivo obrigatório estiver ausente ou for ponteiro LFS, peça a obtenção do original, em vez de usar a miniatura. Falta de renderizador também deve ser informada. Não declare um PPTX validado apenas por conseguir salvá-lo.

Não invente datas, preços, descontos, regras de cancelamento ou cobertura de produtos com base nos exemplos desta documentação.

## Entregar
Entregue a peça e os arquivos editáveis solicitados. Informe de forma curta: template e assets usados, adaptação relevante, validação realizada e pendências. Sem substituições silenciosas. Não publique nem altere Drive/Figma/GitHub por esta skill sem pedido específico.
