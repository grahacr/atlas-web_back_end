const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
    it('should return 5 when adding 2.4 and 3.1', function() {
        assert.strictEqual(calculateNumber(2.4, 3.1), 5);
    });

    it('should return 2 when adding -3.1 and 5.2', function() {
        assert.strictEqual(calculateNumber(-3.1, 5.2), 2);
    });

    it('should return 0 when adding 0.3 and 0.2', function() {
        assert.strictEqual(calculateNumber(0.3, 0.2), 0);
    })
});