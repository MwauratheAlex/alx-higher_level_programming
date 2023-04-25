#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const endpoint = process.argv[2];
const wedgeAntillesId = 18;

request(endpoint, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const films = JSON.parse(body).results;

  const wedgeAntillesFilms = films.filter((film) =>
    film.characters.some((character) =>
      character.endsWith('/' + wedgeAntillesId + '/')
    )
  );

  console.log(wedgeAntillesFilms.length);
});
