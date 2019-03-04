import threading
import time

exitFlag = 1

'''how to use threads in subclasses'''


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)   # assert self._initialized, "Thread.__init__() not called"
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting ' + self.name)
        print_time(self.name, self.counter, 5 )
        print('exit' + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            pass
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)
thread1.start()
thread2.start()
print('exit main thread')


