from PIL import Image
from pathlib import Path
import json
records=json.loads(Path('docs/source/downloads.json').read_text())
lines=['# Image sources and reuse record','','Downloaded 17 November 2026. All photographs originate from the existing Sealteck website and are reused under the user’s authorization to rebuild that website. Public accessibility does not establish copyright ownership. No explicit public licence was found; existing owner/stock licences must cover the new deployment before public launch. No Aramco images or third-party replacement stock were used.','','Images are illustrative of applications; they are not evidence of named completed projects. No official image logo was found: the original SEALTECK text wordmark is preserved.','','| Local asset | Original source | Dimensions | Licence status |','| --- | --- | --- | --- |']
for r in records:
 if 'file' not in r:continue
 p=Path(r['file']);im=Image.open(p).convert('RGB');w,h=im.size
 for size in [640,1280,1920]:
  out=im.copy();out.thumbnail((size,size*2));out.save(p.parent/(p.stem+'-'+str(size)+'.webp'),'WEBP',quality=80,method=6)
 lines.append(f'| `{p.stem}-{{640,1280,1920}}.webp` | {r["source"]} | {w} × {h} | Existing Sealteck asset; owner licence not independently verified |')
lines+=['','Responsive variants never upscale source pixels. Some installation originals are small; they are used in cards rather than as cinematic heroes. Original downloads are retained for provenance. Asset missing: independently verified licence documents and a separate official logo file.']
Path('docs/image-sources.md').write_text('\n'.join(lines),encoding='utf-8')

