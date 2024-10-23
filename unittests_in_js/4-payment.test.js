const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi with stub', function() {
    let calculateStub;
    let consoleSpy;

    beforeEach(() => {
        calculateStub = sinon.stub(Utils, 'calculateNumber').returns(10);
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        calculateStub.restore();
        consoleSpy.restore();
    });

    it('should call calculateNumber and return 10 and console.log the value', function() {
        const result = sendPaymentRequestToApi(100, 20);
        expect (result).to.equal(10);
        expect (consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
    });
});