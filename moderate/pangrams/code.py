#!python3
def get_missing_letters(in_str):
    ''' (string) -> string

    Takes a string and returns all the letters (US-ASCII characters) it is
    missing (which prevent it from being a pangram) all lower case and in
    alphabetic order. In case the input string is already a pangram, it will
    return 'NULL'

    >>> get_missing_letters('a')
    'bcdefghijklmnopqrstuvwxyz'

    >>> get_missing_letters('acD^8340Mdf')
    'beghijklnopqrstuvwxyz'

    >>> get_missing_letters('A quick brown fox jumps over the lazy dog')
    'NULL'

    >>> get_missing_letters('A slow yellow fox crawls under the proactive dog')
    'bjkmqz'
    '''
    letters = list('abcdefghijklmnopqrstuvwxyz')
    for char in in_str.lower():
        try:
            letters.remove(char)
        except ValueError:
            pass

    return ''.join(letters) if len(letters) > 0 else 'NULL'

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
            print(get_missing_letters(test))

        test_cases.close()
