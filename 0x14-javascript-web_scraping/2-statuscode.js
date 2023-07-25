#!/usr/bin/node
#a script that display the status code of a GET request.

const request = require('request');

request(process.argv[2], function (_err, res) {
  console.log('code:', res.statusCode); // Print the response status code if a response was received
});
