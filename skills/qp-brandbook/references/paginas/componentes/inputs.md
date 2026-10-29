# Inputs

Fonte: Brand Navigator /componentes/inputs. Atualização na origem: 2026-05-04T21:17:51.75476+00:00.

> Transcrição da página publicada. Exemplos de interface e dados ilustrativos permanecem exemplos; não são políticas comerciais.


<!-- bloco 0 · 2b24a029-fb41-4e30-ab23-3c58b8cf1dff · section -->

<h2>Inputs</h2><p>Inputs são o ponto de contato direto entre a pessoa e o produto. Cada campo bem desenhado reduz dúvida, evita erro e acelera a conversão. Por isso, eles precisam ser <strong>claros, generosos e acessíveis</strong>.</p>


<!-- bloco 1 · e2ed4d07-d85d-455c-88d1-cdcfdd1a0226 · section -->

<h3>Anatomia</h3><ul><li>Fonte <strong>Inter</strong> em todos os elementos.</li><li>Label em <strong>Body 2</strong> (14px), sempre visível.</li><li>Texto digitado em <strong>Body 1</strong> (16px) — tamanho mínimo seguro contra zoom indesejado em iOS.</li><li>Stroke <strong>Gray 200</strong> no estado padrão.</li><li>Radius entre <strong>8px e 12px</strong>.</li><li>Padding interno entre <strong>12 e 16px</strong>.</li><li>Mensagem de apoio (<em>helper</em>) em Caption logo abaixo do campo.</li></ul>


<!-- bloco 2 · ad4b0328-7c9b-4ea4-90c7-860d29191051 · section -->

<h3>Estados</h3><table style='width:100%;border-collapse:collapse'><thead><tr><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Estado</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Stroke</th><th style='text-align:left;padding:10px;border-bottom:1px solid #D5D8DE;background:#F7F8FB'>Comportamento</th></tr></thead><tbody><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Default</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Gray 200</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Estado de repouso</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Hover</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Gray 300</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Mouse sobre o campo</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Focus</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Cor primária + ring</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Campo ativo via clique ou Tab</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Filled</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Gray 200/300</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Campo já preenchido</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Error</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Danger 500</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Validação crítica + mensagem</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Success</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Success 500</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Validação positiva (quando útil)</td></tr><tr><td style='padding:10px;border-bottom:1px solid #EDF0F7;font-family:monospace;font-size:13px'>Disabled</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Gray 200, opacidade 50%</td><td style='padding:10px;border-bottom:1px solid #EDF0F7;'>Indisponível, sem cursor</td></tr></tbody></table>


<!-- bloco 3 · 20e2b5cd-80d1-4de2-bc21-89675149dc4e · section -->

<h3>Exemplo visual</h3><div style='display:grid;grid-template-columns:repeat(2,1fr);gap:16px;max-width:720px'><div><label style='display:block;font-size:14px;font-weight:600;margin-bottom:6px'>Origem</label><input style='width:100%;padding:14px;border:1px solid #EDF0F7;border-radius:8px;font-size:16px' placeholder='De onde você sai?'></div><div><label style='display:block;font-size:14px;font-weight:600;margin-bottom:6px'>Destino</label><input style='width:100%;padding:14px;border:2px solid #0066FF;border-radius:8px;font-size:16px' value='São Paulo'></div><div><label style='display:block;font-size:14px;font-weight:600;margin-bottom:6px'>E-mail</label><input style='width:100%;padding:14px;border:1px solid #CC2929;border-radius:8px;font-size:16px' value='endereco-invalido'><p style='color:#CC2929;font-size:12px;margin-top:6px'>Informe um e-mail válido</p></div><div><label style='display:block;font-size:14px;font-weight:600;margin-bottom:6px;color:#9CA3AF'>CPF</label><input disabled style='width:100%;padding:14px;border:1px solid #EDF0F7;border-radius:8px;font-size:16px;background:#F7F8FB;color:#9CA3AF' value='000.000.000-00'></div></div>


<!-- bloco 4 · 28809bad-8bd4-44f5-8bca-c934c451df29 · section -->

Use sempre <code>autocomplete</code>, <code>inputmode</code> e máscaras adequadas. Em mobile, isso muda totalmente o teclado mostrado e evita erros de digitação.

Bom hábito

Placeholder no lugar de label, mensagens de erro genéricas ('campo inválido') e campos com altura menor que 44px em mobile.

Evite


<!-- bloco 5 · 9a29bfee-8c2f-430d-b154-8958aa8261f0 · section -->

Exemplo ao vivo


<!-- bloco 6 · b35e01cb-8a32-4670-9291-37c90ee91b16 · section -->

Exemplo ao vivo
