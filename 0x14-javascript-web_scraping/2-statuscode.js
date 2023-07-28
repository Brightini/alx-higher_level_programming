#!/usr/bin/node
// This script displays the status code of a GET request

const url = process.argv[3];
const request = require('request');

request.get(url, (error, response) => {
  if (error) throw error;
  console.log('code: ', response.statusCode);
});
