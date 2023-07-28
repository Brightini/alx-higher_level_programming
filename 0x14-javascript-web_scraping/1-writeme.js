#!/usr/bin/node
// This script write a string to a file

const filepath = process.argv[2];
const data = process.argv[3];
const fs = require('fs');

fs.writeFile(filepath, data, 'UTF-8', (error) => {
  if (error) throw error;
});
