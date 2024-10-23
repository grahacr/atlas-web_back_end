//test suite for getpaymenttokenfromapi
const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentToken api call success', function() {
    it('should return a successful response when true', function(done) {
        getPaymentTokenFromAPI(true)
        .then(response => {
            expect(response).to.deep.equal({ data: 'Successful response from the API' });
            done();
        })
        .catch(done);
    });

    it('should return undefined when success is false', function(done) {
        getPaymentTokenFromAPI(false)
        .then(response => {
            expect(response).to.be.undefined;
            done();
        })
        .catch(done);
    });
});