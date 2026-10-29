# Botões

Fonte: Brand Navigator /componentes/botoes. Atualização na origem: 2026-05-04T21:17:51.75476+00:00.

> Transcrição da página publicada. Exemplos de interface e dados ilustrativos permanecem exemplos; não são políticas comerciais.


<!-- bloco 0 · d4ba7e9d-a5bd-4cd8-9d84-f75388aa432e · section -->

<h2>Botões</h2><p>Botões são o motor da conversão. Cada clique em <em>BUSCAR</em>, <em>PAGAR AGORA</em> ou <em>CONFIRMAR</em> precisa transmitir segurança, clareza e direção. Por isso, na Quero Passagem, botões seguem regras rígidas de hierarquia, contraste e linguagem.</p>


<!-- bloco 1 · d1990c3a-eeb9-478e-9701-d50b52d118cc · section -->

<h3>Anatomia</h3><ul><li>Fonte <strong>Inter</strong>, sempre em <strong>uppercase</strong>.</li><li>Cantos arredondados entre 8px e 12px.</li><li>Altura generosa, com boa área de clique.</li><li>Contraste alto entre texto e fundo.</li><li>Ícones opcionais — sempre alinhados à esquerda do texto.</li></ul><h3>Tamanhos</h3><table style='width:100%;border-collapse:collapse'><thead><tr><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Tamanho</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Texto</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Padding</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Uso</th></tr></thead><tbody><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Small</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>12px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>8–12px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Ações compactas, interfaces densas</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Regular</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>14px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>12–16px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Botão padrão da interface</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Large</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>18px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>16–24px</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>CTAs principais e grandes</td></tr></tbody></table>


<!-- bloco 2 · bf5acbb8-0f18-46fd-b2e7-ae760635df06 · section -->

<h3>Hierarquia visual</h3><div style='display:flex;flex-wrap:wrap;gap:12px'><button style='background:#0066FF;color:#fff;border:none;padding:12px 24px;border-radius:8px;font-weight:700;text-transform:uppercase;font-size:14px'>Primário</button><button style='background:#003D99;color:#fff;border:none;padding:12px 24px;border-radius:8px;font-weight:700;text-transform:uppercase;font-size:14px'>Primário hover</button><button style='background:transparent;color:#0066FF;border:1px solid #0066FF;padding:12px 24px;border-radius:8px;font-weight:700;text-transform:uppercase;font-size:14px'>Secundário</button><button style='background:#E6F0FF;color:#0066FF;border:1px solid #0066FF;padding:12px 24px;border-radius:8px;font-weight:700;text-transform:uppercase;font-size:14px'>Sec. claro</button><button style='background:transparent;color:#0066FF;border:none;padding:12px 24px;font-weight:700;text-transform:uppercase;font-size:14px'>Terciário</button><button style='background:#0B9652;color:#fff;border:none;padding:12px 24px;border-radius:8px;font-weight:700;text-transform:uppercase;font-size:14px'>Sucesso</button><button style='background:#CC2929;color:#fff;border:none;padding:12px 24px;border-radius:8px;font-weight:700;text-transform:uppercase;font-size:14px'>Perigo</button><button style='background:transparent;color:#CC2929;border:1px solid #CC2929;padding:12px 24px;border-radius:8px;font-weight:700;text-transform:uppercase;font-size:14px'>Perigo outline</button><button style='background:#D5D8DE;color:#fff;border:none;padding:12px 24px;border-radius:8px;font-weight:700;text-transform:uppercase;font-size:14px'>Desabilitado</button></div>


<!-- bloco 3 · 05e64259-edf2-4a4a-ab4a-880543b8f2b6 · section -->

<h3>Quando usar cada variante</h3><ul><li><strong>Primário</strong> — ação principal da tela. Apenas <strong>um</strong> por área visível.</li><li><strong>Secundário outline</strong> — ações importantes, mas alternativas (ex.: voltar, login).</li><li><strong>Secundário claro</strong> — filtros e ações em áreas com fundo claro.</li><li><strong>Terciário</strong> — ações leves, dentro de cards (ex.: ver detalhes, editar).</li><li><strong>Sucesso / Perigo</strong> — apenas para reforçar consequência da ação.</li></ul>


<!-- bloco 4 · 3e921c89-5de3-417e-af26-7e3600f5cf0b · section -->

<h3>Estados obrigatórios</h3><p>Todo botão precisa prever os seguintes estados:</p><ul><li><strong>Default</strong> — estado de repouso.</li><li><strong>Hover</strong> — fundo escurece levemente.</li><li><strong>Active / pressed</strong> — leve compressão visual.</li><li><strong>Focus</strong> — outline visível para teclado.</li><li><strong>Disabled</strong> — fundo cinza, sem cursor de clique.</li><li><strong>Loading</strong> — spinner ou texto 'CARREGANDO', mantendo a largura original.</li></ul>


<!-- bloco 5 · 4e0c2b46-8f16-45f6-8c03-0a16727f74b5 · section -->

Use verbos no infinitivo ou imperativo curto: BUSCAR, PAGAR, CONFIRMAR, EDITAR, CANCELAR. Quanto mais direto, maior a conversão.

Texto que converte

Frases longas em uppercase, dois botões primários competindo na mesma tela e cores fora da paleta semântica para criar 'destaque extra'.

Evite


<!-- bloco 6 · ed531a0b-651b-4f46-98ad-070029fbdb02 · section -->

Exemplo ao vivo


<!-- bloco 7 · 130f526f-29e6-4933-a694-efce2398d156 · section -->

Exemplo ao vivo
