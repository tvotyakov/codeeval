#!python3
def get_next_to_last_word(in_str):
    '''(string) -> string

    Finds and returns next-to-last word in a given string in_str.

    >>> get_next_to_last_word('some line with text')
    'with'
    >>> get_next_to_last_word('another line')
    'another'
    '''
    return in_str.split(' ')[-2]

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
            print(get_next_to_last_word(test))

        test_cases.close()
