"""Render the shared public navigation/footer into static pages. No hosting dependencies."""
from pathlib import Path
from html.parser import HTMLParser
import re

ROOT = Path(__file__).resolve().parents[1]
NAV = '''<a class="journey-skip" href="#page-content">Skip to content</a>
<header class="journey-header">
  <div class="journey-top"><div class="container">Consultations in Ranchi &amp; Garhwa <a href="tel:+916206091982" data-wa-cta="nav">Call 62060 91982</a></div></div>
  <div class="container journey-nav">
    <a href="index.html" class="journey-logo"><strong>Dr. Vikeerna Bharti</strong><span>General &amp; laparoscopic surgeon</span></a>
    <button class="journey-menu-button" type="button" aria-expanded="false" aria-controls="journey-menu">Menu <span aria-hidden="true">☰</span></button>
    <nav id="journey-menu" aria-label="Main navigation">
      <div class="nav-group"><button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-treatments">Treatments</button><div class="nav-sub" id="nav-treatments"><a href="gallbladder-stone-surgery-ranchi.html">Gallbladder stone surgery</a><a href="hernia-surgery-ranchi.html">Hernia surgery</a><a href="varicose-veins-treatment-ranchi.html">Varicose veins (RFA)</a><a href="piles-fistula-surgery-ranchi.html">Piles, fissure &amp; fistula</a><a href="appendix-surgery-ranchi.html">Appendix surgery</a><a href="bariatric-surgery-ranchi.html">Bariatric &amp; obesity surgery</a><a href="thyroid-surgery-ranchi.html">Thyroid surgery</a><a href="acid-reflux-surgery-ranchi.html">Acid reflux &amp; hiatus hernia</a><a href="emergency-surgery-ranchi.html">Emergency surgery (24/7)</a><a href="index.html#treatments">All treatments</a></div></div>
      <div class="nav-group"><button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-clinics">Clinics &amp; OPD</button><div class="nav-sub" id="nav-clinics"><a href="bariatu-surgery-clinic-ranchi.html">Bariatu OPD — Ranchi Dental and Polyclinic</a><a href="appointments.html#locations">Samford Super Speciality Hospital</a><a href="surgeon-in-garhwa.html">Garhwa — Sai Sushila Sishu Hospital</a><a href="laparoscopic-surgeon-jharkhand.html">Travelling from across Jharkhand</a><a href="appointments.html">All clinics &amp; timings</a></div></div>
      <div class="nav-group"><button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-about">About</button><div class="nav-sub" id="nav-about"><a href="about-dr-vikeerna-bharti.html">About Dr. Bharti</a><a href="gallery.html">Gallery &amp; news</a><a href="blog.html">Research &amp; publications</a><a href="index.html#reviews">Patient reviews</a></div></div>
      <a href="second-opinion-surgery-ranchi.html">Second opinion</a><a class="journey-button small" href="appointments.html">Book a consultation</a>
    </nav>
  </div>
</header>'''
FOOTER = '''<footer class="journey-footer"><div class="container journey-footer-grid">
<div><a class="journey-footer-name" href="index.html">Dr. Vikeerna Bharti</a><p>General &amp; laparoscopic surgeon<br>MS General Surgery, PGIMER Chandigarh<br>FMAS · FIAGES · FALS (Robotic)</p><a href="tel:+916206091982">+91 62060 91982</a><br><a href="mailto:contact@drbhartisurgery.com">contact@drbhartisurgery.com</a></div>
<div><h2>Your visit</h2><a href="appointments.html">Appointments &amp; locations</a><a href="second-opinion-surgery-ranchi.html">Surgical second opinion</a><a href="bariatu-surgery-clinic-ranchi.html">Ranchi Dental and Polyclinic</a><a href="surgeon-in-garhwa.html">Garhwa visits</a><a href="laparoscopic-surgeon-jharkhand.html">Travelling from Jharkhand</a></div>
<div><h2>Explore</h2><a href="index.html#treatments">Conditions &amp; treatments</a><a href="emergency-surgery-ranchi.html">Emergency surgery (24/7)</a><a href="blog.html">Research &amp; publications</a><a href="about-dr-vikeerna-bharti.html">About Dr. Bharti</a><a href="gallery.html">Gallery &amp; newspaper coverage</a><a href="index.html#reviews">Patient reviews</a><a href="index.html#bmi">BMI calculator</a><a href="https://www.facebook.com/drvikeerna" target="_blank" rel="noopener">Facebook</a><a href="privacy-policy.html">Privacy policy</a></div>
</div><div class="container journey-footnote"><p>For an emergency, seek urgent in-person care at a hospital. Do not wait for a website or WhatsApp reply. Website information does not replace an individual medical assessment.</p><p>© 2026 Dr. Vikeerna Bharti</p></div></footer>
<nav class="journey-mobile-actions" aria-label="Quick contact"><a href="appointments.html">Book OPD</a><a href="tel:+916206091982" data-wa-cta="sticky_bar">Call doctor</a><a href="appointments.html#locations">Clinic directions</a></nav>'''

class Blocks(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.text=text; self.lines=[0]; self.stack=[]; self.spans=[]
        for m in re.finditer('\n',text): self.lines.append(m.end())
        self.feed(text)
    def position(self):
        line,col=self.getpos(); return self.lines[line-1]+col
    def handle_starttag(self,tag,attrs):
        if tag in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}: return
        a=dict(attrs); classes=a.get('class','').split()
        target=(a.get('id') in {'nav','mobNav'} or any(c in classes for c in ['utbar','wa-float','mobile-cta','journey-header','journey-skip','journey-mobile-actions']) or tag=='footer')
        self.stack.append((tag,self.position(),target))
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0]==tag:
                _,start,target=self.stack[i]; self.stack=self.stack[:i]
                if target: self.spans.append((start,self.position()+len('</'+tag+'>')))
                break

def render():
    for p in ROOT.glob('*.html'):
        text=p.read_text(encoding='utf-8')
        if p.name=='404.html':
            text=re.sub(r'(\b(?:href|src)=")/(?!/)', r'\1', text)
        text=re.sub(r'<script src="(?:journey|patient-tools)\.js[^"\s]*" defer></script>\s*', '', text)
        spans=Blocks(text).spans
        spans=[s for s in spans if not any(t[0]<s[0] and t[1]>=s[1] for t in spans)]
        for a,b in sorted(spans,reverse=True): text=text[:a]+text[b:]
        text=re.sub(r'\n[ \t]*\n(?:[ \t]*\n)*', '\n', text)
        text=re.sub(r'(<body\b[^>]*>)',lambda m:m[1]+'\n'+NAV+'\n',text,count=1)
        text=text.replace('</body>','\n'+FOOTER+'\n</body>')
        if 'id="page-content"' not in text:
            text=text.replace('</header>', '</header>\n<div id="page-content" tabindex="-1"></div>',1)
        if 'href="journey.css' not in text: text=text.replace('</head>','<link rel="stylesheet" href="journey.css?v=20261010d">\n</head>')
        if 'src="journey.js' not in text: text=text.replace('</body>','<script src="journey.js?v=20261010d" defer></script>\n</body>')
        text=re.sub(r'journey\.css\?v=[^"\s]+', 'journey.css?v=20261010d', text)
        text=re.sub(r'journey\.js\?v=[^"\s]+', 'journey.js?v=20261010d', text)
        text=text.replace('site.js?v=20260928','site.js?v=20261009')
        text=re.sub(r'patient-tools\.js\?v=[^"\s]+', 'patient-tools.js?v=20261010d', text)
        if 'src="patient-tools.js' not in text: text=text.replace('</body>','<script src="patient-tools.js?v=20261010d" defer></script>\n</body>')
        text=re.sub(r'\n[ \t]*\n(?:[ \t]*\n)*', '\n', text)
        if p.name=='404.html':
            text=re.sub(r'(\b(?:href|src)=")(?!(?:[a-z]+:|/|#))', r'\1/', text)
        p.write_text(text,encoding='utf-8')

if __name__=='__main__': render()
