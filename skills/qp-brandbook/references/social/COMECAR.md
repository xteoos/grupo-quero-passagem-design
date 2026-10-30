# Criar peças sociais a partir do repertório real

As orientações abaixo resultam da revisão visual dos 280 exports do Social - Ads em 30/10/2026 e do pedido do responsável. São padrões de aplicação observados, não um novo manual universal. Dados de campanha, datas e ofertas continuam ligados à peça de origem.

## Antes do primeiro layout

1. Após `sync`, leia o guia da marca: [Quero Passagem](quero-passagem.md), [Viajo Mucho](viajo-mucho.md) ou [Rodon](rodon.md). Consulte [famílias e IDs](familias.json).
2. Escolha uma família pelo assunto: inspiração de viagem, rodoviário, destino, hotel, oferta, interação ou institucional. Não usar automaticamente o visual de slide para criar post.
3. Busque `--category pecas-sociais --family ID_DA_FAMILIA`. Em instalações antigas sem --family, use --query ID_DA_FAMILIA ou atualize o ZIP da skill. Obtenha e ABRA visualmente ao menos duas peças próximas do pedido. Se só houver uma adequada, use essa e registre a cobertura. Leia as dimensões reais: faixa de carrossel não é post único.
4. Busque os elementos separadamente: `stickers`, `letterings`, `linhas-e-percursos`, `ilustracoes`. Para QP, os elementos das pranchas já estão separados em stickers; a categoria ilustrações inclui cidades. Abra as prévias e escolha os que têm relação com a mensagem. Guia de cores não é template; foto isolada não é uma composição.
5. Defina internamente: se a família usa fotografia ou fundo gráfico, como a chamada conversa com ela, qual combinação tipográfica sustenta a hierarquia e qual elemento da marca ajuda a contar a ideia. Só então componha. Não precisa pedir uma nova aprovação para cada escolha rotineira.

## Liberdade com identidade

Crie uma composição nova usando a gramática da família: pode alterar foto, frase, hierarquia, posição de selos, percurso e recorte. Referência serve para entender relações, não para colar a imagem inteira e escrever em cima dela. Mantenha texto real, logo oficial e elementos de composição independentes. Para adaptar palavras de um lettering rasterizado, reconstrua as faixas e use as fontes reais; não distorça ou remende letras na imagem.

O responsável autorizou criar variações de stickers quando fizer sentido. Parta de um elemento de referência da mesma marca e conserve caráter, contorno, paleta, proporções internas e tratamento de textura. Identifique a variação como derivada, não como arquivo oficial do acervo. Não alterar logos, inventar selos de certificação ou reutilizar mensagens de uma campanha fora de contexto. A autorização para variações gráficas não autoriza novas alegações comerciais.

Não é obrigatório usar ônibus, linha, sticker e todas as fontes na mesma arte. Cada elemento precisa cumprir um papel: conduzir o olhar, sinalizar tema, destacar uma palavra ou conectar foto e chamada. Repetição sem motivo descaracteriza o resultado tanto quanto eliminar todo o repertório.

## O que reprovar na revisão

- A família interativa virou uma foto com título, perdeu seus campos de resposta ou recebeu fotografia por obrigação.
- A peça está apenas nas cores certas, mas poderia ser de qualquer marca ao trocar o logo.
- Layout de slide, pilha de cards arredondados ou bloco fotográfico isolado foi usado sem relação com as referências sociais escolhidas.
- Todos os textos usam o mesmo peso/fonte, ou cada palavra tem uma fonte sem hierarquia.
- Gradientes difusos, brilho 3D, sombras suaves ou ícones genéricos substituem os recortes, adesivos e grafismos efetivamente observados. Só usar tais recursos se houver evidência na família escolhida.
- Stickers aleatórios, tamanho que compete com o título, ou linha cortando olhos, boca, preço ou CTA.
- A composição da QP foi transportada para Viajo Mucho/Rodon trocando apenas cor e logo.
- A imagem gerada incorpora textos/logos simulados em vez dos arquivos controláveis.

## Conferir e entregar

Renderize nas dimensões finais; veja também em tamanho de celular. Compare lado a lado com as duas referências: escala do título, ocupação da foto, ritmo, sobreposição, contraste e presença dos elementos característicos. Se a comparação não sustentar a identidade, revise a composição antes de entregar; hashes e fontes carregadas não provam qualidade de design.

Informe em uma linha a família, os IDs das peças e dos elementos usados e as variações criadas. Não declarar reprodução exata quando a entrega for uma composição original inspirada no repertório.

## Leitura do catálogo

`source_name` preserva o nome no Figma; `name` é o nome curado para busca. `category` descreve o que o arquivo É; `family` agrupa uma linguagem de composição; `composition_role` explica para que serve. `review_level=triagem-visual` significa análise em prancha de contato; não implica aprovação de oferta ou revisão detalhada de todos os textos. Abra o item escolhido antes de usar. Os caminhos antigos em assets/templates/figma foram mantidos para preservar as fontes; eles não definem mais a categoria do item.
