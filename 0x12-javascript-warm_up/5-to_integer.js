#!/usr/bin/node
const process = require('process');
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a Number');
} else {
  console.log(`My number: ${process.argv[2]}`);
}
