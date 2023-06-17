#!/usr/bin/node

// array destructuring to remove the first two arguments (path to interpreter and module name)
const [, , ...args] = process.argv;

if (args.length < 2) {
  console.log(0);
} else {
  const sortedNumbers = args.sort((a, b) => b - a);
  const secondLargest = sortedNumbers[1];

  console.log(secondLargest);
}
