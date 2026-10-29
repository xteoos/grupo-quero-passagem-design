# Acessibilidade

Fonte: Brand Navigator /fundamentos/acessibilidade. Atualização na origem: 2026-05-04T21:17:51.75476+00:00.

> Transcrição da página publicada. Exemplos de interface e dados ilustrativos permanecem exemplos; não são políticas comerciais.


<!-- bloco 0 · 76efe470-2111-49a5-9a59-4b36b803aadf · section -->

<h2>Acessibilidade</h2><p>Acessibilidade não é um item da checklist final — é o ponto de partida do design. Na Quero Passagem, qualquer pessoa deve conseguir comprar uma passagem, navegar pelo app ou ler uma comunicação, independentemente de visão, audição, mobilidade ou contexto de uso.</p><p>Esta página reúne os critérios mínimos que todo produto e peça da marca deve respeitar.</p>


<!-- bloco 1 · eb2164d7-ca37-4ec9-b13f-1da22ca898fa · section -->

<h3>Contraste de cores</h3><p>Seguimos as recomendações da <strong>WCAG 2.2 AA</strong> como linha de base, e <strong>AAA</strong> sempre que possível.</p><table style='width:100%;border-collapse:collapse'><thead><tr><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Elemento</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Contraste mínimo</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Observação</th></tr></thead><tbody><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Texto normal (até 18px)</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>4.5:1</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>AA mínimo</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Texto grande (≥18px bold ou ≥24px)</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>3:1</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>AA mínimo</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Componentes interativos (bordas, ícones)</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>3:1</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>AA mínimo</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Texto sobre imagem</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>4.5:1 com overlay</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Use overlay escuro quando necessário</td></tr></tbody></table>


<!-- bloco 2 · 26a0e1cc-d29e-4e33-a7d3-f5b8777eed0a · section -->

<h3>Foco visível</h3><p>O estado de foco é o que permite a navegação por teclado. Ele <strong>nunca</strong> deve ser removido — apenas estilizado.</p><ul><li>Outline azul externo de 2 a 4px com boa visibilidade.</li><li>Não confiar apenas em mudança de cor interna do componente.</li><li>Garantir que o foco apareça em links, botões, inputs, tabs, cards clicáveis e qualquer elemento interativo.</li></ul>


<!-- bloco 3 · 032ae460-7e60-412e-8d48-d487e94526fe · section -->

<h3>Tamanho mínimo de toque</h3><p>Em mobile, alvos de toque devem ter pelo menos <strong>44x44px</strong>. Em desktop, mantenha botões e ícones clicáveis com altura mínima de 40px.</p>


<!-- bloco 4 · 36340240-9ad6-4cf6-baaa-a7860870f634 · section -->

<h3>Texto e leitura</h3><ul><li><strong>Tamanho mínimo</strong>: 14px para conteúdo funcional, 12px apenas para captions e metadados.</li><li><strong>Line-height</strong>: mínimo 1.4 para corpo de texto, 1.2 para títulos.</li><li><strong>Largura de linha</strong>: idealmente entre 50 e 75 caracteres.</li><li><strong>Evite uppercase em blocos longos</strong> — ele reduz a velocidade de leitura.</li><li><strong>Hierarquia semântica</strong>: use h1 → h2 → h3 na ordem correta, não apenas por estilo.</li></ul>


<!-- bloco 5 · af6cf40c-19e3-474f-92cb-73c237963d80 · section -->

<h3>Imagens, ícones e mídia</h3><ul><li>Toda imagem informativa precisa de <code>alt</code> descritivo. Imagens decorativas usam <code>alt=""</code>.</li><li>Ícones que carregam significado sozinhos precisam de <code>aria-label</code>.</li><li>Vídeos devem ter legendas; áudios devem ter transcrição.</li><li>Não comunique <strong>apenas</strong> por cor — combine cor com ícone ou texto (ex.: erro vermelho + ícone + mensagem).</li></ul>


<!-- bloco 6 · 07091b36-d216-4c9d-a750-7d241c1d72ca · section -->

<h3>Formulários acessíveis</h3><ul><li>Todo campo precisa de <code>label</code> visível e associado via <code>for</code>/<code>id</code>.</li><li>Erros descritos em texto, próximos ao campo, e anunciados a leitores de tela.</li><li>Placeholder não substitui label.</li><li>Use <code>autocomplete</code> sempre que possível (nome, email, telefone, cartão).</li></ul>


<!-- bloco 7 · 0572b7e4-9a3a-4c66-88ff-48c6899f5d11 · section -->

Teste cada novo fluxo navegando apenas pelo teclado (Tab, Shift+Tab, Enter, Esc). Se algo não responder ou desaparecer do foco, é bug de acessibilidade.

Faça

Comunicar status apenas com cor, esconder o outline de foco, usar texto cinza-claro sobre branco ou inserir botões e links sem rótulo descritivo.

Evite

Lighthouse, axe DevTools, Wave e o leitor de tela nativo do sistema (NVDA, VoiceOver, TalkBack) resolvem 80% dos problemas antes de chegarem em produção.

Ferramentas úteis


<!-- bloco 8 · bdaeb2b6-f575-4cbe-a353-698415e7e398 · section -->

Exemplo ao vivo


<!-- bloco 9 · de7e07a7-775a-439c-b3fa-fdb80dfe0bf4 · section -->

Exemplo ao vivo
