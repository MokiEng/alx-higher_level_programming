#!/usr/bin/node

exports.converter = function (base) {
  if (this > 0) {
    (this / base >> 0).converter(base);
    console.log(this % base);
  };
};
