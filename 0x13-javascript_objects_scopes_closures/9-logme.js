#!/usr/bin/node

let i = 0;

exports.logMe = function (item) {
  const logger = function () {
    console.log(i, ':', item);
    i++;
  };

  return logger();
};
