#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  // prints a rectangle object using the character 'X'
  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  // exchanges the value of the width and height variables in a rectangle object
  rotate () {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // doubles the values of the width and height variables of a rectangle object
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
