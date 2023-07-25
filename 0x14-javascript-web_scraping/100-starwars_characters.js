#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
req.get(apiUrl + movie_id, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const j of dd) {
    req.get(j, function (error, response, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
