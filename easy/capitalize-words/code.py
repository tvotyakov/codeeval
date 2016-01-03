#!python3
import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.rstrip('\n')
    if not test: continue # ignore an empty line
    print(' '.join(map(lambda s: s[0].upper() + s[1:], test.split(' '))))

test_cases.close()