import import_test
import time
class Foo(object):
    pass

# print(type(Foo), Foo.__name__, Foo.__bases__,
#       Foo.__module__,)

f = Foo()
# print(type(f), f.__class__, f.__dict__)


print(time.__dict__)
print(time.__name__)
print('__file__: ',import_test.__file__)
print(type(time.__dict__['strftime'])) # <class 'builtin_function_or_method'>
print(time.__dict__['strftime'].__class__)
# print('__path__: ',import_test.__path__)