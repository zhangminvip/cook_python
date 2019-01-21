def compare(a, b):
    if a is b:
        print(1)
    if a == b:
        print(2)
    if type(a) is type(b):
        print(3)

a = 2
b = 2
print(id(a), id(b)) # python2/3 will reuse memory
compare(a, b)
