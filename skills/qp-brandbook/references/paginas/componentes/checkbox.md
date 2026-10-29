# Checkbox

Fonte: Brand Navigator /componentes/checkbox. Atualização na origem: 2026-05-04T21:17:51.75476+00:00.

> Transcrição da página publicada. Exemplos de interface e dados ilustrativos permanecem exemplos; não são políticas comerciais.


<!-- bloco 0 · d422cad6-6ab0-4e9d-b94d-397b87f33bdd · section -->

<h2>Checkbox</h2><p>Checkboxes representam <strong>escolhas independentes</strong> — o usuário pode marcar nenhuma, uma ou várias opções ao mesmo tempo. São usadas para filtros, listas de preferências, termos de aceite e seleção múltipla.</p>


<!-- bloco 1 · 1b5f25ea-5437-4ff3-995a-51dade9436a6 · section -->

<h3>Anatomia</h3><ul><li>Quadrado com radius 4px.</li><li>Estado <strong>marcado</strong>: fundo azul + ícone de check branco.</li><li>Estado <strong>indeterminado</strong>: fundo azul + traço horizontal (para 'selecionar todos' parcial).</li><li>Label clicável posicionada à direita.</li><li>Espaço entre quadrado e label: 8px.</li></ul><h3>Estados</h3><ul><li>Default · Hover · Focus · Checked · Indeterminate · Disabled · Error</li></ul>


<!-- bloco 2 · a24f5f3f-d255-4e4e-a61f-fb28be61d3b1 · section -->

<h3>Demonstração</h3><div style='display:flex;flex-direction:column;gap:12px;font-size:14px'><label style='display:flex;align-items:center;gap:8px'><input type='checkbox' style='width:18px;height:18px'> Quero receber promoções por e-mail</label><label style='display:flex;align-items:center;gap:8px'><input type='checkbox' checked style='width:18px;height:18px'> Aceito os termos de uso</label><label style='display:flex;align-items:center;gap:8px;color:#9CA3AF'><input type='checkbox' disabled style='width:18px;height:18px'> Opção indisponível</label></div>


<!-- bloco 3 · b44b02f9-b8fc-4e88-8336-868199816417 · section -->

Sempre permita clicar no texto da label, não apenas no quadradinho. Isso aumenta a área de toque e melhora a usabilidade.

Boa prática

Usar checkbox para escolha única (o correto é radio) ou esconder a label dependendo apenas de ícone.

Evite


<!-- bloco 4 · 95b2dadc-1175-465f-8121-2e37abfff2dc · section -->

Exemplo ao vivo
