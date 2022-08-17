#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let aux = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      aux++;
    }
  }
  return (aux);
};
