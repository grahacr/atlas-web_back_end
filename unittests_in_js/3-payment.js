//
const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const sumShipping = Utils.calculateNumber('SUM', totalAmount, totalShipping)
    console.log(`The total is: ${sumShipping}`)
}

module.exports = sendPaymentRequestToApi;