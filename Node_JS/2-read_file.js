// parse through csv database and log data
// modules needed
const fs = require('fs');
const path = require('path');

// function with filePath included
function countStudents(filePath) {
    try {
        // read file and parse lines at new line
        const data = fs.readFileSync(filePath, 'utf-8');
        const lines = data.trim().split('\n');

        // initialize students array which includes field, with list of student names and their count
        const students = {};

        // parse each line to identify fields and store students names and count
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
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

// export function to be used
module.exports = countStudents;