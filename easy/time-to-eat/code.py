#!python3
def sort_times(in_str):
    ''' (string) -> list of strings

    Expects input string with timestamps separated by space. Returns a list of
    the timestamps reverse sorted from the biggest to the smallest one.

    >>> sort_times('02:26:31 14:44:45 09:53:27')
    ['14:44:45', '09:53:27', '02:26:31']

    >>> sort_times('05:33:44 21:25:41')
    ['21:25:41', '05:33:44']
    '''
    return sorted(in_str.split(' '), reverse = True)

def serialize_str(in_list):
    ''' (list of strings) -> string

    Returns string with values from the given list separated by space

    >>> serialize_str(['14:44:45', '09:53:27', '02:26:31'])
    '14:44:45 09:53:27 02:26:31'

    >>> serialize_str([])
    ''

    >>> serialize_str(['21:25:41'])
    '21:25:41'

    >>> serialize_str(['21:25:41', '05:33:44'])
    '21:25:41 05:33:44'
    '''
    return ' '.join(in_list)

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
            print(serialize_str(sort_times(test)))

        test_cases.close()
