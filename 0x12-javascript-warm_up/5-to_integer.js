#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My number:', firstArg);
}
