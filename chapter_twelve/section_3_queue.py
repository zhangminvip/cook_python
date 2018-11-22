from queue import Queue
import queue
from threading import Thread, Event
import logging
import time

_sentinel = object()


def producer(out_q):
    # while True:
    try:
        for i in range(10):
            evt = Event()

            data = i
            out_q.put((data, evt))
            print('generate one')
            if i == 5:
                print('Waiting for product 5 to be consumed')
                evt.wait()
                print('producer: product 5 is consumed')
        print('Put a termination signal into the task queue')
        out_q.put((_sentinel, evt))
    except queue.Full:
        print('queue is full')
        # logging.warning('queue item %r',data)

def consumer(in_q):
    # time.sleep(2)
    while True:
        try:
            data, evt = in_q.get(timeout=5.0)
            if data is _sentinel:
                break
            print(data,'is consumed')
            in_q.task_done()
            evt.set()
        except queue.Empty:
            print('no task')


q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()
t2.start()

# q.join()
