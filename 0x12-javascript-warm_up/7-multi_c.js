#!/usr/bin/node
const process = require('process');
let num = parseInt(process.argv[2]);
if (process.argv.length === 2 || isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < num; count++) {
    console.log('C is fun');
  }
}
