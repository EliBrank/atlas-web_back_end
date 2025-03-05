const expect = require('chai').expect;
const request = require('request');

describe('Express API', () => {
  describe('Index page', () => {

    it('Check for correct status code, message on default endpoint', (done) => {
      request.get('http://localhost:7865', (error, response, body) => {
        if (error) return done(error);
        expect(response.statusCode).to.equal(200);
        const expectedResponse = 'Welcome to the payment system';
        expect(body).to.equal(expectedResponse);
        done();
      });
    });

  });

  describe('Cart page', () => {

    it('Cart endpoint handles integer IDs', (done) => {
      request.get('http://localhost:7865/cart/12', (error, response, body) => {
        if (error) return done(error);
        expect(response.statusCode).to.equal(200);
        const expectedResponse = 'Payment methods for cart 12';
        expect(body).to.equal(expectedResponse);
        done();
      });
    });

    it('Cart endpoint rejects non-integer IDs', (done) => {
      request.get('http://localhost:7865/cart/hello', (error, response, body) => {
        if (error) return done(error);
        expect(response.statusCode).to.equal(404);
        done();
      });
    });

  });

  describe('Payments page', () => {

    it('Payments endpoint returns correct structure', (done) => {
      request.get('http://localhost:7865/available_payments', (error, response, body) => {
        if (error) return done(error);
        expect(response.statusCode).to.equal(200);
        const parsedBody = JSON.parse(body);
        const expectedResponse = {
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        };
        expect(parsedBody).to.deep.equal(expectedResponse);
        done();
      });
    });

  });

  describe('Login page', () => {

    it('Login endpoint displays welcome message with username', (done) => {
      const userName = 'Betty';
      request.post({
        url: 'http://localhost:7865/login',
        json: true,
        body: { "userName": userName }
      }, (error, response, body) => {
        if (error) return done(error);
        expect(response.statusCode).to.equal(200);
        const expectedResponse = `Welcome ${userName}`;
        expect(body).to.deep.equal(expectedResponse);
        done();
      });
    });

  });
});
