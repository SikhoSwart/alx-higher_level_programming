#!/usr/bin/node
exports.esrever = function (list) {
  const newL = [];
  let i = list.length - 1;
  for (i; i >= 0; i--) {
    newL.push(list[i]);
  }
  return newL;
};
