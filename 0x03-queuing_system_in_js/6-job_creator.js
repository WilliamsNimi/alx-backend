import { createQueue } from 'kue';

let queue = createQueue();

const job = queue.create('push_notification_code', {
    phoneNumber: '0908734256',
    message: 'Yo! Wagwan',
}).save( function(err) {
    if (!err){
	console.log(`Notification job created: ${job.id}`);
    }
});

job.on('complete', () => console.log(`Notification job completed`)).on('failed', (err) => console.log(`Notification job failed: ${err}` ));
