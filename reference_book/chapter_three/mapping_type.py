zhangmin = {'name': 'zhangmin', 'age': 12, 'friend': []}
wang = {'name': 'wang', 'age': 11, 'friend': [zhangmin]}
zhou = {'name': 'zhou', 'age': 10, 'friend': [zhangmin, wang]}
persons = {'person': [zhangmin, wang, zhou]}
# print(len(zhou))
# print('friend' in zhou)
# zhou.clear()
# print(zhou)
# print(zhou.get('wo',None)) # default is None
# print(zhangmin.items())
# print(zhangmin.keys())

# print(zhangmin.pop('a','not exist'))
# print(zhangmin.pop('a'))

# print(zhangmin.popitem())

# extra =  {'school':'hanshan'}
# zhangmin.update(extra)
# print(zhangmin)

# print(zhangmin.values())

# print('age' in zhangmin)

# print(zhangmin.fromkeys(['book_name','author','publish_time'],' '))
# dict.fromkeys()

# print(zhangmin.setdefault('birthday', '1997-1-1'))
# print(zhangmin)
# print(zhangmin.setdefault('birthday', '1998'))
# print(zhangmin)


# python2 :list python3: iterator
print(type(zhangmin.items()))
print(zhangmin.items())
print(zhangmin.keys())
print(list(zhangmin)) #save keys
print(list(zhangmin.items()))  # save all

