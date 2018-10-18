from threading import Thread, Event
import time
def countdown(n, start_evt):
    print('countdown starting')
    start_evt.set()
    while n > 0:
        print('T-minus',n)
        n -= 1
        time.sleep(1)

start_evt = Event()
print('launch countdown')
t = Thread(target=countdown, args=(10,start_evt))
t.start()

start_evt.wait()
print('countdown is running')