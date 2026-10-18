"""Homepage sections restored on 10 October 2026 (symptom finder, gallery preview, reviews, FAQs)."""
from html import escape as e
from restored_content import SYMPTOM_FINDER, GALLERY, INSURANCE
from original_content import SERVICES, HOME_FAQS
from google_reviews import review_section_cards, review_summary, review_actions

SYMPTOMS = ('<section class="journey-section tint" id="symptom-finder"><div class="container"><p class="journey-eyebrow">Start with what you feel</p>'
    '<h2>Common symptoms and where to read more</h2><p class="section-intro">Patients usually search for a symptom, not a diagnosis. These are common patterns only; an examination is needed to know the cause.</p>'
    '<div class="symptom-grid">' + ''.join(
        f'<a class="symptom-card" href="{href}#symptoms"><strong>{e(sym)}</strong><span>{e(cond)} →</span></a>' for sym, cond, href in SYMPTOM_FINDER) +
    '</div><p class="journey-small">Severe abdominal pain, fever with jaundice, vomiting blood or chest pain need urgent hospital care.</p></div></section>')

_preview = [g for g in GALLERY if g[4] == 'theatre'][:4] + [g for g in GALLERY if g[4] == 'milestones'][:2] + [g for g in GALLERY if g[4] == 'news'][:6]
GALLERY_PREVIEW = ('<section class="journey-section" id="media"><div class="container"><p class="journey-eyebrow">Gallery &amp; newspaper coverage</p>'
    '<h2>Clinical &amp; community gallery</h2><p class="section-intro">In the operating theatre, professional milestones, health camps and newspaper coverage.</p><div class="gallery-grid preview">' + ''.join(
        f'<figure><a href="{full}" target="_blank" rel="noopener"><img src="{thumb}" width="560" height="420" loading="lazy" alt="{e(alt, quote=True)}"></a><figcaption>{e(cap)}</figcaption></figure>'
        for full, thumb, alt, cap, _ in _preview) +
    '</div><div class="journey-actions"><a class="journey-button secondary" href="gallery.html">View the full gallery</a></div>'
    '<p class="journey-small">Newspaper reports are shown as published; they describe past events and do not predict an individual result.</p></div></section>')

REVIEWS = ('<section class="journey-section tint" id="reviews"><div class="container journey-split"><div><p class="journey-eyebrow">Patient feedback</p>'
    '<h2>Patient reviews on Google</h2>' + review_summary() + review_actions() + '</div>'
    '<div class="journey-card"><h3>Why patients come for a second opinion</h3><ul class="journey-list"><li>MS General Surgery from PGIMER Chandigarh; senior residency at PGIMER and AIIMS Bhubaneswar</li>'
    '<li>FMAS, FIAGES and FALS (Robotic) fellowships in minimal access surgery</li><li>Laparoscopic gallbladder, hernia and abdominal-wall, bariatric, anorectal, thyroid and vein surgery</li>'
    '<li>Published surgical research, including The Lancet Global Health and a Springer book chapter</li><li>Three locations: Bariatu and Samford in Ranchi, and visiting OPD in Garhwa</li></ul>'
    '<a class="journey-textlink" href="about-dr-vikeerna-bharti.html">More about Dr. Bharti →</a></div></div><div class="container">'+review_section_cards(6)+'</div></section>')

_PRACTICAL = [
 ('What should I bring?', 'Bring available reports and scans, previous prescriptions, a list of medicines and allergies, and any previous operation or discharge records. You do not need to order new tests just to request an appointment.'),
 ('Can I come for a second opinion?', 'Yes. Bring the existing treatment recommendation and available reports so that your concerns and options can be discussed in person.'),
 ('Do I need a reply before visiting?', 'You can attend the Ranchi OPDs during the listed hours without waiting for a WhatsApp confirmation. For help with timing, call 62060 91982. Garhwa visits depend on the visiting schedule, so check the date before travelling.'),
 ('Which operations does Dr. Bharti perform?', 'General and laparoscopic surgery, including gallbladder stone surgery, hernia and abdominal wall repair, appendix surgery, piles, fissure and fistula surgery, thyroid surgery, acid reflux and hiatus hernia surgery, sleeve gastrectomy and radiofrequency ablation for varicose veins.'),
 ('Where is surgery done if it is advised?', 'Planned and emergency operations are done at Samford Super Speciality Hospital, Ranchi. General and laparoscopic surgery, including hernia surgery, is also available at Sai Sushila Sishu Hospital, Garhwa. The right hospital is discussed after assessment.'),
 ('Is cashless treatment or Ayushman Bharat available?', INSURANCE.replace('Insurance and Ayushman Bharat: at', 'At')),
 ('I live outside Ranchi. How do I plan my visit?', 'Choose the OPD that suits your journey, bring all existing reports and allow time for tests if they are needed. See the travel information for patients from across Jharkhand.'),
 ('Can I consult in Hindi?', 'आप अपनी परेशानी और सवाल हिंदी में बता सकते हैं। अपॉइंटमेंट के लिए 62060 91982 पर कॉल या WhatsApp करें।'),
]
def faq_html():
    out = []
    for q, a in FAQS:
        lang = ' lang="hi"' if q == 'Can I consult in Hindi?' else ''
        extra = ' <a href="laparoscopic-surgeon-jharkhand.html">Travel information →</a>' if q.startswith('I live outside') else ''
        out.append(f'<details><summary>{e(q)}</summary><p{lang}>{e(a)}{extra}</p></details>')
    return ''.join(out)
def faq_schema(url):
    return {'@type': 'FAQPage', '@id': url + '#faq', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQS]}

SERVICES_HTML = ('<section class="journey-section" id="treatments"><div class="container"><p class="journey-eyebrow">Conditions &amp; treatment</p><h2>Comprehensive surgical services</h2>'
    '<p class="section-intro">General and laparoscopic surgery at Samford Super Speciality Hospital, Ranchi, with consultations at Bariatu and Samford and a visiting OPD in Garhwa. The right treatment depends on an individual assessment.</p><div class="service-grid">' +
    ''.join(f'<a class="service-card" href="{h}"><strong>{e(t)}</strong><span>{e(d)}</span><em>Full details &amp; FAQs →</em></a>' for h, t, d in SERVICES) + '</div></div></section>')

FAQS = list(HOME_FAQS) + [f for f in _PRACTICAL if f[0] not in ('Which operations does Dr. Bharti perform?',)]
