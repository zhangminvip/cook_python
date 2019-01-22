line = 'Good,100,490.10'
field_type = [str, int, float]
raw_fields = line.split(',')
print(raw_fields)
fields = [ty(val) for ty, val in zip(field_type, raw_fields)]
print(fields)
for i in zip(field_type, raw_fields):
    print(i,type(i))