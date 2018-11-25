def print_matches(matchtext):
    print('Looking for ', matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)


matcher = print_matches('python')
matcher.__next__()
matcher.send('python is cool')
print()
print()
print()
matcher.send('python is cool')
print()
print()
print()
