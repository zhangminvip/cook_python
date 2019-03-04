import os
import sys

'''use Process'''
program = 'python'
print('process calling')
arguments = ['called_Process.py']
os.execvp(program, (program,) + tuple(arguments))
# print((program,) + tuple(arguments))
print('good bye')