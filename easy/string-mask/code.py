#!python3
def change_case(in_str, mask):
    ''' (string, string) -> string

    Takes input string (in_str) and binary mask and changes cases of in_str
    letters according to mask: to upper case if a letter finds itself as 1, or
    leave it as is, if it's 0.

    >>> change_case('hello', '11001')
    'HEllO'

    >>> change_case('world', '10000')
    'World'

    >>> change_case('cba', '111')
    'CBA'
    '''
    return ''.join(ch.upper() if bit == '1' else ch for ch, bit in zip(in_str, mask))

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
            print(change_case(*test.split(' ')))

        test_cases.close()
