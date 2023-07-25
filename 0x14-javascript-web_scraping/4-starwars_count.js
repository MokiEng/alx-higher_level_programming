#!/usr/bin/node
const request = require('request');
const swUri = process.argv[2];
let t = 0;

request(swUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let k = 0; k < body.length; ++k) {
    const characters = body[k].characters;

    for (let m = 0; m < characters.length; ++m) {
      const character = characters[m];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        t += 1;
      }
    }
  }

  console.log(t);
});
