#!python3
def hidden_digits(in_str):
    '''(string) -> string

    Finds all visible and hidden digits in the in_str string
    and return them out in order of their appearance as one string.

    >>> hidden_digits('abcdefghik')
    '012345678'
    >>> hidden_digits('Xa,}A#5N}{xOBwYBHIlH,#W')
    '05'
    >>> hidden_digits("(ABW>'yy^'M{X-K}q,")
    'NONE'
    >>> hidden_digits('6240488')
    '6240488'
    '''
    hidden_digit_map = 'abcdefghij'
    result = ''
    for ch in in_str:
        if ch.isdigit():
            result += ch
        else:
            pos = hidden_digit_map.find(ch)
            if pos != -1:
                result += str(pos)
    return 'NONE' if result == '' else result
    
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
            print(hidden_digits(test))

        test_cases.close()
