//
import { createClient, print } from "redis";

const subscriber = createClient();

subscriber.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
    subscriber.subscribe('holberton school channel');
});

subscriber.on('message', (channel, message) => {
    console.log(`${message}`);
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});