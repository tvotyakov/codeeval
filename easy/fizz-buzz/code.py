#!python3
import sys

def line_to_fizz_buzz(line):
    """ str -> str

    >>> line_to_fizz_buzz('3 5 10')
    '1 2 F 4 B F 7 8 F B'

    >>> line_to_fizz_buzz('2 7 15')
    '1 F 3 F 5 F B F 9 F 11 F 13 FB 15'
    """
    
    def num_to_fizz_buzz(val):
        return ('FB' if val % fizz == 0 and val % buzz == 0
           else 'F' if val % fizz == 0
           else 'B' if val % buzz == 0
           else str(val))

    fizz, buzz, count = map(int, line.split(' ', 3))
    return ' '.join(map(num_to_fizz_buzz, range(1, count + 1)))

if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        import doctest
        doctest.testmod()
    else:    
        test_cases = open(sys.argv[1], 'r')
        for test in (test.rstrip('\n') for test in test_cases):
            if not test: continue
            print(line_to_fizz_buzz(test))

        test_cases.close()
