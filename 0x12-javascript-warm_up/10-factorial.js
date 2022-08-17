#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);
function factorial (num) {
  if (num === 0) {
    return 1;
  }
  if (!num) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(num));
