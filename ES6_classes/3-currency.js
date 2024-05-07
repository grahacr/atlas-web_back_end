export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw new Error('Code must be a string');
    }
    if (typeof name !== 'string') {
      throw new Error('Name must be a string')
    }
    this._name = name;
    this._code = code;
  }
  get code() {
    return this._code;
  }
  set code(code2) {
    if (typeof code2 !== 'string') {
      throw new Error('Code must be a string');
    }
    this._code = code2;
  }
  get name() {
    return this._name;
  }
  set name(name2) {
    if (typeof name2 !== 'string') {
      throw new Error('Name must be a string');
    }
    this._name = name2;
  }
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
