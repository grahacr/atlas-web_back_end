const request = require('supertest');
const { expect } = require('chai');
const app = require('./api');
const { describe } = require('mocha');

describe('GET /', function() {
    it('should return status code 200', function(done) {
        request(app)
            .get('/')
            .expect(200, done);
    });

    it('should return correct console message', function(done) {
        request(app)
            .get('/')
            .expect('Content-Type', /text/)
            .expect('Welcome to the payment system', done);
    });
});

describe('GET /CART/:id', function() {
    it('should return status code 200 when :id is a number', function(done) {
        request(app)
            .get('/cart/123')
            .expect(200)
            .expect('Payment methods for cart 123', done);
    });
    it('should return status code 404 when :id is not a number', function(done) {
        request(app)
            .get('/cart/abc')
            .expect(404, done);
    });
    it('should return status code 404 when :id is an empty string', function(done) {
        request(app)
            .get('/cart/')
            .expect(404, done);
    });
})