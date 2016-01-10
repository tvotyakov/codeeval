#!python3
def calc_num_with_zeros(zeros_count, max_num):
    ''' (int, int) -> int

    Returns count of integers from 1 to max_num including
    which contains zeros_count zeros in its binary
    representation.

    >>> calc_num_with_zeros(1, 1)
    0

    >>> calc_num_with_zeros(1, 2)
    1

    >>> calc_num_with_zeros(2, 4)
    1

    >>> calc_num_with_zeros(1, 8)
    3
    '''
    return sum(1
        for i in range(1, max_num + 1)
        if '{0:b}'.format(i).count('0') == zeros_count)

def parse_input(in_str):
    ''' (string) -> tuple of integer

    Function expects string in_str which contains
    two integers delimited by space and returns
    tuple of the integers.

    >>> tuple(parse_input('1 1'))
    (1, 1)

    >>> tuple(parse_input('2 3'))
    (2, 3)

    >>> tuple(parse_input('1 8'))
    (1, 8)

    >>> tuple(parse_input('2 4'))
    (2, 4)
    '''
    return map(int, in_str.split(' '))

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
            print(calc_num_with_zeros(*parse_input(test)))

        test_cases.close()