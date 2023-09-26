#!/usr/bin/node

const request = require('request');
const url_link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url_link, (err, res, body) => {
  if (err) console.log(err);
  else console.log(JSON.parse(body).title);
});
