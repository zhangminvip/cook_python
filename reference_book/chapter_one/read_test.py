import time

file = open('access-log')
while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        file.close()
        time.sleep(1)
        file = open('access-log')
        file.seek(where)
    else:
        print (line) # already has newline