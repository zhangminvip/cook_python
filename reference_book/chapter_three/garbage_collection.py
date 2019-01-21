import sys

a = 37
b = 37
# b = a
c = []
c.append(b)
del c
b = 23

print(sys.getrefcount(a))