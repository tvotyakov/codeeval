#!python3
def get_swapped_string(in_str):
    ''' (string) -> string

    Takes a string where each word has a single digit positive integer as a
    prefix and a suffix, swaps the numbers while retaining the word in between
    and returns resulting string. Words in the given string and resulting
    strings should be separated by a space.

    >>> get_swapped_string('0a0 0b0')
    '0a0 0b0'

    >>> get_swapped_string('0a1 0b1')
    '1a0 1b0'

    >>> get_swapped_string('0abcd9')
    '9abcd0'

    >>> get_swapped_string('0abcd9 2cdef7')
    '9abcd0 7cdef2'

    >>> get_swapped_string('4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5')
    '0Always4 8look5 9on4 2the7 8bright4 7side9 8of3 5life5'

    >>> get_swapped_string('5Nobody5 7expects3 5the4 6Spanish4 9inquisition0')
    '5Nobody5 3expects7 4the5 4Spanish6 0inquisition9'
    '''
    return ' '.join(word[-1] + word[1:-1] + word[0]
                        for word in in_str.split(' ') if word)

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
            print(get_swapped_string(test))

        test_cases.close()
