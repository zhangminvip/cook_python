from queue import Queue
from threading import Thread, Event

_sentinel = object()


def producer(out_q):
    # while True:
    for i in range(10):
        evt = Event()

        data = i
        out_q.put((data, evt))
        if i == 5:
            print('wait')
            evt.wait()
            print('complete')
    out_q.put((_sentinel, evt))


def consumer(in_q):
    while True:
        data, evt = in_q.get()
        if data is _sentinel:
            break
        print(data)
        in_q.task_done()
        evt.set()


q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()
t2.start()

# q.join()
