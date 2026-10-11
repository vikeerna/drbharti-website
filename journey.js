/* Shared accessible navigation and a reviewable WhatsApp handoff. */
(function () {
  'use strict';
  var toggle = document.querySelector('.journey-menu-button');
  var menu = document.getElementById('journey-menu');
  function closeMenu() { if (menu && toggle) { menu.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false'); } }
  if (toggle && menu) {
    toggle.addEventListener('click', function () { var open = toggle.getAttribute('aria-expanded') !== 'true'; toggle.setAttribute('aria-expanded', String(open)); menu.classList.toggle('is-open', open); });
    menu.addEventListener('click', function (event) { if (event.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', function (event) { if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); } });
  }
  if (typeof document.addEventListener === 'function') {
  document.querySelectorAll('.nav-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var group = btn.parentNode, open = btn.getAttribute('aria-expanded') !== 'true';
      document.querySelectorAll('.nav-group.is-open').forEach(function (g) { if (g !== group) { g.classList.remove('is-open'); g.querySelector('.nav-toggle').setAttribute('aria-expanded', 'false'); } });
      group.classList.toggle('is-open', open); btn.setAttribute('aria-expanded', String(open));
    });
  });
  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape') return;
    var g = document.querySelector('.nav-group.is-open');
    if (g) { g.classList.remove('is-open'); var b = g.querySelector('.nav-toggle'); b.setAttribute('aria-expanded', 'false'); b.focus(); }
  });
  document.addEventListener('click', function (event) {
    if (!event.target.closest('.nav-group')) document.querySelectorAll('.nav-group.is-open').forEach(function (g) { g.classList.remove('is-open'); g.querySelector('.nav-toggle').setAttribute('aria-expanded', 'false'); });
  });
  }
  var form = document.getElementById('consultation-request');
  if (!form) return;
  var clinics = {bariatu: 'Ranchi Dental and Polyclinic, Ranchi', samford: 'Samford Super Speciality Hospital, Ranchi', garhwa: 'Garhwa — please confirm the next visit date', unsure: 'Please help me choose a clinic'};
  var purposes = {opd: 'OPD consultation', second_opinion: 'Surgical second opinion', follow_up: 'Follow-up consultation'};
  var clinic = document.getElementById('clinic');
  var purpose = document.getElementById('purpose');
  var output = document.getElementById('booking-output');
  var link = document.getElementById('whatsapp-request');
  var params = new URLSearchParams(location.search);
  if (Object.prototype.hasOwnProperty.call(clinics, params.get('clinic'))) clinic.value = params.get('clinic');
  if (Object.prototype.hasOwnProperty.call(purposes, params.get('purpose'))) purpose.value = params.get('purpose');
  function clearPreview() { output.hidden = true; link.removeAttribute('href'); }
  clinic.addEventListener('change', clearPreview); purpose.addEventListener('change', clearPreview);
  document.querySelectorAll('.journey-card a[href*="appointments.html?clinic="]').forEach(function (choice) {
    choice.addEventListener('click', function (event) {
      var selected = new URL(choice.href).searchParams.get('clinic');
      if (!Object.prototype.hasOwnProperty.call(clinics, selected)) return;
      event.preventDefault(); clinic.value = selected; clearPreview();
      form.scrollIntoView({block: 'start'}); clinic.focus({preventScroll: true});
    });
  });
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (!Object.prototype.hasOwnProperty.call(clinics, clinic.value) || !Object.prototype.hasOwnProperty.call(purposes, purpose.value)) return;
    var message = 'Hello Dr. Bharti, I would like to request a ' + purposes[purpose.value] + '.\nPreferred clinic: ' + clinics[clinic.value] + '.\nI would like to visit during OPD hours. Please help me with any visit instructions.\nEnquiry from drbhartisurgery.com.';
    document.getElementById('booking-message').textContent = message;
    link.href = 'https://wa.me/916206091982?text=' + encodeURIComponent(message);
    link.setAttribute('data-wa-location', clinic.value);
    output.hidden = false;
    document.getElementById('booking-ready').focus();
  });
})();
