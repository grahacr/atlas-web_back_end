export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new Error('sqft must be a number');
    } else {
      this._sqft = sqft;
    }
  }

  get sqft() {
    return this._sqft;
  }
}

if (typeof Building.evacuationWarningMessage !== 'function') {
      throw new TypeError('Class extending Building must override evacuationWarningMessage');
    }
