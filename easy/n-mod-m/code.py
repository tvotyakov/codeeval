#!python3
def mod(n, m):
    '''(int, int) -> int

    >>> mod(10, 5)
    0
    >>> mod(3, 2)
    1
    >>> mod(20, 6)
    2
    >>> mod(2, 3)
    2
    '''
    assert m != 0
    
    return n - m * (n // m)

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
            print(mod(*map(int, test.split(',', 2))))

        test_cases.close()
