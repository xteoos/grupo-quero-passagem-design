# Crie materiais com a cara da Quero Passagem

Este é o guia de marca da Quero Passagem e das marcas do grupo, preparado para ajudar pessoas e ferramentas de inteligência artificial a criar **apresentações, posts, anúncios e comunicados**.

Aqui você encontra orientações de cores, fontes, fotografias e escrita, além de logos, imagens e modelos prontos para adaptar. Você pode usar esta base mesmo sem conhecer design ou programação.

## O que é uma “skill”?

Pense em uma skill como um **guia de trabalho que a IA consulta antes de criar**. A nossa se chama `qp-brandbook`: ela explica como usar os materiais da marca, quais arquivos escolher e o que conferir antes de entregar.

Ela vem acompanhada das fontes, imagens, modelos e referências. Por isso, é preciso usar **a pasta completa**, e não apenas o arquivo de instruções `SKILL.md`.

## Quero começar: o que faço?

### 1. Dê acesso aos materiais

Se você usa **Codex ou Claude Code no computador**, peça à ferramenta para preparar a base. Pode copiar esta mensagem:

> Baixe o repositório https://github.com/xteoos/grupo-quero-passagem-design. Baixe também os arquivos grandes com Git LFS. Prepare a skill qp-brandbook para uso neste projeto, usando a pasta completa skills/qp-brandbook. Confira se consegue abrir as fontes, fotos e modelos antes de começarmos.

Essa preparação precisa ser feita uma vez por computador ou projeto. Se a ferramenta pedir uma ação que você não conhece, peça ajuda a alguém da equipe técnica. As instruções manuais estão [mais abaixo](#instalação-manual-para-quem-vai-configurar).

Se você usa **ChatGPT, Claude no navegador ou outra IA**, envie este pedido:

> Use o guia https://github.com/xteoos/grupo-quero-passagem-design. Comece pelo arquivo skills/qp-brandbook/SKILL.md e consulte as referências da marca. Antes de criar, confirme quais fontes, imagens e modelos você consegue realmente acessar. Se faltar algo, diga quais arquivos preciso fornecer.

O link ajuda a encontrar as instruções, mas **não garante acesso a todos os arquivos nem capacidade de editar uma apresentação**. Quando necessário, anexe à conversa as referências e os arquivos escolhidos. A instalação local descrita aqui é para Codex e Claude Code; as versões no navegador têm seus próprios recursos e limites.

### 2. Diga o que você precisa

Informe a marca, para quem é o material, o objetivo, onde será usado e como quer receber. Não precisa escrever um pedido técnico.

**Apresentação:**

> Use a skill qp-brandbook. Preciso de uma apresentação da Quero Passagem para uma reunião interna, com 6 slides. O objetivo é apresentar o projeto descrito no texto abaixo. Use o modelo oficial e entregue um PowerPoint editável. Não invente dados. Conteúdo: [cole aqui].

**Post:**

> Use a skill qp-brandbook. Crie um post da Quero Passagem para Instagram, no tamanho 1080 × 1350, com o tema [tema]. Use fotografias e elementos do acervo. Entregue a imagem pronta e um arquivo que possamos editar. Texto obrigatório: [texto].

**Comunicado:**

> Use a skill qp-brandbook. Crie um comunicado interno da Quero Passagem sobre [assunto], usando o modelo de comunicados. Inclua estas informações: [informações]. Se faltar uma data ou orientação importante, me pergunte. Quero receber em [formato].

**Outras marcas do grupo:**

> Use a skill qp-brandbook para criar um post da Viajo Mucho, em espanhol para o México, sobre [tema]. Use os modelos dessa marca e a adaptação tipográfica em Lilita One prevista nesta base.

Para Rodon, informe a marca no pedido; os títulos adaptados usam Nunito ExtraBold. A IA deve selecionar os modelos e os elementos próprios de cada marca.

### 3. Confira antes de compartilhar

Peça para a IA mostrar a peça pronta e explicar brevemente qual modelo usou e se ficou alguma pendência. Confira textos, acentos, logos, fotos e informações do seu pedido. Um exemplo antigo pode conter datas ou ofertas que não valem mais.

Se quiser ajustar, peça em linguagem comum: “diminua o texto”, “troque a fotografia” ou “deixe o título mais visível, mantendo a identidade da marca”.

## Quero ver os materiais disponíveis

Depois de baixar a base, abra [o catálogo visual](catalogo/index.html) no navegador. Ele permite buscar materiais, filtrar por marca e ver a origem de cada arquivo. A prévia ajuda a escolher; use o arquivo original na produção.

Se as fontes não carregarem ao abrir o arquivo diretamente, peça à IA: “Inicie o catálogo local deste projeto”. O endereço padrão é [abrir catálogo local](http://127.0.0.1:8769/catalogo/), disponível apenas enquanto o servidor estiver ativo no seu computador.

| O que você procura | Onde encontrar |
|---|---|
| Instruções que a IA deve seguir | [Skill qp-brandbook](skills/qp-brandbook/SKILL.md) |
| Cores, fontes, fotos e escrita | [Referências da marca](skills/qp-brandbook/references/) |
| Logos, fotos, fontes e modelos | [Arquivos para criar as peças](skills/qp-brandbook/assets/) |
| O que foi coletado e o que ainda falta | [Cobertura e pendências](fontes-de-origem/COBERTURA.md) |
| Exemplos e conferências realizadas | [Relatório de validação](validacao/RELATORIO.md) |

## O que mudou nas fontes

- **Viajo Mucho:** Lilita One substitui Mauren nos títulos das novas adaptações; Work Sans continua nos textos de apoio.
- **Rodon:** Nunito ExtraBold, peso 800, substitui All Round Gothic nos títulos das novas adaptações; Poppins continua nos textos de apoio.
- **Quero Passagem:** Sora, Inter, Instrument Serif e Bacalar Expanded com acentos estão incluídas. A Bacalar foi importada do mesmo kit usado pelo Brand Navigator, conforme indicado pelo responsável. A IA deve carregar a fonte e conferir o resultado na ferramenta escolhida.

As substituições foram solicitadas pelo responsável para facilitar o uso da base. Os modelos originais foram preservados. Veja [as regras de tipografia](skills/qp-brandbook/references/tipografia.md) e os [modelos adaptados](skills/qp-brandbook/assets/templates/adaptados/).

## Instalação manual para quem vai configurar

Você precisa de Git e Git LFS, que baixam o projeto e seus arquivos grandes. O acervo ocupa aproximadamente 3 GB. Com essas ferramentas instaladas, execute no Terminal:

```sh
git clone https://github.com/xteoos/grupo-quero-passagem-design.git
cd grupo-quero-passagem-design
git lfs install --local
git lfs pull
```

Evite depender apenas do botão “Download ZIP” do GitHub: alguns arquivos podem vir como pequenos arquivos de referência, em vez de fotos ou apresentações reais. `git lfs pull` baixa os originais.

**Codex:** copie a pasta inteira `skills/qp-brandbook` para `.agents/skills/qp-brandbook` dentro do projeto em que vai trabalhar. Para usar em vários projetos, a localização pessoal é `~/.agents/skills/qp-brandbook`. Abra uma nova conversa e peça “Use $qp-brandbook…”. Consulte a [documentação do Codex](https://developers.openai.com/codex/skills).

**Claude Code:** copie a mesma pasta inteira para `.claude/skills/qp-brandbook` no projeto, ou `~/.claude/skills/qp-brandbook` para uso pessoal. Abra uma nova sessão e use `/qp-brandbook` seguido do pedido. Consulte a [documentação do Claude Code](https://code.claude.com/docs/en/skills).

Dentro da pasta instalada devem existir `SKILL.md`, `references`, `assets`, `scripts` e `agents`. Copiar só o texto de `SKILL.md` não leva as fontes e os materiais junto. Ao atualizar esta base, atualize também a cópia instalada.

## Para quem mantém esta base

O passo a passo técnico de atualização, instalação das ferramentas de validação e conferência dos arquivos está em [Atualizar a base](fontes-de-origem/ATUALIZAR.md).

As regras vêm das páginas publicadas do Brand Navigator e os materiais vêm das fontes registradas no Drive e Figma. Arquivos históricos e prévias com marca d’água têm identificação própria. Usar a skill não publica a peça automaticamente nem altera os arquivos de origem.
