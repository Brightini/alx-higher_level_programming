#!/usr/bin/node
function callMeMoby (x, callBack) {
  for (let i = 0; i < x; i++) {
    callBack();
  }
}

module.exports.callMeMoby = callMeMoby;
