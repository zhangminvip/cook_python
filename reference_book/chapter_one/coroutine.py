def print_matches(matchtext):
    print('Looking for ', matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)


matcher = print_matches('python')
print(matcher.__next__())
print(matcher.send('python is cool'))
