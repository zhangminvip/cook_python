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




print ()