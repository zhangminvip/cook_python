mylist = [1, 4, -5, 10, -7, 2, 3, -1]
list =[n for n in mylist if n >0]
print(list)


# if you want to save memory
pos = (n for n in mylist if n > 0)
for p in pos:
    print(p)
