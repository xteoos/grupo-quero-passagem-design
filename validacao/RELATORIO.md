# Validação da preparação local

Revisão aprovada para publicação em 30/10/2026: **670 registros ativos**. Os resultados anteriores abaixo documentam as etapas já realizadas. Há dependências tipográficas e de acesso explicitadas; isso não equivale à aprovação de toda peça possível.

## Executado
- Validador oficial de skill: aprovado.
- Verificação de arquivos, SHA-256, SVGs e pacotes Office: aprovada; nenhum original ausente ou ponteiro Git LFS confundido com imagem.
- Quatro testes de falha: arquivo ausente, ponteiro LFS, hash alterado e arquivo vazio/original íntegro.
- Navegador local: busca, filtros combinados, ampliação/fechamento de previews, layout de 390px sem rolagem horizontal e console sem erros de JavaScript.
- Fontes reais carregadas em Chromium: Sora Light, Inter, Instrument Serif Italic, Lilita One, Nunito ExtraBold e Bacalar Expanded do kit usado no Brand Navigator. As três fontes adicionadas passaram no mapa de caracteres de acentos portugueses e espanhóis; o navegador confirma os PostScript LilitaOne e Nunito-ExtraBold, o peso 800 da Nunito e a fonte web customizada da Bacalar em peso 600, sem fallback nos títulos. A Bacalar servida pelo kit tem nomes internos reduzidos; os nomes CSS e peso são definidos explicitamente. A faixa Sora foi corrigida para 100–800 conforme o eixo do arquivo; Inter conserva 100–900.
- Revisão visual dos quatro slides HTML, comunicado QP, post QP, catálogo desktop e mobile. Texto e recortes conferidos; sem overflow nos editáveis após as correções.
- Revisão independente da skill e de 26 imagens Jessy. Achados incorporados: pesos reais da Sora, CLI de busca e identificação das 16 prévias com marca d’água.
- Git: branch main com origin apontando para o repositório público autorizado; atributos e filtros LFS verificados. Brand Navigator original permaneceu limpo.

## Exemplos
[Apresentação QP](exemplos/apresentacao-qp.html): quatro slides HTML derivados de layouts do modelo oficial, com texto editável e fundos/elementos originais.
[Comunicado QP](exemplos/comunicado-qp.html): exemplo sem datas ou políticas inventadas, com fundo e assinatura do modelo.
[Post QP](exemplos/post-qp.html): estudo com Bacalar Expanded com acentos em peso 600, Instrument Serif Italic, paleta normativa, recorte PNG e logo negativo oficiais. O título “AÇÃO QUE TE MOVE” testa acentos reais em Bacalar. Não é reprodução exata do frame QP 1:1759.
[Viajo Mucho](exemplos/viajo-mucho.html) e [Rodon](exemplos/rodon.html): adaptações com Lilita One Regular e Nunito ExtraBold, solicitadas pelo responsável. Títulos e apoio são editáveis; as regiões fotográficas são recortes dos previews oficiais, preservados com essa limitação. Há cópias portáveis dentro da skill e miniaturas no catálogo. Não são reconstruções integralmente vetoriais nem exportações .fig.

Bacalar ativa: OpenType importado do mesmo kit do Brand Navigator, indicado pelo responsável. Os 26 acentos/sinais testados estão presentes. O ZIP anterior e os OTFs locais do Navigator têm hashes idênticos e não são a versão ativa. A autorização de uso foi registrada. Evidências: [origem do arquivo ativo](../fontes-de-origem/bacalar-brand-navigator.json) e [diagnóstico do ZIP](../fontes-de-origem/bacalar-recebida.json).

[Amostra de acentos e pesos](fontes-adaptadas.png): conferência visual de Bacalar, Lilita One e Nunito com português e espanhol.

[Resultados do navegador](browser-checks.json), [casos e fontes](exemplos/casos.json), [revisão independente inicial](independent-review.md) e [revisão das fotografias](jessy-watermark-observations.json).

## Limites
Os arquivos PPTX/DOCX oficiais foram preservados e inspecionados estruturalmente. Os exemplos criados nesta validação são HTML, não apresentações novas salvas em Google Slides nem testes manuais no PowerPoint. Conversões de HTML para outros formatos exigem nova renderização e conferência.

As versões PDF dos modelos são exportações da fonte, usadas para suas miniaturas. O catálogo não altera os originais. Previews Figma não substituem um arquivo .fig editável.

As fontes dos exemplos estão incluídas e a integridade passa sem pendências de fonte. Mauren e All Round Gothic foram substituídas nas adaptações a pedido do responsável; os originais continuam preservados. O arquivo Bacalar é de entrega web, com tabela de nomes reduzida: a instalação em Figma/Office não foi validada e pode exigir arquivo desktop próprio. O uso local em HTML é a evidência disponível. Git LFS foi instalado para a publicação. Os três atalhos não resolvidos estão documentados na cobertura.


## Distribuição sob demanda para IAs · 30/10/2026

O ZIP distribution/qp-brandbook.zip contém apenas a skill, referências, metadados de interface e scripts: cerca de 160 KB após a curadoria social, sem os binários do acervo. O bundle remoto reúne 49 referências e os hashes de 1.244 arquivos (incluindo previews e dependências), sem duplicar as imagens. Esses números são diferentes dos 659 itens lógicos do catálogo.

Cinco testes do helper verificam download LFS pelo endpoint de mídia, reaproveitamento de arquivo íntegro, recuperação de arquivo de cache corrompido, rejeição de ponteiros/conteúdo incorreto, contenção de caminhos e obtenção de dependências CSS. Resultados dos downloads reais: [remote-downloads.json](remote-downloads.json). A ferramenta não usa o executável Git nem Git LFS para essa consulta.

O README orienta instalação do ZIP leve e busca sob demanda; o download completo não é apresentado como alternativa de uso. O helper atualiza as referências no início de cada pedido e fixa uma revisão para seus downloads. Acesso à internet, Python 3 e permissão de gravação continuam necessários para o helper.

Teste da versão inicial pelo ZIP público em pasta vazia: sincronização das 44 referências, busca e download de um logo e obtenção de um HTML adaptado com suas dependências aprovados. Foram materializados 14 arquivos (cerca de 3,3 MB), sem clone e sem Git/LFS. Evidência: [remote-package.json](remote-package.json).


## Curadoria social e linguagem das marcas · 30/10/2026

Revisados visualmente 280 exports, com 202 peças completas e 78 itens de apoio. Os guias QP image 57/58/59, o percurso Frame 4, o lettering Group 12 e o selo postal Ativo 12-8 1 agora têm tipos e nomes próprios. Viajo Mucho e Rodon receberam a mesma distinção. Nove pranchas de contato e quatro testes de regressão de classificação/famílias estão em [revisao-social](revisao-social/). A triagem é visual, sem prometer inspeção minuciosa de todos os textos ou acesso editável offline ao Figma.

Quatro [estudos de composição](social/casos.json), com HTML e PNG, testam foto/percurso/faixas QP, lettering misto QP, colagem Viajo Mucho e foto/balões Rodon. Foram usados elementos e logos reais, texto controlável e fontes locais. Não são novos templates oficiais nem simulações de uma campanha vigente. Os estudos QP, VM e Rodon que usam fotos de preview Figma têm resolução e edição fotográfica limitadas; a peça QP de lettering usa o original fotográfico do ensaio Irineu.

O [teste de navegador](social/browser-checks.json) verifica filtros semânticos, busca pelo nome original, categorias, famílias, carregamento das imagens, fontes efetivamente renderizadas e ausência de corte nos textos novos. Houve conferência visual dos estudos com as referências escolhidas; isso mostra uma aplicação possível das novas instruções, não garante o resultado de toda IA ou dispensa revisão de novas peças.

A skill manda abrir referências antes de compor e comparar o resultado renderizado com elas. A autorização do responsável permite stickers derivados quando úteis e identificados, preservando logos, identidade e veracidade das mensagens.

Também foram inspecionados e renomeados os percursos vetoriais 100:21/100:22, a trama de laços 108:34 e a prancha Component 4 (31:29208) da biblioteca de assets. A prancha foi retirada da categoria de ilustração individual; os dois percursos ganharam categoria e instruções próprias.


## Teste local · metas de viagem e organização simplificada

O teste segue o pedido curto de criar um story QP sobre metas de viagem, consultando o perfil qp-metas-viagem e as duas referências 2469:2004 / 2443:1497. Foram usados os elementos originais separados, sem colar o PNG da peça completa como fundo. O cabeçalho e os campos contêm texto real em Bacalar Expanded 600, Sora e Instrument Serif Italic. A escolha de marinho para o fundo e a troca da variante Semi Expanded observada pela Expanded disponível são adaptações explicitadas em [producao.json](metas-viagem/producao.json).

O [story PNG](metas-viagem/story-metas.png), a [prova HTML preenchível](metas-viagem/story.html), a [comparação visual](metas-viagem/comparacao.png) e os [resultados do navegador](metas-viagem/browser-checks.json) permitem revisão concreta. Verificados: 1080 × 1920, fontes efetivas sem fallback, textos sem corte, dois stickers, balão, quatro campos, foco do botão de assinatura, preenchimento com São Paulo, limpeza e visualização em 390px sem rolagem horizontal. O PNG não cria widgets nativos do Instagram. Esta é uma aplicação feita na mesma conversa, não teste independente de outro modelo ou aprovação humana final.

A organização ativa contém 42 stickers QP e seis ilustrações de cidades. Oito itens (seis fundos e duas pranchas QP) foram retirados do catálogo, mantendo os originais em fontes-de-origem/arquivo, com os hashes preservados. O teste também confirma que os filtros QP não oferecem fundos, cidades ou pranchas como categorias separadas. A categoria ilustrações reúne os destinos; os itens individuais das pranchas QP estão em stickers.

O helper ganhou modo explícito de revisão local para testar o pacote sem consultar o GitHub. Ele conserva esse modo nos próximos syncs e só volta ao GitHub com sync --github. Os testes de contrato verificam que nenhuma chamada de rede ocorre nesse modo. Nada desta etapa foi publicado ou enviado por push.


Publicação da organização e do teste autorizada pelo responsável em 30/10/2026. As anotações de teste local e github_updated=false nos relatórios descrevem o estado durante a validação anterior à autorização; não são uma consulta ao estado remoto atual.
