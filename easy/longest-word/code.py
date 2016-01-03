#!python3
def longest_word(in_str):
    '''(string) -> string

    Finds and returns the longest word in the in_str sentence.
    If the sentence has more than one word of the same length
    you should pick the first one.

    >>> longest_word('some line with text')
    'some'
    >>> longest_word('another line')
    'another'
    '''
    return max(in_str.split(' '), key = lambda s: len(s))

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
            print(longest_word(test))

        test_cases.close()
