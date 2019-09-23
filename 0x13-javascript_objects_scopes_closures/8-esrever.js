#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  const len = list.length - 1;
  for (let index = len; index >= 0; index--) {
    rev.push(list[index]);
  }
  return (rev);
};
