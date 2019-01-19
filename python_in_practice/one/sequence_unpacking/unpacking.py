def f(x, y, fontsize):
    s = 'sssss:{x}, tttt:{y}'
    print(locals(),type(locals()))
    print(s.format(**locals()))


# f(2,3,100)

# args = dict(x =2,y = 3, fontsize = 100)
# f(**args)


# args = (2,3,100)
# f(*args)


def unpack(a):
    print (a)

def ff(*args, **kwargs): # not pass dict or tuple
    print(args)
    print(kwargs)
    print('ff:', locals())
    # unpack(*args)     # if you pass dict and tuple ,this is result
    # f(**locals()) #error
    f(*args, **kwargs)


# ff(1,1,2,3,fontsize = 'sdlfj', y = 'sldjf', x = 'sdlfkjj', z = 'sldkfj')
# ff((2,3,4))   # if you pass dict and tuple ,this is result
# ff(1,2, fontsize=100,sie=100)  # 参数和f函数的参数匹配，不能多也不能少
ff(1,2,3, fontsize=100)  #TypeError: f() got multiple values for argument 'fontsize'