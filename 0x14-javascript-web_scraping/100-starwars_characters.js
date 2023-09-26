#!/usr/bin/node

const request = require('request');
const urllink = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url_link, (err, res, body) => {
  if (err) console.log(err);
  else {
    JSON.parse(body).characters.forEach(character => {
      request.get(character, (err, res, body) => {
        if (err) console.log(err);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});
