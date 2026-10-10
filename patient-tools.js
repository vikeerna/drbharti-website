(function (root) {
  'use strict';
  function calculateBMI(height, weight) {
    if (!Number.isFinite(height) || !Number.isFinite(weight) || height < 100 || height > 250 || weight < 20 || weight > 350) return null;
    return Math.round(weight / Math.pow(height / 100, 2) * 10) / 10;
  }
  function nextGarhwaDate(now) {
    const parts = new Intl.DateTimeFormat('en-CA', {timeZone: 'Asia/Kolkata', year:'numeric', month:'2-digit', day:'2-digit'}).formatToParts(now);
    const part = name => Number(parts.find(p => p.type === name).value);
    const today = Date.UTC(part('year'), part('month') - 1, part('day'));
    for (let offset = 0; offset < 2; offset++) {
      const month = new Date(Date.UTC(part('year'), part('month') - 1 + offset, 1));
      const first = 1 + (7 - month.getUTCDay()) % 7;
      for (const day of [first, first + 14]) {
        const candidate = new Date(Date.UTC(month.getUTCFullYear(), month.getUTCMonth(), day));
        if (candidate.getTime() >= today) return candidate;
      }
    }
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {calculateBMI, nextGarhwaDate};
  if (!root.document) return;
  root.document.querySelectorAll('[data-garhwa-next]').forEach(el => {
    el.textContent = new Intl.DateTimeFormat('en-IN', {timeZone:'UTC', weekday:'long', day:'numeric', month:'long', year:'numeric'}).format(nextGarhwaDate(new Date()));
  });
  const form = root.document.getElementById('bmi-form');
  if (form) form.addEventListener('input', () => { root.document.getElementById('bmi-result').textContent = ''; });
  if (form) form.addEventListener('submit', event => {
    event.preventDefault();
    const result = calculateBMI(Number(form.querySelector('#bmi-height').value), Number(form.querySelector('#bmi-weight').value));
    root.document.getElementById('bmi-result').textContent = result === null ? 'Please check your height and weight and use the units shown.' : 'Your BMI is ' + result.toFixed(1) + ' kg/m². Discuss this alongside your waist measurement, health and weight history. This result is not a diagnosis or a recommendation for surgery.';
  });
})(typeof window === 'undefined' ? {} : window);
