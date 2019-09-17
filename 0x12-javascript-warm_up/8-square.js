#!/usr/bin/node
const process = require('process');
let str = '';
if (process.argv.length === 2 || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  let index = 0;
  let index2 = 0;
  while (index < parseInt(process.argv[2])) {
    while (index2 < parseInt(process.argv[2])) {
      str = str + 'X';
      index2++;
    }
    console.log(str);
    index++;
  }
}
