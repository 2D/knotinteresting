var http = require('http');
var blocks = require('./getBlocks');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write("Blocks found: " + blocks.getBlocks());
  res.end();
}).listen(8080);
