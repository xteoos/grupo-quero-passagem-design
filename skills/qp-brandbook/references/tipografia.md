# Tipografia
Fonte: [página Tipografia](paginas/fundamentos/tipografia.md) e Tipografia.pdf do kit oficial do Drive.

| Família | Papel documentado | Aplicação |
|---|---|---|
| Sora | Primária | Leitura acessível, simplicidade; usar pesos reais disponíveis, com Light nas combinações editoriais demonstradas |
| Inter | Corpo de texto | Textos de apoio, materiais gráficos e componentes digitais |
| Bacalar Expanded | Apoio, títulos ou palavras-chave | Sempre em CAIXA ALTA; variação expandida; arquivo completo pendente |
| Instrument Serif Italic | Apoio, excelência e tranquilidade | Destaque pontual em itálico, conforme as combinações exemplificadas |

A página demonstra misturas “Bacalar Expanded Caixa Alta + Sora Light + Instrument Serif Italic” e sua reordenação. Misturar famílias é uma possibilidade expressiva, não obrigação de usar quatro fontes em toda peça.

Textos longos podem ser alinhados à esquerda ou ao centro; evitar justificação e alinhamento à direita. Ajuste a hierarquia ao formato e ao modelo, sem importar automaticamente os tamanhos de UI para um slide ou post.

## Arquivos e carregamento
Sora e Inter variáveis, Instrument Serif Regular/Italic e licenças OFL estão em assets/fontes. [fonts.css](../assets/fonts.css) é gerado com caminhos locais e pesos reais. Não usar CDN por necessidade de um arquivo local que já existe.

Em HTML, espere document.fonts.ready e confira document.fonts.check antes da captura. Em Figma, use a família e o estilo realmente disponíveis. Em PPTX, mantenha o tema e os placeholders do modelo, confira a disponibilidade na máquina de renderização e não confunda a referência de uma fonte com seu arquivo embutido.

Frase de verificação: “AÇÃO · São João · Coração · ônibus · amanhã · ¿A dónde viajas?”.

## Bacalar pendente
Os OTFs BacalarTest locais e do Drive foram identificados como Demo/Trial e excluídos. O kit Adobe usado pelo site existente não é um arquivo desktop nem garante uso offline em outras ferramentas. Não baixar fontes de teste de sites de terceiros para contornar essa ausência.

Quando o responsável fornecer a versão completa autorizada para uso interno, colocar o arquivo em assets/fontes/bacalar, atualizar fonts.css e o índice, verificar o mapa de caracteres, renderizar a frase de teste e remover a pendência somente após esse teste.
