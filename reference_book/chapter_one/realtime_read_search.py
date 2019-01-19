# coding:utf-8

import time



def print_matches(matchtext):
    print('Looking for ', matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)



# 这个函数不能读取一个持续增长的日志文件，
def tail(f):
    # f.seek(0, 2)
    while True:
        where = f.tell()
        line = f.readline()
        if not line:
            f.close()
            print('sleep')
            time.sleep(1)
            f = open('access-log')
            f.seek(where)
            continue
        yield line

matchers = [
    print_matches('python'),
    print_matches('guido'),
    print_matches('jython')
]

print(type(matchers))

for m in matchers:
    m.__next__()

wwwlog = tail(open('access-log', 'r'))
for line in wwwlog:
    for m in matchers:
        m.send(line)

# for m in matchers:
#     m.close()