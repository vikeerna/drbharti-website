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
for name in ['index.html','bariatu-surgery-clinic-ranchi.html']:
    m=main(name); assert 'class="review-embed"' in m and 'output=embed' in m and 'loading="lazy"' in m, name
assert 'AggregateRating' not in ''.join(x.read_text(encoding='utf-8') for x in pages)
assert 'images/garhwa-anaesthesia-workstation.jpg' in g and 'garhwa-anesthesia-photo' not in g
assert 'Google may set cookies' in main('privacy-policy.html')
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
print('PASS: content restoration — symptoms, Hindi, second-opinion band, insurance, homepage sections, Garhwa reception-first, location pages, gallery/about, sitemap, BMI reset; original FAQ counts, nav dropdown links, Garhwa OT, thyroid/RFA/emergency facts; round 3: FALS, no dates/awards, Hindi on 15 pages, emergency page, Google review embed, new Garhwa photo.')
