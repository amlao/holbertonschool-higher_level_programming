#!/usr/bin/node
exports.esrever = function (list) {
  let desiree = list.length - 1;
  let desarray = [];
  for (; desiree >= 0; desiree--) {
    desarray.push(list[desiree]);
  }
  return desarray;
};
