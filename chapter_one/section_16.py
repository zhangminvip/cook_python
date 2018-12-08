mylist = [1, 4, -5, 10, -7, 2, 3, -1]
l =[n for n in mylist if n >0]
print(list)


# if you want to save memory
pos = (n for n in mylist if n > 0)

for p in pos:
    print(p)

# more complex filtering rules
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals =  list(filter(is_int, values))
print(ivals)

clip_neg = [n if n >0 else 0 for n in mylist]
print(clip_neg)

