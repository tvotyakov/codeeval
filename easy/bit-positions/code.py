#!python3
def check_bits(n, p1, p2):
    '''(int, int, int) -> boolean

    Returns True if the bits of number n in position p1 and p2
    are the same or not.

    >>> check_bits(86, 2, 3)
    True

    >>> check_bits(125, 1, 2)
    False
    '''
    return (n >> (p1 - 1)) & 1 == (n >> (p2 - 1)) & 1

if __name__ == '__main__':
    import sys
    if (len(sys.argv) <= 1):
        import doctest
        doctest.testmod()
    else:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            test = test.rstrip('\n')
            if not test: continue # ignore an empty line
            print('true' if check_bits(*map(int, test.split(',', 3))) else 'false')

        test_cases.close()
