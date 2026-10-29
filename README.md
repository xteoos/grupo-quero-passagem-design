# Quero Passagem · Brandbook para IAs

Base de marca para criar apresentações, posts, anúncios e comunicados com assets oficiais. A skill lê apenas as referências necessárias para cada pedido. O formato final é combinado com quem solicita a peça.

## Começar
1. Abra [o catálogo visual](catalogo/index.html). Funciona localmente, sem login ou aplicação web.
2. Leia [a skill](skills/qp-brandbook/SKILL.md) e consulte [as páginas oficiais extraídas](skills/qp-brandbook/references/paginas/INDEX.md).
3. Confira [a cobertura e as pendências](fontes-de-origem/COBERTURA.md). Bacalar, Mauren e All Round Gothic completas estão pendentes para os modelos que as exigem.
4. Faça um pedido informando marca, público, objetivo, canal e formato. Exemplo: “Use $qp-brandbook para criar um comunicado interno da Quero Passagem sobre uma mudança de processo. Entrega em HTML editável, usando o template de comunicados e sem inventar datas.”

## Instalar a skill
O pacote inteiro `skills/qp-brandbook/` precisa acompanhar o SKILL.md. Copiar apenas o Markdown perde os assets e as referências.

**Codex:** copie ou vincule a pasta completa em `~/.codex/skills/qp-brandbook` (ou no diretório de skills do CODEX_HOME, quando personalizado).
**Claude Code:** copie a pasta completa para `.claude/skills/qp-brandbook/` no projeto de trabalho, ou `~/.claude/skills/qp-brandbook/` para uso pessoal.
**Outras IAs:** forneça o SKILL.md, as referências relevantes e os arquivos selecionados. Um link de GitHub privado, sozinho, não concede acesso a uma IA. Use a integração autenticada da ferramenta ou uma cópia local do repositório.

A instalação não concede autorização para publicar peças, editar fontes no Drive/Figma ou alterar este acervo.

## Fontes e limites
As regras vêm das páginas publicadas do Brand Navigator; os arquivos vêm do Drive e Figma indicados pelo responsável. Conteúdo mockado do código não foi usado como norma.
- **Fontes pendentes:** Bacalar, Mauren e All Round Gothic; consultar [as dependências da skill](skills/qp-brandbook/references/dependencias.md). Os arquivos Demo/Trial foram excluídos. Sora, Inter e Instrument Serif são locais. Entregas que exigem Bacalar permanecem pendentes até receber o arquivo completo.
- Previews de templates são referências visuais. Texto e logos devem continuar como elementos controláveis na peça nova.
- Fotos antigas e arquivos sem revisão de aplicação aparecem identificados; não presumir que toda imagem do acervo representa a identidade atual.
- Sem credenciais, dados de usuários ou .env do projeto de origem neste repositório.
- Sem garantia de que uma IA genérica consegue ler arquivos locais, renderizar fontes ou editar todos os formatos. A skill exige informar limitações concretas.

## Git e Git LFS
Repositório público: [xteoos/grupo-quero-passagem-design](https://github.com/xteoos/grupo-quero-passagem-design), branch `main`.

Para obter o projeto completo, incluindo os originais armazenados com Git LFS:

```sh
git clone git@github.com:xteoos/grupo-quero-passagem-design.git
cd grupo-quero-passagem-design
git lfs install --local
git lfs pull
```

Instale Git LFS antes de trabalhar com os arquivos grandes. O download de um ZIP do GitHub pode conter ponteiros LFS em vez dos originais; confira os arquivos com o verificador.
Antes de adicionar arquivos ao Git, instale Git LFS e rode neste repositório:

```sh
git lfs install --local
git lfs pull
```

Em clones, `git lfs pull` baixa os originais. Fotografias, PDFs e apresentações usam LFS; miniaturas e documentação ficam no Git comum. Os filtros locais exigem LFS, para evitar adicionar os originais por engano sem o filtro.

## Manter e validar
Use Python 3.11+ com Pillow para miniaturas e Node 22+ para atualizar o snapshot do projeto de origem.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_catalog.py
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/test_validation.py
```

A atualização das fontes segue [o procedimento de manutenção](fontes-de-origem/ATUALIZAR.md). Os conectores fazem a autenticação; URLs temporárias ficam apenas em .cache e não são versionadas. Não há atualização automática nem escrita nas fontes.

Leia [o relatório de validação](validacao/RELATORIO.md) antes de tratar os exemplos como evidência de conformidade.


Para visualizar com o carregamento local de fontes, execute `python3 scripts/serve.py` e abra http://127.0.0.1:8769/catalogo/. Para repetir a verificação de navegador: `npm ci`, `npx playwright install chromium` e `npm run check:browser` com o servidor ativo. Não é necessário instalar essas ferramentas para apenas usar a skill.
