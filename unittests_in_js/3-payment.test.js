const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');

describe('Payment tests', () => {
  it('Check that Utils is called (correctly)', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');
    const testAmount = 100, testShipping = 20;

    sendPaymentRequestToApi(testAmount, testShipping);

    sinon.assert.calledWithExactly(spy, 'SUM', testAmount, testShipping);
    spy.restore();
  });
});
