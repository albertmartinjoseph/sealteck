import urllib.request, pathlib, concurrent.futures, json
urls=pathlib.Path('docs/source/asset-urls.txt').read_text(encoding='utf-8-sig').splitlines()
urls=[u for u in urls if any(x in u for x in ['cmp_td_hero','rvg_install','data-center_3','capa-22-scaled-1.webp','WhatsApp-Image']) and not any(x in u for x in ['-150x','-300x','-768x','-1024x','-1200x'])]
def download(pair):
 i,u=pair
 try:
  data=urllib.request.urlopen(u,timeout=30).read(); p=pathlib.Path('public/images')/('original-'+str(i)+pathlib.Path(u).suffix);p.write_bytes(data);return dict(file=str(p).replace('\\','/'),source=u)
 except Exception as e:return dict(source=u,error=str(e))
results=list(concurrent.futures.ThreadPoolExecutor(6).map(download,enumerate(urls)))
pathlib.Path('docs/source/downloads.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
