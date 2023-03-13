#!/usr/bin/node

const args = process.argv.slice(2);

function secondLargest (args) {
  let largest = 0;
  let secondLargest = 0;

  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);

    if (isNaN(num)) {
      return (0);
    }

    if (num > largest) {
      secondLargest = largest;
      largest = num;
    }
  }
  return (secondLargest);
}

console.log(secondLargest(args));
