#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      /* Create an empty object if width or height is invalid */
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
