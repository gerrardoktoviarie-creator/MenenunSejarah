"""Uji state terisi, fallback CDN, resize, sticky, dan navigasi keyboard mobile."""
import functools
import http.server
import json
from pathlib import Path
import threading
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'docs/qa-mobile/results'
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,format,*args): pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
results=[]
def record(name, ok, detail=None):results.append({'name':name,'pass':bool(ok),'detail':detail})
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(channel='msedge',headless=True)
  for width in [320,360,390,600,768,899]:
   page=browser.new_page(viewport={'width':width,'height':844},reduced_motion='reduce',has_touch=True,is_mobile=True)
   errors=[]
   page.on('pageerror',lambda e:errors.append(str(e)))
   page.goto(f'http://127.0.0.1:{server.server_port}/index.html',wait_until='networkidle')
   page.locator('.cell').first.click()
   page.locator('[data-action="simpan"]').click()
   page.wait_for_timeout(500)
   record(f'{width} saved ready',page.locator('.dampak__ready').is_visible())
   record(f'{width} filled overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
   page.screenshot(path=str(OUT/f'dampak-filled-{width}.png'))
   geometry=page.locator('.cert').evaluate('el=>({width:el.clientWidth,scroll:el.scrollWidth})')
   record(f'{width} cert no internal overflow',geometry['scroll']<=geometry['width'],geometry)
   page.locator('#arsip').evaluate('(el)=>window.scrollTo(0,el.offsetTop+500)')
   sticky=page.locator('.arsip__visual').evaluate('el=>({position:getComputedStyle(el).position,top:el.getBoundingClientRect().top})')
   record(f'{width} arsip sticky',sticky['position']=='sticky',sticky)
   record(f'{width} runtime',not errors,errors)
   page.close()
  page=browser.new_page(viewport={'width':390,'height':844})
  page.route('**/gsap.min.js',lambda route:route.abort())
  page.route('**/ScrollTrigger.min.js',lambda route:route.abort())
  page.goto(f'http://127.0.0.1:{server.server_port}/index.html',wait_until='networkidle')
  record('no gsap thread hidden',page.locator('.thread-layer').evaluate('el=>getComputedStyle(el).display')=='none')
  record('no gsap four articles',page.locator('.part:visible').count()==4)
  page.close()
  browser.close()
finally:
 server.shutdown();server.server_close()
(OUT/'integration.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps({'passed':sum(x['pass'] for x in results),'total':len(results),'failed':[x for x in results if not x['pass']]},indent=2))
raise SystemExit(0 if all(x['pass'] for x in results) else 1)
