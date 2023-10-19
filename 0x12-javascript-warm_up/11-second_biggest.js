#!/usr/bin/node
const args = process.argv.slice(2);
let Max = 0;
if (args.length > 1) {
  const integers = args.map(Number);
  integers.sort((a, b) => b - a);
  Max = integers[1];
}
console.log(Max);
