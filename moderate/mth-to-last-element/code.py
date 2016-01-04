#!python3
def get_mth_to_last_element(in_str, m):
    '''(string, int) -> string

    Returns the m-th (1-based index) to last char of the
    given in_str string. Returns None if m is larger than the
    string size.

    >>> get_mth_to_last_element('abcd', 4)
    'a'

    >>> get_mth_to_last_element('efgh', 2)
    'g'

    >>> get_mth_to_last_element('efgh', 5)
    '''
    return in_str[-m] if m <= len(in_str) else None
    
def parse_string(in_str):
    '''(string) -> tuple(string, int)

    >>> parse_string('a b c d 4')
    ('abcd', 4)

    >>> parse_string('e f g h 2')
    ('efgh', 2)
    '''
    in_list = in_str.split(' ')
    return ''.join(in_list[:-1]), int(in_list[-1])

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
            ch = get_mth_to_last_element(*parse_string(test))
            if ch != None:
                print(ch)

        test_cases.close()