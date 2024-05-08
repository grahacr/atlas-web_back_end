export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }
  toString() {
    return `[object ${this._code}]`
  }

  get name() {
    return this._name;
  }

  set name(name2) {
    if (typeof name2 !== 'string') {
      throw new Error('name must be a string');
    }
    this._name = name2;
  }

  get code() {
    return this._code;
  }

  set code(code2) {
    if (typeof code2 !== 'string') {
      throw new Error('code must be a string');
    }
    this._code = code2;
  }
}
