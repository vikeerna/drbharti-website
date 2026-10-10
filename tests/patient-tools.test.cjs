const assert = require('node:assert/strict');
const {calculateBMI, nextGarhwaDate} = require('../patient-tools.js');
assert.equal(calculateBMI(170,75),26);
for (const args of [[0,75],[-170,75],[NaN,75],[170,Infinity],[99,70],[170,351]]) assert.equal(calculateBMI(...args),null);
assert.equal(calculateBMI(200,80),20);
const cases = [
  ['2026-10-10T12:00:00Z','2026-10-18'],
  ['2026-10-18T12:00:00Z','2026-10-18'],
  ['2026-10-18T18:29:59Z','2026-10-18'],
  ['2026-10-18T18:30:00Z','2026-11-01'],
  ['2026-12-31T12:00:00Z','2027-01-03'],
  ['2028-02-29T12:00:00Z','2028-03-05'],
  ['2026-11-02T12:00:00Z','2026-11-15']
];
for (const [input,expected] of cases) assert.equal(nextGarhwaDate(new Date(input)).toISOString().slice(0,10),expected);
console.log('PASS: BMI calculation/input bounds; Garhwa IST date, today, month/year rollover and leap year.');
