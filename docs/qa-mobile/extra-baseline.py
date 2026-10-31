"""Keadaan piagam terisi, audit clipping, hero pendek, dan Lighthouse opsional."""
import functools
import http.server
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import threading
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('baseline', HERE / 'baseline.py')
assert spec is not None and spec.loader is not None
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(base.QuietHandler, directory=str(base.ROOT)))
threading.Thread(target=server.serve_forever, daemon=True).start()
url = f'http://127.0.0.1:{server.server_port}/index.html'
result = {'filled': [], 'unclipped': [], 'shortHero': []}
try:
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='msedge', headless=True)
        for width in base.WIDTHS:
            page = browser.new_page(viewport={'width': width, 'height': 900 if width >= 900 else 844}, reduced_motion='reduce')
            page.goto(url, wait_until='networkidle')
            page.evaluate("""() => {const matrix=Array.from({length:12},(_,y)=>Array.from({length:12},(_,x)=>(x+y)%2)); SL.storage.writeMotif(matrix,'Uji inventaris');}""")
            page.reload(wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            data = page.evaluate(base.INVENTORY)
            (base.OUT / f'inventory-filled-{width}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
            page.locator('#dampak').evaluate('(el)=>window.scrollTo(0,el.getBoundingClientRect().top+scrollY)')
            page.screenshot(path=str(base.OUT / f'dampak-filled-{width}.png'))
            result['filled'].append({'width': width, 'visible': len(data['elements']), 'overflow': data['overflow']})
            # Hanya ubah CSS di browser pengujian untuk mendeteksi clipping yang menyamarkan akar masalah.
            page.evaluate("document.body.style.overflowX='visible'")
            result['unclipped'].append({'width': width, 'overflow': page.evaluate('Math.max(0,document.documentElement.scrollWidth-innerWidth)')})
            page.close()
        for width, height in [(390,844),(360,640),(844,390)]:
            page = browser.new_page(viewport={'width':width,'height':height}, reduced_motion='reduce')
            page.goto(url, wait_until='networkidle')
            result['shortHero'].append(page.evaluate("""() => ({width:innerWidth,height:innerHeight,items:[...document.querySelectorAll('.boot__title,.boot__lead,.boot__action .btn')].map(el=>{const r=el.getBoundingClientRect();return {selector:el.className,top:r.top,bottom:r.bottom,withinViewport:r.top>=0&&r.bottom<=innerHeight}})})"""))
            page.screenshot(path=str(base.OUT/f'hero-{width}x{height}.png'))
            page.close()
        browser.close()
    env = os.environ.copy()
    env['CHROME_PATH'] = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
    run = subprocess.run(['npx.cmd','--yes','--cache','C:/Users/Gerrad/AppData/Local/hermes/cache/scratch/npm-cache','lighthouse',url,'--chrome-flags=--headless','--output=json','--output-path='+str(base.OUT/'lighthouse-mobile.json'),'--quiet'], env=env, capture_output=True, text=True, timeout=180)
    result['lighthouse'] = {'exit':run.returncode}
    if run.returncode == 0:
        report=json.loads((base.OUT/'lighthouse-mobile.json').read_text(encoding='utf-8'))
        result['lighthouse']['scores']={key:value['score'] for key,value in report['categories'].items()}
        result['lighthouse']['url']=report['finalDisplayedUrl']
    else:
        result['lighthouse']['error']=run.stderr[-2000:]
finally:
    server.shutdown()
    server.server_close()
    (base.OUT/'extra-summary.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
