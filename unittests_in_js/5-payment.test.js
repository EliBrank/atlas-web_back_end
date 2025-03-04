const sandbox = require('sinon').createSandbox();
const sendPaymentRequestToApi = require('./4-payment.js');
const Utils = require('./utils.js');

describe('Payment tests', () => {
  let spy;

  beforeEach(() => {
    spy = sandbox.spy(console, 'log');
  });

  afterEach(() => {
    sandbox.restore();
  });

  it('Check that Utils is called correctly', () => {
    const testAmount = 100, testShipping = 20;

    sendPaymentRequestToApi(testAmount, testShipping);
    sandbox.assert.calledOnceWithExactly(spy, 'The total is: 120');
  });

  it('Check that Utils is called correctly', () => {
    const testAmount = 10, testShipping = 10;

    sendPaymentRequestToApi(testAmount, testShipping);
    sandbox.assert.calledOnceWithExactly(spy, 'The total is: 20');
  });
});
