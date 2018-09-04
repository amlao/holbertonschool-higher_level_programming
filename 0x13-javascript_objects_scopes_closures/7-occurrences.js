#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let cc = 0;
  for (; counter < list.length;) {
    if (list[counter] === searchElement) {
      cc++;
    }
    counter++;
  }
  return counter;
};
