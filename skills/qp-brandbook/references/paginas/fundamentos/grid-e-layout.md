# Grid e layout

Fonte: Brand Navigator /fundamentos/grid-e-layout. Atualização na origem: 2026-05-04T21:17:51.75476+00:00.

> Transcrição da página publicada. Exemplos de interface e dados ilustrativos permanecem exemplos; não são políticas comerciais.


<!-- bloco 0 · 13d56652-fd70-4861-b654-4dcff7e6a2d1 · section -->

<h2>Grid e layout</h2><p>O grid da Quero Passagem nasce de uma ideia simples: <strong>cada elemento precisa ter um lugar previsível na tela</strong>. Ele organiza a informação, dá ritmo à leitura e garante que a interface continue coerente entre uma landing institucional, um checkout transacional ou um dashboard interno.</p><p>Mais do que uma malha técnica, o grid é o que faz a marca parecer arrumada — mesmo quando o conteúdo muda, o layout permanece confiável.</p>


<!-- bloco 1 · 1503689d-0a8e-4141-87e2-00dc7e64d268 · section -->

<h3>Princípios de composição</h3><ul><li><strong>Containers bem definidos.</strong> Toda página vive dentro de um container central, com largura máxima controlada.</li><li><strong>Alinhamento à esquerda.</strong> Nossa leitura começa pela esquerda; mantenha títulos e textos ancorados ali.</li><li><strong>Modularidade.</strong> Cards, blocos e seções funcionam como peças encaixáveis — fáceis de combinar e reorganizar.</li><li><strong>Respiro intencional.</strong> Espaço vazio não é desperdício, é hierarquia.</li><li><strong>Separação clara entre seções.</strong> Use 40, 48 ou 64px verticais para delimitar grandes blocos.</li></ul>


<!-- bloco 2 · b14983f1-7002-473a-9f3c-33501c60ffd8 · section -->

<h3>Larguras de referência</h3><p>O sistema considera três contextos principais — desktop, tablet e mobile — sempre garantindo conforto de leitura.</p><table style='width:100%;border-collapse:collapse'><thead><tr><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Largura</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Token</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Dispositivo de referência</th></tr></thead><tbody><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>1920px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Desktop large</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Monitores amplos e apresentações</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>1536px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Desktop default</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Desktop padrão amplo</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>1366px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Desktop small</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Notebooks e desktops comuns</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>840px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Tablet</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Tablets e telas intermediárias</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>412px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Mobile large</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Samsung S20 FE e similares</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>390px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Mobile default</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>iPhone 13/14</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>360px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Mobile small</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Android compacto</td></tr></tbody></table>


<!-- bloco 3 · 1d230d6d-62ec-42c2-8e08-dadea8f98a9b · section -->

<h3>Breakpoints</h3><table style='width:100%;border-collapse:collapse'><thead><tr><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Breakpoint</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Faixa</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Uso</th></tr></thead><tbody><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Mobile small</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>até 360px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Smartphones menores</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Mobile default</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>361–412px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Smartphones comuns</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Tablet</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>413–840px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Tablets e telas intermediárias</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Desktop small</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>841–1366px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Notebooks</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Desktop default</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>1367–1536px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Desktop padrão</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Desktop large</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>acima de 1536px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Monitores grandes</td></tr></tbody></table>


<!-- bloco 4 · d3a56be5-5b42-4579-87d1-5f3744c7c1d7 · section -->

<h3>Como o grid se comporta em cada tela</h3><h4>Desktop</h4><ul><li>Container centralizado com largura máxima</li><li>Grids de 2, 3 ou 4 colunas conforme densidade</li><li>Espaçamento horizontal generoso entre cards</li><li>Hierarquia visual ampla, com títulos grandes e respiros laterais</li></ul><h4>Tablet</h4><ul><li>Uma ou duas colunas, raramente três</li><li>Cards em grade aproveitando o espaço horizontal</li><li>Menus adaptados, ainda com boa área de toque</li></ul><h4>Mobile</h4><ul><li>Layout em coluna única</li><li>Cards empilhados, CTAs em largura total</li><li>Redução de títulos muito grandes</li><li>Menor densidade de informações por tela</li></ul>


<!-- bloco 5 · f322d6c1-5750-4846-9978-d5160ede44ba · section -->

Em telas muito grandes (acima de 1536px), trave o conteúdo principal em uma largura máxima. Nunca deixe parágrafos longos atravessarem 1200px — o olho perde a linha e a leitura cansa.

Regra prática para containers

Composições com 5+ colunas em desktop, gutters inconsistentes entre seções e blocos sem alinhamento vertical comum. O layout perde ritmo e a marca parece improvisada.

Evite


<!-- bloco 6 · c60b940f-4e8e-457b-8a8f-fa0400a153fb · section -->

<h3>Diagrama mental</h3><p>Pense em cada página como uma pilha de seções — todas com o mesmo container, separadas por espaços previsíveis. Dentro de cada seção, o conteúdo se distribui em colunas que reagem ao breakpoint.</p><pre style='background:#F7F8FB;padding:16px;border-radius:12px;font-family:monospace;font-size:13px;line-height:1.6'>┌─────────────── container ───────────────┐
│  Hero                                    │  ← seção 1
├──────────────────────────────────────────┤
│  [card] [card] [card]                    │  ← seção 2 (3 cols)
├──────────────────────────────────────────┤
│  [bloco texto]      [bloco imagem]       │  ← seção 3 (2 cols)
└──────────────────────────────────────────┘</pre>


<!-- bloco 7 · dba59d92-8c78-4649-8e16-c4892cb546f6 · section -->

Exemplo ao vivo
