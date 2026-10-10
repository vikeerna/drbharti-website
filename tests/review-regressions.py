"""All-page regression checks for the October review and restored features."""
from pathlib import Path
from urllib.parse import unquote
import re
ROOT=Path(__file__).resolve().parents[1]
blocked=['zero recurrences','metro-level','industry-leading','every district','book your slot','slots are limited','name and age','name & age','reviews them before','replies may be delayed','rfa — no incision','kidney reduced back','every 1st and 3rd sunday','advanced laparoscopic & bariatric surgeon']
for p in ROOT.glob('*.html'):
    text=unquote(p.read_text(encoding='utf-8')).lower().replace('&amp;','&')
    for phrase in blocked: assert phrase not in text, f'{p.name}: stale claim/process {phrase}'
    assert re.search(r'src="/?patient-tools\.js',text),p.name
    assert 'dr-vikeerna-bharti-logo.png' not in text,p.name
for name in ['index.html','appointments.html','surgeon-in-garhwa.html']:
    text=(ROOT/name).read_text(encoding='utf-8')
    assert 'data-garhwa-next' in text and 'not live availability' in text,name
for name in ['index.html','bariatric-surgery-ranchi.html']:
    assert 'id="bmi-form"' in (ROOT/name).read_text(encoding='utf-8'),name
appendix=(ROOT/'appendix-surgery-ranchi.html').read_text(encoding='utf-8').split('<main',1)[1]
assert appendix.index('Possible appendicitis needs urgent') < appendix.index('Plan a follow-up visit')
for name in ['blog-post-etep.html','blog-post-lumbar-hernia.html']:
    main=(ROOT/name).read_text(encoding='utf-8').split('<main',1)[1].split('</main>',1)[0]
    assert 'PGIMER' not in main,name
print('PASS: review regressions across all pages, restored features, appendix urgency and research attribution.')
