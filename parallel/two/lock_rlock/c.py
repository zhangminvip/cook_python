import threading

shared_resource_with_lock = 0
shared_resource_without_lock = 0
COUNT = 1000000
shared_resource_lock =threading.Lock()



def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()

def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()


def increment_without_lock():
    '''为什么最后值不等于0: 因为shared_resource_without_lock +1执行后，
    -1操作可能执行了几次了，如果我们把+1后的值赋给全局变量，就相当于-1白做了，（没赋值就跳转（加锁就是杜绝这种情况），他赋值了，他就白做了，赋值后跳转，他赋值了，再跳回来，我就白做了）（他赋值被我改了，我赋值被他改了）
    加锁操作就是让次都不白做，不中断自增和自减，原子操作概念：不中断自增自减'''
    global shared_resource_without_lock
    for i in range(COUNT):
        shared_resource_without_lock += 1

def decrement_without_lock():
    global shared_resource_without_lock
    for i in range(COUNT):
        shared_resource_without_lock -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print('the value of shared variable with lock management is %s' % shared_resource_with_lock)
    print('the value of shared variable with race condition is %s' % shared_resource_without_lock)
