def print_matches(matchtext):
    print('Looking for ', matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)

