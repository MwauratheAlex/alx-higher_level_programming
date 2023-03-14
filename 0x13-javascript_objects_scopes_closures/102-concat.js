#!/usr/bin/node

const fs = require('fs');
const paths = process.argv.slice(2);

if (paths.length === 3) {
  fs.readFile(paths[0], (err, dt) => {
    if (err) throw err;
    fs.appendFile(paths[2], dt.toString(), (err) => { if (err) throw err; });
  });

  fs.readFile(paths[1], (err, dt) => {
    if (err) throw err;
    fs.appendFile(paths[2], dt.toString(), (err) => { if (err) throw err; });
  });
}
