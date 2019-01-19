s = '''sdfjls
sldfjl
sdlfj'''
print(s)


ss = ''
# ss = '\''
ss = r'\\u00f1'


# python3
ss = b'jalape\xc3\xb1o'
print(ss.decode('utf-8'))