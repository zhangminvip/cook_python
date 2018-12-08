from collections import OrderedDict
import json
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['ss'] = 3
d['hh'] = 4
data = json.dumps(d)
a = {'foo':1,'bar':2}
print(data)
print(d)
print('a',a)