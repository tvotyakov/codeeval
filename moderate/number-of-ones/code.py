#!python3
def number_of_ones(num):
    '''(int) -> int

    Returns the number of 1 bits in the internal representation
    of a given integer num.

    >>> number_of_ones(0)
    0

    >>> number_of_ones(10)
    2
    
    >>> number_of_ones(22)
    3
    
    >>> number_of_ones(56)
    3
    '''

    if num == 0: return 0
    
    def bin_digits(num):
        while num > 0:
            yield num % 2
            num >>= 1

    return sum(d for d in bin_digits(num) if d)

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
            print(number_of_ones(int(test)))

        test_cases.close()
