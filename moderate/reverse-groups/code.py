#!python3
def reverse_groups(in_list, group_len):
    ''' (list, integer) -> list

    Reverses the elements of the list (in place), group_len items at a time.
    If the number of elements is not a multiple of group_len, then the remaining
    items in the end will be left as is. Resulting list will be return either.

    >>> reverse_groups(['1'], 1);
    ['1']

    >>> reverse_groups(['1', '2'], 1);
    ['1', '2']

    >>> reverse_groups(['1', '2'], 2)
    ['2', '1']

    >>> reverse_groups(['1', '2', '3', '4', '5', '6'], 3)
    ['3', '2', '1', '6', '5', '4']

    >>> reverse_groups(['1', '2', '3', '4', '5', '6', '7', '8'], 3)
    ['3', '2', '1', '6', '5', '4', '7', '8']
    '''
    for i in range(0, len(in_list), group_len):
        tmp = in_list[i: i + group_len]
        if len(tmp) == group_len:
            in_list[i: i + group_len] = tmp[::-1]
    return in_list

def parse_str(in_str):
    ''' (string) -> (list of strings, integer)

    Expects a string with list of integer separated by comma followed by
    another integer separated by semicolon. Returns tuple of the list and
    latter integer.

    >>> parse_str('1;1')
    (['1'], 1)

    >>> parse_str('1,2,3;2')
    (['1', '2', '3'], 2)

    >>> parse_str('10,9,8,7,6;3')
    (['10', '9', '8', '7', '6'], 3)
    '''
    _list, num = in_str.split(';')
    _list = _list.split(',')
    num = int(num)
    return _list, num

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
            print(','.join(reverse_groups(*parse_str(test))))

        test_cases.close()
