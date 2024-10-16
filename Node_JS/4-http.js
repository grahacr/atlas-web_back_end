// require node http module to create small HTTP server
const http = require('http');

// assign server to variable with text display in page body for any endpoint as plain text
const app = http.createServer((req, res) => {
    res.write('Hello Holberton School!');
    res.end();
}).listen(1245);

module.exports = app;
