from threading import Thread
from time import sleep

'''use thread'''


class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = 'hello parallel python'

    def print_message(self):
        print(self.message)

    def run(self):
        print('thread starting\n')
        x = 0
        while ( x < 10):
            self.print_message()
            sleep(2)
            x += 1
        print('Thread Ended')

print('Process Started')
hello_Python = CookBook()
hello_Python.start()
print('Process Ended')