"""Restored, reviewed patient-education content (10 October 2026, Claude build).

Plain facts only: no rankings, outcome rates or superiority claims. Owner-confirmed
facts used here: Samford 11 AM-5 PM OPD; Samford accepts major insurance/TPA and
Ayushman Bharat; Garhwa offers general and laparoscopic surgery including hernia
surgery; written consent is on file for the archived patient and camp photographs.
"""

INSURANCE = ('Insurance and Ayushman Bharat: at Samford Super Speciality Hospital, where Dr. Bharti operates, '
             'cashless treatment is available under major health-insurance and TPA plans, Ayushman Bharat and the Jharkhand Rajya Karmi Swasthya Bima Yojana (state employees’ health insurance). '
             'Eligibility depends on your policy or card and is confirmed by the hospital insurance desk.')

# Per treatment page: what it is, common symptoms, Hindi line, page-specific FAQs.
# 'faqs_replace' replaces the shared generic FAQs; 'faqs_add' is appended.
TREATMENT_EXTRA = {
'gallbladder-stone-surgery-ranchi.html': dict(
    title='Gallbladder Stone Surgery in Ranchi | Laparoscopic | Dr. Vikeerna Bharti',
    what_title='What are gallbladder stones?',
    what='The gallbladder is a small pouch under the liver that stores bile. Gallbladder stones (gallstones, पित्त की पथरी) form when bile hardens into stones. Many people have no symptoms; others have repeated attacks of pain or complications such as inflammation of the gallbladder, jaundice or pancreatitis.',
    symptoms_title='Gallbladder stone symptoms: where is gallbladder pain felt?',
    symptoms=['Pain in the upper right side of the abdomen, or the upper middle part just below the ribs',
              'Pain that may spread to the back or the right shoulder blade',
              'Attacks that often start after a meal, especially oily food, and can last from about half an hour to several hours',
              'Nausea, vomiting, bloating or indigestion with the pain',
              'The location of the pain is the same in women and men; gallstones are more common in women'],
    symptoms_note='Acidity, ulcers, kidney stones and heart problems can cause similar pain, so an examination and ultrasound are needed before deciding on treatment. Fever, yellow eyes or constant severe pain need urgent hospital care.',
    hindi='पित्त की थैली की पथरी (गॉलब्लैडर स्टोन) में अक्सर पेट के ऊपरी दाएँ हिस्से में दर्द होता है, जो खाने के बाद बढ़ सकता है। दूरबीन (लैप्रोस्कोपिक) ऑपरेशन और दूसरी राय के लिए अपनी अल्ट्रासाउंड रिपोर्ट लेकर मिलें।',
    faqs_add=[('Where is gallbladder pain felt?','Usually in the upper right abdomen or the upper middle abdomen below the ribs, sometimes spreading to the back or right shoulder blade. Similar pain has other causes, so an examination and ultrasound are needed.'),
              ('Can gallbladder stones dissolve with medicines?','Medicines rarely clear gallbladder stones reliably, and stones often return when they are stopped. If stones are causing symptoms, discuss whether removing the gallbladder is appropriate.'),
              ('Is gallbladder surgery covered by insurance or Ayushman Bharat?','At Samford Super Speciality Hospital, cashless treatment is available under major health-insurance and TPA plans, Ayushman Bharat and the Jharkhand Rajya Karmi Swasthya Bima Yojana (state employees’ health insurance). The hospital insurance desk confirms eligibility for your policy or card.')]),
'hernia-surgery-ranchi.html': dict(
    title='Laparoscopic Hernia Surgery in Ranchi | Dr. Vikeerna Bharti',
    what_title='What is a hernia?',
    what='A hernia is a bulge that appears when fat or part of the bowel pushes through a weak area in the abdominal wall. Common types are inguinal and femoral hernias in the groin, umbilical hernias at the navel, and incisional hernias at an old operation scar. A hernia does not heal on its own; belts may ease discomfort but do not repair it.',
    symptoms_title='Hernia symptoms',
    symptoms=['A swelling in the groin, at the navel or near an old scar',
              'A bulge that becomes more obvious when standing, coughing or lifting and may go back when lying down',
              'Heaviness, dragging discomfort or pain, especially at the end of the day',
              'A hernia that has returned after an earlier repair'],
    symptoms_note='A hernia that becomes painful, firm and will not go back, especially with vomiting or difficulty passing stool or gas, needs urgent hospital care.',
    hindi='हर्निया में जांघ के जोड़ (ग्रोइन), नाभि या पुराने ऑपरेशन की जगह पर उभार होता है, जो खांसने या खड़े होने पर बढ़ता है। दूरबीन से हर्निया ऑपरेशन (TEP, TAPP, eTEP) और जटिल हर्निया के इलाज के लिए परामर्श लें।',
    faqs_add=[('Does a hernia go away without surgery?','No. A hernia does not heal by itself. Some small inguinal hernias with few symptoms can be watched after examination, but femoral hernias and painful hernias usually need repair.'),
              ('Who is a hernia specialist?','Hernias are treated by general and laparoscopic surgeons. Dr. Bharti performs open and laparoscopic hernia repairs, including TEP, TAPP, eTEP, eTEP-RS, IPOM and TAR, at Samford Super Speciality Hospital, Ranchi.'),
              ('Is hernia surgery covered by insurance or Ayushman Bharat?','At Samford Super Speciality Hospital, cashless treatment is available under major health-insurance and TPA plans, Ayushman Bharat and the Jharkhand Rajya Karmi Swasthya Bima Yojana (state employees’ health insurance). The hospital insurance desk confirms eligibility.')]),
'varicose-veins-treatment-ranchi.html': dict(
    what_title='What are varicose veins?',
    what='Varicose veins are swollen, twisted veins under the skin, usually in the legs. They develop when valves inside the veins stop working properly, so blood pools in the leg. Standing for long hours, pregnancy, family history and increasing age make them more likely.',
    symptoms_title='Varicose vein symptoms',
    symptoms=['Visible bulging, blue or purple veins on the legs',
              'Aching, heavy or tired legs, worse after standing',
              'Swelling around the ankles, itching or night cramps',
              'Darkening or hardening of the skin near the ankle, eczema or a slow-healing wound'],
    symptoms_note='A bleeding vein needs urgent care. Sudden painful swelling of one leg, chest pain or breathlessness needs emergency assessment.',
    hindi='पैरों की नसें फूलना (वेरिकोज वेन्स) में नसें उभरी और टेढ़ी दिखती हैं और पैर भारी लगते हैं। डॉपलर जांच और RFA (रेडियोफ्रीक्वेंसी एब्लेशन) के बारे में परामर्श लें।',
    faqs_add=[('Which doctor treats varicose veins in Ranchi?','Varicose veins are assessed and treated by surgeons experienced in vein procedures. Dr. Bharti assesses varicose veins and performs radiofrequency ablation (RFA) and vein surgery at Samford Super Speciality Hospital, Ranchi.'),
              ('Is RFA covered by insurance or Ayushman Bharat?','Coverage depends on your policy or scheme. At Samford Super Speciality Hospital the insurance desk confirms eligibility for major health-insurance and TPA plans, Ayushman Bharat and the Jharkhand Rajya Karmi Swasthya Bima Yojana (state employees’ health insurance).')]),
'piles-fistula-surgery-ranchi.html': dict(
    what_title='Piles, fissure or fistula: how they differ',
    what='Piles (haemorrhoids, बवासीर) are swollen blood vessels in and around the anus. An anal fissure is a small tear in the lining of the anus. An anal fistula (भगंदर) is a small tunnel between the inside of the anus and the skin, usually after an abscess. They feel different and are treated differently, so an examination matters.',
    symptoms_title='Common symptoms',
    symptoms=['Piles: bright red bleeding during stool, a soft lump at the anus, itching; often little pain',
              'Fissure: sharp, cutting pain during and after passing stool, sometimes with a streak of blood',
              'Fistula: repeated boils, pus or discharge near the anus, with pain or swelling',
              'Pilonidal sinus: swelling, pain or discharge near the top of the buttock cleft'],
    symptoms_note='Rectal bleeding should not be assumed to be piles. Bleeding with weight loss, change in bowel habit or a family history of bowel cancer needs proper examination.',
    hindi='बवासीर (पाइल्स), फिशर (गुदा की अंदरूनी परत में छोटी दरार) और भगंदर (फिस्टुला) के लक्षण अलग होते हैं। खून आना, दर्द या मवाद हो तो जांच करवाएँ; इलाज की विधि जांच के बाद तय होती है।',
    faqs_replace=[('Can piles be treated without surgery?','Yes, many patients improve with fibre, fluids, stool softeners and prescribed medicines. Persistent bleeding, prolapsing piles or other features may need a procedure after examination.'),
                  ('Is laser treatment better for piles or fistula?','Laser is one technique for selected cases. It is not suitable for every patient, and recurrence can occur with any method. Ask which technique is proposed for your condition and why.'),
                  ('Can I bring a recommendation from another hospital?','Yes. Bring the treatment recommendation and available reports for an in-person second opinion.')]),
'appendix-surgery-ranchi.html': dict(
    what_title='What is appendicitis?',
    what='The appendix is a small pouch attached to the large bowel in the lower right abdomen. Appendicitis means it is inflamed, usually suddenly. Without timely treatment it can burst and cause a serious infection in the abdomen.',
    symptoms_title='Appendicitis symptoms: where is appendix pain felt?',
    symptoms=['Pain that often starts around the navel and moves to the lower right abdomen',
              'Pain that gets worse on walking, coughing or pressing the area',
              'Loss of appetite, nausea or vomiting',
              'Fever; symptoms can be different in children, older people and during pregnancy'],
    symptoms_note='These symptoms need same-day hospital assessment. Do not wait for an OPD appointment or a WhatsApp reply.',
    hindi='अपेंडिक्स (अपेंडिसाइटिस) में दर्द अक्सर नाभि के पास से शुरू होकर पेट के निचले दाएँ हिस्से में आता है, साथ में बुखार या उल्टी हो सकती है। ऐसा दर्द हो तो तुरंत नज़दीकी अस्पताल जाएँ।',
    faqs_replace=[('Can appendicitis be treated without an operation?','Appendicitis needs urgent hospital assessment. Surgery is commonly needed; antibiotics may be considered in selected cases after examination and tests. Do not try to make this decision at home or wait for an OPD appointment.'),
                  ('Where is appendix pain felt?','Often first around the navel, then in the lower right abdomen. Pain can be in a different place in children, older people and pregnant women, so seek hospital assessment for severe or worsening abdominal pain.'),
                  ('When should I see Dr. Bharti in OPD?','For a follow-up after treatment, for an appendix lump being watched, or to discuss a planned operation advised elsewhere. Urgent symptoms need hospital care first.')]),
'bariatric-surgery-ranchi.html': dict(
    what_title='When is obesity treated as a medical condition?',
    what='Obesity is a long-term condition that affects blood sugar, blood pressure, joints, sleep and fertility. Asian guidelines use lower body-mass-index (BMI) thresholds than Western ones because health risks rise at lower weights in South Asian people.',
    symptoms_title='When to consider an obesity assessment',
    symptoms=['Weight that has stayed high despite diet, exercise and medical treatment',
              'Weight-related conditions such as type 2 diabetes, high blood pressure, sleep apnoea, fatty liver or joint pain',
              'Difficulty with daily activity, breathlessness or snoring linked to weight',
              'Wanting to understand whether medicines, a supervised programme or surgery is appropriate'],
    symptoms_note='Bariatric surgery is considered only after assessment by the treating team. It is a permanent change and needs long-term follow-up.',
    hindi='मोटापा (ओबेसिटी) और उससे जुड़ी डायबिटीज़, ब्लड प्रेशर या नींद की समस्या के लिए जांच करवाएँ। दूरबीन से स्लीव गैस्ट्रेक्टॉमी के बारे में परामर्श लें।',
    faqs_replace=[('Who is suitable for sleeve gastrectomy?','Adults with severe obesity, particularly with weight-related conditions such as diabetes, after medical, nutritional and anaesthetic assessment. Suitability is decided individually.'),
                  ('Will I need to follow a special diet after surgery?','Yes. Food is reintroduced in stages, from liquids to soft and then regular food, with smaller portions, vitamin supplements as prescribed and regular follow-up.'),
                  ('Is bariatric surgery covered by insurance?','Coverage varies by policy. At Samford Super Speciality Hospital the insurance desk can check eligibility under your health-insurance or TPA plan.')]),
'thyroid-surgery-ranchi.html': dict(
    what_title='What are thyroid swellings?',
    what='The thyroid is a butterfly-shaped gland at the front of the neck. A goitre (घेंघा) is an enlarged gland; a nodule is a lump within it. Most nodules are not cancer, but they need assessment with blood tests, ultrasound and sometimes a needle test (FNAC).',
    symptoms_title='Thyroid swelling symptoms',
    symptoms=['A swelling at the front of the neck that moves when you swallow',
              'A feeling of pressure, difficulty swallowing or breathing when lying flat',
              'A change in voice or hoarseness',
              'Symptoms of an over- or under-active thyroid, such as weight change, palpitations or tiredness'],
    symptoms_note='Rapid growth of a lump, voice change or breathing difficulty needs prompt assessment.',
    hindi='गले में थायराइड की गांठ या सूजन (घेंघा) निगलते समय ऊपर-नीचे होती है। अपनी थायराइड जांच, अल्ट्रासाउंड और FNAC रिपोर्ट लेकर परामर्श लें।',
    faqs_replace=[('Does every thyroid nodule need surgery?','No. Many nodules only need monitoring. Surgery is discussed for suspicious test results, large or growing swellings, pressure symptoms or some over-active thyroid conditions.'),
                  ('Will I need tablets after thyroid surgery?','After total thyroidectomy, thyroid hormone tablets are needed for life. After removal of half the gland, some patients still need tablets; this is checked at follow-up.'),
                  ('Can I bring a recommendation from another hospital?','Yes. Bring the treatment recommendation and available reports for an in-person second opinion.')]),
'acid-reflux-surgery-ranchi.html': dict(
    what_title='What are acid reflux and hiatus hernia?',
    what='Acid reflux (GERD, एसिडिटी) happens when stomach acid flows back into the food pipe. A hiatus hernia is when part of the stomach moves up through the diaphragm into the chest, which can make reflux worse. Most people are treated with medicines and lifestyle changes.',
    symptoms_title='Acid reflux symptoms',
    symptoms=['Burning pain behind the breastbone (heartburn), often after meals or when lying down',
              'Sour or bitter taste, regurgitation of food or sour burps',
              'Cough, hoarseness or throat discomfort, especially at night',
              'Symptoms that continue despite regular medicines'],
    symptoms_note='Difficulty swallowing, weight loss, vomiting blood, black stools or chest pain need prompt medical assessment. Do not assume chest pain is acidity.',
    hindi='सीने में जलन, खट्टी डकार या खाना ऊपर आना एसिडिटी (GERD) या हायटस हर्निया के लक्षण हो सकते हैं। लंबे समय से दवा के बाद भी परेशानी हो तो जांच और इलाज के विकल्पों पर चर्चा करें।',
    faqs_replace=[('Is surgery an option for long-term acidity?','For selected patients with confirmed reflux or a hiatus hernia whose symptoms continue despite treatment, laparoscopic fundoplication may be discussed after endoscopy and other tests.'),
                  ('Is hiatus hernia the same as acidity?','No. A hiatus hernia is a structural problem at the diaphragm that can cause or worsen reflux. Not every hiatus hernia needs surgery.'),
                  ('Can I bring a recommendation from another hospital?','Yes. Bring the treatment recommendation and available reports for an in-person second opinion.')]),
}

CREDENTIAL_BAND = ('<section class="journey-section second-opinion-band"><div class="container journey-split"><div>'
    '<p class="journey-eyebrow">Already advised surgery?</p><h2>Get a second opinion from Dr. Bharti</h2>'
    '<p>Bring your reports and the recommendation you received. Understand your diagnosis, the options that may suit you and the questions to ask before deciding.</p></div>'
    '<div class="journey-card"><ul class="journey-list"><li><strong>MS General Surgery</strong>, PGIMER Chandigarh</li><li><strong>Senior residency</strong>, PGIMER and AIIMS Bhubaneswar</li>'
    '<li><strong>FMAS · FIAGES · FALS (Robotic)</strong> in minimal access surgery</li><li>Consultant at Samford Super Speciality Hospital, Ranchi</li></ul>'
    '<div class="journey-actions"><a class="journey-button" href="appointments.html?purpose=second_opinion#request">Request a second opinion</a>'
    '<a class="journey-button secondary" href="tel:+916206091982">Call 62060 91982</a></div></div></div></section>')

SYMPTOM_FINDER = [
 ('Pain in the upper right abdomen after meals','Possible gallbladder stones','gallbladder-stone-surgery-ranchi.html'),
 ('A bulge in the groin, at the navel or near an old scar','Possible hernia','hernia-surgery-ranchi.html'),
 ('Swollen, twisted leg veins or heavy, aching legs','Possible varicose veins','varicose-veins-treatment-ranchi.html'),
 ('Bleeding, pain or discharge around the anus','Piles, fissure or fistula','piles-fistula-surgery-ranchi.html'),
 ('Pain moving to the lower right abdomen with fever','Possible appendicitis — needs urgent hospital care','appendix-surgery-ranchi.html'),
 ('A swelling at the front of the neck','Thyroid swelling or nodule','thyroid-surgery-ranchi.html'),
 ('Heartburn, sour burps or food coming back up','Acid reflux or hiatus hernia','acid-reflux-surgery-ranchi.html'),
 ('Weight affecting your health','Obesity assessment and treatment','bariatric-surgery-ranchi.html'),
]

# Gallery: (full image, thumbnail, width, height, caption, group). Owner confirmed consent is on file.
GALLERY = [
 ('images/ot-laparoscopy-dr-bharti-1.jpg','images/thumb/ot-laparoscopy-dr-bharti-1.jpg','Dr. Vikeerna Bharti performing laparoscopic surgery','Dr. Bharti during laparoscopic surgery','theatre'),
 ('images/ot-laparoscopy-dr-bharti-2.jpg','images/thumb/ot-laparoscopy-dr-bharti-2.jpg','Dr. Vikeerna Bharti operating with laparoscopic instruments','Keyhole surgery in progress','theatre'),
 ('images/ot-surgical-team.jpg','images/thumb/ot-surgical-team.jpg','Dr. Vikeerna Bharti with the operating theatre team','With the operating theatre team','theatre'),
 ('images/ot-laparoscopy-dr-bharti-3.jpg','images/thumb/ot-laparoscopy-dr-bharti-3.jpg','Dr. Vikeerna Bharti operating through laparoscopic ports','Laparoscopic surgery through small ports','theatre'),
 ('images/ot-laparoscopy-tower.jpg','images/thumb/ot-laparoscopy-tower.jpg','Dr. Vikeerna Bharti during laparoscopic appendix surgery','Laparoscopic appendix surgery','theatre'),
 ('images/ot-laparoscopy-dr-bharti-4.jpg','images/thumb/ot-laparoscopy-dr-bharti-4.jpg','Dr. Vikeerna Bharti with an assistant during keyhole surgery','Teamwork during keyhole surgery','theatre'),
 ('images/ot-laparoscopy-dr-bharti-5.jpg','images/thumb/ot-laparoscopy-dr-bharti-5.jpg','Dr. Vikeerna Bharti in the operating theatre','In the operating theatre','theatre'),
 ('images/ot-instrument-trolley.jpg','images/thumb/ot-instrument-trolley.jpg','Instruments in use during an emergency laparotomy','During an emergency laparotomy','theatre'),
 ('images/gallery_surgical_laparoscopy_1.jpg','images/thumb/gallery_surgical_laparoscopy_1.jpg','Laparoscopic surgery in the operating theatre','Laparoscopic (keyhole) surgery','theatre'),
 ('images/gallery_surgical_ot_team_1.jpg','images/thumb/gallery_surgical_ot_team_1.jpg','Operating theatre team at Samford Hospital during laparoscopic surgery','Operating theatre team, Samford Hospital','theatre'),
 ('images/gallery_surgical_ot_team_2.jpg','images/thumb/gallery_surgical_ot_team_2.jpg','Surgical team in the operating theatre','Surgical team at work','theatre'),
 ('images/gallery_profile_samford_welcome.jpg','images/thumb/gallery_profile_samford_welcome.jpg','Samford Super Speciality Hospital welcome announcement for Dr. Vikeerna Bharti','Joining Samford Super Speciality Hospital, Ranchi','milestones'),
 ('images/gallery_conference_paras_recognition.jpeg','images/thumb/gallery_conference_paras_recognition.jpg','Dr. Vikeerna Bharti at Paras HEC Hospital, Ranchi','At Paras HEC Hospital, Ranchi','milestones'),
 ('images/gallery_personal_with_patient.jpg','images/thumb/gallery_personal_with_patient.jpg','Dr. Vikeerna Bharti with a patient at Samford Hospital','With a patient, Samford Hospital (shared with consent)','milestones'),
 ('images/gallery_media_garhwa_modular_ot_1.jpeg','images/thumb/gallery_media_garhwa_modular_ot_1.jpg','Newspaper report on the modular operation theatre opening in Garhwa','Modular operation theatre opens in Garhwa','news'),
 ('images/gallery_media_garhwa_modular_ot_2.jpeg','images/thumb/gallery_media_garhwa_modular_ot_2.jpg','Dainik Bhaskar report on the Garhwa operation theatre inauguration','Dainik Bhaskar: operation theatre inauguration, Garhwa','news'),
 ('images/gallery_media_free_camp_50.jpeg','images/thumb/gallery_media_free_camp_50.jpg','Prabhat Khabar report on a free medical camp in Garhwa','Prabhat Khabar: free medical camp, Garhwa (February 2021)','news'),
 ('images/gallery_media_health_camp_135.jpeg','images/thumb/gallery_media_health_camp_135.jpg','Newspaper report on a health camp in Garhwa','Health camp in Garhwa','news'),
 ('images/gallery_media_free_operation_camp.jpeg','images/thumb/gallery_media_free_operation_camp.jpg','Newspaper report on a free surgery camp','Free surgery camp','news'),
 ('images/gallery_media_sai_sushila_story.jpeg','images/thumb/gallery_media_sai_sushila_story.jpg','Newspaper feature on Sai Sushila Sishu Hospital community work','Sai Sushila Sishu Hospital: community health work','news'),
 ('images/gallery_media_varicose_vein_success.jpeg','images/thumb/gallery_media_varicose_vein_success.jpg','Newspaper report on varicose vein treatment by radiofrequency ablation at Samford Hospital','Newspaper report: varicose vein treatment with RFA, Samford Hospital','news'),
 ('images/gallery_media_vascular_surgery_saved_arm.jpeg','images/thumb/gallery_media_vascular_surgery_saved_arm.jpg','Newspaper report on emergency vascular surgery at Constant Lievens Hospital','Newspaper report: emergency vascular surgery, Constant Lievens Hospital','news'),
]
CLINIC_PHOTOS = [
 ('images/ranchi_dental_polyclinic.jpg',940,529,'Ranchi Dental and Polyclinic shopfront on Bariatu Road, Ranchi','Ranchi Dental and Polyclinic, Bariatu Road'),
 ('images/samford_hospital_building.jpg',880,495,'Samford Super Speciality Hospital building, Kokar, Ranchi','Samford Super Speciality Hospital, Kokar'),
 ('images/sai_sushila_hospital_garhwa.jpg',880,495,'Sai Sushila Sishu Hospital building in Garhwa','Sai Sushila Sishu Hospital, Garhwa'),
]
GARHWA_PHOTOS = [
 ('images/garhwa-ot-photo.jpg',720,540,'Operation theatre with laparoscopy equipment at Sai Sushila Sishu Hospital, Garhwa','Operation theatre with laparoscopy setup'),
 ('images/garhwa-anaesthesia-workstation.jpg',1200,900,'Anaesthesia workstation in the Garhwa operation theatre','Anaesthesia workstation'),
 ('images/garhwa-autoclave-photo.jpg',720,540,'Horizontal autoclave for sterilising surgical instruments in Garhwa','Instrument sterilisation (autoclave)'),
]
GOOGLE_PROFILE='https://www.google.com/maps/search/?api=1&amp;query=Dr.+Vikeerna+Bharti%2C+Bariatu+Road%2C+Ranchi&amp;query_place_id=ChIJxcKRJAbj9DkREUTv8FsVn08'
GOOGLE_REVIEW='https://search.google.com/local/writereview?placeid=ChIJxcKRJAbj9DkREUTv8FsVn08'
