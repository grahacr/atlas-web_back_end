//
const readDatabase = require('../utils');

class StudentsController {
    static async getAllStudents(req, res) {

        const dbfile = process.argv[2];

        try {
            const students = await readDatabase(dbfile);
            let response = 'This is the list of our students:\n';

            Object.keys(students).sort().forEach((field) => {
                response += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
            });

            res.status(200).send(response);
        } catch (error) {
            res.status(500).send('Cannot load database');
        }
    }

    static async getAllStudentsByMajor(res, req) {
        
    }
}