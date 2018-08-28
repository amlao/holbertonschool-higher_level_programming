#!/usr/bin/node
let goliath = 0;
let number = process.argv.slice(2);
if (number.length > 1) {
  number.sort();
  goliath = number[number.length - 2];
}
console.log(goliath);
