class HolbertonClass {
  constructor(size, location) {
    if (typeof size === 'number' && typeof location === 'string') {
      this._size = size;
      this._location = location;
    } else {
      throw new TypeError('Size must be a number and location must be a string');
    }
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}

export default HolbertonClass;
