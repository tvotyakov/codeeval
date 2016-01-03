#!python3
import sys
test_cases = open(sys.argv[1], 'r')

result = 0
for test in test_cases:
    test = test.rstrip('\n')
    if not test: continue # ignore an empty line
    print(1 if int(test) % 2 == 0 else 0)

test_cases.close()
