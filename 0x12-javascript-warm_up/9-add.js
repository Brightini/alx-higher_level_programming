#!/usr/bin/node

add(Number(process.argv[2]), Number(process.argv[3]));

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
