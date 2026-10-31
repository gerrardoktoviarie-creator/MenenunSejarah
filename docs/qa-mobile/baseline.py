"""Baseline Fase 0; tidak mengubah sumber produk atau profil browser pengguna."""
import argparse
import functools
import http.server
import json
from pathlib import Path
import threading
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs' / 'qa-mobile' / 'baseline'
WIDTHS = [1440, 1280, 1024, 768, 390, 320]
SECTIONS = ['beranda', 'arsip', 'playground', 'dampak', 'kredit']
# Satu fungsi yang sama dipakai baseline desktop dan semua lebar pembanding.
INVENTORY = r'''() => {
 const path = el => {
   const steps = [];
   while (el && el.nodeType === 1) {
     const tag = el.localName;
     const siblings = el.parentElement ? [...el.parentElement.children].filter(x => x.localName === tag) : [el];
     steps.unshift(`${tag}:nth-of-type(${siblings.indexOf(el)+1})`);
     if (el.id === 'konten' || el.parentElement === document.body) break;
     el = el.parentElement;
   }
   return steps.join(' > ');
 };
 const strict = el => {
   const r = el.getBoundingClientRect(), s = getComputedStyle(el);
   if (!(r.width > 0 && r.height > 0) || s.display === 'none' || s.visibility !== 'visible' || Number(s.opacity) < .05) return false;
   let left = Math.max(r.left, -scrollX), right = Math.min(r.right, document.documentElement.scrollWidth-scrollX);
   let top = Math.max(r.top, -scrollY), bottom = Math.min(r.bottom, document.documentElement.scrollHeight-scrollY);
   for (let p=el.parentElement;p;p=p.parentElement) {
     const ps = getComputedStyle(p), pr=p.getBoundingClientRect();
     if (ps.display === 'none' || ps.visibility !== 'visible' || Number(ps.opacity) < .05) return false;
     if (/(hidden|clip|auto|scroll)/.test(ps.overflowX)) {left=Math.max(left,pr.left);right=Math.min(right,pr.right);}
     if (/(hidden|clip|auto|scroll)/.test(ps.overflowY)) {top=Math.max(top,pr.top);bottom=Math.min(bottom,pr.bottom);}
   }
   return right>left && bottom>top;
 };
 const elements=[...document.querySelectorAll('body *')].filter(el => !['script','style','link','meta','title','desc','defs','pattern'].includes(el.localName));
 const records=elements.filter(strict).map(el=>{
   const r=el.getBoundingClientRect(), s=getComputedStyle(el);
   const text=(el.textContent||'').replace(/\s+/g,' ').trim().slice(0,40);
   return {key:el.localName+'|'+path(el)+'|'+text,path:path(el),tag:el.localName,text,
     section:el.closest('.page-section')?.id||'shell',fontSize:parseFloat(s.fontSize),
     rect:{x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height},
     interactive:el.matches('a,button,input,select,textarea,[role="gridcell"]'),
     ariaHidden:!!el.closest('[aria-hidden="true"]'),
     overflowX:s.overflowX};
 });
 return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,
   overflow:Math.max(0,document.documentElement.scrollWidth-innerWidth),
   bodyOverflowX:getComputedStyle(document.body).overflowX,
   gsap:!!window.gsap, scrollTrigger:!!window.ScrollTrigger,
   fonts:document.fonts.status, elements:records,
   protruding:elements.filter(strict).filter(el=>{const r=el.getBoundingClientRect();return r.right>innerWidth+1||r.left< -1;}).map(el=>({path:path(el),text:(el.textContent||'').trim().slice(0,40)})).slice(0,100)};
}'''

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def run(widths):
    OUT.mkdir(parents=True, exist_ok=True)
    handler = functools.partial(QuietHandler, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    summary = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(channel='msedge', headless=True)
            for width in widths:
                context = browser.new_context(viewport={'width': width, 'height': 900 if width >= 900 else 844}, reduced_motion='reduce')
                page = context.new_page()
                errors, network = [], []
                page.on('pageerror', lambda e: errors.append(str(e)))
                page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
                page.on('requestfailed', lambda r: network.append({'url': r.url, 'failure': r.failure}))
                page.goto(f'http://127.0.0.1:{server.server_port}/index.html', wait_until='networkidle')
                page.evaluate('document.fonts.ready')
                page.wait_for_timeout(700)
                data = page.evaluate(INVENTORY)
                data.update(errors=errors, networkFailures=network)
                (OUT / f'inventory-{width}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
                for section in SECTIONS:
                    page.locator('#'+section).evaluate('(el)=>window.scrollTo(0,el.getBoundingClientRect().top+scrollY)')
                    page.wait_for_timeout(100)
                    page.screenshot(path=str(OUT / f'{section}-{width}.png'))
                summary.append({'width':width, 'visible':len(data['elements']), 'overflow':data['overflow'], 'errors':errors, 'networkFailures':network, 'gsap':data['gsap'], 'bodyOverflowX':data['bodyOverflowX']})
                (OUT / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
                print(json.dumps(summary[-1], ensure_ascii=False), flush=True)
                context.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    print(f'Baseline tersimpan: {OUT}', flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--widths', type=int, nargs='+', default=WIDTHS)
    args = parser.parse_args()
    run(args.widths)
