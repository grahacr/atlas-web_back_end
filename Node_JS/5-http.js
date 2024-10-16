// create small http server with different path endpoints

const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello Holberton School!\n');
    }
    else if (req.url == '/students') {
        const dbfile = process.argv[2];
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.write('This is the list of our students:\n');

        countStudents(dbfile)
            .then((output) => {
                res.write(`${output}\n`);
                res.end();
            })
            .catch (error => {
                res.end(error.message);
            });
    }
}).listen(1245);

module.exports = app;