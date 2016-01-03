#!python3
import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.rstrip('\n')
    if not test: continue # ignore an empty line
    line = test.split(',')
    print(line[0].rfind(line[1]))

test_cases.close()
