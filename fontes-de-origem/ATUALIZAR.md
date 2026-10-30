# Atualizar a base
1. Leia o inventário e a cobertura atuais. Confirme se os mesmos links continuam sendo as fontes desejadas.
2. Para páginas públicas: `node scripts/extract_brand_navigator.mjs /caminho/brand-navigator`. O script lê a configuração pública apenas do projeto indicado; não copie o .env.
3. Execute `python3 scripts/prepare_pages.py` e materialize as imagens com `python3 scripts/download_transfers.py --queue .cache/page-transfers.json`.
4. Para Drive: use o conector autenticado para percorrer as quatro raízes, subpastas e atalhos acessíveis. Se uma listagem indicar paginação ou atingir o limite, continue pela busca paginada; não declare cobertura completa de uma página parcial.
5. Leia metadados antes de exportar. Exporte Google Slides em PPTX e documentos em DOCX; armazene links para vídeos e originais de produção pesados. Fontes Demo/Trial sem autorização expressa ficam excluídas; preservar o arquivo Bacalar do kit usado no Brand Navigator, indicado e autorizado pelo responsável em 30/10/2026.
6. Renove e baixe cada pequeno lote imediatamente: URLs de transferência expiram. Guarde-as somente em .cache, nunca nos inventários versionados.
7. Para Figma: ler páginas e frames; exportar elementos reutilizáveis e previews sem modificar a fonte. Preserve ID, dimensões e página de origem. Não promover nome de layer ou peça isolada a regra de marca.
8. Registre alterações e lacunas, reconstrua catálogo e índice com `scripts/build_catalog.py`, execute `scripts/validate.py` e revise visualmente as mudanças. Não atualize o manual curado automaticamente se uma norma mudou.

Não sobrescrever arquivos fornecidos posteriormente pelo responsável, incluindo a família Bacalar autorizada. Não fazer push, publicar site ou alterar fontes externas por este procedimento.


## Preparar as ferramentas locais

Para usar a skill, não é necessário instalar as ferramentas de manutenção abaixo. Elas servem para quem adiciona arquivos ou valida alterações.

Use Python 3.11+ e Node 22+:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_examples.py
.venv/bin/python scripts/build_catalog.py
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/test_validation.py
```

Para ver o catálogo, execute `python3 scripts/serve.py` e abra http://127.0.0.1:8769/catalogo/. Para repetir a conferência de navegador, mantenha o servidor ativo, execute `npm ci`, `npx playwright install chromium` e `npm run check:browser`.

Mudanças de fonte devem atualizar também references/typography-policy.json, tipografia.md, dependencias.md e os exemplos. Preserve os registros das fontes originais. Depois de regenerar modelos HTML, reconstrua catálogo e hashes. Fontes de teste sem autorização ficam fora do pacote. A versão Bacalar ativa vem do kit usado no Brand Navigator e está registrada em typography-policy.json por ID, peso e hash. Não reintroduzir o ZIP sem acentos como se fosse a versão corrigida. Guarde diagnóstico e hashes dos arquivos excluídos.


## Distribuição leve para IAs

Depois de mudar referências, scripts ou acervo, execute `python3 scripts/build_distribution.py`. Versione distribution/brandbook-bundle.json e distribution/qp-brandbook.zip junto com a mudança. O bundle contém as referências e um manifesto dos arquivos; o ZIP leva somente SKILL.md, references, scripts e agents. Nunca incluir assets ou arquivos temporários no ZIP de instalação.

O helper remoto fixa o SHA de main no início do pedido, obtém esse bundle e verifica os arquivos necessários por tamanho e SHA-256. LFS é responsabilidade da manutenção do acervo; não é requisito para quem instala a skill. Teste o pacote extraído numa pasta vazia, incluindo fonte comum e pelo menos um original LFS, antes de declarar o fluxo validado.


## Curadoria e validação social

Atualize os papéis/nome curado/família em asset-reviews.json preservando source_name, ID, caminho e bytes. Reclassifique pelo conteúdo visual, nunca só pelo nome da página. Atualize references/social/familias.json e os guias quando uma evidência ou direção do responsável mudar.

Reconstrua o catálogo, execute `python3 scripts/test_social_catalog.py`, `python3 scripts/test_remote_assets.py` e `python3 scripts/validate.py --strict`. Para rever os estudos, execute `python3 scripts/build_social_examples.py` e, com servidor local ativo, `node scripts/check_social.cjs` (Playwright necessário). Os estudos são exemplos de validação, não novas normas. Ao final, regenere o bundle e o ZIP com build_distribution.py.


Na revisão local de organização QP, os itens retirados são marcados com catalog_exclude em asset-reviews.json e têm caminho histórico, motivo, hash e archive_path em retirados-do-catalogo.json. Não recolocar fundos/pranchas QP no acervo de uso automaticamente durante uma nova coleta. O bundle distribui apenas os caminhos dos itens ativos, suas prévias e fonts.css.

Para testar antes de publicar, use o pacote em uma instalação separada com remote_assets.py sync --local-root /caminho/da/base. O modo local é preservado nos syncs seguintes; para voltar à publicação use sync --github. O procedimento não faz commit ou push. A validação de metas está em scripts/build_travel_goals_test.py e scripts/check_travel_goals.cjs.
