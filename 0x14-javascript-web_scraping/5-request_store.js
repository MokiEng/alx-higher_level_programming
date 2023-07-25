#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Function to fetch the webpage content and store it in a file
function getWebpageContent(url, filePath) {
  request.get(url, (err, response, body) => {
    if (err) {
      console.error(err);
    } else {
      if (response.statusCode === 200) {
        fs.writeFile(filePath, body, 'utf-8', (writeErr) => {
          if (writeErr) {
            console.error(writeErr);
          } else {
            console.log(`Webpage content saved to "${filePath}"`);
          }
        });
      } else {
        console.error(`Failed to fetch the webpage. Status code: ${response.statusCode}`);
      }
    }
  });
}

// Read the command-line arguments (URL and file path)
const url = process.argv[2];
const filePath = process.argv[3];

// Call the function to fetch the webpage content and store it in the file
getWebpageContent(url, filePath);
