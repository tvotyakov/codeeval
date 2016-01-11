#!python3
def get_trimmed_str(in_str, max_chars = 55, min_chars = 40):
    ''' (string, int) -> string

    Returns the given string if its length <= max_chars characters.
    If its length > max_chars characters, it will be trimmed to min_chars characters.
    If resulting string has spaces, than it will be trimmed once again
    to the last space (the space will be removed too). Eventually,
    '... <Read More>' will be added to the end of the resulting string
    and it will be returned.

    >>> get_trimmed_str('')
    ''

    >>> get_trimmed_str('Test string')
    'Test string'

    >>> get_trimmed_str('Amy Lawrence was proud and glad, and she tried to make Tom see it in her face - but he wouldn\\'t look.')
    'Amy Lawrence was proud and glad, and... <Read More>'

    >>> get_trimmed_str('TestStringWithMoreThanFiftyFiveCharactersAndWithoutSpaces')
    'TestStringWithMoreThanFiftyFiveCharacter... <Read More>'

    >>> get_trimmed_str('Amy Lawrence was proud and glad, and it is long test string ends with space after trimming to 40 characters.')
    'Amy Lawrence was proud and glad, and it... <Read More>'
    '''
    if len(in_str) <= max_chars: return in_str
    result = in_str[:min_chars]
    space_pos = result.rfind(' ')
    if space_pos >= 0:
        result = result[:space_pos]
    result += '... <Read More>'
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
            print(get_trimmed_str(test))

        test_cases.close()