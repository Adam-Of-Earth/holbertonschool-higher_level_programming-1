#!/usr/bin/node
const process = require('process');
/**
 * Finds the factorial of a number
 * @param  {Number} num Number to find factorial of
 * @return {Number}     Factorial of num
 */
function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return (1);
  }
  return (num * factorial(num - 1));
}
console.log(factorial(process.argv[2]))
