import multiprocessing
from multiprocessing import Process, Pool
import os
import pika
import time
import sys



def create_worker(useless):

    def callback(ch, method, properties, body):
        print("%s [x] Received %r" % (os.getpid(),body))
        time.sleep(body.count(b'.'))
        print("%s [x] Done" % os.getpid())
        ch.basic_ack(delivery_tag = method.delivery_tag)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*]{} Waiting for messages. To exit press CTRL+C'.format(os.getpid()))
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,queue='task_queue')

    channel.start_consuming()
    sys.stdout.flush()

print(multiprocessing.cpu_count())
pool = Pool(processes=5)
pool.map(create_worker, (1,2,3,4,5))
# time.sleep(100)


