//create similar more complex http server using express module instead
//after downloading express

const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
    const dbfile = process.argv[2];
    res.status(200).write('This is the list of our students:\n');

    countStudents(dbfile)
        .then((output) => {
            res.write(`${output}\n`);
            res.end();
        })
        .catch((error) => {
            res.status(500).send(error.message);
        });
}).listen(port);

module.exports = app;