const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi with stub', function() {
    let calculateStub;
    let consoleSpy;

    beforeEach(() => {
        calculateStub = sinon.stub(Utils, 'calculateNumber').returns(120);
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        calculateStub.restore();
        consoleSpy.restore();
    });

    it('should log "the total is: 120" when called with 100 and 20', function() {
        const result = sendPaymentRequestToApi(100, 20);
        expect (consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
        expect (consoleSpy.calledOnce).to.be.true;
    });

    it('should log "The total is: 20" when called with 10 and 10', function() {
        calculateStub.returns(20);
        sendPaymentRequestToApi(10, 10);
        expect(consoleSpy.calledOnce).to.be.true;
        expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
    });
});