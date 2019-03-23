from multiprocessing import Process
import pika
import time


def create_worker():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                        queue='task_queue')

    channel.start_consuming()



p1 = Process(target=create_worker, args=())
p2 = Process(target=create_worker, args=())
p1.start()
p2.start()
p1.join()
p2.join()