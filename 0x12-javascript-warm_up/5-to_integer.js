#!/usr/bin/node
let number = process.argv[2]

if (process.argv.length == 2) {
    console.log("Not a number");
}
else {
    console.log(`My number: ${number}`);
}
