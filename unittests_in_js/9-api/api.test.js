const expect = require('chai').expect;
const request = require('request');

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
