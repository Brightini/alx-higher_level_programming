#!/usr/bin/node
// This script gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const options = {
  url: process.argv[2],
  method: 'GET'
};

const filepath = process.argv[3];

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  fs.writeFile(filepath, data, 'UTF-8', (error) => {
	if (error) throw error;
  });
});
