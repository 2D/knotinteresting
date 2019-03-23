var http = require('http');
var fs = require('fs');
var blocks = require('./getBlocks');

var routes = {};

http.createServer(function (req, res) {
  fs.readFile('listBlocks.html', function(err, data) {
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.write(data);
      res.end();
    });
}).listen(8080);

function blockCallback(resultData) {
  return "data from callback" + resultData.status;
}
