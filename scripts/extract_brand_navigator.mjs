/** Snapshot público e ordenado. As credenciais são lidas apenas do ambiente do projeto de origem. */
import fs from 'node:fs';import path from 'node:path';import {parseEnv} from 'node:util';import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const input=process.argv[2];if(!input)throw Error('Uso: node scripts/extract_brand_navigator.mjs /caminho/brand-navigator');
let cfg={};for(const name of ['.env','.env.local']){const p=path.join(input,name);if(fs.existsSync(p))Object.assign(cfg,parseEnv(fs.readFileSync(p,'utf8')));}
const url=cfg.VITE_SUPABASE_URL,key=cfg.VITE_SUPABASE_PUBLISHABLE_KEY||cfg.VITE_SUPABASE_ANON_KEY;
if(!url||!key)throw Error('Configuração pública ausente no projeto de origem');
const u=new URL('/rest/v1/areas',url);u.searchParams.set('select','slug,title,intro,description,sort_order,pages(id,slug,title,description,status,visibility,builder_saved,updated_at,sort_order,blocks(id,type,content,sort_order))');
const r=await fetch(u,{headers:{apikey:key,Authorization:'Bearer '+key}});if(!r.ok)throw Error('HTTP '+r.status);
const areas=(await r.json()).filter(a=>['design-na-qp','fundamentos','componentes'].includes(a.slug)).sort((a,b)=>a.sort_order-b.sort_order);
for(const a of areas){a.pages=a.pages.filter(p=>p.status==='published').sort((a,b)=>a.sort_order-b.sort_order);for(const p of a.pages)p.blocks.sort((a,b)=>a.sort_order-b.sort_order);}
fs.writeFileSync(path.join(root,'fontes-de-origem/brand-navigator.json'),JSON.stringify({collected_at:new Date().toISOString(),source:new URL(url).origin,access:'public-api',areas},null,2)+'\n');
console.log(JSON.stringify(areas.map(a=>({area:a.slug,pages:a.pages.length,blocks:a.pages.reduce((n,p)=>n+p.blocks.length,0)}))));
