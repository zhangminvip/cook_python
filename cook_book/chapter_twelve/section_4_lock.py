import threading
from threading import Semaphore

class SharedCounter:
    '''
        A counter object that can be shared by multiple threads.
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta = 1):
        with self._value_lock:
            self._value += delta

    def decr(self, delta = 1):
        with self._value_lock:
            self._value -= delta

class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    _lock = threading.RLock()
    def __init__(self, initial_value = 0):
        self._value = initial_value

    def incr(self,delta=1):
        '''
        Increment the counter with locking
        '''
        with SharedCounter._lock:
            self._value += delta

    def decr(self,delta=1):
        '''
        Decrement the counter with locking
        '''
        with SharedCounter._lock:
             self.incr(-delta)


_fetch_url_sema = Semaphore(5)
import urllib.request
def fetch_url(url):
    with _fetch_url_sema:
        return urllib.request.urlopen(url)