#!/usr/bin/node

const request = require('request');

function printMovieCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (!characterError && characterResponse.statusCode === 200) {
            const characterData = JSON.parse(characterBody);
            const characterName = characterData.name;
            console.log(characterName);
          } else {
            console.log(`Failed to fetch character data for URL: ${characterUrl}`);
          }
        });
      });
    } else {
      console.log(`Failed to fetch movie data for ID: ${movieId}`);
    }
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.log("Please provide a movie ID.");
} else {
  printMovieCharacters(movieId);
}
