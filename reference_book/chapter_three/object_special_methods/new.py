import traceback
class Example():

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        super().__init__()
        self.address = 'Los Angeles'

    def __del__(self):
        print('del')


# e = Example()
# print(e.address)


e = Example.__new__(Example)
if isinstance(e,Example):
    print('e is Example')
    e.__init__()
    print(e.address)


del e # will only reduce a reference of an object , not necessarily call __del__()
try:
    print(e.address)
except:
    traceback.print_exc()

print('end')

