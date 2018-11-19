filename = 'spam.txt'
result = filename.endswith('.txt')
import os
filename = os.listdir('.')
list = [name for name in filename if name.endswith('.py')]
exist = any(name.endswith('.py')  for name in filename)
print()