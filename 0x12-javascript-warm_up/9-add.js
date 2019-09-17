#!/usr/bin/node
const process = require('process');
/**
 * Add two numbers together
 * @param  {Number} a The first Number
 * @param  {Number} b The second Number
 * @return {Number}   Sum of a and b
 */
function add (a, b) {
  console.log(a + b);
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
