#!python3
import sys
test_cases = open(sys.argv[1], 'r')

result = 0
for test in test_cases:
    test = test.rstrip('\n')
    if not test: continue # ignore an empty line
    line = list(set(map(int, test.split(','))))
    line.sort()
    print(','.join(map(str, line)))

test_cases.close()
