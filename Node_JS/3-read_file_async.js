//
const fs = require('fs').promises;
const path = require('path');

function countStudents(filePath) {
    return fs.readFile(filePath, 'utf-8')
        .then(fileContent => {
        const lines = fileContent.trim().split('\n');
        const students = {};

        lines.slice(1).forEach(line => {
            const fields = line.split(',');
            const field = fields[3].trim();
            const student = fields[0];

            if (field) {
                // initialize students array with field if not already existing field
                if (!students[field]) {
                    students[field] = { count: 0, names: [] };
                }
                // store student names and count of each student in each field
                students[field].count += 1;
                students[field].names.push(student);
            }
        });
        // get total students object using reduce on the values of students array
        const totalStudents = Object.values(students).reduce(
            (sum, entry) => sum + entry.count, 0);

        console.log(`Number of students: ${totalStudents}`);

        // iterate through each field and output student info in each field 
        for (const field in students) {
                console.log(`Number of students in ${field}: ${students[field].count}. List: ${students[field].names.join(', ')}`);
            }
        })
        .catch(error => {
            throw new Error('Cannot load the database');
        });
}

module.exports = countStudents;