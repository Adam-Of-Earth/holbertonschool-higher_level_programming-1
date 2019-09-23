#!/usr/bin/node
const dic = require('./101-data').dict;
const newDic = {};
const val = Object.values(dic);
const setVal = [...new Set(val)];
for (let index = 0; index < setVal.length; index++) {
  newDic[setVal[index]] = [];
}
for (const key in dic) {
  newDic[dic[key]].push(key);
}
console.log(newDic);
