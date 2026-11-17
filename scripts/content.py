import json
from bs4 import BeautifulSoup
from pathlib import Path
pages=json.loads(Path('docs/source/content-inventory.json').read_text(encoding='utf-8-sig'));out={}
for p in pages:
 soup=BeautifulSoup(p['html'],'html.parser');blocks=[]
 for el in soup.find_all(string=True):
  t=str(el).strip()
  if not t or el.parent.name in ['script','style']:continue
  try:t=t.encode('cp1252').decode('utf-8')
  except (UnicodeError,ValueError):pass
  parent=el.find_parent(['h1','h2','h3','h4','li','p'])
  tag=parent.name if parent else 'p'
  if el.parent.name=='span' and ('title' in ' '.join(el.parent.get('class',[]))):tag='h3'
  if blocks and parent and blocks[-1].get('_id')==id(parent):blocks[-1]['text']+=' '+t
  else:blocks.append({'tag':tag,'text':t.replace('-answer for',''),'_id':id(parent) if parent else None})
 for b in blocks:b.pop('_id',None)
 out[p['slug']]={'title':p['title'],'blocks':blocks}
Path('src/content.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
