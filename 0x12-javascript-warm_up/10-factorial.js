#!/usr/bin/node
function factorial (num) {
  if (!num) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
