import os
from urllib.request import urlopen

filename = 'spam.txt'
result = filename.endswith('.txt')

filename = os.listdir('.')
list = [name for name in filename if name.endswith('.py')]
exist = any(name.endswith('.py')  for name in filename)

# check file path
def read_data(name):
    if name.startwith(('http:','https','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# check if  a specified file type exists in a floder
if any(name.endswith('.py') for name in os.listdir('.')):
    print('exist')



print()