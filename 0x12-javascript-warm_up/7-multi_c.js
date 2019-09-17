#!/usr/bin/node
const process = require('process');
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < process.argv.length) {
    console.log('C is fun');
    count++;
  }
}
