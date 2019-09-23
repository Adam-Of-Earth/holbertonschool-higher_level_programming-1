#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w > 0 && h > 0)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    const row = 'X'.repeat(this.width);
    for (let index = 0; index < this.height; index++) {
      console.log(row);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
