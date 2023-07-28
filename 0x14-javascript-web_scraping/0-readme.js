#!/usr/bin/node
// This script reads and prints the content of a file

const filepath = process.argv[2];
const fs = require('fs');

fs.readFile(filepath, 'UTF-8', (error, content) => {
  if (error) throw error;
  console.log(content.toString());
});
