#!/usr/bin/node

const request = require('request');
const swUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
request(swUri, function (_err, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let k = 0; k < characters.length; ++k) {
    request(characters[k], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
