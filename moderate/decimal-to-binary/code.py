#!python3
def dec_to_bin(num):
    '''(int) -> string

    Returns binary representation of the given integer num.

    >>> dec_to_bin(0)
    '0'

    >>> dec_to_bin(2)
    '10'
    
    >>> dec_to_bin(10)
    '1010'
    
    >>> dec_to_bin(67)
    '1000011'
    '''

    if num == 0: return '0'
    
    def bin_digit(num):
        while num > 0:
            yield num % 2
            num >>= 1

    return ''.join(str(digit) for digit in bin_digit(num))[::-1]

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
            print(dec_to_bin(int(test)))

        test_cases.close()
