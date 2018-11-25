import time

def print_matches(matchtext):
    print('Looking for ', matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)

def tail(f):
    # f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
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

wwwlog = tail(open('access-log'))
for line in wwwlog:
    for m in matchers:
        m.send(line)