#!/usr/bin/node
let number = process.argv[2];
function factorial (number) {
  if (isNaN(number) || number === 1) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}
console.log(factorial(parseInt(number)));
