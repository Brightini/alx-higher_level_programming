#!/usr/bin/node
// This script prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

let count = 0;

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  for (const movie of json.results) {
    if (movie.characters.includes(
      'https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
