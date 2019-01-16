import re


line = 'asdf fjdk;afed, fjek, sdkf, foo'
result = re.split(r'([;,\s])\s*', line)
re.split(r'[;,\s]\s*', line)
re.split(r'([;,\s])\s*', line)
values = result[::2]
delimiters = result[1::2] + ['']
orginal = ''.join(v+d for v,d in zip(values,delimiters))
print()

# if __name__=="__main__":

