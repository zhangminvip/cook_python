import re
text = 'yeah, but no, but yeah, but no, but yeah'
r = text =='yeah'
r1 = text.find('no')
text1 = '11/27/2012'
text2 = 'Nov 27 2012'
if re.match(r'\d+/\d+/\d+',text1):
    print ('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+',text2):
    print ('yes')
else:
    print('NO')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print ('yes')
else:
    print('no')
if datepat.match(text2):
    print ('yes')
else:
    print('nono')

text = 'Today is 11/27/2012, PyCon starts 3/13/2013'
list_date = datepat.findall(text)

detepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = detepat2.match('11/23/2018')
group = m.groups()
list_date2 = detepat2.findall(text)

for month,day,year in detepat2.findall(text):
    print('{}-{}-{}'.format(month,day,year))


for m in detepat2.finditer(text):
    print (m.groups())
print ()