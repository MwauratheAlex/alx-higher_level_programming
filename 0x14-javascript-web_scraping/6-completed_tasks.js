#!/usr/bin/node
// computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

const completedTasks = {};

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const todos = JSON.parse(body);

  Object.entries(todos).forEach((todo) => {
    if (todo[1].completed === true) {
      if (todo[1].userId in completedTasks) {
        completedTasks[todo[1].userId]++;
      } else {
        completedTasks[todo[1].userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
