#!/usr/bin/node
const Character = 'X';
const number = process.argv[2];
if (number === undefined || isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log(Character.repeat(number));
  }
}
