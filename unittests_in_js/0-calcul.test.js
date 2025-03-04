const assert = require('chai').assert;
const calculateNumber = require('./0-calcul.js');

describe('Calculator', () => {
  it('Integers are not rounded', () => {
    const result = calculateNumber(3, 5);
    assert.equal(result, 8);
  });

  it('Numbers are correctly rounded down', () => {
    const result = calculateNumber(3.2, 5.3);
    assert.equal(result, 8);
  });

  it('Numbers are correctly rounded up', () => {
    const result = calculateNumber(2.7, 7.5);
    assert.equal(result, 11);
  });
});
