#!/usr/bin/node
//prints the title of a Star Wars movie where the episode number matches a given integer

const request = require("request");
const endpoint = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

request(endpoint, (error, response, body) => {
	console.log(JSON.parse(body).title);
});
