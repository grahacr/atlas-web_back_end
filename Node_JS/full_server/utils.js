//
import fs from 'fs/promises';

async function readDatabase(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf-8');
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
        return students;
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = readDatabase;