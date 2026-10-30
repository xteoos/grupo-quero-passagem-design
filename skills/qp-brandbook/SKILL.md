---
name: qp-brandbook
description: Crie ou revise apresentações, posts, anúncios e comunicados da Quero Passagem, Viajo Mucho, Rodon e demais marcas do grupo usando regras, templates, fontes e assets oficiais. Use quando houver pedido de material dessas marcas; não confunda o acervo com autorização para publicar.
---

# Brandbook Quero Passagem

Crie materiais coerentes com a marca escolhida, preservando o conteúdo e o formato pedidos. Instale o pacote leve: ele busca no GitHub apenas os materiais necessários. Todos os caminhos abaixo são relativos à pasta desta skill. Não é necessário clonar o repositório nem instalar Git LFS.

## Consultar a base atual

Leia [acesso remoto](references/acesso-remoto.md). No início de cada pedido, execute `python3 scripts/remote_assets.py sync` usando o caminho desta skill. Só então leia as regras atualizadas. Busque candidatos com `find`, obtenha previews para escolher e use `get` para materializar originais antes de compor. Não baixe o acervo inteiro. Se a ferramenta não puder consultar, baixar ou renderizar, informe o limite concreto.

## Antes de compor
Identifique marca, público, objetivo, canal, idioma e formato de entrega a partir do pedido. Pergunte somente pelos dados importantes que faltarem. O formato não tem padrão obrigatório: pode ser PPTX, PDF, Google Slides, Figma, HTML, SVG ou imagem, conforme a necessidade e as ferramentas disponíveis.

Leia [marcas](references/marcas.md), [produção](references/producao.md) e [dependências](references/dependencias.md). Depois carregue apenas as referências pertinentes:
- Qualquer peça: [cores](references/cores.md), [tipografia](references/tipografia.md) e [linguagem](references/linguagem.md).
- Fotografias: [direção fotográfica](references/fotografia.md).
- Layouts, stickers e ilustrações: [composição](references/composicao.md) e [templates](references/templates.md).
- Dúvida sobre a norma: [páginas oficiais](references/paginas/INDEX.md).
- Encontrar arquivos: [índice do acervo](references/assets-index.json). Use `python3 scripts/remote_assets.py find --brand quero-passagem --category logos` e baixe os itens selecionados com `get --id`. O índice registra caminhos relativos à raiz desta skill.

## Posts, anúncios e outras peças gráficas

Antes de desenhar, leia [o guia social](references/social/COMECAR.md) e o guia da marca nele indicado. Escolha uma família de composição e ABRA as referências visuais; não basta ler nomes, cores ou fontes. Use a tipografia em papéis contrastantes, a fotografia e os elementos contextualizados como descritos nas famílias. Não transpor o layout de apresentação para um post. Classifique a busca pelo papel real do arquivo: peças completas, stickers, letterings, percursos, guias e fundos são recursos distintos. Variações de stickers são permitidas pelo responsável quando fizerem sentido, preservando o caráter da marca e sendo identificadas como derivadas.

## Criar com o acervo
1. Para apresentações e comunicados, selecione o modelo editável da marca e do formato. Para posts e peças gráficas, escolha a família e as referências em `pecas-sociais`; elas orientam uma composição original, sem exigir copiar um layout inteiro. Abra os previews e consulte os originais editáveis quando necessário; registre os IDs. Não use uma campanha isolada como regra geral.
2. Escolha os arquivos reais pelo catálogo. Confira marca, finalidade, dimensões, marca d’água e situação. Não usar prévias com marca d’água em artes finais nem remover a marca para reaproveitar a prévia. Um item histórico ou pendente de revisão não é automaticamente adequado para uma peça atual.
3. Importe fontes, logos e elementos oficiais. Nunca redesenhe um logo nem peça a um gerador de imagens para simulá-lo. Use texto real com a fonte carregada; o raster da peça pronta não substitui o editável quando ele foi pedido.
4. Faça variações controladas: altere conteúdo, fotos, proporção e organização conforme a família do template; preserve hierarquia, caráter, proporções e aplicações da marca.
5. Renderize o resultado no formato solicitado. Confira fontes efetivas, acentos, quebras, recortes, contraste, legibilidade, logos e relação com o template.

## Limites que afetam a entrega
Nas novas adaptações Viajo Mucho, substitua Mauren por Lilita One Regular (400); em Rodon, substitua All Round Gothic por Nunito ExtraBold (800). As trocas foram solicitadas pelo responsável e não precisam de nova autorização por peça. Reajuste quebras e hierarquia, mantenha Work Sans/Poppins no apoio e não altere logos. Use os arquivos locais e registre a adaptação; os modelos originais continuam como evidência.

Use a Bacalar Expanded com acentos importada do mesmo kit do Brand Navigator, peso 600, em CAIXA ALTA. Obtenha `assets/fonts.css` com `get --path assets/fonts.css` e carregue o arquivo local; não usar os BacalarTest do ZIP como se fossem a versão corrigida. Os acentos portugueses e espanhóis foram conferidos no arquivo importado. Leia [tipografia](references/tipografia.md) e [a política de fontes](references/typography-policy.json) para a origem e os limites de instalação: é um OpenType de entrega web com nomes internos reduzidos. Em Figma, Office e outros editores, confira se a fonte realmente foi instalada e renderizada; se a ferramenta precisar de arquivo desktop com nomes completos, informe essa dependência específica e obtenha o arquivo adequado. A fonte não está genericamente bloqueada: o uso HTML local com acentos é validado.

O responsável autorizou o uso da Bacalar. Não pedir essa autorização novamente por causa do nome Trial no ZIP anterior. Não substituir fonte, remover acentos ou aceitar fallback silencioso.

Se um arquivo obrigatório estiver ausente ou for ponteiro LFS, tente obtê-lo pelo helper remoto; se falhar, informe a pendência em vez de usar a miniatura. Falta de renderizador também deve ser informada. Não declare um PPTX validado apenas por conseguir salvá-lo.

Não invente datas, preços, descontos, regras de cancelamento ou cobertura de produtos com base nos exemplos desta documentação.

## Entregar
Entregue a peça e os arquivos editáveis solicitados. Informe de forma curta: template e assets usados, adaptação relevante, validação realizada e pendências. Sem substituições silenciosas. Não publique nem altere Drive/Figma/GitHub por esta skill sem pedido específico.
