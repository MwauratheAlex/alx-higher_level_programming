#!/usr/bin/node
//gets the contents of a webpage and stores it in a file.

const request = require("request");
const fs = require("fs");

const url = process.argv[2];
const filepath = process.argv[3];

request(url, (error, response, body) => {
	fs.writeFile(filepath, body, "utf-8");
});
