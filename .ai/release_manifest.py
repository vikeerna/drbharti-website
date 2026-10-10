"""Build a review manifest of public files; never include host configuration or unused media."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib, json, re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/'outputs'/'website-build-claude-2026-10-10c'
# Deliberately reviewed images only. Adding another asset requires reviewing its contents.
IMAGES={
 'images/dr-vikeerna-bharti-portrait.jpg','images/apple-touch-icon.png',
 'images/amrita_logo.png','images/pgimer_logo.png','images/aiims_logo.png',
 'images/paras_hec_logo.png','images/samford_logo.png',
 'images/gallery_media_garhwa_modular_ot_1.jpeg','images/gallery_media_garhwa_modular_ot_2.jpeg',
 'images/thumb/gallery_media_garhwa_modular_ot_1.jpg','images/thumb/gallery_media_garhwa_modular_ot_2.jpg',
 # 10 Oct: owner confirmed written consent on file for archived patient/camp photographs
 'images/ranchi_dental_polyclinic.jpg','images/samford_hospital_building.jpg','images/sai_sushila_hospital_garhwa.jpg','images/garhwa-ot-photo.jpg','images/garhwa-anaesthesia-workstation.jpg','images/garhwa-autoclave-photo.jpg','images/gallery_surgical_laparoscopy_1.jpg','images/thumb/gallery_surgical_laparoscopy_1.jpg','images/gallery_surgical_ot_team_1.jpg','images/thumb/gallery_surgical_ot_team_1.jpg','images/gallery_surgical_ot_team_2.jpg','images/thumb/gallery_surgical_ot_team_2.jpg','images/gallery_profile_samford_welcome.jpg','images/thumb/gallery_profile_samford_welcome.jpg','images/gallery_personal_with_patient.jpg','images/thumb/gallery_personal_with_patient.jpg','images/gallery_conference_paras_recognition.jpeg','images/thumb/gallery_conference_paras_recognition.jpg','images/gallery_media_free_camp_50.jpeg','images/thumb/gallery_media_free_camp_50.jpg','images/gallery_media_health_camp_135.jpeg','images/thumb/gallery_media_health_camp_135.jpg','images/gallery_media_free_operation_camp.jpeg','images/thumb/gallery_media_free_operation_camp.jpg','images/gallery_media_sai_sushila_story.jpeg','images/thumb/gallery_media_sai_sushila_story.jpg','images/gallery_media_varicose_vein_success.jpeg','images/thumb/gallery_media_varicose_vein_success.jpg','images/gallery_media_vascular_surgery_saved_arm.jpeg','images/thumb/gallery_media_vascular_surgery_saved_arm.jpg',
 # 10 Oct round 2: owner's new operating-theatre photographs (EXIF stripped)
 'images/ot-laparoscopy-dr-bharti-1.jpg','images/thumb/ot-laparoscopy-dr-bharti-1.jpg','images/ot-laparoscopy-dr-bharti-2.jpg','images/thumb/ot-laparoscopy-dr-bharti-2.jpg','images/ot-laparoscopy-dr-bharti-3.jpg','images/thumb/ot-laparoscopy-dr-bharti-3.jpg','images/ot-laparoscopy-dr-bharti-4.jpg','images/thumb/ot-laparoscopy-dr-bharti-4.jpg','images/ot-laparoscopy-dr-bharti-5.jpg','images/thumb/ot-laparoscopy-dr-bharti-5.jpg','images/ot-laparoscopy-tower.jpg','images/thumb/ot-laparoscopy-tower.jpg','images/ot-surgical-team.jpg','images/thumb/ot-surgical-team.jpg','images/ot-instrument-trolley.jpg','images/thumb/ot-instrument-trolley.jpg'
}
files={p.name for p in ROOT.glob('*.html')} | {'style.css','journey.css','site.js','journey.js','patient-tools.js','favicon.ico','robots.txt','sitemap.xml'} | IMAGES
class Assets(HTMLParser):
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if key not in ('src','href','data-full') or not value:continue
            url=urlsplit(value)
            if url.scheme or url.netloc or not url.path:continue
            path=unquote(url.path).lstrip('/')
            assert path in files, f'Unreviewed or missing linked asset: {path}'
for p in ROOT.glob('*.html'):Assets().feed(p.read_text(encoding='utf-8'))
for name in ('style.css','journey.css'):
    for value in re.findall(r'url\([\s\'"]*([^\)\'"\s]+)',(ROOT/name).read_text(encoding='utf-8')):
        if not urlsplit(value).scheme:assert value in files,value
assert all((ROOT/name).is_file() for name in files)
OUT.mkdir(exist_ok=True,parents=True)
manifest={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(files)}
(OUT/'reviewed-public-file-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
excluded=sorted(p.relative_to(ROOT).as_posix() for p in (ROOT/'images').rglob('*') if p.is_file() and p.relative_to(ROOT).as_posix() not in IMAGES)
(OUT/'excluded-media-review.txt').write_text('Excluded from the proposed upload; private originals retained. Existing server copies are NOT deleted by an upload. Review exact paths on the host before removal.\n\n'+'\n'.join(excluded),encoding='utf-8')
print(f'PASS: {len(files)} reviewed public files; {len(excluded)} unused images excluded; .htaccess excluded. No ZIP or upload created.')
