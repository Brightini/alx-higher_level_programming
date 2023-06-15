const Square = require('./5-square');

module.exports = class Square extends Square {

  charPrint(c) {
	if (c !== undefined) {
		for (let i = 0; i < this.height; i++) {
			let row = '';
			for (let j = 0; j < this.width; j++) {
			  row += c;
			}
			console.log(row);
		  }
	}
  }
};
