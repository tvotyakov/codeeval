#!python3
def remove_characters(in_str, chars):
    '''(string, string) -> string

    Removes characters chars from the given string in_str. 

    >>> remove_characters('how are you', 'abc')
    'how re you'

    >>> remove_characters('hello world', 'def')
    'hllo worl'
    '''
    return ''.join(ch for ch in in_str if ch not in chars)

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
            print(remove_characters(*test.split(', ', 2)))

        test_cases.close()
