"""Offline checks for deployable static pages, links and structured data."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids=set(); self.links=[]; self.schemas=[]; self.canonicals=[]
        self.schema=None; self.h1=0; self.scripts=[]
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='h1': self.h1+=1
        for key in ('href','src','data-full'):
            if a.get(key): self.links.append(a[key])
        if tag=='link' and a.get('rel')=='canonical': self.canonicals.append(a['href'])
        if tag=='script':
            if a.get('type')=='application/ld+json': self.schema=''
            if a.get('src'): self.scripts.append(a['src'])
    def handle_data(self,data):
        if self.schema is not None: self.schema+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.schema is not None:
            self.schemas.append(json.loads(self.schema)); self.schema=None

pages={p.name:Page(p.read_text(encoding='utf-8')) for p in ROOT.glob('*.html')}
errors=[]
for name,page in pages.items():
    if page.h1!=1: errors.append(f'{name}: {page.h1} H1 headings')
    if sum(urlsplit(src).path=='site.js' for src in page.scripts)!=1: errors.append(f'{name}: missing/duplicate analytics script')
    for link in page.links:
        u=urlsplit(link)
        if u.scheme or u.netloc: continue
        path=unquote(u.path).lstrip('/') or (name if u.fragment else 'index.html')
        target=ROOT/path
        if not target.exists(): errors.append(f'{name}: missing {link}')
        elif u.fragment and target.suffix=='.html' and unquote(u.fragment) not in pages[target.name].ids:
            errors.append(f'{name}: missing anchor {link}')
    if name not in ('404.html','piles-fissure-fistula-treatment-ranchi.html') and len(page.canonicals)!=1:
        errors.append(f'{name}: expected one canonical')
urls=[e.text for e in ET.parse(ROOT/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert 'https://drbhartisurgery.com/bariatu-surgery-clinic-ranchi.html' in urls
for url in urls:
    assert (ROOT/(urlsplit(url).path.lstrip('/') or 'index.html')).exists(),url
assert 'id="clinic" required' in (ROOT/'index.html').read_text(encoding='utf-8')
assert 'autoDates' not in (ROOT/'surgeon-in-garhwa.html').read_text(encoding='utf-8')
if errors: raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} pages; local links, assets, anchors, JSON-LD, sitemap and contact checks.')
