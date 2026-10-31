"""Kontrak mobile dan snapshot regresi desktop; Playwright dipasang di luar repo."""
import functools
import http.server
import json
from pathlib import Path
import threading
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent/'results'
OUT.mkdir(exist_ok=True)
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
checks=[]
def check(name, ok, detail=None):
    checks.append({'name':name,'pass':bool(ok),'detail':detail})
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(channel='msedge',headless=True)
        for width in [320,360,390,480,600,768,899,900,1024,1280,1440]:
            page=browser.new_page(viewport={'width':width,'height':844 if width<900 else 900},reduced_motion='reduce')
            errors=[]
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.goto(f'http://127.0.0.1:{server.server_port}/index.html',wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            data=page.evaluate('''() => {
              const style=s=>getComputedStyle(document.querySelector(s));
              return {overflow:document.documentElement.scrollWidth-innerWidth,
                ruler:style('.pg__ruler').display, row:style('.pg__row-labels').display,
                cell:parseFloat(style('.cell').fontSize),trust:parseFloat(style('.boot__trust').fontSize),
                legend:parseFloat(style('.pg__legend').fontSize),
                controls:style('.pg__controls').position,
                thread:style('.thread-layer').display,
                body:style('body').overflowX};
            }''')
            check(f'{width}: overflow',data['overflow']<=0,data)
            check(f'{width}: runtime',not errors,errors)
            if width<900:
                check(f'{width}: coordinates',data['ruler']!='none' and data['row']!='none',data)
                check(f'{width}: readable',data['cell']>=11 and data['trust']>=16 and data['legend']>=16,data)
                check(f'{width}: sticky controls',data['controls']=='sticky',data)
                check(f'{width}: thread',data['thread']!='none',data)
                check(f'{width}: no global clipping',data['body']=='visible',data)
            page.screenshot(path=str(OUT/f'hero-{width}.png'))
            page.close()
        browser.close()
finally:
    server.shutdown()
    server.server_close()
(OUT/'checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
print(json.dumps({'passed':sum(x['pass'] for x in checks),'total':len(checks),'failed':[x for x in checks if not x['pass']]},indent=2))
raise SystemExit(0 if all(x['pass'] for x in checks) else 1)
