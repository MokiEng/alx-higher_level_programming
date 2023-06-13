#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      /* Create an empty object if width or height is invalid */
      return {};
    }

    this.width = w;
    this.height = h;
  }

  print () {
    if (this.width === 0 || this.height === 0) {
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
