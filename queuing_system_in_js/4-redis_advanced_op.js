import { createClient, print } from "redis";

const client = createClient();

client.on('error', (error) => {
    console.log(`Redis client not connected to the server`);
});

client.connect().then(() => {
    console.log('Redis client connected to the server');

    client.hSet('HolbertonSchools', 'Portland', 50, print);
    client.hSet('HolbertonSchools', 'Seattle', 80, print);
    client.hSet('HolbertonSchools', 'New York', 20, print);
    client.hSet('HolbertonSchools', 'Bogota', 20, print);
    client.hSet('HolbertonSchools', 'Cali', 40, print);
    client.hSet('HolbertonSchools', 'Paris', 2, print);

    client.hGetAll('HolbertonSchools', (err, reply) => {
        if (err) {
            console.error('Error retrieving hash');
        } else {
            console.log(reply);
        }
    });
}).catch((error) => {
    console.error('Connection error:', error);
});