#!/usr/bin/node
const spongebob = require('./5-square');
module.exports = class Square extends spongebob {
  charPrint (c) {
    if ( c === 'undefined') {
      let xwidth = 'X'.repeat(this.width);
    for (let count = 0; count < this.height; count++) {
      console.log(xwidth);
    }
    let cwidth = c.repeat(this.width);
    for (let cc = 0; cc < this.height; cc++) {
      console.log(cwidth);
    }
  }
};
