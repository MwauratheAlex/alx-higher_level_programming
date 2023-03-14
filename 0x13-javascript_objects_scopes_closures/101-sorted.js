#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

Object.entries(dict).forEach(([key, value]) => {
  if (!newDict[value]) {
    newDict[value] = [key];
  } else {
    newDict[value].push(key);
  }
});

console.log(newDict);
