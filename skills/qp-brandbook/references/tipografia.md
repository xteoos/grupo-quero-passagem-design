# Tipografia

Fonte das regras QP: [página Tipografia](paginas/fundamentos/tipografia.md) e Tipografia.pdf do kit oficial. Adaptações de Viajo Mucho e Rodon solicitadas pelo responsável em 30/10/2026 estão discriminadas abaixo; não alteram os arquivos de origem.

| Marca / família | Papel | Aplicação |
|---|---|---|
| QP · Sora | Primária | Leitura acessível; pesos reais de 100 a 800, com Light nas combinações editoriais demonstradas |
| QP · Inter | Corpo | Textos de apoio, materiais gráficos e componentes digitais |
| QP · Bacalar Expanded | Apoio, títulos ou palavras-chave | Sempre em CAIXA ALTA e variação Expanded; versão com acentos do kit usado no Brand Navigator; peso 600 |
| QP · Instrument Serif Italic | Apoio | Destaque pontual em itálico, excelência e tranquilidade |
| Viajo Mucho · Lilita One Regular | Títulos adaptados no lugar de Mauren | Peso 400 real, sem negrito artificial; preservar caixa alta e caráter expressivo onde o modelo demonstrar |
| Viajo Mucho · Work Sans | Apoio | Regular e SemiBold conforme o modelo escolhido |
| Rodon · Nunito ExtraBold | Títulos adaptados no lugar de All Round Gothic | Peso 800 real do arquivo variável; preservar caráter arredondado e leitura clara |
| Rodon · Poppins Regular | Apoio | Peso 400 conforme o modelo escolhido |

## Escolhas para facilitar o uso

As substituições de Mauren e All Round Gothic são autorizadas nesta base para novas peças e adaptações. Não é necessário pedir autorização de novo a cada uso. Elas não são reproduções tipográficas idênticas: confira tamanho, largura, entrelinha e quebras após trocar a fonte. Não substitua a tipografia dos logos.

A escolha de **Lilita One** aproxima o peso visual, a suavidade e o caráter expressivo dos títulos Mauren observados no frame Viajo Mucho 1:3470. É uma decisão de design para esta base. A distribuição oficial descreve a família como uma fonte de destaque para títulos e textos curtos: [Google Fonts · Lilita One](https://github.com/google/fonts/tree/main/ofl/lilitaone).

A escolha de **Nunito ExtraBold** aproxima os terminais arredondados e a presença dos títulos All Round Gothic observados no frame Rodon 42:42, com boa leitura em títulos de duas ou três linhas. A distribuição oficial identifica Nunito como uma família sem serifa de terminais arredondados: [Google Fonts · Nunito](https://github.com/google/fonts/tree/main/ofl/nunito). Use Nunito, não Nunito Sans.

Estas orientações não estabelecem automaticamente a tipografia das outras marcas do grupo. O registro da decisão e os arquivos utilizados estão em [typography-policy.json](typography-policy.json).

## Composição QP

A página demonstra “Bacalar Expanded Caixa Alta + Sora Light + Instrument Serif Italic” e sua reordenação. Misturar famílias é uma possibilidade expressiva; não é obrigatório usar quatro fontes na mesma peça.

Textos longos podem ser alinhados à esquerda ou ao centro; evitar justificação e alinhamento à direita. Ajuste a hierarquia ao formato, sem importar automaticamente tamanhos de UI para slides ou posts.

## Arquivos e carregamento

As fontes disponíveis e os textos de licença recebidos estão em assets/fontes. A Bacalar foi importada do kit usado no Brand Navigator a pedido do responsável. Seu arquivo OpenType e o aviso de origem foram preservados. [fonts.css](../assets/fonts.css) carrega os arquivos locais com famílias, estilos e pesos reais. Lilita One é estática, peso 400; Nunito é variável, pesos 200–1000. Não sintetize negrito ou itálico ausente.

Em HTML, aguarde document.fonts.ready e verifique o carregamento do arquivo e a fonte efetivamente renderizada. Em Figma, carregue a família e o estilo disponíveis. Em PPTX, confira a fonte na máquina de renderização; citar seu nome no arquivo não significa que ela está embutida.

Frase de verificação: “AÇÃO · São João · Coração · ônibus · amanhã · ¿A dónde viajas?”. Confira também CAIXA ALTA nos títulos QP. Lilita One, Nunito e a Bacalar importada do kit cobrem todos os acentos e sinais dessa frase verificados no mapa de caracteres.

## Bacalar com acentos, do Brand Navigator

A fonte efetivamente usada pelo Brand Navigator vem do kit `https://use.typekit.net/ril0uew.css`, configurado em index.html e priorizado em src/index.css. A pedido do responsável em 30/10/2026, foi importado o arquivo **OpenType de Bacalar Expanded servido por esse kit**, sem alterar os bytes.

Arquivo local: `assets/fontes/bacalar/BacalarExpanded-BrandNavigator-Semibold.otf`. Família da skill: **Bacalar Expanded**; estilo normal; **peso 600**, o mesmo declarado no kit. O [fonts.css](../assets/fonts.css) registra o nome e o peso explicitamente. Não usar peso 400 ou negrito artificial como se fossem estilos importados desse arquivo.

Os 26 acentos e sinais portugueses/espanhóis testados estão presentes, incluindo Á, Ã, Ç, É, Ó, Ô, á, ã, ç, é, ó, ô, ¿ e ñ. A renderização deve conferir o texto real e a fonte efetiva; cobertura do mapa de caracteres não dispensa a conferência visual. Exemplo de título: **AÇÃO QUE TE MOVE**.

O responsável informou autorização de uso da Bacalar e indicou a versão do Brand Navigator. O arquivo não é OFL: o aviso do kit e a referência de licença estão em assets/fontes/bacalar/Origem-BrandNavigator.txt. Metadados, peso e hash estão em [typography-policy.json](typography-policy.json); o diagnóstico completo está em fontes-de-origem/bacalar-brand-navigator.json na base de manutenção.

### HTML e editores de apresentação

O OpenType importado é o arquivo de entrega web: possui uma tabela de nomes reduzida. Em **HTML**, carregue-o pelo CSS local; não há dependência do kit externo para renderizar a peça. Não usar o nome PostScript “-” como nome de família na composição: a família CSS é Bacalar Expanded.

Em **Figma, PowerPoint, Google Slides ou outro editor**, confirme a disponibilidade e a renderização no próprio programa. Este pacote não atesta instalação desktop nem embutimento em Office. Se a ferramenta não aceitar o arquivo servido pelo kit, obtenha a versão desktop com nomes completos; informe essa limitação concreta, sem transformar uma prova HTML em evidência de compatibilidade desktop.

### ZIP enviado anteriormente

O ZIP fornecido tem BacalarTest sem acentos; seus arquivos são idênticos aos OTFs de fallback presentes no código do Brand Navigator. A correção vista no site vem do kit Adobe, não desses OTFs. Embora o responsável tenha autorizado seu uso apesar da marcação Demo / Trial, **eles não são a versão ativa desta base**. O registro da autorização, nomes e hashes foi preservado em fontes-de-origem/bacalar-recebida.json; o pacote usa a versão com acentos indicada posteriormente.
