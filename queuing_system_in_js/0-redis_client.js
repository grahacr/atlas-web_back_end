import { createClient} from 'redis';

const client = createClient();

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

client.connect().then(() => {
    console.log('Redis client connected to the server');
});