#!/usr/bin/node
const filesys = require('fs');
try {
  const data = filesys.readFileSync(process.argv[2], 'utf8');
  console.log(data);
} catch (err) {
  console.log(err);
}
