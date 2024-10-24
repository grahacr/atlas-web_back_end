import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

client.connect().then(() => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err) => {
        if (err) {
            print(err);
        } else {
            print(null, `Successfully set ${schoolName} to ${value}`);
        }
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error('Error retrieving value for schoolName');
        } else {
            console.log(`Value for ${schoolName}: ${reply}`);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFransisco', '100');
displaySchoolValue('HolbertonSanFransisco');