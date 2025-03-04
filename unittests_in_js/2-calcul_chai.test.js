const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('Calculator', () => {
  describe('Add', () => {
    const calcType = 'SUM';

    it('Numbers are not rounded', () => {
      const result = calculateNumber(calcType, 3, 5);
      expect(result).to.equal(8);
    });

    it('Numbers are correctly rounded down', () => {
      const result = calculateNumber(calcType, 3.2, 5.3);
      expect(result).to.equal(8);
    });

    it('Numbers are correctly rounded up', () => {
      const result = calculateNumber(calcType, 2.7, 7.5);
      expect(result).to.equal(11);
    });
  })

  describe('Subtract', () => {
    const calcType = 'SUBTRACT';

    it('Numbers are not rounded', () => {
      const result = calculateNumber(calcType, 3, 5);
      expect(result).to.equal(-2);
    });

    it('Numbers are correctly rounded down', () => {
      const result = calculateNumber(calcType, 3.2, 5.3);
      expect(result).to.equal(-2);
    });

    it('Numbers are correctly rounded up', () => {
      const result = calculateNumber(calcType, 2.7, 7.5);
      expect(result).to.equal(-5);
    });

    it('Negative numbers correctly subtract', () => {
      const result = calculateNumber(calcType, -5, -8.2);
      expect(result).to.equal(3);
    });
  })

  describe('Divide', () => {
    const calcType = 'DIVIDE';

    it('Numbers are not rounded', () => {
      const result = calculateNumber(calcType, 6, 3);
      expect(result).to.equal(2);
    });

    it('Numbers are correctly rounded down', () => {
      const result = calculateNumber(calcType, 6.2, 3.3);
      expect(result).to.equal(2);
    });

    it('Numbers are correctly rounded up', () => {
      const result = calculateNumber(calcType, 11.8, 3.5);
      expect(result).to.equal(3);
    });

    it('Fractional results are given as floats', () => {
      const result = calculateNumber(calcType, 1, 5);
      expect(result).to.equal(0.2);
    });

    it('Divide by zero returns Error text', () => {
      const result = calculateNumber(calcType, 5, 0);
      expect(result).to.equal('Error');
    });

    it('Negative numbers correctly evaluate', () => {
      const result = calculateNumber(calcType, -8, 2);
      expect(result).to.equal(-4);
    });
  })
});
