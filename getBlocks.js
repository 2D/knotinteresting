
const request = require('./node_modules/request');

var resultData = {};

exports.getBlocks = function () {
  request('https://api.etherscan.io/api?module=block&action=getblockreward&blockno=2165403',
    { json: true },
    (err, res, body) => {
      if (err) {
        return console.log(err);
      }
      resultData = body;
      return console.log(JSON.stringify(resultData));
  });
  return "fred";
};
