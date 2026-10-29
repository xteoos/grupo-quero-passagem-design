# Validação da preparação local

Resultado em 29/10/2026: **integridade aprovada para os 651 registros locais**. Há dependências tipográficas e de acesso explicitadas; isso não equivale à aprovação de toda peça possível.

## Executado
- Validador oficial de skill: aprovado.
- Verificação de arquivos, SHA-256, SVGs e pacotes Office: aprovada; nenhum original ausente ou ponteiro Git LFS confundido com imagem.
- Quatro testes de falha: arquivo ausente, ponteiro LFS, hash alterado e arquivo vazio/original íntegro.
- Navegador local: busca, filtros combinados, ampliação/fechamento de previews, layout de 390px sem rolagem horizontal e console sem erros de JavaScript.
- Fontes reais carregadas em Chromium: Sora Light, Inter e Instrument Serif Italic. A faixa Sora foi corrigida para 100–800 conforme o eixo do arquivo; Inter conserva 100–900.
- Revisão visual dos quatro slides HTML, comunicado QP, post QP, catálogo desktop e mobile. Texto e recortes conferidos; sem overflow nos editáveis após as correções.
- Revisão independente da skill e de 26 imagens Jessy. Achados incorporados: pesos reais da Sora, CLI de busca e identificação das 16 prévias com marca d’água.
- Git: branch main com origin apontando para o repositório público autorizado; atributos e filtros LFS verificados. Brand Navigator original permaneceu limpo.

## Exemplos
[Apresentação QP](exemplos/apresentacao-qp.html): quatro slides HTML derivados de layouts do modelo oficial, com texto editável e fundos/elementos originais.
[Comunicado QP](exemplos/comunicado-qp.html): exemplo sem datas ou políticas inventadas, com fundo e assinatura do modelo.
[Post QP](exemplos/post-qp.html): estudo com Sora Light e Instrument Serif Italic, paleta normativa, recorte PNG e logo negativo oficiais. Não reproduz o frame que exige Bacalar.
[Viajo Mucho](exemplos/viajo-mucho.html) e [Rodon](exemplos/rodon.html): casos negativos de dependência. Exibem a referência original e o briefing; as novas artes finais permanecem pendentes de Mauren e All Round Gothic. Nenhuma fonte de teste ou substituição foi usada para simular conclusão.

[Resultados do navegador](browser-checks.json), [casos e fontes](exemplos/casos.json), [revisão independente inicial](independent-review.md) e [revisão das fotografias](jessy-watermark-observations.json).

## Limites
Os arquivos PPTX/DOCX oficiais foram preservados e inspecionados estruturalmente. Os exemplos criados nesta validação são HTML, não apresentações novas salvas em Google Slides nem testes manuais no PowerPoint. Conversões de HTML para outros formatos exigem nova renderização e conferência.

As versões PDF dos modelos são exportações da fonte, usadas para suas miniaturas. O catálogo não altera os originais. Previews Figma não substituem um arquivo .fig editável.

O modo estrito do verificador continua sinalizando as três fontes comerciais ausentes. Git LFS foi instalado para a publicação. Os três atalhos não resolvidos estão documentados na cobertura.
