#!/usr/bin/node
let first = parseInt(process.argv[2]);
let second = parseInt(process.argv[3]);
function add (first, second) {
  return first + second;
}
console.log(add(first, second));
