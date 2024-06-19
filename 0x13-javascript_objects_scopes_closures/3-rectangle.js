#!/usr/bin/node
class Rectangle {
  constructor (h, w) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!isNaN(this.width) && !isNaN(this.height)) {
      for (let i = 0; i < this.width; i++) {
        console.log('X'.repeat(this.height));
      }
    }
  }
}
module.exports = Rectangle;
