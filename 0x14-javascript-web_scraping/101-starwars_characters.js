#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
const Name = {};
request(url, function (error, response, body) {
  if (error) { return; }
  let count = 0;
  const characterList = JSON.parse(body).characters;
  for (let index = 0; index < characterList.length; index++) {
    request(characterList[index], function (error, response, body) {
      if (error) { return; }
      const character = JSON.parse(body);
      Name[character.url] = character.name;
      count++;
      if (count === characterList.length) {
        for (const char of characterList) {
          console.log(Name[char]);
        }
      }
    });
  }
});
