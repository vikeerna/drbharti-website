/* Contact events represent clicks, not sent messages or confirmed appointments. */
(function () {
  'use strict';
  var live = location.hostname === 'drbhartisurgery.com';
  var locations = ['bariatu', 'samford', 'ranchi', 'garhwa', 'general', 'unsure', 'unknown'];
  var placements = ['hero', 'sidebar', 'inline', 'float', 'sticky_bar', 'location_card', 'form', 'unknown'];
  function safe(value, allowed) { return allowed.indexOf(value) !== -1 ? value : 'unknown'; }
  function pageLocation() {
    if (location.pathname.indexOf('bariatu-') !== -1) return 'bariatu';
    if (location.pathname.indexOf('surgeon-in-garhwa') !== -1) return 'garhwa';
    return 'general';
  }
  window.trackContact = function (eventName, clinic, placement) {
    if (!live || typeof window.gtag !== 'function') return;
    if (['whatsapp_click', 'phone_click', 'directions_click'].indexOf(eventName) === -1) return;
    window.gtag('event', eventName, {
      wa_location: safe(clinic, locations),
      wa_cta: safe(placement, placements),
      page: location.pathname,
      page_location: location.origin + location.pathname
    });
  };
  if (live && typeof window.gtag === 'function') {
    var referringOrigin = '';
    try { referringOrigin = document.referrer ? new URL(document.referrer).origin : ''; } catch (_) {}
    window.gtag('event', 'page_view', {
      page_location: location.origin + location.pathname,
      page_referrer: referringOrigin,
      page_title: document.title
    });
  }
  document.addEventListener('click', function (event) {
    var a = event.target.closest && event.target.closest('a[href]');
    if (!a) return;
    var url;
    try { url = new URL(a.href); } catch (_) { return; }
    var name;
    if (url.hostname === 'wa.me') name = 'whatsapp_click';
    else if (url.protocol === 'tel:') name = 'phone_click';
    else if (['maps.app.goo.gl', 'share.google', 'maps.google.com'].indexOf(url.hostname) !== -1 ||
      (url.hostname === 'www.google.com' && url.pathname.indexOf('/maps') === 0)) name = 'directions_click';
    else return;
    var clinic = a.getAttribute('data-location') || a.getAttribute('data-wa-location') || pageLocation();
    if (a.getAttribute('data-wa-topic') === 'bariatu') clinic = 'bariatu';
    if (url.hostname === 'maps.app.goo.gl' && url.pathname === '/aGJb7LgdmoKjzaMR6') clinic = 'bariatu';
    if (url.hostname === 'share.google' && url.pathname === '/OEVRSj332FV14wfzm') clinic = 'bariatu';
    if (url.hostname === 'share.google' && url.pathname === '/YnRtz8G7uHBbTMSdU') clinic = 'garhwa';
    window.trackContact(name, clinic, a.getAttribute('data-wa-cta') || 'unknown');
  }, true);
})();
