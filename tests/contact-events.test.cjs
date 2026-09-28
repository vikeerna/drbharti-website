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
// Exercise the actual form handler: clinic in the message, one analytics event,
// no name, phone or message in analytics. No network requests are made.
const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
const formSource=html.match(/function handleSubmit\(e\) \{[\s\S]*?\n    \}/)[0];
let opened; const recorded=[];
const fields={clinic:{value:'bariatu',selectedIndex:0,options:[{text:'Bariatu clinic, Ranchi'}]},name:{value:'TEST PERSON'},phone:{value:'0000000000'},treatment:{selectedIndex:0,options:[{text:'Consultation'}]},msg:{value:'PRIVATE TEST'}};
const formContext={document:{getElementById:id=>fields[id]},window:{trackContact:(...args)=>recorded.push(args),open:(...args)=>{opened=args;}},setTimeout:()=>{}};
vm.createContext(formContext); vm.runInContext(formSource,formContext);
formContext.handleSubmit({preventDefault(){},target:{querySelector:()=>({})}});
assert.equal(recorded.length,1);
assert.equal(recorded[0].join('|'),'whatsapp_click|bariatu|form');
assert.ok(new URL(opened[0]).searchParams.get('text').includes('Preferred clinic: Bariatu clinic, Ranchi'));
assert.equal(opened[2],'noopener,noreferrer');
assert.ok(!JSON.stringify(recorded).includes('TEST'));
console.log('PASS: local suppression, sanitised events, contact classification and appointment form.');
console.log(`PASS: syntax of ${scripts} inline JavaScript blocks.`);
