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



from itertools import compress
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
# more5 = [count for count in counts if count > 5]
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))


######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])


SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

print(cost)