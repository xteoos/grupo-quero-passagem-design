# Atualizar a base
1. Leia o inventário e a cobertura atuais. Confirme se os mesmos links continuam sendo as fontes desejadas.
2. Para páginas públicas: `node scripts/extract_brand_navigator.mjs /caminho/brand-navigator`. O script lê a configuração pública apenas do projeto indicado; não copie o .env.
3. Execute `python3 scripts/prepare_pages.py` e materialize as imagens com `python3 scripts/download_transfers.py --queue .cache/page-transfers.json`.
4. Para Drive: use o conector autenticado para percorrer as quatro raízes, subpastas e atalhos acessíveis. Se uma listagem indicar paginação ou atingir o limite, continue pela busca paginada; não declare cobertura completa de uma página parcial.
5. Leia metadados antes de exportar. Exporte Google Slides em PPTX e documentos em DOCX; armazene links para vídeos e originais de produção pesados. Exclua fontes Demo/Trial.
6. Renove e baixe cada pequeno lote imediatamente: URLs de transferência expiram. Guarde-as somente em .cache, nunca nos inventários versionados.
7. Para Figma: ler páginas e frames; exportar elementos reutilizáveis e previews sem modificar a fonte. Preserve ID, dimensões e página de origem. Não promover nome de layer ou peça isolada a regra de marca.
8. Registre alterações e lacunas, reconstrua catálogo e índice com `scripts/build_catalog.py`, execute `scripts/validate.py` e revise visualmente as mudanças. Não atualize o manual curado automaticamente se uma norma mudou.

Não sobrescrever arquivos fornecidos posteriormente pelo responsável, especialmente a Bacalar completa. Não fazer push, publicar site ou alterar fontes externas por este procedimento.
