import multiprocessing
import time

def foo(i):
    time.sleep(3)
    print('called function in process: %s' %i)
    return


if __name__=='__main__':
    Process_job = []
    for i in range(5):
        p  = multiprocessing.Process(target=foo, args=(i,))
        Process_job.append(p)
        p.start()
        # time.sleep(5)
        p.join()