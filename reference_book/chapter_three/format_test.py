s = 'you name is {person[name]}, your age is {person[age]}'
# ss ='you name is {person[""}, your age is {person["age"]}'
person = {'name':'zhangmin','age':12}
print(s.format(person=person))

# print(person["name"])

sss ='you name is {0}, your age is {person}'
print(sss.format('zhang',person='ll'))