# Loading states

Fonte: Brand Navigator /componentes/loading-states. Atualização na origem: 2026-05-04T21:17:51.75476+00:00.

> Transcrição da página publicada. Exemplos de interface e dados ilustrativos permanecem exemplos; não são políticas comerciais.


<!-- bloco 0 · c818c64c-d544-4a8d-83e1-79299f1c5958 · section -->

<h2>Loading states</h2><p>Loading não é tempo perdido — é tempo comunicado. Cada espera bem desenhada transmite que o sistema está trabalhando e que a pessoa não está sozinha.</p>


<!-- bloco 1 · a391721e-b1ef-4d25-84b0-1e42d900a642 · section -->

<h3>Tipos de loading</h3><ul><li><strong>Spinner</strong> — para ações curtas (até 2s) em botões e pequenas áreas.</li><li><strong>Skeleton</strong> — para carregamento de páginas e listas (preferido em conteúdo previsível).</li><li><strong>Progress bar</strong> — para ações longas com progresso conhecido (upload, processamento).</li><li><strong>Indeterminate progress</strong> — para ações longas sem progresso conhecido.</li></ul>


<!-- bloco 2 · 7d214448-c49d-4d59-93c0-914458e767e4 · section -->

<h3>Skeleton em ação</h3><div style='display:flex;flex-direction:column;gap:12px;max-width:500px'><div style='background:linear-gradient(90deg,#EDF0F7,#F7F8FB,#EDF0F7);height:24px;width:60%;border-radius:6px'></div><div style='background:linear-gradient(90deg,#EDF0F7,#F7F8FB,#EDF0F7);height:16px;width:90%;border-radius:6px'></div><div style='background:linear-gradient(90deg,#EDF0F7,#F7F8FB,#EDF0F7);height:16px;width:80%;border-radius:6px'></div></div>


<!-- bloco 3 · 6929ffcf-81c3-412f-88e1-3287c0e563f6 · section -->

Em botões: troque o texto por spinner mantendo a largura original. Em telas: use skeleton no formato do conteúdo final. Em ações longas: comunique o que está acontecendo ('Confirmando pagamento...').

Diretrizes

Telas em branco sem feedback, spinners gigantes em meio à tela e botões que somem ou mudam de tamanho durante o loading.

Evite


<!-- bloco 4 · e49c9956-1620-428d-81ed-c8d7c49e0d07 · section -->

Exemplo ao vivo
