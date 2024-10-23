const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
    it('should return 5 when adding 2.4 and 3.1', function() {
        assert.strictEqual(calculateNumber('SUM', 2.4, 3.1), 5);
    });

    it('should return -8 when subtracting -3.1 and 5.2', function() {
        assert.strictEqual(calculateNumber('SUBTRACT', -3.1, 5.2), -8);
    });

    it('should return 4 when dividing 15.6 by 4.1', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 15.6, 4.1), 4);
    })

    it('should return an error when dividing a if b is zero', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 4, 0), 'Error');
    })
});