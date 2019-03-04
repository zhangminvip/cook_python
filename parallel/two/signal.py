# coding:utf-8

import threading
import time
import random

'''信号量本身自带锁'''
semaphore = threading.Semaphore(0)

def consumer():
    print('consumer is waitting')
    semaphore.acquire()
    print('consumer notify: consumed item number %s' % item)

def producer():
    global item
    time.sleep(10)
    item = random.randint(0, 1000)
    print('producer notify: produced item number %s' % item)
    semaphore.release()


for _ in range(5):
    t1 = threading.Thread(target=consumer)
    t2 = threading.Thread(target=producer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

