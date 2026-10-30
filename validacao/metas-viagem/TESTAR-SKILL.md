# Testar a skill local antes de publicar

Esta revisão ainda não foi enviada ao GitHub. O pacote atualizado está em distribution/qp-brandbook.zip nesta pasta de projeto. Instale-o em uma pasta de teste separada; não use o ZIP público para avaliar estas mudanças.

Na skill instalada, execute:

```sh
python3 scripts/remote_assets.py sync --local-root /caminho/do/quero-passagem-brandbook-ai
```

A resposta deve informar `mode: local-review`. Esse modo permanece nessa instalação nos próximos pedidos, inclusive se a IA chamar `sync` sem opções. Não consulta o GitHub nem sobrescreve a revisão local com a versão publicada. Para voltar à versão publicada depois, use `sync --github` explicitamente.

Pedido para testar, sem fornecer a solução no prompt:

> Use a skill qp-brandbook para criar um story interativo da Quero Passagem sobre metas de viagem, em 1080 × 1920. Entregue a arte base em PNG e uma versão editável. Não publique.

A skill deve localizar a família qp-interativo, abrir as referências 2469:2004 e 2443:1497 e usar os elementos individuais pertinentes. O perfil qp-metas-viagem é consultável em references/social/familias.json.

## Como avaliar o resultado

- Cabeçalho em balão com Sora e Bacalar, com hierarquia clara.
- Campos de metas com Bacalar no título, Sora no apoio e Instrument Serif Italic nas palavras de intenção.
- Ilustrações/stickers relacionados ao assunto, posicionados sem impedir o preenchimento.
- Campos com espaço útil para a resposta, pílula de assinatura/chamada e percurso no rodapé.
- Fundo gráfico coerente; fotografia não é obrigatória nessa referência.
- Fontes realmente carregadas, textos editáveis e renderização nas dimensões pedidas.
- Sem colar a imagem pronta da referência como fundo. Um PNG não cria automaticamente widgets nativos do Instagram.

A prova story.html nesta pasta é um teste de aplicação feito nesta conversa, não uma avaliação independente de outro modelo. Ela permite clicar e preencher as linhas; o botão de assinatura leva ao primeiro campo. O arquivo story-metas.png é a arte base vazia. A comparação visual com a referência é uma evidência de composição, sem representar uma aprovação do responsável ou garantia de futuras gerações.
