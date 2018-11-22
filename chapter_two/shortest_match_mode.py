import re
str_par = re.compile(r'"(.*)"')
text1 = 'Computer says "no"'
print(str_par.findall(text1))

text2 = 'computer say"no." phone says "yes.""'
print(str_par.findall(text2))

str_par2 = re.compile(r'"(.*?)"')
print(str_par2.findall(text2))

