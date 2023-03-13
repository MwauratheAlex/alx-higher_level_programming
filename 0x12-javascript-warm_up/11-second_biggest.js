#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const secondLargest = args.map(Number).sort((a, b) => b - a)[1];
  console.log(secondLargest);
}
