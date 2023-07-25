#!/usr/bin/node

const request = require('request');

// Function to fetch the movie title based on the movie ID
function getMovieTitle(movieId) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
  request.get(url, (err, response, body) => {
    if (err) {
      console.error('Error occurred while making the request:', err);
    } else {
      if (response.statusCode === 200) {
        const movieData = JSON.parse(body);
        console.log(movieData.title);
      } else {
        console.error(`Movie with ID ${movieId} not found.`);
      }
    }
  });
}

// Read the command-line argument (movie ID)
const movieId = process.argv[2];

// Call the function to fetch and print the movie title
getMovieTitle(movieId);
