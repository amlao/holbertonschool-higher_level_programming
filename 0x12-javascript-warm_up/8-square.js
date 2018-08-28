#!/usr/bin/node
const num_times = Number(process.argv[2]);
if (num_times) {
    for (let i = 0; i < process.argv[2]; i++) {
	console.log(Array(num_times + 1).join('X'));
    }
} else {
    console.log('Missing size');
}
