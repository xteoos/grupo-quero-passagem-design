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
