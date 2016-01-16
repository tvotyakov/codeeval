#!python3
def decode_str(in_str):
    ''' (string) -> string

    Decodes a given string using following decoding rules
        A | B | C | D | E | F | G | H | I | J | K | L | M
        U | V | W | X | Y | Z | N | O | P | Q | R | S | T
    and returns resulting string.

    >>> decode_str('mke')
    'try'

    >>> decode_str('mh')
    'to'

    >>> decode_str('lhsby')
    'solve'

    >>> decode_str('pm')
    'it'
    '''
    def decode_char(ch):
        diff = 0
        if ch <= 'f':
            diff = 20
        elif ch <= 'm':
            diff = 7
        elif ch <= 't':
            diff = -7
        else:
            diff = -20

        return chr(ord(ch) + diff)

    return ''.join(map(decode_char, in_str))

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
            print(decode_str(test))

        test_cases.close()
