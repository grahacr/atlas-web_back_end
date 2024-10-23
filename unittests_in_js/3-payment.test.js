const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
    let calculateSpy;

    beforeEach(() => {
        calculateSpy = sinon.spy(Utils, 'calculateNumber');
    })

    afterEach(() => {
        calculateSpy.restore();
    });

    it('should call calculateNumber with correct arguments for SUM', function() {
        sendPaymentRequestToApi(100, 20);
        expect (calculateSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    });
});