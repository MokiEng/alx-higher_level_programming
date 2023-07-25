#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (err, _res, body) {
  if (err) {
    console.log(err);
  } else if (_res.statusCode === 200) {
    const completed = {};
    const tasks_comp = JSON.parse(body);
    for (const val in tasks_comp) {
      const task = tasks_comp[val];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + _res.statusCode);
  }
});
