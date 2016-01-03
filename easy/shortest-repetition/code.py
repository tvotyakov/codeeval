#!python3
def is_period(src_string, checking_string):
    ''' (string, string) -> boolean

    Return true, if checking_string is a period of src_string.
    A string is a period of another string if the latter can be formed
    by concatenating one or more repetition of the former.

    >>> is_period('abcabcabcabc', 'abcabcabcabc')
    True

    >>> is_period('abcabcabcabc', 'abcabc')
    True

    >>> is_period('abcabcabcabc', 'abc')
    True

    >>> is_period('abcabcabcabc', 'cba')
    False
    '''
    return src_string == checking_string * (len(src_string) //
                                            len(checking_string))

def min_period(src_string):
    ''' (string) -> int

    Returns the smallest period of the src_string. A string
    is said to have period p if it can be formed by concatenating
    one or more repetitions of another string of length p.

    >>> min_period('abcabcabcabc')
    3

    >>> min_period('bcbcbcbcbcbcbcbcbcbcbcbcbcbc')
    2

    >>> min_period('dddddddddddddddddddd')
    1

    >>> min_period('abcdefg')
    7
    '''
    l = result = len(src_string)
    for i in range(l, 0, -1):
        if not l % i and is_period(src_string, src_string[:i]):
            result = i
    return result

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
            print(min_period(test))

        test_cases.close()
