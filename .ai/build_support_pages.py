"""Legacy URL refresh: retain useful information with the current visit workflow."""
from html import escape as e
from page_frame import write_page, ROOT
from patient_features import SCHEDULE
from academic_record import PUBLICATIONS, PREPRINT, PRESENTATIONS, CONFERENCES
from page_frame import BASE
from round3_content import EMERGENCY_FAQ, emergency_body, hindi_section
from location_pages import GARHWA, GARHWA_FAQ, BARIATU, BARIATU_FAQ, JHARKHAND, JHARKHAND_FAQ, about_body, gallery_body

def faq_schema(file, faqs):
    return [{'@type':'FAQPage','@id':BASE+file+'#page-faq','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in faqs]}]

def section(title, text, id=''):
    return f'<section class="journey-section"{(" id="+chr(34)+id+chr(34)) if id else ""}><div class="container reading-width"><h2>{title}</h2>{text}</div></section>'

def page(file, title, description, heading, intro, content, schema=None, closing=None):
    close_h, close_p = closing or ('Plan an in-person consultation', 'Bring your available reports, prescriptions and questions.')
    body=f'''<main id="page-content" tabindex="-1"><section class="journey-hero compact"><div class="container reading-width"><p class="journey-breadcrumb"><a href="index.html">Home</a> / {e(heading)}</p><h1>{e(heading)}</h1><p class="journey-intro">{intro}</p></div></section>{content}<section class="journey-section tint"><div class="container reading-width"><h2>{close_h}</h2><p>{close_p} You can attend the Ranchi OPDs during the listed hours. For Garhwa, check the visiting date before travelling.</p><div class="journey-actions"><a class="journey-button" href="appointments.html">Clinics and OPD timings</a><a class="journey-button secondary" href="second-opinion-surgery-ranchi.html">Discuss a second opinion</a></div></div></section></main>'''
    write_page(file,title,description,body,extra_schema=schema)

page('surgeon-in-garhwa.html','Surgeon in Garhwa | Sai Sushila Sishu Hospital | Dr. Vikeerna Bharti',
     'General and laparoscopic surgeon in Garhwa. Dr. Vikeerna Bharti visits Sai Sushila Sishu Hospital, usually on the 1st and 3rd Sundays; hernia and keyhole surgery available.',
     'Surgeon in Garhwa — Sai Sushila Sishu Hospital',
     'Visiting surgical OPD with Dr. Vikeerna Bharti, general and laparoscopic surgeon, at Sai Sushila Sishu Hospital, Sai Gram, Chetna, Garhwa. Consultation, second opinion and surgery close to home.',
     GARHWA, faq_schema('surgeon-in-garhwa.html', GARHWA_FAQ))

page('bariatu-surgery-clinic-ranchi.html','General Surgeon in Bariatu, Ranchi | Dr. Vikeerna Bharti',
     'General and laparoscopic surgeon in Bariatu, Ranchi. Consult Dr. Vikeerna Bharti at Ranchi Dental and Polyclinic near Manipal Hospital. Mon–Sat 9–10 AM and 5–7:30 PM.',
     'General & laparoscopic surgeon in Bariatu, Ranchi',
     'Meet Dr. Vikeerna Bharti at Ranchi Dental and Polyclinic for a surgical consultation, second opinion or follow-up on Bariatu Road, near Manipal Hospital, Ranchi.',
     BARIATU, faq_schema('bariatu-surgery-clinic-ranchi.html', BARIATU_FAQ))

page('laparoscopic-surgeon-jharkhand.html','Laparoscopic Surgeon for Jharkhand Patients | Dr. Vikeerna Bharti, Ranchi',
     'Travelling to Ranchi for laparoscopic surgery or a second opinion? OPD locations, travel planning, insurance and Ayushman Bharat at Samford, and Garhwa visiting OPD.',
     'Laparoscopic surgeon for patients across Jharkhand',
     'Planning a surgical consultation from elsewhere in Jharkhand? Dr. Vikeerna Bharti consults in Ranchi at Bariatu and Samford Super Speciality Hospital, with a visiting OPD in Garhwa.',
     JHARKHAND, faq_schema('laparoscopic-surgeon-jharkhand.html', JHARKHAND_FAQ))

page('about-dr-vikeerna-bharti.html','About Dr. Vikeerna Bharti | General & Laparoscopic Surgeon, Ranchi',
     'Dr. Vikeerna Bharti: MBBS, MS General Surgery (PGIMER Chandigarh), FMAS, FIAGES, FALS (Robotic). Qualifications, clinical experience, operative experience and research of a laparoscopic surgeon in Ranchi.',
     'About Dr. Vikeerna Bharti',
     'Consultant general and laparoscopic surgeon in Ranchi, Jharkhand.',
     about_body())

page('gallery.html','Gallery | Dr. Vikeerna Bharti, Laparoscopic Surgeon in Ranchi',
     'Photographs from the operating theatre, clinics in Ranchi and Garhwa, professional milestones and newspaper coverage of Dr. Vikeerna Bharti’s surgical work.',
     'Gallery',
     'The operating theatre, our clinics and hospitals, and newspaper coverage of community and surgical work.',
     gallery_body())

page('blog.html','Research, Publications & Book Chapter | Dr. Vikeerna Bharti',
     'Explore Dr. Vikeerna Bharti’s surgical publications, including eTEP and lumbar hernia papers, a Springer chapter and GlobalSurg collaboration.',
     'Research, publications and book chapter','Published papers, a Springer book chapter and a preprint by Dr. Vikeerna Bharti. <a href="#publications">Publications</a> · <a href="#book-chapter">Book chapter</a> · <a href="#preprint">Preprint</a>. Research reports do not predict an individual patient’s outcome.',
     section('Journal publications and book chapter',PUBLICATIONS,'publications')+
     section('Preprint and work under review',PREPRINT,'preprint')+
     hindi_section('blog.html',tint=False)+
     section('Newspaper archive','''<p>View newspaper coverage of the Garhwa operation theatre opening, health camps and surgical work.</p><a href="gallery.html#news">Read newspaper clippings →</a>'''))

page('emergency-surgery-ranchi.html','Emergency Surgery in Ranchi | 24/7 at Samford | Dr. Vikeerna Bharti',
     '24/7 emergency surgery at Samford Super Speciality Hospital, Ranchi: appendicitis, perforation, intestinal obstruction, strangulated hernia, gallbladder emergencies and trauma. Dr. Vikeerna Bharti.',
     'Emergency surgery in Ranchi, 24/7',
     'Dr. Vikeerna Bharti attends general surgical emergencies day and night at Samford Super Speciality Hospital, H.B. Road, Kokar Chowk, Ranchi.',
     emergency_body()+hindi_section('emergency-surgery-ranchi.html'),
     faq_schema('emergency-surgery-ranchi.html', EMERGENCY_FAQ),
     closing=('After emergency care: follow-up visits', 'These links are for recovery and follow-up, not urgent assessment. Bring your discharge summary and reports.'))

page('blog-post-etep.html','eTEP Hernia Research at AIIMS Bhubaneswar | Dr. Bharti',
     'A patient-friendly summary of the 2024 eTEP case series from AIIMS Bhubaneswar, co-authored by Dr. Vikeerna Bharti, with a link to the original paper.',
     'Research: managing a peritoneal tear during eTEP',
     'A summary of “Peritoneal rent: No hindrance to completing eTEP”, published in Asian Journal of Medical Sciences in February 2024.',
     section('What the paper examined','''<p>This retrospective series from AIIMS Bhubaneswar described 10 inguinal (groin) hernia operations in which the peritoneum—the lining of the abdominal cavity—tore during eTEP surgery. The authors described repairing the tear and completing the planned extraperitoneal repair.</p><p>It is a small case series, not a trial establishing superiority over open surgery or a guarantee of success for future patients. The safe approach during an operation depends on the findings.</p><p>Dr. Vikeerna Bharti is the second author. His affiliation in the paper is Senior Resident, General Surgery, AIIMS Bhubaneswar.</p>''')+
     section('Original publication','''<p><strong>Authors, in publication order:</strong> Srishti Swarupa, Vikeerna Bharti, Leesa Misra, Nivedita Sahoo, Manash Ranjan Sahoo and Sreeparna Ghosh.</p><p>Asian Journal of Medical Sciences, 2024; 15(2): 223–226.</p><a class="journey-textlink" href="https://www.nepjol.info/index.php/AJMS/article/view/51501/46769" target="_blank" rel="noopener">Read the original journal paper (PDF) ↗</a><p><a href="hernia-surgery-ranchi.html">Hernia types and operations explained for patients →</a></p><a href="blog.html">All publications →</a>'''))

page('blog-post-lumbar-hernia.html','Lumbar Hernia Publication | Dr. Vikeerna Bharti',
     'Find Dr. Vikeerna Bharti’s 2022 publication on primary lumbar hernia and laparoscopic mesh repair, plus a link to discuss hernia assessment in Ranchi.',
     'Publication: primary lumbar hernia',
     'Primary Lumbar Hernia: Case Series with Technical Description of Laparoscopic Mesh Repair.',
     section('Publication details','''<p><strong>Authors:</strong> Vikeerna Bharti, Leesa Misra and Manash Ranjan Sahoo.</p><p><em>International Journal of Scientific Research</em>, 2022. DOI: 10.36106/ijsr/8401438.</p><p>The paper concerns laparoscopic mesh repair of primary lumbar hernia. For the study methods and findings, consult the original publication.</p><a class="journey-textlink" href="https://doi.org/10.36106/ijsr/8401438" target="_blank" rel="noopener">View the original publication ↗</a>''')+
     section('Discussing a hernia diagnosis','''<p>Bring your examination notes, available scans and any previous operation records. A published case series does not determine which repair is appropriate for an individual person.</p><p><a href="hernia-surgery-ranchi.html">Read about hernia assessment and repair options →</a></p><a href="blog.html">All publications →</a>'''))

page('404.html','Page Not Found | Dr. Vikeerna Bharti',
     'The requested page could not be found. Find treatment information, clinic locations and contact details for Dr. Vikeerna Bharti.',
     'Let’s help you find the right page','This page may have moved. Use the links below to continue.',
     section('Where would you like to go?','''<div class="journey-conditions"><a href="index.html">Homepage</a><a href="index.html#treatments">Conditions and treatments</a><a href="appointments.html">Clinics and contact</a><a href="blog.html">Research and publications</a></div>'''))
p=ROOT/'404.html'
p.write_text(p.read_text(encoding='utf-8').replace('index, follow, max-image-preview:large','noindex, follow'),encoding='utf-8')
print('Built nine support pages with consistent identity and visit wording.')

# Preserve the retired piles URL without carrying its old enquiry form or claims.
write_page('piles-fissure-fistula-treatment-ranchi.html', 'Piles, Fissure & Fistula Information Has Moved',
           'Continue to the current piles, fissure and fistula treatment information from Dr. Vikeerna Bharti in Ranchi.',
           '<main id="page-content" tabindex="-1"><section class="journey-section"><div class="container"><h1>Piles, fissure and fistula information</h1><p>This page has moved.</p><a class="journey-button" href="piles-fistula-surgery-ranchi.html">Continue to treatment information</a></div></section></main>')
p=ROOT/'piles-fissure-fistula-treatment-ranchi.html'
s=p.read_text(encoding='utf-8').replace('index, follow, max-image-preview:large','noindex, follow')
s=s.replace('<link rel="canonical" href="https://drbhartisurgery.com/piles-fissure-fistula-treatment-ranchi.html">','<link rel="canonical" href="https://drbhartisurgery.com/piles-fistula-surgery-ranchi.html"><meta http-equiv="refresh" content="0; url=piles-fistula-surgery-ranchi.html">')
p.write_text(s,encoding='utf-8')
