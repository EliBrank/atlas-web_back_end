const Utils = require('./utils.js'); // Use destructuring and correct relative path
const sinon = require("sinon");

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const paymentSum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${paymentSum}`);
}

module.exports = sendPaymentRequestToApi;
