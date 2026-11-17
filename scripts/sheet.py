from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
files=list(Path('public/images').glob('*')); canvas=Image.new('RGB',(1000,((len(files)+3)//4)*170),'white'); d=ImageDraw.Draw(canvas)
for i,p in enumerate(files):
 im=Image.open(p);im.thumbnail((245,140));x=(i%4)*250;y=(i//4)*170;canvas.paste(im,(x,y));d.text((x,y+142),p.name,fill='black')
canvas.save('docs/source/contact-sheet.jpg')
