#!/usr/bin/node

const request = require('request');

// Function to compute the number of completed tasks by user ID
function countCompletedTasks(apiUrl) {
  request.get(apiUrl, (err, response, body) => {
    if (err) {
      console.error(err);
    } else {
      if (response.statusCode === 200) {
        const todos = JSON.parse(body);
        const completedTasks = {};

        todos.forEach((todo) => {
          if (todo.completed) {
            if (completedTasks[todo.userId]) {
              completedTasks[todo.userId]++;
            } else {
              completedTasks[todo.userId] = 1;
            }
          }
        });

        console.log(completedTasks);
      } else {
        console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
      }
    }
  });
}
