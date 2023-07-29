#!/usr/bin/node
// This script prints the number of movies where the character “Wedge Antilles” is present

const request = require('require');

const options = {
  url: process.argv[2],
  method: 'GET'
};

const count = 0;

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  for (const movie of json.characters) {
    if (movie.characters.includes('18') {
      count++;
    }
  }
  console.log(count);
});
