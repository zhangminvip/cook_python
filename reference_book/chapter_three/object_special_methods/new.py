class Example(object):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        super().__init__()
        self.address = 'Los Angeles'


# e = Example()
# print(e.address)


e = Example.__new__(Example)
if isinstance(e,Example):
    print('e is Example')
    e.__init__()
    print(e.address)




