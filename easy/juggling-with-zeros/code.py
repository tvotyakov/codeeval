#!python3
def zero_based_to_int(zero_based_number):
    ''' (string) -> integer

    Converts the given zero-based representation of number to
    its integer value.

    >>> zero_based_to_int('')

    >>> zero_based_to_int('0 0')
    0

    >>> zero_based_to_int('00 0')
    1

    >>> zero_based_to_int('0 0 00 0')
    1

    >>> zero_based_to_int('00 0 0 00 00 0')
    9

    >>> zero_based_to_int('00 0 0 000 00 0000000 0 000')
    9208

    >>> zero_based_to_int('0 000000000 00 00')
    3
    '''
    if (zero_based_number == ''):
        return None

    parts = zero_based_number.split(' ')
    assert(len(parts) % 2 == 0)

    zero_flag = None
    result = ''
    for i, val in enumerate(parts):
        if zero_flag == None:
            zero_flag = val == '0'
            continue

        result += ('0' if zero_flag else '1') * len(val)
        zero_flag = None
    return int(result, 2)

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
            print(zero_based_to_int(test))

        test_cases.close()