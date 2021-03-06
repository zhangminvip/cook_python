import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write('Usage: %s [info] [warn] [error]' % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

print('[*] Waiting for logs, To exits press CTRL + C')


def call_back(ch, method, properties, body):
    print('[x] %s %s' % (method.routing_key, body))


channel.basic_consume(call_back, queue=queue_name, no_ack=True)
channel.start_consuming()