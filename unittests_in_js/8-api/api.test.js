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

});
