"""Checks for the 10 October 2026 content restoration (Claude build)."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
T=['gallbladder-stone-surgery-ranchi.html','hernia-surgery-ranchi.html','varicose-veins-treatment-ranchi.html','piles-fistula-surgery-ranchi.html','appendix-surgery-ranchi.html','bariatric-surgery-ranchi.html','thyroid-surgery-ranchi.html','acid-reflux-surgery-ranchi.html']
def main(name): return (ROOT/name).read_text(encoding='utf-8').split('<main',1)[1].split('</main>',1)[0]
for name in T:
    m=main(name)
    assert 'id="symptoms"' in m and 'href="#symptoms"' in m, name
    assert 'lang="hi"' in m and 'Get a second opinion from Dr. Bharti' in m, name
    assert 'Ayushman Bharat' in m, name
    assert 'Does every patient need an operation?' not in m, name
gb=main('gallbladder-stone-surgery-ranchi.html'); assert 'Where is gallbladder pain felt?' in gb
home=main('index.html')
for anchor in ['id="symptom-finder"','id="reviews"','id="media"','id="bmi"','writereview?placeid=','gallery.html','about-dr-vikeerna-bharti.html','Ranchi Dental and Polyclinic, Bariatu Road']:
    assert anchor in home, anchor
for name in ['index.html','appointments.html','surgeon-in-garhwa.html']:
    m=main(name)
    # Garhwa: the primary button calls hospital reception; WhatsApp to the doctor comes after it.
    assert m.count('class="journey-button" href="tel:+918264103707"')==1, name
    i=m.index('class="journey-button" href="tel:+918264103707"')
    assert m.find('appointments.html?clinic=garhwa#request', i)!=-1, name
g=main('surgeon-in-garhwa.html')
assert g.index('href="tel:+918264103707"') < g.index('appointments.html?clinic=garhwa#request')
for phrase in ['laparoscopic surgery, including hernia surgery','self-paid','Nagar Untari','images/garhwa-ot-photo.jpg']: assert phrase in g, phrase
j=main('laparoscopic-surgeon-jharkhand.html'); assert 'Hazaribagh' in j and 'Ayushman Bharat' in j
b=main('bariatu-surgery-clinic-ranchi.html'); assert 'images/ranchi_dental_polyclinic.jpg' in b and 'lang="hi"' in b
gal=main('gallery.html'); assert gal.count('<figure')>=20 and 'written consent' in gal
sm=(ROOT/'sitemap.xml').read_text(encoding='utf-8'); assert 'gallery.html' in sm and 'about-dr-vikeerna-bharti.html' in sm
assert "addEventListener('input'" in (ROOT/'patient-tools.js').read_text(encoding='utf-8')
for p in ROOT.glob('*.html'):
    t=p.read_text(encoding='utf-8')
    assert 'Meral' not in t and 'JMC' not in t and 'Reg. No' not in t, p.name
for name in ['index.html','bariatu-surgery-clinic-ranchi.html','laparoscopic-surgeon-jharkhand.html','surgeon-in-garhwa.html','hernia-surgery-ranchi.html']:
    assert 'Rajya Karmi Swasthya Bima Yojana' in main(name), name

# Round 2: no original FAQ lost (counts from the live September site, duplicates merged)
MIN={'gallbladder-stone-surgery-ranchi.html':10,'hernia-surgery-ranchi.html':10,'varicose-veins-treatment-ranchi.html':11,'piles-fistula-surgery-ranchi.html':7,'bariatric-surgery-ranchi.html':9,'appendix-surgery-ranchi.html':7,'thyroid-surgery-ranchi.html':7,'acid-reflux-surgery-ranchi.html':7,'index.html':10,'surgeon-in-garhwa.html':6}
for name,n in MIN.items():
    c=main(name).count('<details>'); assert c>=n,(name,c,n)
for p in ROOT.glob('*.html'):
    t=p.read_text(encoding='utf-8')
    for href in T+['surgeon-in-garhwa.html','bariatu-surgery-clinic-ranchi.html','about-dr-vikeerna-bharti.html','gallery.html','laparoscopic-surgeon-jharkhand.html']:
        assert (f'href="{href}"' in t.split('<main',1)[0] or f'href="/{href}"' in t.split('<main',1)[0]) or p.name=='piles-fissure-fistula-treatment-ranchi.html', (p.name,href)
th=main('thyroid-surgery-ranchi.html'); assert 'He does not operate on thyroid cancer' in th
g=main('surgeon-in-garhwa.html'); assert 'Stryker' in g and 'modular operation theatre' in g
v=main('varicose-veins-treatment-ranchi.html'); assert 'usually go home the next day' in v and 'virtually painless' not in v.lower() and 'no scar' not in v.lower()
assert '24/7' in main('appendix-surgery-ranchi.html')
# Round 3 (owner edits, 10 Oct)
pages=sorted(x for x in ROOT.glob('*.html') if 'http-equiv="refresh"' not in x.read_text(encoding='utf-8'))
for x in pages:
    t=x.read_text(encoding='utf-8')
    for bad in ['First prize','EZ-SELSICON','Awards and presentations','Conferences and workshops','Other consultant appointments','प्रशिक्षित','2016–2018','2018–2021']:
        assert bad not in t,(x.name,bad)
for name in ['index.html','about-dr-vikeerna-bharti.html','second-opinion-surgery-ranchi.html']:
    assert 'FALS (Robotic)' in main(name), name
assert 'Fellowship of Advanced Laparoscopic Surgery (Robotic)' in main('index.html') and 'Fellowship of Advanced Laparoscopic Surgery (Robotic)' in main('about-dr-vikeerna-bharti.html')
assert 'Constant Lievens' not in main('about-dr-vikeerna-bharti.html') and 'Constant Lievens' not in main('index.html')
for name in T+['index.html','blog.html','second-opinion-surgery-ranchi.html','emergency-surgery-ranchi.html','surgeon-in-garhwa.html','bariatu-surgery-clinic-ranchi.html','laparoscopic-surgeon-jharkhand.html']:
    m=main(name); assert m.count('id="hindi"')==1 and 'lang="hi"' in m, name
em=main('emergency-surgery-ranchi.html')
for k in ['Intestinal obstruction','Perforation and peritonitis','strangulated hernia','day and night','id="page-faq"','Samford Super Speciality Hospital']: assert k.lower() in em.lower(), k
assert 'id="emergency"' in home and 'emergency-surgery-ranchi.html' in home
assert (ROOT/'sitemap.xml').read_text(encoding='utf-8').count('emergency-surgery-ranchi.html')==1
_SHOW='SHOW_CARDS = True' in (ROOT/'.ai'/'google_reviews.py').read_text(encoding='utf-8')
for name in ['index.html','bariatu-surgery-clinic-ranchi.html']:
    m=main(name); assert ('class="review-card"' in m or not _SHOW) and 'iframe' not in m and 'query_place_id=ChIJxcKRJAbj9DkREUTv8FsVn08' in m and 'writereview?placeid=' in m, name
assert 'AggregateRating' not in ''.join(x.read_text(encoding='utf-8') for x in pages)
assert 'images/garhwa-anaesthesia-workstation.jpg' in g and 'garhwa-anesthesia-photo' not in g
assert (('stored on this website, using text recorded from the public Google profile' in main('privacy-policy.html'))==('SHOW_CARDS = True' in (ROOT/'.ai'/'google_reviews.py').read_text(encoding='utf-8'))) and 'Updated 17 October 2026' in main('privacy-policy.html')
# Round 3 review fixes (ChatGPT B1-B4, improvements)
allhtml=''.join(x.read_text(encoding='utf-8') for x in pages)
for bad in ['गुदा में चीरा','avoids the risk','all general surgical emergencies','painless','आंत रुकना','Ranchi (2025)','Ranchi (2024)']:
    assert bad not in allhtml, bad
for name in ['index.html','laparoscopic-surgeon-jharkhand.html']:
    assert 'वे बवासीर, फिशर, भगंदर और सौम्य थायराइड रोगों की सर्जरी' in main(name), name
assert 'भगंदर में आमतौर पर ऑपरेशन की आवश्यकता होती है' in main('piles-fistula-surgery-ranchi.html')
assert 'ICU support' in em and 'Vascular emergencies' in em and 'IAGES' in main('index.html') and 'IAGES' in main('about-dr-vikeerna-bharti.html')
assert 'After emergency care: follow-up visits' in em and 'Call Dr. Bharti: 62060 91982' in em and 'cold, pale or numb' in em
for name in ['surgeon-in-garhwa.html','bariatu-surgery-clinic-ranchi.html','laparoscopic-surgeon-jharkhand.html']:
    assert re.search(r'<section[^>]*id="hindi"[^>]*lang="hi"', main(name)), name
# 12 Oct: owner-checked photo placement and restored original disease graphics.
for name,want,never in [
 ('gallbladder-stone-surgery-ranchi.html',['images/gallbladder-stone-disease-infographic.jpg','images/ot-laparoscopy-dr-bharti-4.jpg'],['ot-laparoscopy-tower']),
 ('appendix-surgery-ranchi.html',['images/ot-laparoscopy-tower.jpg'],['ot-laparoscopy-dr-bharti-4']),
 ('hernia-surgery-ranchi.html',['images/hernia-disease-infographic.jpg','images/ot-laparoscopy-dr-bharti-3.jpg','href="blog-post-etep.html"','href="blog-post-lumbar-hernia.html"','Hernia repair explained in a diagram'],[]),
 ('bariatric-surgery-ranchi.html',['images/bariatric-sleeve-gastrectomy-infographic.jpg','images/ot-laparoscopy-dr-bharti-2.jpg'],[]),
 ('varicose-veins-treatment-ranchi.html',['images/varicose-rfa-before-after.jpg','Varicose veins treatment with RFA, explained','images/varicose-rfa-technique-infographic.jpg'],['ot-laparoscopy','ot-surgical-team']),
 ('thyroid-surgery-ranchi.html',[],['ot-surgical-team','ot-laparoscopy']),
 ('piles-fistula-surgery-ranchi.html',[],['ot-instrument-trolley','ot-laparoscopy']),
 ('emergency-surgery-ranchi.html',['images/ot-instrument-trolley.jpg','images/ot-surgical-team.jpg','emergency laparotomy'],[])]:
    m=main(name)
    for w in want: assert w in m,(name,w)
    for n in never: assert n not in m,(name,n)
# 12 Oct: image SEO — ImageObject schema and image sitemap entries for the varicose figures.
vv=(ROOT/'varicose-veins-treatment-ranchi.html').read_text(encoding='utf-8'); sm=(ROOT/'sitemap.xml').read_text(encoding='utf-8')
for img in ['images/varicose-rfa-before-after.jpg','images/varicose-rfa-technique-infographic.jpg']:
    assert f'"contentUrl": "https://drbhartisurgery.com/{img}"' in vv, img
    assert f'<image:loc>https://drbhartisurgery.com/{img}</image:loc>' in sm, img
assert 'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"' in sm
# 17 Oct: all Google reviews shown; no retired Google short links anywhere.
from importlib import util as _u
_spec=_u.spec_from_file_location('google_reviews',ROOT/'.ai'/'google_reviews.py'); _gr=_u.module_from_spec(_spec); _spec.loader.exec_module(_gr)
home=main('index.html'); bar=main('bariatu-surgery-clinic-ranchi.html')
if _gr.SHOW_CARDS:
    for _m in (home,bar):
        assert _m.count('class="review-card"')==_gr.COUNT and _m.count('role="img" aria-label="')==_gr.COUNT and 'Approx. ' in _m
    assert f'Show all {_gr.COUNT} reviews' in home or _gr.COUNT<=6
    assert all(1<=r[1]<=5 for r in _gr.REVIEWS) and len({(r[0],r[3]) for r in _gr.REVIEWS})==_gr.COUNT
else:
    for _m in (home,bar,main('privacy-policy.html')):
        assert 'review-card' not in _m and '4.9' not in _m and 'from 13 reviews' not in _m
    assert 'Open Google profile' in home and 'Open Google profile' in bar
for x in pages:
    t=x.read_text(encoding='utf-8'); assert 'maps.app.goo.gl' not in t and 'share.google/' not in t and '&amp;amp;' not in t, x.name
print('PASS: content restoration — symptoms, Hindi, second-opinion band, insurance, homepage sections, Garhwa reception-first, location pages, gallery/about, sitemap, BMI reset; original FAQ counts, nav dropdown links, Garhwa OT, thyroid/RFA/emergency facts; round 3: FALS, no dates/awards, Hindi on 15 pages, emergency page, Google review embed, new Garhwa photo; owner-checked theatre photos and restored disease graphics.')
