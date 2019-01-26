# coding:utf-8
'''
可变对象与不可变对象的区别在于对象本身是否可变。

python内置的一些类型中

• 可变对象：list dict set
• 不可变对象：tuple string int float bool

可变对象变化后内存地址不变
不可变对象变化后内存地址改变
所以可变对象__hash__函数应该返回None,  这样写： __hash__ = None

== 号自动调用__eq__函数。
is 检查的是对象内存地址。


__getattribute__()和 __getattr__()区别：

1、如果某个类定义了 __getattribute__() 方法，
在每次引用属性或方法名称时 Python 都调用它（特殊方法名称除外，因为那样将会导致讨厌的无限循环）。

2、如果某个类定义了 __getattr__() 方法，Python 将只在正常的位置查询属性时才会调用它。
如果实例 x 定义了属性 color， x.color 将 不会 调用x.__getattr__('color')；
而只会返回 x.color 已定义好的值。

'''

class Example():

    def __init__(self, val):
        '''
        :param val: int
        '''
        if isinstance(val, int):
            self.value = val
        else:
            raise IOError('Initialization parameters should be integer')

    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False

    def __hash__(self):
        print('id / 6 : ', id(self) / 6)
        return int(id(self) / 6)


    def __repr__(self):
        # print('value: ',self.value)
        return '(repr) value: ' + str(self.value)

    def __str__(self):
        return '(str) value: ' + str(self.value)

    def __lt__(self, other):
        print('lt'.center(50, '*'))
        if self.value < other.value:
            print('True')
            return True
        else:
            print('False')
            False

    def __instancecheck__(self, instance):
        '''???'''
        print('haha')
        return 'haha'

    def __getattr__(self, item):
        if item == 'val':
            return 'attr val does not exist'
        else:
            raise AttributeError



e = Example(7)
d = Example(7)
r = Example(8)

print(e == d)
print(e == r)
print(hash(e))


t = [r, d, e]
print(t)
t_result = max(t)
print(t_result)

# print(isinstance(e, Example))

print(e.value)