//
const readDatabase = require('../utils');

class StudentsController {
    static async getAllStudents(req, res) {
        const dbfile = process.argv[2];

        try {
            const students = await readDatabase(dbfile);
            let result = 'This is the list of our students:\n';

            const sortedFields = Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
            sortedFields.forEach(field => {
                result += `Number of students in ${field}: ${students[field].count}. List: ${students[field].names.join(', ')}\n`;
            });
            res.stat(200).send(result);
        } catch (error) {
            res.status(500).send('Cannot load database');
        }
    }
}

module.exports = StudentsController;