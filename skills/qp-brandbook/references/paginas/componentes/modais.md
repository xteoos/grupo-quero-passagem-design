# Modais

Fonte: Brand Navigator /componentes/modais. Atualização na origem: 2026-06-02T14:31:31.786767+00:00.

> Transcrição da página publicada. Exemplos de interface e dados ilustrativos permanecem exemplos; não são políticas comerciais.


<!-- bloco 0 · 1c4f2337-8d09-449f-9fcd-c24e15ff5bba · section -->

<h2>Modais</h2><p>Modais interrompem o fluxo para focar a atenção em uma decisão importante. Use com cautela: cada modal é uma pausa forçada na jornada do usuário.</p>


<!-- bloco 1 · 23d3e37e-be0a-48b7-98ae-83f994ae3c8e · section -->

<h3>Estrutura</h3><ul><li><strong>Radius</strong>: 16 a 24px.</li><li><strong>Padding interno</strong>: 24 a 32px.</li><li><strong>Sombra</strong>: suave e difusa.</li><li><strong>Overlay</strong>: fundo escuro com 40–60% de opacidade.</li><li><strong>Título</strong>: Sora Header 4 ou Header 5.</li><li><strong>Corpo</strong>: Inter Body 1 ou Body 2.</li><li><strong>Botões</strong>: no rodapé, alinhados à direita (em desktop) ou em largura total (em mobile).</li><li><strong>Espaçamento entre blocos</strong>: 16 a 24px.</li></ul>


<!-- bloco 2 · f3670ff0-05b0-4e91-97ad-3651c3e78559 · section -->

<h3>Quando usar</h3><ul><li>Confirmações destrutivas (cancelar pedido, excluir item).</li><li>Coleta rápida de dados que interrompe o fluxo intencionalmente.</li><li>Detalhes que cabem em poucos parágrafos.</li></ul><h3>Quando evitar</h3><ul><li>Conteúdo longo — use uma página ou drawer.</li><li>Informações secundárias — use tooltip ou inline.</li><li>Empilhar múltiplos modais (anti-padrão grave).</li></ul>


<!-- bloco 3 · ecf86a0a-565a-41d7-9a94-ef068d306567 · section -->

Todo modal precisa: focar o primeiro elemento ao abrir, prender o foco dentro dele (focus trap), fechar com Esc e devolver o foco ao elemento que o abriu.

Acessibilidade essencial

Modais sem botão de fechar visível, modais que aparecem antes da pessoa interagir e modais para promoções intrusivas.

Evite


<!-- bloco 4 · 324aece4-1f3c-4799-99e6-0d18dc6dbd3a · section -->

Exemplo ao vivo
