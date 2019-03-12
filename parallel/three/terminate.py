import multiprocessing
import time

def foo():
    print('starting function')
    time.sleep(0.1)
    print('finish function')

if __name__=='__main__':
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running :', p, p.is_alive())
    p.terminate()
    print('Process terminate',p, p.is_alive())
    p.join()
    print('Process joined', p, p.is_alive())
    print('Process exit code', p.exitcode)