#!/usr/bin/node

const fs = require('fs');

#Function to read and print the content of the file
function readAndPrintFileContent(filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error('Error reading the file:', err);
    } else {
      console.log('File content:');
      console.log(data);
    }
  });
}
