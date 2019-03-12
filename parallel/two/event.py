import time
from threading import Thread, Event
import random

items = []
event = Event()


class consumer(Thread):
    def __init__(self):
        Thread.__init__(self, items, event)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print('Consumer notify: %d popped from list by %s' %(item, self.name))


class producer(Thread):
    def __init__(self, integers, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        global items
        for i in range(100):
            time.sleep(2)
            item = random.randint(0, 256)
            self.items.append(item)
            print('Producer notify: item N %d appended to list by %s' % (item, self.name))
            self.event.set()
            self.event.clear()


