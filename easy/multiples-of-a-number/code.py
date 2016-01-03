#!python3
def multiples_of_number(x, n):
    '''(int, int) -> int

    Returns the smallest multiple of n which is greater than or equal to x.

    >>> multiples_of_number(8, 8)
    8
    >>> multiples_of_number(13, 8)
    16
    >>> multiples_of_number(17,16)
    32
    '''
    result = n
    while result < x:
        result += n
    return result

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
            print(multiples_of_number(*map(int, test.split(',', 2))))

        test_cases.close()
