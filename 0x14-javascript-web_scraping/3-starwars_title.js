#!/usr/bin/node
// The script prints the title of a movie based on an integer passed to the command line

const request = require('request');

const options = {
  url: `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  method: 'GET'
};

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
