# Crie materiais com a cara da Quero Passagem

Este é o guia de marca da Quero Passagem e das marcas do grupo, preparado para ajudar pessoas e ferramentas de inteligência artificial a criar **apresentações, posts, anúncios e comunicados**.

Aqui você encontra orientações de cores, fontes, fotografias e escrita, além de logos, imagens e modelos prontos para adaptar. Você pode usar esta base mesmo sem conhecer design ou programação.

## O que é uma “skill”?

Pense em uma skill como um **guia de trabalho que a IA consulta antes de criar**. A nossa se chama `qp-brandbook`: ela explica como usar os materiais da marca, quais arquivos escolher e o que conferir antes de entregar.

A instalação é pequena: leva as instruções e as ferramentas de consulta. Quando você faz um pedido, a IA consulta este GitHub e baixa somente as fontes, imagens e modelos necessários. Você não precisa baixar o projeto inteiro nem instalar Git ou Git LFS.

## Quero começar: o que faço?

### 1. Instale a skill uma vez

[**Baixar a skill qp-brandbook**](https://raw.githubusercontent.com/xteoos/grupo-quero-passagem-design/main/distribution/qp-brandbook.zip)

Se você usa **Codex ou Claude Code**, pode copiar esta mensagem para a ferramenta:

> Instale a skill qp-brandbook usando o pacote https://raw.githubusercontent.com/xteoos/grupo-quero-passagem-design/main/distribution/qp-brandbook.zip. Extraia a pasta qp-brandbook no diretório de skills deste projeto. Não clone o repositório. Leia SKILL.md e use a consulta ao GitHub para obter só os materiais necessários para meus pedidos.

Depois de instalar, abra uma nova conversa para a ferramenta reconhecer a skill. As instruções manuais estão [mais abaixo](#instalação-manual-para-quem-vai-configurar).

Se você usa **ChatGPT, Claude no navegador ou outra IA**, verifique se a ferramenta permite adicionar skills. Quando permitir, use o mesmo pacote. Se ela não tiver esse recurso, envie:

> Consulte https://github.com/xteoos/grupo-quero-passagem-design, começando por skills/qp-brandbook/SKILL.md. Siga o acesso remoto descrito na skill e obtenha apenas os materiais necessários. Antes de criar, confirme quais arquivos você consegue baixar e usar de verdade.

A ferramenta precisa acessar a internet e conseguir baixar e trabalhar com arquivos. Um link, sozinho, não dá essas capacidades à IA. Se ela não puder realizar alguma etapa, deve explicar o que falta e pedir apenas os arquivos necessários.

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

Peça à IA: “Mostre algumas opções de templates e fotografias adequadas para este pedido antes de criar”. Ela consulta o catálogo no GitHub e baixa as prévias necessárias para você escolher. Os originais são obtidos quando usados na peça.

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

Baixe [o pacote leve da skill](https://raw.githubusercontent.com/xteoos/grupo-quero-passagem-design/main/distribution/qp-brandbook.zip) e extraia o ZIP. Dentro dele há uma pasta chamada `qp-brandbook`.

**Codex:** coloque essa pasta em `.agents/skills/qp-brandbook` no projeto em que vai trabalhar. Para usar em vários projetos, use `~/.agents/skills/qp-brandbook`. Abra uma nova conversa e peça “Use $qp-brandbook…”.

**Claude Code:** coloque a pasta em `.claude/skills/qp-brandbook` no projeto, ou `~/.claude/skills/qp-brandbook` para uso pessoal. Abra uma nova sessão e use `/qp-brandbook` seguido do pedido.

Mantenha a pasta inteira do pacote, incluindo `SKILL.md`, `references`, `scripts` e `agents`. Não é preciso baixar a pasta de imagens deste repositório. A IA usa Python 3, internet e permissão para salvar arquivos para buscar os materiais conforme a necessidade. Não é necessário instalar bibliotecas Python adicionais.

A skill consulta as regras e o catálogo atuais no início de cada pedido. Os materiais baixados são reaproveitados após uma conferência de integridade. Para atualizar as ferramentas da própria skill, substitua a instalação pelo pacote mais recente.

## Para quem mantém esta base

O passo a passo técnico de atualização, instalação das ferramentas de validação e conferência dos arquivos está em [Atualizar a base](fontes-de-origem/ATUALIZAR.md).

As regras vêm das páginas publicadas do Brand Navigator e os materiais vêm das fontes registradas no Drive e Figma. Arquivos históricos e prévias com marca d’água têm identificação própria. Usar a skill não publica a peça automaticamente nem altera os arquivos de origem.
