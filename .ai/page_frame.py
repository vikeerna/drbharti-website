"""Shared page metadata and identity; no generation on import."""
from pathlib import Path
from html import escape
import json
ROOT=Path(__file__).resolve().parents[1]
BASE="https://drbhartisurgery.com/"

def write_page(filename,title,description,body,extra_schema=None):
    url=BASE+('' if filename=='index.html' else filename)
    doctor={'@type':'Physician','@id':BASE+'#doctor','name':'Dr. Vikeerna Bharti','url':BASE,'telephone':'+916206091982','image':BASE+'images/dr-vikeerna-bharti-portrait.jpg','description':'General and laparoscopic surgeon. MS General Surgery, PGIMER Chandigarh; FMAS; FIAGES; FALS (Robotic). Consultations in Ranchi and visiting OPD in Garhwa.','address':{'@type':'PostalAddress','streetAddress':'Ranchi Dental and Polyclinic, near Manipal Hospital, Bariatu Road','addressLocality':'Ranchi','addressRegion':'Jharkhand','addressCountry':'IN'},'sameAs':['https://www.facebook.com/drvikeerna','https://orcid.org/0000-0002-0344-1229']}
    graph=[doctor,{'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':description,'about':{'@id':BASE+'#doctor'},'inLanguage':'en-IN'}]
    if filename in ('index.html','appointments.html','bariatu-surgery-clinic-ranchi.html'):
        for key,name,address,hours in [('bariatu','Ranchi Dental and Polyclinic — Dr. Vikeerna Bharti','Ranchi Dental and Polyclinic, near Manipal Hospital, Bariatu Road',['Mo-Sa 09:00-10:00','Mo-Sa 17:00-19:30']),('samford','Samford Super Speciality Hospital — Dr. Vikeerna Bharti','H.B. Road, Kokar Chowk',['Mo-Sa 11:00-17:00'])]:
            if filename=='bariatu-surgery-clinic-ranchi.html' and key!='bariatu': continue
            graph.append({'@type':'MedicalClinic','@id':BASE+'#'+key,'name':name,'telephone':'+916206091982','address':{'@type':'PostalAddress','streetAddress':address,'addressLocality':'Ranchi','addressRegion':'Jharkhand','addressCountry':'IN'},'openingHours':hours})
    graph.extend(extra_schema or [])
    head=f'''<!DOCTYPE html><html lang="en-IN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{escape(title)}</title><meta name="description" content="{escape(description,quote=True)}"><meta name="author" content="Dr. Vikeerna Bharti"><meta name="robots" content="index, follow, max-image-preview:large"><link rel="canonical" href="{url}"><link rel="icon" href="favicon.ico"><link rel="apple-touch-icon" href="images/apple-touch-icon.png"><link rel="stylesheet" href="style.css?v=20260928b"><meta property="og:type" content="website"><meta property="og:site_name" content="Dr. Vikeerna Bharti"><meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}images/dr-vikeerna-bharti-portrait.jpg"><meta name="twitter:card" content="summary_large_image"><script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False)}</script><script async src="https://www.googletagmanager.com/gtag/js?id=G-RT77KDZZ8Q"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());if(location.hostname==='drbhartisurgery.com')gtag('config','G-RT77KDZZ8Q',{{send_page_view:false}});</script></head><body class="journey-page">'''
    (ROOT/filename).write_text(head+body+'<script src="site.js?v=20261009" defer></script></body></html>',encoding='utf-8')
