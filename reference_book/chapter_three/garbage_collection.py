import sys

a = 37
# b = 37
# # b = a
# c = []
# c.append(b)
# del c
# b = 23
b = {}
b['a'] = a
del b

print(sys.getrefcount(a))

