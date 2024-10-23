const request = require('supertest');
const { expect } = require('chai');
const app = require('./api');

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