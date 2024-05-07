import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw new Error('Amount must be number')
    }
    if (!(currency instanceof Currency)) {
      throw new Error('Currency must be an instance of Currency')
    }
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(amount2) {
    if (typeof amount2 !== 'number') {
      throw new Error('Amount must be number')
    }
    this._amount = amount2;
  }

  get currency() {
    return this._currency;
  }

  set currency(currency2) {
    if (!(currency2 instanceof Currency)) {
      throw new Error('Currency must be an instance of Currency')
    }
    this._currency = currency2;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency._name} (${this._currency._code})`
  }

  static convertPrice(amount, conversationRate) {
    return amount * conversationRate;
  }
}
