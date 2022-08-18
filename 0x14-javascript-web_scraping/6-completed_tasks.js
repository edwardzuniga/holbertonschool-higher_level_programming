#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (!error) {
    const completed = {};
    JSON.parse(body).forEach((tasks) => {
      if (tasks.completed && completed[tasks.userId] === undefined) {
        completed[tasks.userId] = 1;
      } else if (tasks.completed) {
        completed[tasks.userId] += 1;
      }
    });
  }
});
