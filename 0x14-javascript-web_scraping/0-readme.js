#!/usr/bin/node

const fs = require('fs');

#Function to read and print the content of the file
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
