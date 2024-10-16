const fs = require('fs');
const path = require('path');

function countStudents(filePath) {
    try {
        const data = fs.readFileSync(filePath, 'utf-8');
        const lines = data.trim().split('\n');
        const students = {};

        lines.slice(1).forEach(line => {
            const fields = line.split(',');
            const field = fields[3].trim();
            const student = fields[0];

            if (field) {
                if (!students[field]) {
                    students[field] = { count: 0, names: [] };
                }
                students[field].count += 1;
                students[field].names.push(student);
            }
        });

        const totalStudents = Object.values(students).reduce(
            (sum, entry) => sum + entry.count, 0);

        console.log(`Number of students: ${totalStudents}`);
        console.log('Students Object:', students);

        for (const field in students) {
                console.log(`Number of students in ${field}: ${students[field].count}. List: ${students[field].names.join(', ')}`);
            }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;