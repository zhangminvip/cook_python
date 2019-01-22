
name = 'zhangmin'
name.center(50, '*') # will not change the origin string
# print(name.center(50, '*'))
# print(name.count('mi'))
byte_name = b'zhangmin'
space_name = ' zhang min'
encode_name = ' zhangmin'
title = 'Zhang,Min'
separator = ','
# print(byte_name.decode('ascii'))
# print(encode_name.encode('utf-8'))
# print(byte_name.isalnum())
# print(byte_name.isalpha())
# print(byte_name.isdigit())
# print(byte_name.islower())
# print(byte_name.isspace())
# print(byte_name.istitle())
# print(title.istitle())
# print(title.isupper())
# print(separator.join(['zhang', 'min']))
# print(title.lower())
# print(encode_name.ljust(20,'*'))
print(encode_name.lstrip(' '))
