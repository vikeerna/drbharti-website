"""Build individual treatment pages. Run render_shell.py afterwards.

Clinical references are linked visibly. Doctor review remains a release task;
do not label these pages medically reviewed without that review.
"""
from html import escape as e
from page_frame import write_page, BASE
from treatment_details import EXTRA_PAGES, PROCEDURES
from restored_content import TREATMENT_EXTRA, INSURANCE, CREDENTIAL_BAND
from original_content import DETAILS, RECOVERY, WHY, PHOTO, FAQS
from round3_content import hindi_section

PAGES = [
    dict(
        file='gallbladder-stone-surgery-ranchi.html',
        label='Gallbladder stones',
        title='Gallbladder Stone Surgery in Ranchi | Dr. Vikeerna Bharti',
        description='Discuss gallbladder stones, laparoscopic surgery, recovery and cost factors with Dr. Vikeerna Bharti in Ranchi. OPD consultations and second opinions.',
        heading='Gallbladder stone surgery in Ranchi',
        intro='Have gallstones on a scan, recurring pain, or advice to undergo surgery? Discuss what your report means and whether an operation is appropriate for you.',
        hindi='पित्त की थैली में पथरी की रिपोर्ट है? अपनी रिपोर्ट लेकर इलाज और ऑपरेशन की जरूरत पर चर्चा करें।',
        assessment_title='Start with your symptoms and scan',
        assessment='Gallstones may cause no symptoms, or cause episodes of pain in the upper abdomen, sometimes with nausea. Symptoms alone do not establish the diagnosis. Assessment may include an ultrasound and blood tests.',
        bring='Bring your ultrasound report and images, available blood tests, previous prescriptions and any hospital discharge summary. Note when pain occurs and how long it lasts.',
        options=[
            ('Is surgery always necessary?', 'Stones found incidentally without symptoms may not require treatment. Symptoms, complications and stones in the bile duct change the decision.'),
            ('Laparoscopic gallbladder removal', 'When advised, cholecystectomy removes the gallbladder containing the stones through small incisions. Ask how the proposed operation fits your findings.'),
            ('What if the bile duct contains stones?', 'Bile-duct stones may need a separate procedure such as ERCP. Your assessment determines the treatment sequence and whether additional care is needed.'),
        ],
        recovery='After uncomplicated keyhole surgery, discharge may be on the same day or after an overnight stay. Return to work often takes around one to two weeks, depending on your recovery and the work you do. Open surgery or complications can require longer recovery. Follow your own discharge advice about wounds, driving, lifting and follow-up.',
        risks='Discuss bleeding, infection, blood clots, bile leak, injury to the bile duct or nearby organs, retained stones and persistent digestive symptoms. The benefits and risks depend on your health and findings; a small-incision operation is still surgery.',
        cost_title='Gallbladder stone surgery cost in Ranchi',
        cost='Ask for an estimate after your reports and proposed treatment have been assessed. An uncomplicated planned operation and treatment involving bile-duct stones or an emergency can have different costs.',
        cost_items=['Hospital and room category', 'Surgical and anaesthesia charges', 'Tests, medicines and consumables', 'Any separate bile-duct procedure, additional stay and follow-up'],
        urgent='Severe abdominal pain, fever or shivering, yellow eyes or skin, or pain spreading to the back with vomiting needs urgent hospital assessment. Do not wait for an appointment message reply.',
        faqs=[
            ('Is the gallbladder removed or just the stones?', 'The usual operation is removal of the gallbladder containing the stones. Bile-duct stones are a separate issue and may need additional treatment.'),
            ('Can I return to work the next day?', 'Do not plan on a guaranteed next-day return. Your operation, symptoms, job and recovery determine when it is appropriate to resume work.'),
            ('Can I discuss an operation advised elsewhere?', 'Yes. Bring the existing recommendation, ultrasound and available reports to a second-opinion consultation.'),
        ],
        sources=[('NHS: gallstones','https://www.nhs.uk/conditions/gallstones/'), ('NHS: recovery after gallbladder removal','https://www.nhs.uk/tests-and-treatments/gallbladder-removal/recovery/'), ('NHS: complications of gallbladder removal','https://www.nhs.uk/tests-and-treatments/gallbladder-removal/complications/')],
    ),
    dict(
        file='hernia-surgery-ranchi.html',
        label='Hernia repair',
        title='Hernia Surgery in Ranchi | Dr. Vikeerna Bharti',
        description='Consult Dr. Vikeerna Bharti for hernia surgery in Ranchi. Discuss open or laparoscopic repair, mesh, recurrent hernia, recovery and cost factors.',
        heading='Hernia surgery in Ranchi',
        intro='A groin swelling, an abdominal bulge or a hernia that has returned deserves an individual assessment. Understand the repair options and plan around your recovery.',
        hindi='हर्निया या पुराने ऑपरेशन की जगह सूजन है? जांच और इलाज के विकल्पों पर चर्चा के लिए मिलें।',
        assessment_title='Which type of hernia do you have?',
        assessment='A hernia occurs when tissue pushes through a weak area. A bulge may become more obvious with coughing or standing. Groin, umbilical and incisional hernias need different assessments; examination helps identify the type and whether further tests are needed.',
        bring='Bring any ultrasound or CT reports already available. For a recurrent hernia, previous operation notes, the discharge summary and mesh details, if available, are particularly useful. No new scan is required just to request a visit.',
        options=[
            ('Repair or observation?', 'Some adults with an inguinal hernia causing little or no trouble may discuss observation. This is not appropriate for every hernia. Symptoms, hernia type and your health influence the advice.'),
            ('Open or laparoscopic repair?', 'Repair can be performed through an open incision or keyhole approach. Discuss why one approach is proposed for your hernia, including any previous repair.'),
            ('Mesh and complex repairs', 'Mesh is commonly used to reinforce a repair, but the plan is individual. For a large or recurrent hernia, ask about the repair strategy, mesh-related concerns and expected recovery.'),
        ],
        recovery='Recovery after inguinal hernia repair commonly takes several weeks. Desk work may be possible earlier than heavy physical work. Ask for specific advice on lifting, exercise and driving; the schedule depends on the repair and your recovery.',
        risks='Possible problems include wound infection, ongoing pain or numbness, recurrence, blood clots and injury to nearby structures. Ask which risks matter most for your proposed repair.',
        cost_title='Hernia surgery cost in Ranchi',
        cost='The estimate depends on the type and complexity of the hernia and the planned repair. A recurrent or large abdominal-wall hernia may need a different plan from a first-time groin hernia.',
        cost_items=['One side or both sides; first or recurrent repair', 'Open or laparoscopic approach and planned mesh', 'Hospital, anaesthesia and expected stay', 'Tests, medicines, consumables and follow-up'],
        urgent='A hernia with sudden severe pain, vomiting, a firm or tender bulge that no longer goes back in, or difficulty passing stool or gas needs urgent hospital assessment. Do not wait for a routine booking.',
        faqs=[
            ('Can I wait before having hernia surgery?', 'For selected adults with an inguinal hernia and few symptoms, observation may be discussed. Examination is needed before deciding whether that is appropriate for you.'),
            ('Is laparoscopic repair suitable for every hernia?', 'The approach is chosen after assessment. Bring your previous operation records if the hernia has returned so that the repair can be planned with that history in mind.'),
            ('What should I ask about mesh?', 'Ask why mesh is proposed, what alternatives apply to your case, the expected benefits and possible complications, and how future concerns would be assessed.'),
        ],
        sources=[('NHS: hernia','https://www.nhs.uk/conditions/hernia/'), ('NHS: inguinal hernia repair','https://www.nhs.uk/tests-and-treatments/inguinal-hernia-repair/'), ('NHS England: deciding about an inguinal hernia','https://www.england.nhs.uk/wp-content/uploads/2023/11/PRN00250-dst-making-a-decision-about-inguinal-hernia.pdf')],
    ),
    dict(
        file='varicose-veins-treatment-ranchi.html',
        label='Varicose veins',
        title='Varicose Veins & RFA Treatment in Ranchi | Dr. Vikeerna Bharti',
        description='Discuss varicose veins treatment in Ranchi, duplex assessment and suitability for radiofrequency ablation (RFA) with Dr. Vikeerna Bharti.',
        heading='Varicose veins treatment in Ranchi',
        intro='Visible leg veins, aching, swelling or skin changes? Start with an assessment of the cause and discuss whether vein treatment could help.',
        hindi='पैरों की उभरी नसें, भारीपन या त्वचा में बदलाव है? जांच और इलाज के विकल्पों के लिए परामर्श लें।',
        assessment_title='Assessment before choosing a procedure',
        assessment='Varicose veins are enlarged superficial veins, usually in the legs. They may cause aching, heaviness, itching, swelling or skin changes. A duplex ultrasound can assess blood flow and help guide treatment. A photograph alone cannot establish which procedure you need.',
        bring='Bring any venous Doppler or duplex report, previous vein-treatment records and your medicine list. Mention any previous blood clot and any leg wound. You can book the first consultation without uploading leg photographs.',
        options=[
            ('Do all visible veins need treatment?', 'No. Symptoms, skin changes, ultrasound findings and your preferences matter. Activity, skin care and compression may be discussed where appropriate.'),
            ('Radiofrequency ablation (RFA)', 'RFA uses a catheter and heat to close a faulty vein. Dr. Bharti performs RFA at Samford Super Speciality Hospital, Ranchi. Suitability depends on the scan and clinical assessment.'),
            ('Other treatment choices', 'Depending on the findings, alternatives can include foam sclerotherapy or surgery. Discuss which options are suitable and where the recommended treatment can be provided.'),
        ],
        recovery='After RFA, patients usually go home the next day, and walking is encouraged from the day of treatment. Soreness and bruising can occur. Your team will explain compression, activity, travel and follow-up based on the treatment performed. Additional treatment may be needed for remaining or recurrent veins.',
        risks='Ask about bruising, inflammation, skin changes, numbness, burns and blood clots. Soreness and bruising can occur, and varicose veins can recur or develop elsewhere.',
        cost_title='Varicose veins treatment cost in Ranchi',
        cost='A useful estimate follows clinical assessment and review of the duplex findings. Ask for the cost of the proposed treatment rather than relying on a price for an unspecified “laser” procedure.',
        cost_items=['One leg or both legs and the veins requiring treatment', 'Planned procedure and catheter or other consumables', 'Hospital, anaesthesia and ultrasound charges', 'Additional vein treatment, compression and follow-up'],
        urgent='A bleeding varicose vein needs urgent medical attention. Sudden new leg swelling or pain also needs prompt assessment; chest pain or breathlessness requires emergency care. Do not wait for a WhatsApp reply.',
        faqs=[
            ('Are RFA and laser the same treatment?', 'Both are heat-based vein treatments, but they use different energy sources. RFA uses radiofrequency energy; laser treatment uses laser energy. Ask which procedure is being proposed.'),
            ('Will I need compression stockings?', 'That depends on your assessment and aftercare plan. Do not assume that every patient needs stockings or that nobody will need them.'),
            ('Can varicose veins come back?', 'Remaining veins may need further treatment and varicose veins can recur. Discuss follow-up and what to do if symptoms return.'),
        ],
        sources=[('NHS: varicose veins','https://www.nhs.uk/conditions/varicose-veins/'), ('Cambridge University Hospitals: RFA procedure and risks','https://www.cuh.nhs.uk/patient-information/patient-information-on-vnus-closure-radiofrequency-ablation-of-varicose-veins/'), ('NHS: blood clots and urgent symptoms','https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/'), ('NICE: treatment options for varicose veins','https://www.nice.org.uk/guidance/qs67/chapter/quality-statement-3-treatment-of-varicose-veins')],
    ),
]


PAGES.extend(EXTRA_PAGES)
PAGES[1]["sources"].append(("Research: eTEP-RS ventral and incisional hernia repair", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7687670/"))

def build(p):
    from patient_features import BMI
    appendix=p['file']=='appendix-surgery-ranchi.html'
    alert=('<aside class="journey-warning"><strong>Possible appendicitis needs urgent hospital assessment.</strong><p>'+e(p['urgent'])+'</p></aside>') if appendix else ''
    visit_label='Plan a follow-up visit' if appendix else 'Book an OPD consultation'
    visit_purpose='follow_up' if appendix else 'opd'
    visit_note='<p class="journey-small">The visit links below are for non-urgent follow-up or planned discussion after assessment. Do not delay urgent care.</p>' if appendix else ''
    calculator=(BMI if p['file']=='bariatric-surgery-ranchi.html' else '')+hindi_section(p['file'],tint=False)
    x=TREATMENT_EXTRA[p['file']]
    p['title']=x.get('title',p['title'])
    p['hindi']=x['hindi']
    # Every original-site FAQ first, then the newer page-specific questions not already covered.
    faqs=list(FAQS[p['file']]); seen={q.lower() for q,_ in faqs}
    for q,a in list(x.get('faqs_replace',[]))+list(x.get('faqs_add',[])):
        if q.lower() not in seen: faqs.append((q,a)); seen.add(q.lower())
    p['faqs']=faqs
    def detail(sec):
        sid,eyebrow,title,paras,bullets=sec
        body=''.join(f'<p>{e(t)}</p>' for t in paras)+(('<ul class="journey-list">'+''.join(f'<li>{e(b)}</li>' for b in bullets)+'</ul>') if bullets else '')
        return f'<section class="journey-section detail-section" id="{sid}"><div class="container reading-width"><p class="journey-eyebrow">{e(eyebrow)}</p><h2>{e(title)}</h2>{body}</div></section>'
    details=''.join(detail(sec) for sec in DETAILS[p['file']])
    timeline='<ul class="timeline-list">'+''.join(f'<li><strong>{e(k)}</strong><span>{e(v)}</span></li>' for k,v in RECOVERY[p['file']])+'</ul>'
    img,alt=PHOTO[p['file']]
    why=f'''<section class="journey-section tint" id="why"><div class="container journey-split"><div><p class="journey-eyebrow">Your surgeon</p><h2>Why patients consult Dr. Vikeerna Bharti</h2><ul class="journey-list">{''.join(f'<li>{e(w)}</li>' for w in WHY)}</ul><a class="journey-textlink" href="about-dr-vikeerna-bharti.html">Qualifications and operative experience →</a></div><figure class="clinic-photo"><img src="{img}" width="1050" height="1400" loading="lazy" alt="{e(alt,quote=True)}"><figcaption>{e(alt)}</figcaption></figure></div></section>'''
    symptoms=''.join(f'<li>{e(item)}</li>' for item in x['symptoms'])
    about=f'''<section class="journey-section" id="symptoms"><div class="container journey-split"><div><p class="journey-eyebrow">Understanding the condition</p><h2>{e(x['what_title'])}</h2><p>{e(x['what'])}</p></div><div class="journey-card"><h2 class="card-heading">{e(x['symptoms_title'])}</h2><ul class="journey-list">{symptoms}</ul><p class="journey-small">{e(x['symptoms_note'])}</p></div></div></section>'''

    cards=''.join(f'<article class="journey-card"><h3>{e(title)}</h3><p>{e(copy)}</p></article>' for title,copy in p['options'])
    faq=''.join(f'<details{chr(32)+chr(108)+chr(97)+chr(110)+chr(103)+chr(61)+chr(34)+chr(104)+chr(105)+chr(34) if any(chr(0x900)<=c<=chr(0x97f) for c in q) else str()}><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in p['faqs'])
    costs=''.join(f'<li>{e(item)}</li>' for item in p['cost_items'])
    sources=''.join(f'<li><a href="{e(url,quote=True)}" target="_blank" rel="noopener">{e(label)} ↗</a></li>' for label,url in p['sources'])
    related=''.join(f'<a href="{other["file"]}">{e(other["label"])}</a>' for other in PAGES if other is not p)
    procedures=''.join(f'<article><h3>{e(title)}</h3><p>{e(copy)}</p></article>' for title,copy in PROCEDURES[p['file']])
    body=f'''<main id="page-content" tabindex="-1">
<section class="journey-hero"><div class="container"><p class="journey-breadcrumb"><a href="index.html">Home</a> / <a href="index.html#treatments">Treatments</a> / {e(p['label'])}</p><div class="journey-hero-grid"><div><p class="journey-eyebrow">Understand your options · Plan your visit</p><h1>{e(p['heading'])}</h1>{alert}<p class="journey-intro">{e(p['intro'])}</p>{visit_note}<div class="journey-actions"><a class="journey-button" href="appointments.html?purpose={visit_purpose}#request">{visit_label}</a><a class="journey-button secondary" href="appointments.html?purpose=second_opinion#request">Request a second opinion</a></div><p class="journey-small treatment-hindi" lang="hi">{e(p['hindi'])}</p></div>
<aside class="journey-panel treatment-doctor"><div class="treatment-doctor-heading"><img src="images/dr-vikeerna-bharti-portrait.jpg" width="1021" height="1280" alt="Dr. Vikeerna Bharti"><div><p class="journey-eyebrow">Your consultation</p><h2>Dr. Vikeerna Bharti</h2></div></div><p>General &amp; laparoscopic surgeon<br><strong>MS General Surgery, PGIMER Chandigarh</strong><br>FMAS · FIAGES · FALS (Robotic)</p><hr><p><strong>Ranchi Dental and Polyclinic</strong><br>Bariatu Road, Near Manipal Hospital, Ranchi<br>Mon–Sat, 9–10 AM &amp; 5–7:30 PM</p><a class="journey-textlink" href="https://maps.app.goo.gl/aGJb7LgdmoKjzaMR6" target="_blank" rel="noopener" data-location="bariatu" data-wa-cta="location_card"><span aria-hidden="true">⌖ </span>Open clinic directions ↗</a><p class="journey-small"><a href="appointments.html#locations">Samford &amp; Garhwa visit details</a></p></aside></div></div></section>
<nav class="treatment-jumps container" aria-label="On this page"><a href="#symptoms">Symptoms</a><a href="#assessment">Assessment</a><a href="#procedures">Conditions &amp; procedures</a><a href="#options">Treatment options</a><a href="#recovery">Recovery &amp; risks</a><a href="#cost">Cost</a><a href="#page-faq">FAQs</a></nav>
{about}
{details}
<section class="journey-section" id="assessment"><div class="container journey-split"><div><p class="journey-eyebrow">The first consultation</p><h2>{e(p['assessment_title'])}</h2><p>{e(p['assessment'])}</p></div><div class="journey-card"><h3>What to bring</h3><p>{e(p['bring'])}</p><p>Bring a list of medicines and allergies, and the questions you would like answered.</p></div></div></section>
<section class="journey-section tint" id="procedures"><div class="container"><p class="journey-eyebrow">Medical names, explained simply</p><h2>Conditions and operations you may hear about</h2><div class="procedure-list">{procedures}</div><p class="journey-small treatment-note">The procedure is chosen after assessment. A technique listed here is not suitable for every patient.</p></div></section>
<section class="journey-section" id="options"><div class="container"><p class="journey-eyebrow">An individual treatment plan</p><h2>Options to discuss</h2><div class="journey-grid">{cards}</div><p class="journey-small treatment-note">These are general options, not a recommendation for an individual patient. Your examination and reports guide the advice.</p></div></section>
{CREDENTIAL_BAND}
<section class="journey-section" id="recovery"><div class="container journey-split"><div><p class="journey-eyebrow">Planning ahead</p><h2>Recovery and return to routine</h2><p>{e(p['recovery'])}</p>{timeline}</div><div><p class="journey-eyebrow">Informed decisions</p><h2>Benefits and risks belong in the same conversation</h2><p>{e(p['risks'])}</p><a class="journey-textlink" href="second-opinion-surgery-ranchi.html">Already advised a procedure? Plan a second opinion →</a></div></div></section>
<section class="journey-section tint" id="cost"><div class="container journey-split"><div><p class="journey-eyebrow">Ask for a clear estimate</p><h2>{e(p['cost_title'])}</h2><p>{e(p['cost'])}</p><p>Ask what is included and excluded, and how unplanned treatment would be charged.</p><p class="insurance-note">{e(INSURANCE)}</p></div><div class="journey-card"><h3>What can affect the estimate?</h3><ul class="journey-list">{costs}</ul></div></div></section>
{why}
<section class="journey-section" id="page-faq"><div class="container journey-split"><div><p class="journey-eyebrow">Your questions</p><h2>Before you decide</h2><p>Write down anything you are unsure about and bring it to your consultation.</p></div><div class="journey-faq">{faq}</div></div></section>
<div class="container"><aside class="treatment-urgent"><h2>When to seek urgent care</h2><p>{e(p['urgent'])}</p></aside></div>
<section class="journey-section" id="contact"><div class="container journey-split"><div><p class="journey-eyebrow">Take the next step</p><h2>Bring your questions to an OPD visit</h2><p>Choose your clinic and prepare an appointment request. Review the message and press Send in WhatsApp.</p><p>You can visit during the listed OPD hours. For Garhwa, please check the visiting date before travelling.</p><div class="journey-actions"><a class="journey-button" href="appointments.html#request">Choose your appointment</a><a class="journey-button secondary" href="tel:+916206091982">Call 62060 91982</a></div></div><div><p class="journey-eyebrow">Further reading</p><h2>Information sources</h2><ul class="treatment-sources">{sources}</ul><p class="journey-small">Content updated 10 October 2026. General patient information; an examination is needed for personalised advice.</p><p class="journey-small"><a href="index.html#about">About Dr. Bharti</a> · <a href="privacy-policy.html">Privacy &amp; enquiries</a></p></div></div></section>
{calculator}<section class="journey-section tint"><div class="container"><h2>Other surgical concerns</h2><div class="journey-conditions">{related}<a href="index.html#treatments">View all conditions</a></div></div></section>
</main>'''
    schema=[{'@type':'FAQPage','@id':BASE+p['file']+'#page-faq','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in p['faqs']]}, {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':BASE},{'@type':'ListItem','position':2,'name':'Treatments','item':BASE+'#treatments'},{'@type':'ListItem','position':3,'name':p['label'],'item':BASE+p['file']}]}]
    write_page(p['file'],p['title'],p['description'],body,extra_schema=schema)


if __name__=='__main__':
    for page in PAGES:
        build(page)
    print(f'Built {len(PAGES)} individual treatment pages; apply shared shell next.')
