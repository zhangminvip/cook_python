from datetime import datetime

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
nice_z = datetime.strftime(y, '%A %B %Y')

# this function is more than 7 times faster than datetime.strptime()
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))


ep_a = parse_ymd(text)

print()
