export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  // Code
  get code() {
    return this._code;
  }

  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newCode;
  }

  // Name
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }

  // Methods
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
