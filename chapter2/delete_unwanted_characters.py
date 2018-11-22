s = ' hello world \n'

print(s.strip())
ep1 = s.lstrip()
ep2 = s.rstrip()
t = '------hello======='
ep3 = t.strip('-=')
ep4 = s.replace(' ', '')
import re
ep5 = re.sub('\s+', ' ', s)

with open('strip_test.csv') as f:
    lines = (line.replace(' ',',') for line in f)
    for line in lines:
        print(line)
print()
