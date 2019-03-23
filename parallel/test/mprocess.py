# coding:utf-8

from multiprocessing import Process, Lock,Value
import os

'''
两个进程打印0~1000 
'''

def f(i):
    while True:
        # l.acquire()
        # if i.value > 1:
        #     i -= 1
        #     print(os.getpid(),i)
        #     l.release()
        # else:
        #     l.release()
        #     break
        with i.get_lock():
            if i.value  > -1:
                print(os.getpid(),i.value)
                i.value -= 1
            else:
                break


i = Value('d', 1000)
p1 = Process(target=f, args=(i,))
p2 = Process(target=f, args=(i,))
p1.start()
p2.start()
p1.join()
p2.join()


