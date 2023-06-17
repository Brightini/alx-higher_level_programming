#!/usr/bin/node

// array destructuring to remove the first two arguments (path to interpreter and module name)
const [, , ...args] = process.argv;

if ((args.length - 2) <= 1) {
  console.log(0);
} else {
  const number = args.map(Number).sort((a, b) => b - a);
  const secondLargest = number[1];

  console.log(secondLargest);
}
