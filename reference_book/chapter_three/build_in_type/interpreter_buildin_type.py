import sys

c = compile('for i in range(5): print(i)','','exec')
print(c.co_name)
print(c.co_nlocals)
print(c.co_argcount)
print(c.co_filename)
print(c.co_stacksize)
print(c.co_flags)
# exec(c)


try:
    a = 1
    raise IOError
except:
    print(sys.exc_info())
    print(sys.exc_info()[2].tb_frame)
    print(sys.exc_info()[2].tb_frame.f_lasti)
    print(sys.exc_info()[2].tb_frame.f_lineno)
    print(sys.exc_info()[2].tb_frame.f_lineno)
    print(sys.exc_info()[2].tb_frame.f_locals)
    print(sys.exc_info()[2].tb_frame.f_code)
    print(sys.exc_info()[2].tb_frame.f_trace)
    print(sys.exc_info()[2].tb_frame.f_back)
    print(sys.exc_info()[2].tb_lineno)
    print(sys.exc_info()[2].tb_next)


print('*'*50)

def gen(x):
    for i in range(x):
        print(i)
        s = (yield)
        print(s)
        # yield y


g = gen(10)
print(g.gi_code)
print(g.gi_frame)
print(g.gi_frame.f_locals)
print(g.gi_running)


print(type(len))
print(type('sldf'.__len__))
print(type(g.__next__))
g.__next__()
g.__next__()
g.send('python')
g.__next__()
g.__next__()
g.__next__()


print('*'*20)
s = slice(2,5)
print(s.start, s.stop, s.step)

print('*'*20)



class Example(object):
    def __getitem__(self, item):
        print(item)

e = Example()
e[3, ..., 4]


