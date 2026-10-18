"""Round 3 (10 Oct 2026): Hindi summaries (as on the original site, corrected), emergency surgery, live Google rating embed."""
from html import escape as e

INS_HI = 'सैमफोर्ड हॉस्पिटल में आयुष्मान भारत, राज्य कर्मी स्वास्थ्य बीमा योजना (RKSBY) और प्रमुख स्वास्थ्य बीमा/TPA से कैशलेस इलाज की सुविधा है (पात्रता अस्पताल का बीमा डेस्क तय करता है)।'
OPD_HI = 'परामर्श: बरियातू (मणिपाल हॉस्पिटल के पास) सोमवार–शनिवार सुबह 9–10 और शाम 5–7:30 बजे; सैमफोर्ड सुपर स्पेशियलिटी हॉस्पिटल, कोकर सुबह 11 से शाम 5 बजे। संपर्क: 62060 91982।'

HINDI = {
'index.html': ('रांची में जनरल एवं लैप्रोस्कोपिक सर्जन — डॉ. विकीर्ण भारती',
  'डॉ. विकीर्ण भारती रांची में पित्त की थैली, हर्निया, अपेंडिक्स और उपयुक्त मामलों में मोटापे तथा एसिड रिफ्लक्स की लैप्रोस्कोपिक (दूरबीन) सर्जरी करते हैं। वे बवासीर, फिशर, भगंदर और सौम्य थायराइड रोगों की सर्जरी तथा वेरिकोज वेन्स का RFA उपचार भी करते हैं। इलाज की विधि जांच के बाद तय होती है। ऑपरेशन सैमफोर्ड सुपर स्पेशियलिटी हॉस्पिटल, रांची में होते हैं। योग्यता: MS जनरल सर्जरी (PGIMER चंडीगढ़), FMAS, FIAGES, FALS (रोबोटिक)। सैमफोर्ड हॉस्पिटल में 24 घंटे आपातकालीन सर्जरी भी उपलब्ध है। ऑपरेशन की सलाह मिली है तो अपनी रिपोर्ट लेकर दूसरी राय (सेकंड ओपिनियन) के लिए आएँ। ' + OPD_HI + ' गढ़वा में आमतौर पर महीने के पहले और तीसरे रविवार को OPD होती है — तारीख 82641 03707 पर पूछें। ' + INS_HI),
'gallbladder-stone-surgery-ranchi.html': ('हिन्दी में सारांश — पित्त की थैली की पथरी का इलाज रांची में',
  'पित्त की थैली (गॉलब्लैडर) की पथरी में पेट के ऊपरी दाएँ हिस्से में दर्द, खासकर तला-भुना खाने के बाद, उल्टी या पेट फूलना हो सकता है। दवाइयों से पथरी आमतौर पर पूरी तरह खत्म नहीं होती; लक्षण होने पर दूरबीन विधि (लैप्रोस्कोपिक कोलेसिस्टेक्टॉमी) से पित्त की थैली निकालने का ऑपरेशन किया जाता है। डॉ. विकीर्ण भारती यह ऑपरेशन सैमफोर्ड सुपर स्पेशियलिटी हॉस्पिटल, रांची में करते हैं; अक्सर मरीज अगले दिन घर जा सकते हैं। बुखार, पीलिया या लगातार तेज दर्द हो तो तुरंत अस्पताल जाएँ। ' + INS_HI + ' ' + OPD_HI),
'hernia-surgery-ranchi.html': ('हिन्दी में सारांश — हर्निया का ऑपरेशन रांची में',
  'हर्निया पेट की दीवार की कमजोरी से बनने वाला उभार है, जो दवा या बेल्ट से ठीक नहीं होता। जांघ के जोड़ (इंगुइनल), नाभि (अम्बिलिकल), पुराने ऑपरेशन की जगह (इंसिज़नल) और दोबारा होने वाले हर्निया का इलाज दूरबीन विधि (TEP, TAPP, eTEP) या ओपन ऑपरेशन से मेश लगाकर किया जाता है। बड़े और जटिल हर्निया के लिए डॉ. विकीर्ण भारती सैमफोर्ड हॉस्पिटल, रांची में eTEP-RS, रिव्स-स्टोपा और TAR जैसी पेट की दीवार की रिकंस्ट्रक्शन सर्जरी भी करते हैं। अचानक तेज दर्द, उल्टी या उभार अंदर न जाए तो तुरंत अस्पताल जाएँ। ' + INS_HI + ' ' + OPD_HI),
'varicose-veins-treatment-ranchi.html': ('हिन्दी में सारांश — पैरों की फूली नसों (वेरिकोज वेन्स) का इलाज रांची में',
  'वेरिकोज वेन्स में पैरों की नसें नीली, फूली और टेढ़ी दिखती हैं, क्योंकि नसों के वाल्व कमजोर हो जाते हैं। इससे पैरों में भारीपन, दर्द, सूजन, खुजली और टखने के पास त्वचा पर कालापन आ सकता है। डॉपलर जांच के बाद डॉ. विकीर्ण भारती सैमफोर्ड हॉस्पिटल, रांची में रेडियोफ्रीक्वेंसी एब्लेशन (RFA) करते हैं — यह सुई के छेद से की जाने वाली प्रक्रिया है और आमतौर पर अगले दिन छुट्टी हो जाती है। नस से खून बहे या एक पैर में अचानक दर्दनाक सूजन हो तो तुरंत अस्पताल जाएँ। ' + INS_HI + ' ' + OPD_HI),
'piles-fistula-surgery-ranchi.html': ('हिन्दी में सारांश — बवासीर, फिशर और भगंदर का इलाज रांची में',
  'बवासीर (पाइल्स), फिशर (गुदा की अंदरूनी परत में छोटी दरार) और भगंदर (फिस्टुला) अलग-अलग बीमारियाँ हैं। बवासीर और फिशर के कुछ मामलों में खान-पान, फाइबर और दवाओं से राहत मिल सकती है। भगंदर में आमतौर पर ऑपरेशन की आवश्यकता होती है; तरीका जांच और फिस्टुला के रास्ते के अनुसार तय होता है। ज़रूरत होने पर डॉ. विकीर्ण भारती सैमफोर्ड हॉस्पिटल में हेमरॉइडेक्टॉमी, LIS (फिशर) और फिस्टुलेक्टॉमी जैसे ऑपरेशन करते हैं। मल में खून आने को हमेशा बवासीर न समझें — जांच करवाएँ। संकोच न करें, शुरुआती अवस्था में इलाज आसान होता है। ' + OPD_HI),
'appendix-surgery-ranchi.html': ('हिन्दी में सारांश — अपेंडिक्स का आपातकालीन ऑपरेशन',
  'दाहिनी ओर पेट के निचले हिस्से में तेज दर्द, बुखार, उल्टी और भूख न लगना अपेंडिसाइटिस (अपेंडिक्स की सूजन) के लक्षण हो सकते हैं। यह आपात स्थिति है — तुरंत अस्पताल जाएँ, WhatsApp के जवाब का इंतज़ार न करें। डॉ. विकीर्ण भारती सैमफोर्ड सुपर स्पेशियलिटी हॉस्पिटल, रांची में दिन-रात 24 घंटे आपातकालीन सर्जरी करते हैं, जिसमें दूरबीन विधि से अपेंडिक्स का ऑपरेशन भी शामिल है। ' + INS_HI),
'bariatric-surgery-ranchi.html': ('हिन्दी में सारांश — मोटापे की सर्जरी (बेरियाट्रिक) रांची में',
  'मोटापे की सर्जरी कोई कॉस्मेटिक इलाज नहीं है। यह उन वयस्क मरीजों के लिए है जिनका वजन बहुत अधिक है और जिन्हें डायबिटीज़, बीपी, नींद में सांस रुकना या जोड़ों की समस्या जैसी बीमारियाँ हैं। पूरी जांच के बाद डॉ. विकीर्ण भारती सैमफोर्ड हॉस्पिटल, रांची में दूरबीन विधि से स्लीव गैस्ट्रेक्टॉमी करते हैं; ओबेसिटी और मेटाबॉलिक क्लिनिक में ऑपरेशन के बाद लंबा फॉलो-अप, डाइट और विटामिन की देखरेख होती है। ' + OPD_HI),
'thyroid-surgery-ranchi.html': ('हिन्दी में सारांश — थायराइड और घेंघा का ऑपरेशन रांची में',
  'गले में सूजन या गांठ (घेंघा, थायराइड नोड्यूल) निगलते समय ऊपर-नीचे होती है। हर गांठ में ऑपरेशन की ज़रूरत नहीं होती; थायराइड ब्लड टेस्ट, अल्ट्रासाउंड और FNAC जांच के बाद फैसला होता है। ज़रूरत होने पर डॉ. विकीर्ण भारती सैमफोर्ड हॉस्पिटल में हेमीथायरॉइडेक्टॉमी या टोटल थायरॉइडेक्टॉमी करते हैं। थायराइड कैंसर के मरीजों को विशेषज्ञ कैंसर केंद्र भेजा जाता है। ' + OPD_HI),
'acid-reflux-surgery-ranchi.html': ('हिन्दी में सारांश — एसिडिटी (GERD) और हायटस हर्निया का इलाज',
  'सीने में जलन, खट्टी डकार और खाना ऊपर आना एसिडिटी (GERD) के लक्षण हैं; हायटस हर्निया में पेट का कुछ हिस्सा डायाफ्राम से ऊपर सीने में चला जाता है। अधिकतर मरीज दवा और खान-पान में बदलाव से ठीक रहते हैं। लंबे समय तक दवा लेने के बाद भी परेशानी रहे तो एंडोस्कोपी और अन्य जांच के बाद दूरबीन विधि से फंडोप्लिकेशन ऑपरेशन किया जा सकता है। सीने में तेज दर्द को एसिडिटी मानकर न टालें। ' + OPD_HI),
'blog.html': ('हिन्दी में सारांश — शोध और प्रकाशन',
  'डॉ. विकीर्ण भारती के शोध कार्य में द लैंसेट ग्लोबल हेल्थ में प्रकाशित GlobalSurg अध्ययन (सहयोगी), स्प्रिंगर पुस्तक में "प्रोलैप्स रेक्टम" अध्याय और हर्निया (eTEP तथा लम्बर हर्निया) पर शोध पत्र शामिल हैं। परामर्श के लिए बरियातू या सैमफोर्ड हॉस्पिटल, रांची में मिलें: 62060 91982।'),
'second-opinion-surgery-ranchi.html': ('हिन्दी में सारांश — ऑपरेशन से पहले दूसरी राय',
  'किसी अस्पताल में ऑपरेशन की सलाह मिली है और आप अनिश्चित हैं? अपनी पुरानी रिपोर्ट, अल्ट्रासाउंड/CT और डॉक्टर का पर्चा लेकर डॉ. विकीर्ण भारती से मिलें। बीमारी, ऑपरेशन की ज़रूरत, दूसरे विकल्प, जोखिम और खर्च पर खुलकर चर्चा होगी। ' + OPD_HI),
'emergency-surgery-ranchi.html': ('हिन्दी में सारांश — रांची में 24 घंटे आपातकालीन सर्जरी',
  'पेट में अचानक तेज दर्द, आंत में छेद (परफोरेशन), आंतों में रुकावट, हर्निया का फंस जाना, अपेंडिक्स, पित्त की थैली में सूजन या पस, दुर्घटना में पेट, छाती या खून की नसों (वैस्कुलर) की चोट — ऐसी आपात स्थिति में तुरंत अस्पताल पहुँचें। डॉ. विकीर्ण भारती सैमफोर्ड सुपर स्पेशियलिटी हॉस्पिटल, एच.बी. रोड, कोकर चौक, रांची में पूर्णकालिक (फुल टाइम) कार्यरत हैं और वहाँ ICU की सुविधा के साथ दिन-रात 24 घंटे आपातकालीन सर्जरी करते हैं, जहाँ संभव हो दूरबीन विधि से। WhatsApp के जवाब का इंतज़ार न करें। ' + INS_HI),
}

def hindi_section(file, tint=True):
    if file not in HINDI: return ''
    t, txt = HINDI[file]
    return (f'<section class="journey-section{" tint" if tint else ""} hindi-summary" id="hindi" lang="hi"><div class="container reading-width">'
            f'<h2>{e(t)}</h2><p>{e(txt)}</p></div></section>')

GOOGLE_EMBED = 'https://www.google.com/maps?q=Dr.+Vikeerna+Bharti,+Bariatu,+Ranchi&output=embed'
def review_embed(title='Dr. Vikeerna Bharti on Google Maps — rating, reviews and directions'):
    return (f'<div class="review-embed"><iframe src="{GOOGLE_EMBED}" title="{e(title, quote=True)}" loading="lazy" '
            'referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>'
            '<p class="journey-small">Google may show a rating card in this map. Its display varies by screen size and browser. Use “Read reviews on Google” to view the current rating and reviews.</p>')

EMERGENCIES = [
 ('Acute appendicitis', 'Including perforated appendix and appendicular abscess; laparoscopic appendicectomy where suitable.', 'appendix-surgery-ranchi.html'),
 ('Perforation and peritonitis', 'Perforated ulcer or bowel causing severe abdominal pain and infection inside the abdomen.', ''),
 ('Intestinal obstruction', 'Blocked bowel with pain, vomiting, swelling of the abdomen and inability to pass stool or gas.', ''),
 ('Obstructed or strangulated hernia', 'A painful hernia that will not go back, which can cut off the blood supply to the bowel.', 'hernia-surgery-ranchi.html'),
 ('Acute gallbladder problems', 'Acute cholecystitis and empyema of the gallbladder; jaundice or fever from bile-duct stones is assessed and treatment arranged.', 'gallbladder-stone-surgery-ranchi.html'),
 ('Abdominal and chest trauma', 'Injuries from road accidents, falls or assault — emergency laparotomy, chest drains and damage-control surgery when needed.', ''),
 ('Vascular emergencies and vascular trauma', 'Arterial injuries and sudden loss of blood supply to a limb (acute limb ischaemia), including embolectomy and vascular repair where suitable.', ''),
 ('Abscesses and severe infections', 'Perianal, breast and soft-tissue abscesses needing urgent drainage.', ''),
]
EMERGENCY_FAQ = [
 ('Is emergency surgery available at night in Ranchi?', 'Yes. Emergency assessment and surgery are available day and night at Samford Super Speciality Hospital, Kokar, Ranchi, where Dr. Vikeerna Bharti works full time and attends emergency operations, including appendix surgery at night. The hospital has anaesthesia and ICU support.'),
 ('What should I do in a surgical emergency?', 'Go directly to the emergency department of Samford Super Speciality Hospital or the nearest hospital. Do not wait for a website or WhatsApp reply. Bring previous reports and a list of medicines if you can.'),
 ('Can emergency operations be done by laparoscopy?', 'Many can, such as appendicectomy and some perforations, gallbladder and hernia emergencies. The surgeon chooses keyhole or open surgery depending on your condition and what is safest.'),
 ('Is insurance or Ayushman Bharat accepted for emergency surgery?', 'At Samford Super Speciality Hospital, cashless treatment is available under major health-insurance and TPA plans, Ayushman Bharat and the Jharkhand Rajya Karmi Swasthya Bima Yojana, subject to eligibility confirmed by the hospital.'),
 ('Which symptoms need emergency surgical care?', 'Sudden severe abdominal pain, pain with fever or repeated vomiting, a swollen tight abdomen, a painful hernia that will not go back, yellow eyes with fever, vomiting blood, injuries to the abdomen or chest, or a limb that suddenly becomes painful, cold, pale or numb.'),
]

def emergency_body():
    cards = ''.join(f'<article class="journey-card"><h3>{e(t)}</h3><p>{e(d)}</p>' + (f'<a class="journey-textlink" href="{h}">Read more →</a>' if h else '') + '</article>' for t, d, h in EMERGENCIES)
    faqs = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in EMERGENCY_FAQ)
    return ('<section class="journey-section"><div class="container"><aside class="journey-warning"><strong>In an emergency, go straight to hospital.</strong>'
            '<p>Go to the emergency department of Samford Super Speciality Hospital, H.B. Road, Kokar Chowk, Ranchi, or the nearest hospital. Do not wait for a website or WhatsApp reply.</p>'
            '<div class="journey-actions"><a class="journey-button" href="https://www.google.com/maps/search/?api=1&amp;query=Samford+Super+Speciality+Hospital%2C+Ranchi&amp;query_place_id=ChIJxRR62Ujj9DkRYOJ-v25p1OU" target="_blank" rel="noopener" data-location="samford">Directions to Samford ↗</a>'
            '<a class="journey-button secondary" href="tel:+916206091982">Call Dr. Bharti: 62060 91982</a></div><p class="journey-small">Do not wait for a call back before seeking emergency care.</p></aside></div></section>'
            '<section class="journey-section tint" id="emergencies"><div class="container"><h2>Surgical emergencies treated 24/7</h2>'
            '<p class="section-intro">Dr. Bharti works full time at Samford Super Speciality Hospital, where emergency assessment and surgery are available day and night with anaesthesia and ICU support. Keyhole or open surgery is chosen according to the condition, and specialist referral is arranged when it is needed.</p>'
            f'<div class="journey-grid">{cards}</div></div></section>'
            '<section class="journey-section"><div class="container"><h2>In the operating theatre</h2><div class="photo-row ot-row">'
            '<figure class="clinic-photo"><img src="images/ot-instrument-trolley.jpg" width="1050" height="1400" loading="lazy" alt="Instruments in use during an emergency laparotomy"><figcaption>During an emergency laparotomy</figcaption></figure>'
            '<figure class="clinic-photo"><img src="images/ot-surgical-team.jpg" width="1400" height="1050" loading="lazy" alt="Dr. Vikeerna Bharti with the operating theatre team"><figcaption>With the operating theatre team</figcaption></figure>'
            '</div></div></section>'
            '<section class="journey-section" id="page-faq"><div class="container reading-width"><h2>Emergency surgery: common questions</h2>'
            f'<div class="journey-faq">{faqs}</div></div></section>')

EMERGENCY_HOME = ('<section class="journey-section emergency-band" id="emergency"><div class="container journey-split"><div><p class="journey-eyebrow">24/7 at Samford Super Speciality Hospital</p>'
    '<h2>Emergency surgery, day and night</h2><p>Dr. Bharti works full time at Samford Super Speciality Hospital, Kokar, Ranchi, and attends general surgical emergencies there day and night, including abdominal, chest and vascular trauma, with ICU support. Treatment depends on the condition and the team’s assessment.</p>'
    '<p><strong>In an emergency, go straight to the hospital.</strong> Do not wait for a WhatsApp reply.</p>'
    '<div class="journey-actions"><a class="journey-button" href="emergency-surgery-ranchi.html">Emergency surgery details</a><a class="journey-button secondary" href="https://www.google.com/maps/search/?api=1&amp;query=Samford+Super+Speciality+Hospital%2C+Ranchi&amp;query_place_id=ChIJxRR62Ujj9DkRYOJ-v25p1OU" target="_blank" rel="noopener" data-location="samford">Directions to Samford ↗</a></div></div>'
    '<div class="journey-card"><h3>Common surgical emergencies</h3><ul class="journey-list">' + ''.join(f'<li>{e(t)}</li>' for t, _, _ in EMERGENCIES) + '</ul></div></div></section>')
