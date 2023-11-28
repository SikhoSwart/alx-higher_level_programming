#!/usr/bin/node
const request = require('request');
const Url = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
request(Url, function (_error, _response, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
