#!python3
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip('\n')
    if not test: continue # ignore an empty line
    print(int(test, 16))

test_cases.close()
