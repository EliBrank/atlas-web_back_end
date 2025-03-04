const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment.js');
const Utils = require('./utils.js');

describe('Payment tests', () => {
  it('Check that Utils is called correctly, with stub', () => {
    const stub = sinon.stub(Utils, 'calculateNumber').callsFake(() => 10);
    const spy = sinon.spy(console, 'log');
    const testAmount = 100, testShipping = 20;

    sendPaymentRequestToApi(testAmount, testShipping);

    sinon.assert.calledWithExactly(spy, 'The total is: 10');
    spy.restore();
  });
});
