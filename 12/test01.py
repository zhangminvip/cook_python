#coding:utf-8
import time

class CountdownTask:

    def __init__(self):
        self._running=True

    def ternimate(self):
        self._running = False


    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)



def countdown(n):
    while n > 0:
        print ('T-minus',n)
        n -= 1
        time.sleep(5)

from threading import Thread
c = CountdownTask()
# t = Thread(target=c.run, args=(10,))
# t.start()
# c.ternimate()
import multiprocessing
p = multiprocessing.Process(target=c.run, args=(10,))
p.start()



