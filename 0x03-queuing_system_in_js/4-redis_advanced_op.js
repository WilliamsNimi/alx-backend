import { createClient } from 'redis';
import redis from 'redis';

const client = createClient()
      .on('error', err => console.log('Redis client not connected to the server: ', err))
      .on('connect', () => console.log('Redis client connected to the server'));

client.hset('HolbertonSchools', 'Portland', '50', (err, reply) => {
    redis.print(`Reply: ${reply}`);
});
client.hset('HolbertonSchools', 'Seattle', '80', (err, reply) => {
    redis.print(`Reply: ${reply}`);
});
client.hset('HolbertonSchools', 'New York', '20', (err, reply) => {
    redis.print(`Reply: ${reply}`);
});
client.hset('HolbertonSchools', 'Bogota', '20', (err, reply) => {
    redis.print(`Reply: ${reply}`);
});
client.hset('HolbertonSchools', 'Cali', '40', (err, reply) => {
    redis.print(`Reply: ${reply}`);
});
client.hset('HolbertonSchools', 'Paris', '2', (err, reply) => {
    redis.print(`Reply: ${reply}`);
});
client.hgetall('HolbertonSchools', function(err, object){
    console.log(object);
});

