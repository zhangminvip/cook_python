def f(x, y, fontsize):
    s = 'sssss:{x}, tttt:{y}'
    print(locals(),type(locals()))
    print(s.format(**locals()))


# f(2,3,100)

# args = dict(x =2,y = 3, fontsize = 100)
# f(**args)


# args = (2,3,100)
# f(*args)


def ff(*args, **kwargs):
    print(args)
    print(kwargs)
    print('ff:', locals())
    # f(**locals()) #error


ff(1,1,2,3,fontsize = 'sdlfj', y = 'sldjf', x = 'sdlfkjj', z = 'sldkfj')

