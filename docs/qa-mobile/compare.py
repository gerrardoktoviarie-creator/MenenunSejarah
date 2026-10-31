"""Bandingkan baseline desktop dan ukur geometri mobile tanpa mengubah baseline."""
import functools
import http.server
import importlib.util
import json
from pathlib import Path
import threading
from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('baseline',HERE/'baseline.py')
assert spec and spec.loader
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
OUT=HERE/'results'
OUT.mkdir(exist_ok=True)
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(base.QuietHandler,directory=str(base.ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
result={'desktop':[],'mobile':[]}
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(channel='msedge',headless=True)
  for width in [320,360,390,480,600,768,899,1024,1280,1440]:
   page=browser.new_page(viewport={'width':width,'height':900 if width>=900 else 844},reduced_motion='reduce')
   page.goto(f'http://127.0.0.1:{server.server_port}/index.html',wait_until='networkidle')
   page.evaluate('document.fonts.ready')
   page.wait_for_timeout(700)
   if width>=900:
    for section in base.SECTIONS:
     page.locator('#'+section).evaluate('(el)=>window.scrollTo(0,el.getBoundingClientRect().top+scrollY)')
     page.wait_for_timeout(100)
     target=OUT/f'{section}-{width}.png'
     page.screenshot(path=str(target))
     old=Image.open(base.OUT/f'{section}-{width}.png').convert('RGB')
     new=Image.open(target).convert('RGB')
     diff=ImageChops.difference(old,new)
     pixels=sum(1 for pixel in diff.getdata() if pixel!=(0,0,0))
     result['desktop'].append({'width':width,'section':section,'changedPixels':pixels,'fraction':pixels/(old.width*old.height)})
   else:
    result['mobile'].append(page.evaluate('''() => {
     const title=document.querySelector('.boot__title'), r=title.getBoundingClientRect();
     const ranges=[...title.querySelectorAll('.boot__mask')].map(el=>{const range=document.createRange();range.selectNodeContents(el);return range.getBoundingClientRect().width});
     return {width:innerWidth,heroRatio:Math.max(...ranges)/r.width,
      heroLines:ranges.length,overflow:document.documentElement.scrollWidth-innerWidth,
      headings:[...document.querySelectorAll('h1,h2,h3')].filter(el=>el.getClientRects().length).map(el=>({text:el.textContent.trim().slice(0,40),width:el.clientWidth,scroll:el.scrollWidth})),
      grid:{client:document.querySelector('.pg__viewport').clientWidth,scroll:document.querySelector('.pg__viewport').scrollWidth},
      arsipVisual:getComputedStyle(document.querySelector('.arsip__visual')).position};
    }'''))
    for section in base.SECTIONS:
     page.locator('#'+section).evaluate('(el)=>window.scrollTo(0,el.getBoundingClientRect().top+scrollY)')
     page.screenshot(path=str(OUT/f'{section}-{width}.png'))
   page.close()
  browser.close()
finally:
 server.shutdown()
 server.server_close()
(OUT/'geometry-desktop.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(result,indent=2,ensure_ascii=False))
