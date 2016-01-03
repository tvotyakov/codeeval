#!python3
def is_self_describing_number(in_str):
    '''(string) -> boolean

    Determines whether given in_str is a string representation
    of a self-describing number or not.

    >>> is_self_describing_number('2020')
    True

    >>> is_self_describing_number('22')
    False

    >>> is_self_describing_number('1210')
    True
    '''
    return ''.join(str(in_str.count(str(i))) for i in range(len(in_str))) == in_str

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
            print(1 if is_self_describing_number(test) else 0)

        test_cases.close()
