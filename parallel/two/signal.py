# coding:utf-8

import threading
import time
import random

'''信号量本身自带锁'''
semaphore = threading.Semaphore(0)

def consumer1():
    print('consumer1 is waitting')
    semaphore.acquire()
    print('consumer1 notify: consumed item number %s' % item)


def consumer2():
    print('consumer2 is waiting')
    semaphore.acquire()
    print('consumer2 notify')

def producer():
    global item
    time.sleep(2)
    item = random.randint(0, 1000)
    print('producer notify: produced item number %s' % item)
    semaphore.release()
    semaphore.release()


for _ in range(5):
    t1 = threading.Thread(target=consumer1)
    t2 = threading.Thread(target=producer)
    t3 =threading.Thread(target=consumer2)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

