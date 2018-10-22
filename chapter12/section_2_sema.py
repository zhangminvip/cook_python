import threading
import time
# Worker thread
def worker(n, sema):
    # Wait to be signaled
    sema.acquire()
    time.sleep(2)
    # Do some work
    print('Working', n)
    sema.release()

# def run(sema):
#     while True:
#         time.sleep(2)
#         sema.release()
#         sema.release()
#         sema.release()
#         sema.release()


# Create some threads

sema = threading.Semaphore(5)

nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()

# t2 = threading.Thread(target=run, args=(sema,))
# t2.start()


