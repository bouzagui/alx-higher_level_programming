#!/usr/bin/node

const Str = String('C is fun');
const number = process.argv[2];
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log(Str.replace(number));
  }
}
