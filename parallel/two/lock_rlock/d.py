import threading
import time


'''在add(), remove()方法中添加获取和释放锁是为了体现rlock与lock的区别，在这里省去也可以'''

class Box(object):
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0


    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()


def adder(box, items):
    while items > 0:
        # print('adding 1 item in the box')
        box.add()
        # time.sleep(2)
        items -= 1

def remover(box, items):
    while items > 0 :
        # print('removing 1 item in the box')
        box.remove()
        # time.sleep(2)
        items -= 1

items = 1000000
box = Box()
t1 = threading.Thread(target=adder, args=(box, items))
t2 = threading.Thread(target=remover, args=(box, items))
t1.start()
t2.start()
t1.join()
t2.join()
print('%s items still remain in the box' % box.total_items)

