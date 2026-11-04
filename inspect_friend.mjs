import {FileBlob,PresentationFile} from 'file:///C:/Users/Sudhanshu/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs';
import fs from 'node:fs/promises';
const p=await PresentationFile.importPptx(await FileBlob.load('Friend/slides/Presentation.pptx'));
await fs.mkdir('friend_preview',{recursive:true});
for(let i=0;i<p.slides.items.length;i++){let b=await p.export({slide:p.slides.items[i],format:'png',scale:0.5});await fs.writeFile(`friend_preview/slide-${String(i+1).padStart(2,'0')}.png`,new Uint8Array(await b.arrayBuffer()));}
