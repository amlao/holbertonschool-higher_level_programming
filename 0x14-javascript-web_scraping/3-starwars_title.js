#!/usr/bin/node
let request = require('request');
request
  .get('http://swapi.co/api/films/' + process.argv[2],
    (error, response, text) => {
      if (error) throw error;
      console.log(JSON.parse(text).title);
    });
