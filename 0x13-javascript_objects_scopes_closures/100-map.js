#!/usr/bin/node
let list = require('./100-data.js').list;
let newarray = list.map((curray, start) => curray * start);
console.log(list);
console.log(newarray);
