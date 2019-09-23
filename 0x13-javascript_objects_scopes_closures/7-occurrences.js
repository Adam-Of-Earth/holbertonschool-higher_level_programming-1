#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const len = list.length;
  for (let index = 0; index < len; index++) {
    if (list[index] === searchElement) {
      count++;
    }
  }
  return (count);
};
