#!/usr/bin/node
const numTimes = Number(process.argv[2]);
if (numTimes) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(Array(numTimes + 1).join('X'));
  }
} else {
  console.log('Missing size');
}
