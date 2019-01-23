def multiply(x):
    return x * 3

s = 'woshinide'
print(list(s))
l = []
l.extend(list(s))
print(l)
print(l.count('i'))
print(l.index('i'))
l.insert(4, 'y')
print(l)
# print(l.insert(4,'y'))
print(l.pop(1))
print(l)
print(l.remove('w'))
print(l)

print(l.reverse())
print(l)
num = [2,5,7,4,9,0]
d = [{'name':'zhangmin','age':12},{'name':'wangsi','age':10},{'name':'limin','age':15}]
d.sort(reverse=True,key=lambda x: x['age'])
print(d)

copy_test = [1,2,[2,3]]
c = copy_test.copy()
print(c,'*'*3 ,copy_test)
c[2][1] = 4
print(c,'*'*3 ,copy_test)
c[0] = 2
print(c,'*'*3 ,copy_test)




