#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let thiswidth = 'X'.repeat(this.width);
    for (let count = 0; count < this.height; count++) {
      console.log(thiswidth);
    }
  }
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
