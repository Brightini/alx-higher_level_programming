#!/usr/bin/node

//  prints the number of arguments already printed and the new argument value
let numOfArgPrinted = -1;
exports.logMe = function (item) {
  numOfArgPrinted++;
  console.log(numOfArgPrinted + ': ' + item);
};
