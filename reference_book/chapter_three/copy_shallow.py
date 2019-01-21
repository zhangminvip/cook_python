a = [1,2,[3, 4]]
b = list(a)
print(b is a)
b.append(100)
print('a:',a)
print('b:',b)
b[2][0] = -100
b[1] = 5
a[1] = 8
a[2][1] = 11

print('a:',a)
print('b:',b)
