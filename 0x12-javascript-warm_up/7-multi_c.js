#!/usr/bin/node

let count = process.argv[2];
if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  while (count > 0) {
    console.log('C is fun');
    count--;
  }
}
