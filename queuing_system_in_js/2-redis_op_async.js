import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

client.connect().then(() => {
    console.log('Redis client connected to the server');
});

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err) => {
        if (err) {
            print(err);
        } else {
            print(null, `Successfully set ${schoolName} to ${value}`);
        }
    });
}

async function displaySchoolValue(schoolName) {
    try {
        const reply = await getAsync(schoolName);
        console.log(`Value for ${schoolName}: ${reply}`);
    } catch (error) {
        console.error(`Error retrieving value for ${schoolName}`);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFransisco', '100');
displaySchoolValue('HolbertonSanFransisco');