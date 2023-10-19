#!/usr/bin/node
const size = process.argv[2];
let i = 0;
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else if (size > 0) {
  for (i; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
