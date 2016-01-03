#!python3
def reverse_words(src):
    '''(str) -> str

    Returns string contains all words from string src in reverse order.
    
    >>> reverse_words('Hello World')
    'World Hello'

    >>> reverse_words('Hello CodeEval')
    'CodeEval Hello'

    >>> reverse_words('This is wild wild West')
    'West wild wild is This'
    '''

    words = src.split(' ')
    words.reverse()
    
    return ' '.join(words)

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
            print(reverse_words(test))

        test_cases.close()
