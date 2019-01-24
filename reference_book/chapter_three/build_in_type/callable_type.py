def foo(x, y):
    return x + y

print(foo.__code__)
print(foo.__dict__)
print(foo.__defaults__)
print(foo.__globals__)
print(foo.__closure__)


class Foo(object):
    def instance_method(self, arg):
        print('instance method')

    @classmethod
    def class_method(cls, arg):
        print('class method')

    @staticmethod
    def static_method(args):
        print('static method')

    def __call__(self, x):
        print(2*x)



f = Foo()
print(id(f))   # decimal
meth = f.instance_method   #python3: method object
meth(37)
umeth = Foo.instance_method # python3: function object has no attribute '__self__'
umeth(f, 37)
# umeth('haha',37)
print('*'*50)
print(type(meth))
print(meth.__name__, meth.__class__, meth.__func__, meth.__self__)  # hexadecimal
print(type(umeth))

print(len.__name__, type(len), len.__self__)

f(2)