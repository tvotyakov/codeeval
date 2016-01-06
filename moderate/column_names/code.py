#!python3
def get_column_name(n):
    ''' (int) -> string

    Returns excel-like column header for the given column
    number n. MS Excel uses letters 'A'-'Z' for the first
    26 columns. Than, it uses two letters for the columns
    name from 'AA' to 'ZZ'. After 'ZZ', Excel uses three
    letters.

    >>> get_column_name(1)
    'A'

    >>> get_column_name(13)
    'M'

    >>> get_column_name(26)
    'Z'

    >>> get_column_name(27)
    'AA'

    >>> get_column_name(30)
    'AD'

    >>> get_column_name(52)
    'AZ'

    >>> get_column_name(53)
    'BA'

    >>> get_column_name(27*26)
    'ZZ'

    >>> get_column_name(27*26 + 1)
    'AAA'

    >>> get_column_name(3702)
    'ELJ'

    >>> get_column_name(27*26*26+26)
    'ZZZ'
    '''

    n -= 1
    res = []
    while(n >= 0):
        res.append(n % 26)
        n = n // 26 - 1
    return ''.join(chr(ord('A') + i) for i in res[::-1])

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
            print(get_column_name(int(test)))

        test_cases.close()
