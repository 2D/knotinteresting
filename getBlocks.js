
const request = require('./node_modules/request');

exports.getBlocks =  function (callback) {
  request('https://api.etherscan.io/api?module=block&action=getblockreward&blockno=2165403',
    { json: true },
    (err, res, body) => {
      if (err) {
        return console.log(err);
      }
      console.log("pre callback");
      console.log(callback(body));
  });
};
