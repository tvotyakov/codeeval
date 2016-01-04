#!python3
import sys
if (len(sys.argv) > 1):
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.rstrip('\n')
        if not test: continue # ignore an empty line
        haystack, needle = test.split(',', 2)
        print(1 if haystack[-len(needle):] == needle else 0)

    test_cases.close()
else:
    print('Usage: trailing_string2.py <source_file>')