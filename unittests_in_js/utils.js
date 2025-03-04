const Utils = {
  calculateNumber: function(type, a, b) {
    const numA = Math.round(a);
    const numB = Math.round(b);
    const typeUppercase = type.toUpperCase();

    switch (typeUppercase) {
      case 'SUM':
        return (numA + numB);
      case 'SUBTRACT':
        return (numA - numB);
      case 'DIVIDE':
        if (numB === 0) {
          return 'Error';
        } else {
          return (numA / numB);
        }
      default:
        return;
    }
  }
}

module.exports = Utils;
