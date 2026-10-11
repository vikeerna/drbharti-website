"""Local SEO release checks; does not claim live indexing or rankings."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
BASE='https://drbhartisurgery.com/'
class SEO(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.meta={}; self.canonical=[]; self.title=''; self.in_title=False
        self.h1=0; self.images=[]; self.ids=[]; self.visible=[]; self.script=False; self.schema=None; self.schemas=[]
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='meta': self.meta[a.get('name',a.get('property',''))]=a.get('content','')
        if tag=='link' and a.get('rel')=='canonical': self.canonical.append(a.get('href'))
        if tag=='title': self.in_title=True
        if tag=='h1': self.h1+=1
        if tag=='img': self.images.append(a)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='script':
            self.script=True
            if a.get('type')=='application/ld+json': self.schema=''
    def handle_data(self,data):
        if self.in_title:self.title+=data
        if self.schema is not None:self.schema+=data
        if not self.script:self.visible.append(data)
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
        if tag=='script':
            if self.schema is not None:self.schemas.append(json.loads(self.schema));self.schema=None
            self.script=False

pages={p.name:SEO(p.read_text(encoding='utf-8')) for p in ROOT.glob('*.html')}
sitemap={x.text for x in ET.parse(ROOT/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
excluded={'404.html','piles-fissure-fistula-treatment-ranchi.html'}
titles=[]; descriptions=[]
for name,p in pages.items():
    assert p.title and p.meta.get('description'),f'{name}: missing title/description'
    assert p.h1==1 and len(p.ids)==len(set(p.ids)),f'{name}: heading/duplicate IDs'
    assert len(p.canonical)==1,f'{name}: canonical'
    for img in p.images: assert 'alt' in img,f'{name}: missing image alt'
    if name in excluded:continue
    expected=BASE+('' if name=='index.html' else name)
    assert p.canonical==[expected] and expected in sitemap,f'{name}: canonical/sitemap mismatch'
    assert 'noindex' not in p.meta.get('robots',''),f'{name}: unexpectedly noindex'
    assert p.meta.get('viewport') and p.meta.get('og:title') and p.meta.get('og:description') and p.meta.get('og:image'),f'{name}: sharing/mobile metadata'
    titles.append(p.title);descriptions.append(p.meta['description'])
    visible=' '.join(' '.join(p.visible).split())
    for schema in p.schemas:
        for item in schema.get('@graph',[schema]):
            if item.get('@type')=='FAQPage':
                for q in item.get('mainEntity',[]):
                    assert ' '.join(q['name'].split()) in visible,f'{name}: hidden FAQ question'
                    assert ' '.join(q['acceptedAnswer']['text'].split()) in visible,f'{name}: FAQ answer differs'
assert len(titles)==len(set(titles)),'Duplicate indexable page titles'
assert len(descriptions)==len(set(descriptions)),'Duplicate indexable descriptions'
assert 'noindex' in pages['404.html'].meta.get('robots','')
assert BASE+'404.html' not in sitemap
assert 'Sitemap: '+BASE+'sitemap.xml' in (ROOT/'robots.txt').read_text()
for name in ('index.html','appointments.html','second-opinion-surgery-ranchi.html'):
    text=(ROOT/name).read_text(encoding='utf-8').lower()
    assert 'consultation fee' not in text and 'confirmed only' not in text and 'replies may be delayed' not in text
print(f'PASS: {len(pages)} pages; unique indexable titles/descriptions, canonical/sitemap coverage, headings/IDs, image alt text, sharing/mobile metadata, visible FAQ/schema parity and visit wording.')
