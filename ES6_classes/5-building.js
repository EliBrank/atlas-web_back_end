export default class Building {
  constructor(sqft) {
    this.sqft = sqft;

    // allows instantion of Building class but not classes which
    // extend Building without redefining evacuationWarningMessage method
    if (this.constructor !== Building && !this.hasOwnProperty('evacuationWarningMessage')) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // Square Footage
  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (typeof newSqft !== 'number') {
      throw new TypeError('Square Footage must be a number');
    }
    this._sqft = newSqft;
  }
}
