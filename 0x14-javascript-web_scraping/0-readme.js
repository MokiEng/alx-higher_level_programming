#!/usr/bin/node

const fs = require('fs');

#Function to read and print the content of the file
function readAndPrintFileContent(filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}
