#!/usr/bin/node

const number = process.argv[2];
if (process.argv.length === 2 || isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
