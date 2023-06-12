#!/usr/bin/node
const args = process.argv.slice(2).map(arg => parseInt(arg, 10));
const uniqueArgs = [...new Set(args)];
const sortedArgs = uniqueArgs.sort((a, b) => b - a);

if (sortedArgs.length < 2) {
  console.log(0);
} else {
  console.log(sortedArgs[1]);
}
