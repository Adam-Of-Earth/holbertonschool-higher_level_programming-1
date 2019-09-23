#!/usr/bin/node
const list = require('./100-data').list;
const mp = list.map(function (current, index) { return (current * index); })
console.log(list);
console.log(mp);
