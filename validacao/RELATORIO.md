# Validação da preparação local

Resultado atualizado em 30/10/2026: **integridade aprovada para os 659 registros locais**. Há dependências tipográficas e de acesso explicitadas; isso não equivale à aprovação de toda peça possível.

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

O ZIP distribution/qp-brandbook.zip contém apenas a skill, referências, metadados de interface e scripts: cerca de 140 KB, sem os binários do acervo. O bundle remoto reúne 44 referências e os hashes de 1.244 arquivos (incluindo previews e dependências), sem duplicar as imagens. Esses números são diferentes dos 659 itens lógicos do catálogo.

Cinco testes do helper verificam download LFS pelo endpoint de mídia, reaproveitamento de arquivo íntegro, recuperação de arquivo de cache corrompido, rejeição de ponteiros/conteúdo incorreto, contenção de caminhos e obtenção de dependências CSS. Resultados dos downloads reais: [remote-downloads.json](remote-downloads.json). A ferramenta não usa o executável Git nem Git LFS para essa consulta.

O README orienta instalação do ZIP leve e busca sob demanda; o download completo não é apresentado como alternativa de uso. O helper atualiza as referências no início de cada pedido e fixa uma revisão para seus downloads. Acesso à internet, Python 3 e permissão de gravação continuam necessários para o helper.
