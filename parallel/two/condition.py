from threading import Thread, Condition
import time

items = []

condition = Condition()

class consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items
        condition.acquire()
        if len(items) == 0:
            print('Comsumer notify: no item to consume')
            condition.wait()
        items.pop()
        print('Consumer notify: consumed 1 item')
        print('Consumer notify: items to consume are ' + str(len(items)))

        condition.notify()
        condition.release()

    def run(self):
        for _ in range(0, 4):
            time.sleep(5)
            self.consume()

class producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global items
        global condition

        condition.acquire()
        if len(items) == 2:
            print('Producer notify: items producted are ' + str(len(items)))
            print('Producer notify: stop the production')
            condition.wait()

        items.append(1)
        print('Producer notify: total items producted' + str(len(items)))
        condition.notify()
        condition.release()


    def run(self):
        for _ in range(3):
            time.sleep(2)
            self.produce()



consumer = consumer()
producer = producer()
consumer.start()
producer.start()
producer.join()
consumer.join()