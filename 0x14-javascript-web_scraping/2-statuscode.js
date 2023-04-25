#!/usr/bin/node
//display the status code of a GET request.

const url = process.argv[2]
const request = require('request')

request(url, (error, response, body) => {
  console.log('code:', response.statusCode);
});
