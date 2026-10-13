"""Original-site content restored page by page (10 October 2026, Claude build round 2).

Source: the live September 2026 site (sections and every FAQ question), corrected for
accuracy. Owner confirmations used: 24/7 emergency surgery at Samford including night
appendix operations; RFA usually next-day discharge; Dr. Bharti does NOT operate on thyroid
cancer; planned laparoscopic cases usually go home the next day.
Removed from the originals: unsourced percentages, "painless / no scar / no incision",
"only definitive", "safe" promises, superlatives and the unsupported professional title.
"""
CALL = 'Call 62060 91982.'
SAMFORD_OPD = 'Samford Super Speciality Hospital, Kokar Chowk (Mon–Sat 11 AM–5 PM)'
BARIATU_OPD = 'Ranchi Dental and Polyclinic, Bariatu (Mon–Sat 9–10 AM and 5–7:30 PM)'
INS = 'Cashless treatment is available at Samford under major health-insurance and TPA plans, Ayushman Bharat and the Jharkhand Rajya Karmi Swasthya Bima Yojana; the hospital insurance desk confirms eligibility.'
COST = 'The cost depends on the hospital room category, anaesthesia and theatre charges, investigations, the complexity of your case and any insurance or scheme approval. A clear estimate is given after examination and review of your reports. ' + INS

# Page-specific detail sections: (id, eyebrow, title, paragraphs, bullets)
DETAILS = {
'gallbladder-stone-surgery-ranchi.html': [
 ('treatment','The standard treatment','Laparoscopic cholecystectomy',
  ['For gallstones that cause symptoms, removal of the gallbladder (cholecystectomy) is the recommended treatment, and today it is usually done by the laparoscopic (keyhole) method.',
   'Dr. Bharti makes three or four small cuts of 5–10 mm. A camera and fine instruments are passed through them, the gallbladder is separated from the liver and bile ducts, and it is removed through one of the small cuts. Open surgery is used when the findings make keyhole surgery unsafe.'],
  ['Is life normal without a gallbladder? Yes. The liver keeps making bile, which then flows directly into the intestine. Most people have no long-term restriction on diet after recovery.']),
],
'hernia-surgery-ranchi.html': [
 ('types','Where hernias occur','Types of hernia',
  ['Hernias are named by where they appear on the abdominal wall.'],
  ['Inguinal hernia: in the groin; the most common type, especially in men',
   'Femoral hernia: just below the groin crease, more common in women; has a higher risk of getting trapped, so repair is usually advised',
   'Umbilical hernia: at the belly button; common after pregnancy or with excess weight',
   'Ventral or epigastric hernia: in the midline between the breastbone and the navel',
   'Incisional hernia: at the scar of a previous operation',
   'Recurrent hernia: a hernia that has come back after an earlier repair',
   'Lumbar hernia: an uncommon hernia at the side or back of the abdomen']),
 ('repairs','How hernias are repaired','Laparoscopic hernia repair and abdominal wall reconstruction',
  ['TEP and TAPP: for groin hernias, the repair is done through three small keyholes from behind the abdominal wall. The hernia is reduced and a mesh is placed to cover the whole weak area; abdominal pressure then holds the mesh flat.',
   'eTEP (extended-view totally extraperitoneal repair): the surgeon works in the space between the muscle layers without entering the abdominal cavity, which allows a large mesh to reinforce wide defects such as incisional hernias without mesh touching the bowel.',
   'Rives–Stoppa and eTEP-RS: the mesh is placed behind the rectus (six-pack) muscles after the defect is closed; eTEP-RS does this through keyholes.',
   'Abdominal wall reconstruction and TAR: for large, complex or recurrent incisional hernias, transversus abdominis release (TAR) frees a deep muscle layer so that the abdominal wall can be closed and a large mesh placed behind the muscles.',
   'Dr. Bharti performs open and laparoscopic hernia repair, including TEP, TAPP, eTEP, eTEP-RS, Rives–Stoppa, IPOM and TAR, at Samford Super Speciality Hospital. The method is chosen after examination, scans and your previous surgical history.'],
  []),
],
'varicose-veins-treatment-ranchi.html': [
 ('cause','Why they form','Why varicose veins develop: valve failure explained',
  ['Leg veins carry blood upward to the heart against gravity. Small one-way valves inside them stop the blood from falling back down.',
   'When these valves weaken, blood leaks backward and pools in the lower leg. This is called venous reflux. The raised pressure stretches the veins, so they bulge and twist, and pushes fluid and pigment into the skin. Because damaged valves do not repair themselves, varicose veins tend to slowly worsen unless the faulty vein is treated.'],
  ['Bulging veins that become more prominent over time','Brown discolouration around the ankle','Pain, heaviness and swelling after standing','Itching, eczema and, in advanced cases, ulcers']),
 ('rfa','The procedure','How radiofrequency ablation (RFA) is done, step by step',
  ['Dr. Bharti performs RFA at Samford Super Speciality Hospital in the operation theatre, under ultrasound guidance and local anaesthesia. RFA is a modern alternative to open vein stripping and is comparable to laser (EVLT) treatment.'],
  ['Ultrasound mapping: the faulty vein is located and marked',
   'Needle puncture and sheath: the vein is entered through a needle puncture instead of a surgical cut',
   'Catheter placement: a fine RFA catheter is passed along the vein',
   'Controlled heating: radiofrequency energy seals the vein from inside, segment by segment; blood flow continues through healthy deep veins',
   'Time and stay: the treatment usually takes 45–60 minutes, and patients usually go home the next day']),
],
'piles-fistula-surgery-ranchi.html': [
 ('piles','Piles (haemorrhoids)','Piles treatment in Ranchi',
  ['Piles are swollen blood vessels in and around the anus. They are very common, yet many people delay seeing a doctor out of embarrassment. A consultation is private and examination is done with care.',
   'Early piles often settle with fibre, fluids and medicines. For larger (grade 3–4) piles, or piles that have not improved with other treatment, Dr. Bharti performs open haemorrhoidectomy, the surgical removal of the piles. Recovery usually takes two to four weeks with wound care.'],
  ['Bright red bleeding during or after passing stool','Pain, burning or itching around the anus','A lump coming out of the anus that may need to be pushed back','A feeling of incomplete emptying']),
 ('fistula','Anal fistula','Fistula treatment (fistulectomy)',
  ['An anal fistula is a small tunnel between the anal canal and the skin, usually after an abscess. It causes repeated discharge, itching and infections and rarely heals on its own.',
   'Dr. Bharti performs fistulectomy, removal of the fistula tract, and other sphincter-preserving techniques such as a seton or an advancement flap when the tract involves more muscle. Protecting bowel control is a priority in every fistula operation.'],
  []),
 ('fissure','Anal fissure','Fissure treatment (lateral internal sphincterotomy)',
  ['A chronic anal fissure is a tear in the anal lining that causes sharp pain during and after passing stool, often with a little bleeding. A tight anal muscle stops it from healing.',
   'Many fissures heal with stool softeners and prescribed ointments. When they do not, lateral internal sphincterotomy (LIS) relaxes the muscle so that the fissure can heal.'],
  []),
],
'bariatric-surgery-ranchi.html': [
 ('procedure','The procedure','Laparoscopic sleeve gastrectomy',
  ['Bariatric (obesity or metabolic) surgery is considered when diet, exercise and medical treatment have not given lasting results. It is a medical treatment, not a cosmetic one, and it needs a lifelong commitment to diet, vitamins, activity and follow-up.',
   'In sleeve gastrectomy, about three-quarters of the stomach is removed through keyholes, leaving a narrow, banana-shaped tube. This limits how much can be eaten at one time and lowers hunger hormones. Dr. Bharti performs laparoscopic sleeve gastrectomy as the primary surgeon and runs the obesity and metabolic clinic at Samford Super Speciality Hospital.'],
  ['Done through small keyhole cuts under general anaesthesia','Operation usually takes one to two hours','Hospital stay is usually two to three days','The change is permanent; the removed part of the stomach cannot be restored']),
 ('eligibility','Who is considered','Who is considered for bariatric surgery?',
  ['Suitability is decided individually after medical, nutritional and anaesthetic assessment. As a general guide, Asian guidelines consider adults with a BMI of 37.5 or above, or 32.5 or above with conditions such as type 2 diabetes or high blood pressure.',
   'The assessment also looks at how long the weight problem has been present, earlier weight-loss attempts, readiness for change and the ability to attend long-term follow-up.'],
  []),
 ('improvement','What may change','Possible health improvements',
  ['In carefully selected patients, bariatric surgery is associated with weight loss and improvement in weight-related conditions. Results vary between people and depend on following the diet and follow-up plan.'],
  ['Weight: loss of excess weight over 12–18 months, varying between individuals','Type 2 diabetes: blood sugar control may improve; surgery is not a cure','Blood pressure and cholesterol may improve with weight loss','Sleep apnoea and snoring often improve']),
],
'appendix-surgery-ranchi.html': [
 ('treatment','Treatment','Laparoscopic appendicectomy',
  ['Dr. Bharti usually removes the inflamed appendix by laparoscopic appendicectomy through three small cuts. The operation commonly takes 30–45 minutes. An open operation is used when the findings make it safer.'],
  ['Small cuts instead of one larger incision','Less pain after surgery and a lower wound-infection rate','Usually home in 24–48 hours','Light activities in about a week']),
 ('emergency','Emergencies','24/7 emergency surgery at Samford',
  ['Appendicitis can happen at any hour. Dr. Bharti attends emergency surgery, including appendix operations at night, at Samford Super Speciality Hospital, Kokar Chowk, Ranchi. Go directly to hospital for urgent assessment; do not wait for a WhatsApp reply.',
   'If you have severe pain in the lower right abdomen with fever, a sudden worsening of pain or a hard, very tender abdomen, go to the hospital emergency immediately. Do not take painkillers and wait.'],
  []),
],
'thyroid-surgery-ranchi.html': [
 ('conditions','When surgery is considered','Thyroid conditions that may need an operation',
  ['Many thyroid problems are treated with medicines or only need monitoring. Surgery is considered for some conditions.'],
  ['Goitre (enlarged thyroid) causing pressure, difficulty swallowing or breathing, or a visible swelling',
   'Thyroid nodules that are large, growing, or need removal for diagnosis',
   'Multinodular goitre: several nodules enlarging the gland',
   'Over-active thyroid (for example Graves disease) not controlled by medicines']),
 ('types','The operation','Types of thyroid surgery',
  ['Dr. Bharti performs hemithyroidectomy and total thyroidectomy for benign thyroid disease. He does not operate on thyroid cancer; if tests suggest cancer, he will explain the findings and refer you to a specialist cancer centre.'],
  ['Hemithyroidectomy (lobectomy): removal of one half of the gland','Total thyroidectomy: removal of the whole gland, followed by lifelong thyroid hormone tablets','Hospital stay is usually one to two days']),
],
'acid-reflux-surgery-ranchi.html': [
 ('surgery','When surgery is advised','When is surgery considered for acid reflux?',
  ['Most people with acid reflux improve with medicines and changes in eating habits. Surgery is considered after endoscopy and other tests for selected patients:'],
  ['Symptoms not controlled by regular medicines','A hiatus hernia causing reflux','Complications such as severe oesophagitis','Patients who, after discussion, prefer an operation to lifelong tablets and are suitable for it']),
 ('fundoplication','The operation','Laparoscopic fundoplication',
  ['In laparoscopic Nissen fundoplication, the upper part of the stomach is wrapped around the lower end of the food pipe to strengthen the valve between them. A hiatus hernia, if present, is repaired in the same operation. It is done through four or five small cuts, with a hospital stay of usually two to three days.',
   'Many patients are able to reduce or stop acid tablets after recovery, but results vary and some people still need medicines.'],
  []),
],
}

# Recovery timeline: list of (label, text)
RECOVERY = {
'gallbladder-stone-surgery-ranchi.html':[('Hospital stay','Planned laparoscopic gallbladder surgery usually means going home the next day.'),('Walking','Most patients sit up and walk a few hours after waking from anaesthesia.'),('Food','Light liquids on the evening of surgery, soft low-fat food (dal, khichdi, boiled rice) for the first one to two weeks, then a normal diet.'),('Work','Light desk work and daily activities after about 5–7 days; avoid heavy lifting for 4–6 weeks.')],
'hernia-surgery-ranchi.html':[('Hospital stay','Planned laparoscopic hernia repair usually means going home the next day; large or complex repairs need longer.'),('Walking','Walking starts the same evening; stairs and light chores within about two days.'),('Work','Desk work after about 5–7 days.'),('Lifting','Avoid lifting more than 5 kg and strenuous abdominal exercise for 4–6 weeks.')],
'varicose-veins-treatment-ranchi.html':[('Hospital stay','After RFA, patients usually go home the next day.'),('Walking','Walking is encouraged on the day of treatment.'),('After treatment','Some soreness, bruising or tightness along the treated vein is common for a few days; compression advice depends on your treatment.'),('Activity','Most routine activities resume within a few days; follow your discharge advice on travel and exercise.')],
'piles-fistula-surgery-ranchi.html':[('Hospital stay','Planned piles, fissure or fistula surgery usually means going home the next day.'),('Pain','Pain is managed with medicines; warm sitz baths help.'),('Diet','A fibre-rich diet and plenty of water keep stools soft and help healing.'),('Work','Desk work after one to two weeks; full recovery in three to four weeks.')],
'bariatric-surgery-ranchi.html':[('Hospital stay','Usually two to three days.'),('Diet','Liquids first, then purées, then soft food over several weeks, with smaller portions.'),('Activity','Walking from the first day; desk work after about two to three weeks.'),('Follow-up','Reviews at about 1 week, 1, 3, 6 and 12 months and then yearly, with blood tests and vitamin supplements.')],
'appendix-surgery-ranchi.html':[('Hospital stay','After laparoscopic appendicectomy, usually 24–48 hours; longer if the appendix had burst.'),('Activity','Light activities in 5–7 days; full activity in 2–3 weeks.'),('Wound care','Keep the small wounds clean and dry and attend your follow-up visit.')],
'thyroid-surgery-ranchi.html':[('Hospital stay','Usually one to two days.'),('Voice','The voice may be slightly hoarse for a few days and usually settles.'),('Tablets','Lifelong thyroid hormone tablets after total thyroidectomy; checked at follow-up after hemithyroidectomy.'),('Activity','Normal activities in one to two weeks.')],
'acid-reflux-surgery-ranchi.html':[('Hospital stay','Usually two to three days.'),('Diet','Soft food for four to six weeks while the repair heals; eat slowly and chew well.'),('Work','Office work after two to three weeks; full activity in four to six weeks.')],
}

WHY = ['MS General Surgery from PGIMER Chandigarh',
       'Senior residency in general surgery at PGIMER Chandigarh and AIIMS Bhubaneswar, with complex gastrointestinal and emergency cases',
       'FMAS, FIAGES and FALS (Robotic) fellowships in minimal access surgery',
       'Operates at Samford Super Speciality Hospital, Ranchi, with 24/7 emergency surgery, ICU support and cashless insurance and Ayushman Bharat',
       'Consultations at Bariatu and Samford in Ranchi, and a visiting OPD at Sai Sushila Sishu Hospital, Garhwa']
# Theatre photo beside "Why patients consult"; placement checked by Dr. Bharti, 12 Oct 2026.
# Pages without a matching operation photo have none (team and laparotomy photos are on the emergency page).
PHOTO = {
'gallbladder-stone-surgery-ranchi.html':('images/ot-laparoscopy-dr-bharti-4.jpg','Dr. Vikeerna Bharti during keyhole surgery'),
'hernia-surgery-ranchi.html':('images/ot-laparoscopy-dr-bharti-3.jpg','Dr. Vikeerna Bharti performing laparoscopic surgery'),
'bariatric-surgery-ranchi.html':('images/ot-laparoscopy-dr-bharti-2.jpg','Dr. Vikeerna Bharti during laparoscopic surgery'),
'appendix-surgery-ranchi.html':('images/ot-laparoscopy-tower.jpg','Dr. Vikeerna Bharti during laparoscopic appendix surgery'),
'acid-reflux-surgery-ranchi.html':('images/ot-laparoscopy-dr-bharti-5.jpg','Dr. Vikeerna Bharti in the operating theatre'),
}

# Original-site disease graphics and RFA result, restored as they were (owner approved 12 Oct 2026;
# written consent on file for the before/after photograph). page: (heading, [(src, width, height, alt, caption, diagram)])
# 12 Oct: RFA technique graphic corrected at owner's request; individual recovery advice replaces absolute claims.
FIGURES = {
'gallbladder-stone-surgery-ranchi.html':('Gallbladder surgery explained in a diagram',[('images/gallbladder-stone-disease-infographic.jpg',1000,1249,'Diagram of gallstones, common symptoms and laparoscopic gallbladder removal','Gallbladder stone disease: symptoms, cause, treatment and recovery',True)]),
'hernia-surgery-ranchi.html':('Hernia repair explained in a diagram',[('images/hernia-disease-infographic.jpg',1000,750,'Diagram showing an abdominal wall hernia and repair options','How a hernia forms, its common signs and treatment',True)]),
'bariatric-surgery-ranchi.html':('Sleeve gastrectomy explained',[('images/bariatric-sleeve-gastrectomy-infographic.jpg',1000,750,'Diagram comparing the stomach before and after sleeve gastrectomy','Sleeve gastrectomy: how it works and who may be considered',True)]),
'varicose-veins-treatment-ranchi.html':('Varicose veins treatment with RFA, explained',[('images/varicose-rfa-before-after.jpg',1200,675,'Varicose veins before and after RFA treatment: clinical photographs of one patient','Before and after Radiofrequency Ablation (RFA): actual clinical photographs of the same patient treated by Dr. Vikeerna Bharti, shown with the patient’s written consent. Individual results may vary.',False),('images/varicose-rfa-technique-infographic.jpg',1055,1491,'Diagram of radiofrequency ablation (RFA) for varicose veins: an ultrasound-guided catheter closes the faulty vein','How RFA treats a faulty vein. Soreness and small marks can occur; compression and recovery advice depend on your treatment.',True)]),
}

# Research links shown under the procedures list.
RESEARCH = {
'hernia-surgery-ranchi.html':'Read Dr. Bharti’s co-authored research on <a href="blog-post-etep.html">eTEP hernia repair</a> and <a href="blog-post-lumbar-hernia.html">laparoscopic repair of primary lumbar hernia</a>. Published research does not predict an individual patient’s result.',
}

# Every original FAQ question, with corrected answers.
FAQS = {
'gallbladder-stone-surgery-ranchi.html':[
 ('What is the cost of gallbladder stone surgery in Ranchi?', COST),
 ('Stomach pain after eating fatty food — what is it?','Pain in the upper right abdomen that starts or worsens after oily or heavy food is a common symptom of gallbladder stones; it can spread to the back or right shoulder. Acidity and other conditions can feel similar, so an ultrasound is needed to confirm the cause.'),
 ('Can gallstones be treated without surgery?','Medicines and diet changes may ease symptoms for a while but do not reliably dissolve or remove gallbladder stones. Once stones cause symptoms, removing the gallbladder is the standard treatment to prevent complications. Stones found by chance without symptoms often do not need an operation.'),
 ('Is gallbladder surgery risky?','Laparoscopic cholecystectomy is one of the most commonly performed operations. Like any operation it has risks, including bleeding, infection, bile leak and, rarely, bile-duct injury. Dr. Bharti explains the benefits and risks for your situation before you decide.'),
 ('How long is the hospital stay after gallbladder surgery?','After planned laparoscopic gallbladder removal, most patients go home the next day. Inflamed or complicated gallbladders may need a longer stay.'),
 ('What to eat after gallbladder surgery?','Start with light, low-fat food such as dal, khichdi and boiled rice for the first one to two weeks, then return gradually to a normal balanced diet. The liver continues to make bile, so most people have no long-term diet restriction.'),
 ('What is a difficult gallbladder or acute cholecystitis?','Acute cholecystitis is inflammation of the gallbladder, often because a stone blocks its outlet. It causes constant pain, fever and tenderness and can make surgery more complex. It needs prompt hospital assessment, and early laparoscopic surgery is often advised.'),
 ('Can gallbladder stones come back after surgery?','Stones cannot form again in the gallbladder because it is removed. Rarely, stones can form or be found later in the bile duct, which is treated separately.'),
 ('What is the difference between open and laparoscopic cholecystectomy?','Open surgery uses one larger cut. Laparoscopic (keyhole) surgery uses three or four small cuts of 5–10 mm for a camera and instruments, usually with less pain, smaller scars and a quicker recovery. Occasionally a keyhole operation is converted to open surgery for safety.'),
 ('Which doctor should I consult for gallbladder stones in Ranchi?','Gallbladder stones are treated by a general or laparoscopic surgeon. Dr. Vikeerna Bharti consults at '+BARIATU_OPD+' and '+SAMFORD_OPD+'. Bring your ultrasound report. '+CALL)],
'hernia-surgery-ranchi.html':[
 ('What is the cost of hernia operation in Ranchi?', COST),
 ('Lump in groin when standing — is it a hernia?','A groin swelling that appears on standing, straining or coughing and goes back when lying down is often an inguinal hernia. Other swellings can look similar, so an examination is needed. A hernia does not heal by itself.'),
 ('How long does hernia surgery take?','A laparoscopic groin hernia repair usually takes about 45–90 minutes; complex abdominal-wall repairs take longer. After planned laparoscopic repair, most patients go home the next day.'),
 ('Is laparoscopic hernia surgery better than open surgery?','Keyhole repair usually means smaller cuts, less pain and a quicker return to activity. Open repair or abdominal wall reconstruction may be better for some large, complex or recurrent hernias, and for some patients who cannot have general anaesthesia. The choice depends on your hernia and health.'),
 ('Can a hernia come back after surgery?','Recurrence after modern mesh repair is uncommon but possible. Careful technique, healthy weight, stopping smoking and avoiding heavy lifting while healing reduce the risk. A recurrent hernia can be repaired again, often using a different approach.'),
 ('What is umbilical hernia repair?','It closes the defect at the belly button, with a mesh when the size of the defect requires it. It can be done open or laparoscopically.'),
 ('What is abdominal wall reconstruction (AWR)?','AWR is used for large, complex or recurrent abdominal-wall hernias. The muscle layers are released and moved so that the gap can be closed, and a reinforcing mesh is placed.'),
 ('What is component separation or TAR?','Transversus abdominis release (TAR) is a type of component separation. It releases the innermost side muscle layer, creating space to close a large defect without tension and to place a large mesh behind the muscles. Dr. Bharti performs TAR at Samford Super Speciality Hospital when the assessment supports it.'),
 ('When should I consult a surgeon for an abdominal bulge?','Arrange an assessment when you notice a new bulge. The surgeon can discuss whether and when repair is appropriate. A painful, firm bulge that does not go back, especially with vomiting, needs emergency hospital assessment.'),
 ('Which doctor treats hernia in Ranchi?','Hernias are repaired by general and laparoscopic surgeons; they do not resolve with medicines or a belt. Dr. Vikeerna Bharti performs TEP, TAPP, eTEP, eTEP-RS, Rives–Stoppa, IPOM, open repair and TAR, and consults at '+BARIATU_OPD+' and '+SAMFORD_OPD+'. '+CALL)],
'varicose-veins-treatment-ranchi.html':[
 ('Swollen, twisted veins on the legs — what is the treatment in Ranchi?','These are usually varicose veins caused by leaking valves. After examination and a venous Doppler scan, treatment may include compression, radiofrequency ablation (RFA), foam sclerotherapy or surgery. Dr. Vikeerna Bharti performs RFA at Samford Super Speciality Hospital, Ranchi. '+CALL),
 ('Is varicose vein RFA treatment painful?','RFA is done under local anaesthesia. Most patients feel the anaesthetic injections and a mild warmth or pressure; some soreness or bruising is common for a few days afterwards.'),
 ('Is RFA done without a surgical cut?','RFA is usually performed through a small puncture or access opening and a thin sheath; additional vein procedures may need small incisions. The puncture is covered with a small dressing.'),
 ('Will there be a scar after varicose vein treatment?','RFA leaves only small puncture marks, which usually fade over time. Open vein surgery leaves small scars at the incision sites.'),
 ('Can I go home the same day after varicose vein treatment?','After RFA at Samford, patients usually go home the next day. You can walk on the day of treatment.'),
 ('Do I need to wear compression stockings after RFA?','Many patients wear stockings for a short period after treatment. Whether and how long you need them depends on your treatment and findings; your surgeon will advise you.'),
 ('What is the cost of varicose vein treatment in Ranchi?','The cost depends on which veins are affected, one or both legs, the procedure and consumables, and the hospital stay. An estimate is given after examination and a venous Doppler scan. '+INS),
 ('Can varicose veins come back after RFA?','The treated vein usually stays closed, but new varicose veins can develop over the years, and some patients need further treatment. Staying active, keeping a healthy weight and attending follow-up help.'),
 ('Are varicose veins dangerous if left untreated?','Many varicose veins cause only symptoms, but they can progress to skin darkening, swelling, eczema, ulcers or bleeding, and sometimes to blood clots. Assessment helps decide whether and when treatment is needed.'),
 ('पैरों की फूली नसों (वेरिकोज वेन्स) का इलाज रांची में कहाँ होता है?','डॉ. विकीर्ण भारती रांची के सैमफोर्ड सुपर स्पेशियलिटी हॉस्पिटल, कोकर चौक में डॉपलर जांच के बाद वेरिकोज वेन्स का रेडियोफ्रीक्वेंसी एब्लेशन (RFA) करते हैं। इसमें सर्जिकल चीरे की जगह सुई से नस तक पहुँचा जाता है और आमतौर पर अगले दिन छुट्टी मिल जाती है। संपर्क: 62060 91982।'),
 ('Which doctor treats varicose veins in Ranchi?','Varicose veins are treated by surgeons who perform vein procedures. Dr. Vikeerna Bharti, a general and laparoscopic surgeon, performs RFA and vein surgery at Samford Super Speciality Hospital and consults at '+BARIATU_OPD+' and '+SAMFORD_OPD+'. Bring any venous Doppler report. '+CALL)],
'piles-fistula-surgery-ranchi.html':[
 ('What is the cost of piles surgery in Ranchi?', COST),
 ('Bleeding during bowel movements — what to do?','Bright red bleeding during or after stool is often caused by piles or a fissure, but other conditions can cause it, so do not self-treat for long. See a surgeon for examination, especially if there is weight loss, a change in bowel habit or a family history of bowel cancer.'),
 ('Is piles surgery painful?','The operation is done under anaesthesia, so you do not feel pain during it. Pain afterwards is expected and is managed with medicines, sitz baths and soft stools.'),
 ('Can a fistula heal without surgery?','An anal fistula rarely heals on its own and usually needs surgery. The operation is planned to remove or open the tract while protecting the muscles that control bowel movements.'),
 ('What is the difference between piles and fistula?','Piles are swollen blood vessels that cause bleeding or a lump. A fistula is a small tunnel from inside the anal canal to the skin, causing discharge and repeated boils. They are different conditions with different treatments.'),
 ('How long is recovery after piles surgery?','Most planned cases go home the next day. Desk work is usually possible after one to two weeks and full recovery takes three to four weeks. A high-fibre diet and plenty of water help healing.'),
 ('Which doctor should I see for piles, fissure or fistula in Ranchi?','These conditions are treated by a general surgeon. Many early cases settle with diet and medicines, so an operation is not always the first step. Dr. Vikeerna Bharti consults at '+BARIATU_OPD+' and '+SAMFORD_OPD+'. '+CALL),
 ('Is laser treatment better for piles or fistula?','Laser is one technique for selected cases. It is not suitable for every patient, and recurrence can occur with any method. Ask which technique is proposed for your condition and why.')],
'bariatric-surgery-ranchi.html':[
 ('What is the cost of bariatric surgery in Ranchi?','The cost depends on the hospital stay, anaesthesia, investigations, nutrition and follow-up care and the complexity of your case. A clear estimate is given after assessment. Insurance cover for bariatric surgery varies by policy; the Samford insurance desk can check your eligibility.'),
 ('Is bariatric surgery available in Ranchi?','Yes. Dr. Vikeerna Bharti performs laparoscopic sleeve gastrectomy at Samford Super Speciality Hospital, Ranchi, for carefully assessed patients, with a structured obesity and metabolic clinic for preparation and follow-up.'),
 ('Who is a suitable candidate for bariatric surgery?','Suitability is decided after a full assessment. As a general guide for Asian adults, a BMI of 37.5 or above, or 32.5 or above with conditions such as type 2 diabetes or high blood pressure, may be considered.'),
 ('Does sleeve gastrectomy cure diabetes?','It does not cure diabetes. In some patients with obesity and type 2 diabetes, blood sugar control improves and medicine needs reduce after surgery; the degree of improvement varies.'),
 ('How long does sleeve gastrectomy take?','The operation usually takes one to two hours, with a hospital stay of two to three days. Desk work is usually possible after two to three weeks.'),
 ('Is the surgery reversible?','No. The removed part of the stomach cannot be put back, which is discussed carefully before deciding.'),
 ('What follow-up is needed after bariatric surgery?','Regular reviews, vitamin and mineral supplements, diet monitoring and lifestyle support for at least two years, with reviews at about 1 week, 1, 3, 6 and 12 months and then yearly.'),
 ('What is recovery like after sleeve gastrectomy?','Food moves from liquids to purées to soft food over several weeks. Walking is encouraged from the first day.'),
 ('Which surgeon performs weight-loss surgery in Ranchi?','Weight-loss surgery is performed by surgeons experienced in bariatric surgery after assessment of BMI, weight-related conditions and earlier weight-loss attempts. Dr. Vikeerna Bharti performs laparoscopic sleeve gastrectomy and runs the obesity and metabolic clinic at Samford Super Speciality Hospital. '+CALL)],
'appendix-surgery-ranchi.html':[
 ('Pain in the right side of the abdomen with fever — is it appendicitis?','Pain that starts near the navel and moves to the lower right abdomen within a day, with fever, nausea or vomiting, is typical of appendicitis. It is a surgical emergency: go to a hospital emergency the same day. Samford Super Speciality Hospital, Kokar Chowk, Ranchi, has 24/7 emergency surgery.'),
 ('Can appendicitis be treated without an operation?','Appendicitis needs urgent hospital assessment. Surgery is the standard treatment; antibiotics alone may be considered in selected cases after examination and tests. Do not try to make this decision at home or wait for an OPD appointment.'),
 ('What happens if the appendix bursts?','A burst appendix can spread infection through the abdomen (peritonitis). This makes surgery more complex and recovery longer, which is why early assessment matters.'),
 ('Is appendix surgery done at night in Ranchi?','Yes. Dr. Bharti attends emergency surgery, including appendix operations at night, at Samford Super Speciality Hospital, Kokar Chowk, Ranchi, which has anaesthesia and ICU support. Go directly to hospital for urgent assessment; do not wait for a WhatsApp reply.'),
 ('How long is recovery after appendix surgery?','After laparoscopic appendicectomy, most patients go home in 24–48 hours, return to light activities in 5–7 days and to full activity in two to three weeks. Recovery is longer if the appendix had burst.'),
 ('What is the cost of an appendix operation in Ranchi?', COST),
 ('Which doctor should I go to for appendix pain in Ranchi?','Suspected appendicitis should be assessed by a general surgeon the same day, not managed with painkillers at home. Dr. Vikeerna Bharti attends emergency appendix cases at Samford Super Speciality Hospital, Kokar Chowk. '+CALL)],
'thyroid-surgery-ranchi.html':[
 ('What is the cost of a thyroid operation in Ranchi?', COST),
 ('I have a swelling in my neck — do I need surgery?','A swelling at the front of the neck is most often a goitre or thyroid nodule, and many do not need surgery. Assessment includes examination, thyroid blood tests, ultrasound and, when needed, an FNAC needle test. Surgery is discussed for large, growing or pressure-causing swellings and some over-active thyroid conditions.'),
 ('Is thyroid surgery risky?','Thyroidectomy is a well-established operation. Its specific risks include bleeding in the neck, voice change from nerve irritation and low calcium from effects on the parathyroid glands; most effects are temporary. These are explained before surgery.'),
 ('Will I need thyroid tablets after surgery?','After total thyroidectomy, lifelong thyroid hormone (thyroxine) tablets are needed, usually once a day. After hemithyroidectomy, many patients do not need tablets; this is checked with blood tests at follow-up.'),
 ('What is the recovery time after thyroid surgery?','Most patients go home in one to two days and return to normal activities in one to two weeks. The voice may be slightly hoarse for a few days.'),
 ('Does Dr. Bharti operate on thyroid cancer?','No. Dr. Bharti operates on benign thyroid conditions such as goitre and benign nodules. If tests suggest thyroid cancer, he will explain the reports and refer you to a specialist cancer centre.'),
 ('Which doctor performs thyroid surgery in Ranchi?','Thyroid swellings are assessed by general or endocrine surgeons after blood tests, ultrasound and FNAC. Dr. Vikeerna Bharti performs hemithyroidectomy and total thyroidectomy for benign thyroid disease at Samford Super Speciality Hospital and consults at '+BARIATU_OPD+' and '+SAMFORD_OPD+'. '+CALL)],
'acid-reflux-surgery-ranchi.html':[
 ('What is the cost of acid reflux surgery in Ranchi?', COST),
 ('When is surgery needed for acid reflux?','Surgery is considered when symptoms are not controlled by medicines, when a hiatus hernia is causing reflux, or when a suitable patient prefers an operation to lifelong tablets after discussion. Endoscopy and other tests come first.'),
 ('What is laparoscopic fundoplication?','A keyhole operation in which the upper stomach is wrapped around the lower food pipe to strengthen the valve and reduce reflux. It is done through four or five small cuts with a hospital stay of usually two to three days.'),
 ('Is acid reflux surgery permanent?','Fundoplication gives long-term control of reflux for many carefully selected patients, and many reduce or stop daily tablets. Results vary, and some people need medicines again later.'),
 ('How long is recovery after acid reflux surgery?','Usually two to three days in hospital, soft food for four to six weeks, office work after two to three weeks and full activity in four to six weeks.'),
 ('What is a hiatus hernia and does it need surgery?','A hiatus hernia is when part of the stomach moves up through the diaphragm into the chest. Small ones often need only medicines. Large or troublesome hiatus hernias causing reflux, difficulty swallowing or breathing problems may need repair, usually with fundoplication.'),
 ('Which doctor treats acid reflux and hiatus hernia in Ranchi?','Long-standing reflux is first assessed medically, usually with an endoscopy. When surgery is considered, it is done by a general or laparoscopic surgeon. Dr. Vikeerna Bharti performs laparoscopic fundoplication at Samford Super Speciality Hospital. '+CALL)],
}

# Homepage: original service cards and FAQs.
SERVICES = [
 ('gallbladder-stone-surgery-ranchi.html','Gallbladder stone surgery','Laparoscopic cholecystectomy for symptomatic gallstones, including difficult and inflamed gallbladders and bile-duct stones.'),
 ('hernia-surgery-ranchi.html','Hernia surgery & abdominal wall','TEP, TAPP, eTEP, eTEP-RS, IPOM and TAR for groin, umbilical, incisional, recurrent and complex hernias.'),
 ('bariatric-surgery-ranchi.html','Bariatric & obesity clinic','Assessment, laparoscopic sleeve gastrectomy and long-term follow-up for severe obesity.'),
 ('piles-fistula-surgery-ranchi.html','Piles, fissure & fistula','Private consultation, medical treatment and surgery including haemorrhoidectomy, fistulectomy and LIS.'),
 ('varicose-veins-treatment-ranchi.html','Varicose veins (RFA)','Doppler-guided assessment and radiofrequency ablation, usually with next-day discharge.'),
 ('appendix-surgery-ranchi.html','Appendix surgery','Laparoscopic appendicectomy, including emergency operations day and night at Samford Super Speciality Hospital.'),
 ('thyroid-surgery-ranchi.html','Thyroid surgery','Hemithyroidectomy and total thyroidectomy for goitre and benign thyroid nodules.'),
 ('acid-reflux-surgery-ranchi.html','Acid reflux & hiatus hernia','Laparoscopic fundoplication and hiatus hernia repair for selected patients.'),
 ('emergency-surgery-ranchi.html','Emergency surgery (24/7)','Appendicitis, perforation, intestinal obstruction, strangulated hernia, gallbladder emergencies, trauma and abscesses at Samford.'),
]
HOME_FAQS = [
 ('Where can I consult Dr. Vikeerna Bharti in Ranchi?','At '+BARIATU_OPD+', and at '+SAMFORD_OPD+'. You can attend during OPD hours without waiting for a WhatsApp reply. '+CALL),
 ('Stomach pain after eating fatty food — what is it?','Pain in the upper right abdomen after oily food is a common symptom of gallbladder stones. Other conditions can feel similar, so an ultrasound and examination are needed.'),
 ('Lump in groin when standing — is it a hernia?','A groin swelling that appears on standing or coughing and goes back on lying down is often a hernia. Hernias do not heal with medicines; a surgeon will examine you and discuss repair.'),
 ('Bleeding during bowel movements — what to do?','Bright red bleeding is often due to piles or a fissure, but it should not be ignored or self-treated for long. See a surgeon for examination.'),
 ('How long is recovery after laparoscopic hernia or gallbladder surgery?','After planned keyhole surgery, most patients go home the next day, walk the same evening, return to light work in 5–7 days and to full activity in 3–4 weeks. Recovery varies with the operation and your health.'),
 ('Is bariatric surgery available in Ranchi?','Yes. Dr. Bharti performs laparoscopic sleeve gastrectomy at Samford Super Speciality Hospital for carefully assessed patients, with long-term follow-up.'),
 ('Swollen, twisted veins on legs — treatment in Ranchi?','These are usually varicose veins. After a Doppler scan, Dr. Bharti performs radiofrequency ablation (RFA) at Samford Super Speciality Hospital; patients usually go home the next day.'),
 ('Pain in the right side of the abdomen with fever — appendicitis?','Pain moving to the lower right abdomen with fever or vomiting may be appendicitis, a surgical emergency. Go to a hospital emergency the same day. Samford Super Speciality Hospital has 24/7 emergency surgery.'),
 ('Is there a surgeon available in Garhwa, Jharkhand?','Yes. Dr. Bharti usually visits Sai Sushila Sishu Hospital, Garhwa, on the first and third Sundays, where general and laparoscopic surgery, including hernia surgery, is available. Call hospital reception on 82641 03707 to check the date before travelling.'),
 ('Where can I consult a surgeon in Bariatu, Ranchi in the morning or evening?','At Ranchi Dental and Polyclinic, Bariatu Road, near Manipal Hospital: Monday to Saturday, 9–10 AM and 5–7:30 PM. Sunday closed.'),
]
