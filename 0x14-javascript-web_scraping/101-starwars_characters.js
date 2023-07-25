#!/usr/bin/node

const request = require('request');

// Function to get all characters of a Star Wars movie
function getMovieCharacters(movieId) {
  const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;
  request.get(apiUrl, (err, response, body) => {
    if (err) {
      console.error(, err);
    } else {
      if (response.statusCode === 200) {
        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;

        // Function to fetch character names based on URLs
        function fetchCharacterName(characterUrl) {
          request.get(characterUrl, (err, response, body) => {
            if (err) {
              console.error(err);
            } else {
              if (response.statusCode === 200) {
                const characterData = JSON.parse(body);
                console.log(characterData.name);
              } else {
                console.error(`Failed to fetch character data. Status code: ${response.statusCode}`);
              }
            }
          });
        }

        // Fetch and print character names one by one
        characterUrls.forEach(fetchCharacterName);
      } else {
        console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
      }
    }
  });
}

// Read the command-line argument (Movie ID)
const movieId = process.argv[2];

// Call the function to get and print all characters of the Star Wars movie
getMovieCharacters(movieId);
