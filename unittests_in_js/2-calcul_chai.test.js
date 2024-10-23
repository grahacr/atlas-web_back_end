const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
    it('should return 5 when adding 2.4 and 3.1', function() {
        expect(calculateNumber('SUM', 2.4, 3.1)).to.equal(5);
    });

    it('should return -8 when subtracting -3.1 and 5.2', function() {
        expect(calculateNumber('SUBTRACT', -3.1, 5.2)).to.equal(-8);
    });

    it('should return 4 when dividing 15.6 by 4.1', function() {
        expect(calculateNumber('DIVIDE', 15.6, 4.1)).to.equal(4);
    });

    it('should return an error when dividing a if b is zero', function() {
        expect(calculateNumber('DIVIDE', 4, 0)).to.equal('Error');
    });
});