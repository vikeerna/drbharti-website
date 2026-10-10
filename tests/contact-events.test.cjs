const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const root = path.join(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'site.js'), 'utf8');
let scripts=0;
for (const file of fs.readdirSync(root).filter(f=>f.endsWith('.html'))) {
  const html=fs.readFileSync(path.join(root,file),'utf8');
  for (const match of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)) {
    if (/application\/ld\+json|\bsrc\s*=/.test(match[1])) continue;
    new vm.Script(match[2],{filename:file}); scripts++;
  }
}
function setup(hostname='drbhartisurgery.com') {
  const events=[]; let click;
  const window={gtag:(...args)=>events.push(args)};
  const context={window, URL, location:{hostname, origin:'https://'+hostname, pathname:'/bariatu-surgery-clinic-ranchi.html', search:'?name=PRIVATE'}, document:{referrer:'https://example.com/private?name=PRIVATE',title:'Clinic',addEventListener:(type,fn)=>{click=fn;}}};
  vm.runInNewContext(source,context);
  return {events,window,context,click:(href,attrs={})=>click({target:{closest:()=>({href,getAttribute:key=>attrs[key]||null})}})};
}
const live=setup();
assert.equal(live.events.length,1);
live.click('https://wa.me/916206091982?text=PRIVATE');
assert.equal(live.events.length,2);
assert.equal(live.events[1][1],'whatsapp_click');
assert.equal(live.events[1][2].wa_location,'bariatu');
live.click('https://wa.me.attacker.example/');
assert.equal(live.events.length,2);
live.click('tel:+916206091982');
assert.equal(live.events[2][1],'phone_click');
live.click('https://maps.app.goo.gl/aGJb7LgdmoKjzaMR6');
assert.equal(live.events[3][1],'directions_click');
live.window.trackContact('whatsapp_click','PRIVATE','PRIVATE');
assert.equal(live.events[4][2].wa_location,'unknown');
assert.ok(!JSON.stringify(live.events).includes('PRIVATE'));
const local=setup('127.0.0.1');
local.click('tel:+916206091982');
assert.equal(local.events.length,0);
// Exercise actual handoff code. Preparing a message must not open WhatsApp or
// record a contact click. Only allowlisted clinic/purpose values enter the URL.
const journeySource=fs.readFileSync(path.join(root,'journey.js'),'utf8');
function booking(search='') {
  const fields={};
  for(const id of ['consultation-request','clinic','purpose','booking-output','whatsapp-request','booking-message','booking-ready']) {
    fields[id]={value:id==='purpose'?'opd':'',hidden:true,handlers:{},attrs:{},addEventListener(type,fn){this.handlers[type]=fn;},setAttribute(k,v){this.attrs[k]=v;},removeAttribute(k){delete this[k];},focus(){this.focused=true;}};
  }
  vm.runInNewContext(journeySource,{URLSearchParams,location:{search},document:{querySelector:()=>null,querySelectorAll:()=>[],getElementById:id=>fields[id]||null},window:{open(){throw Error('Unexpected automatic handoff');},trackContact(){throw Error('Preview must not record a contact click');}}});
  return {fields,submit:()=>fields['consultation-request'].handlers.submit({preventDefault(){}})};
}
for(const clinic of ['bariatu','samford','garhwa','unsure']) {
  const b=booking('?clinic='+clinic+'&purpose=second_opinion&name=PRIVATE'); b.submit();
  assert.equal(b.fields['booking-output'].hidden,false);
  assert.equal(b.fields['booking-ready'].focused,true);
  const url=new URL(b.fields['whatsapp-request'].href);
  assert.equal(url.origin,'https://wa.me'); assert.equal(url.pathname,'/916206091982');
  assert.match(url.searchParams.get('text'),/Surgical second opinion/);
  assert.ok(!/consultation fee|confirm.*appointment/i.test(url.searchParams.get('text')));
  assert.ok(!url.href.includes('PRIVATE'));
  assert.equal(b.fields['whatsapp-request'].attrs['data-wa-location'],clinic);
  b.fields.clinic.handlers.change();
  assert.equal(b.fields['booking-output'].hidden,true);
  assert.equal(b.fields['whatsapp-request'].href,undefined);
}
const invalid=booking('?clinic=PRIVATE&purpose=__proto__'); invalid.submit();
assert.equal(invalid.fields.clinic.value,'');
assert.equal(invalid.fields.purpose.value,'opd');
assert.equal(invalid.fields['booking-output'].hidden,true);
const html=fs.readFileSync(path.join(root,'appointments.html'),'utf8');
assert.match(html,/id="whatsapp-request" target="_blank" rel="noopener noreferrer"/);
assert.ok(!/<(?:input|textarea)\b/i.test(html));
console.log('PASS: local suppression, sanitised events, contact classification, clinic selection and truthful WhatsApp handoff.');
console.log(`PASS: syntax of ${scripts} inline JavaScript blocks.`);
