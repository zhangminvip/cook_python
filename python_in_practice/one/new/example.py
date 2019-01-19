class Foo(object):

    # price = 50

    def __new__(cls, *args, **kwargs):
        inst = object.__new__(cls, *args, **kwargs)
        print(inst)
        return inst

    def __init__(self, price = 50):
        self.price = price


    def how_much_of_book(self, n):
        print(self)
        return self.price * n


# foo = Foo()
# print(foo.how_much_of_book(10))
# print(dir(Foo))


class Inch(float):
    "Convert from inch to meter"
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg*0.0254)

# print(Inch(12))

