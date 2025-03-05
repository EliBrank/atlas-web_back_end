function getPaymentTokenFromAPI(success) {
  if (success) {
    // Promise.resolve is static method of Promise class
    return Promise.resolve({
      data: 'Successful response from the API'
    });
  }

  return;
}

module.exports = getPaymentTokenFromAPI;
