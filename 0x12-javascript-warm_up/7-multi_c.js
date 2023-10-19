#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  const occ = process.argv[2];
  while (i < occ) {
    console.log('C is fun');
    i++;
  }
}
