//function to determine successfull call to API
function getPaymentTokenFromAPI(success) {
    return new Promise((resolve) => {
        if (success) {
            resolve({ data: 'Successful response from the API' });
        } else {
            resolve();
        }
    });
}

module.exports = getPaymentTokenFromAPI;