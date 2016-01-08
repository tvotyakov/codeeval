#!python3
def convert_roller_case(in_str):
    ''' (string) -> string

    Returns a new string with the same symbols as in the given in_str,
    and cases of the symbols according to the following rules:
        1. The first letter of the line should be in uppercase.
        2. The next letter should be in lowercase.
        3. The next letter should be in uppercase, and so on.
        4. Any characters, except for the letters, are ignored during
           determination of letter case.

    >>> convert_roller_case('')
    ''

    >>> convert_roller_case('a')
    'A'

    >>> convert_roller_case('A')
    'A'

    >>> convert_roller_case('abcd')
    'AbCd'

    >>> convert_roller_case('abc')
    'AbC'

    >>> convert_roller_case('a b.c')
    'A b.C'

    >>> convert_roller_case('A B.C-D')
    'A b.C-d'

    >>> convert_roller_case('To be, or not to be: that is the question.')
    'To Be, Or NoT tO bE: tHaT iS tHe QuEsTiOn.'

    >>> convert_roller_case("Whether 'tis nobler in the mind to suffer.")
    "WhEtHeR 'tIs NoBlEr In ThE mInD tO sUfFeR."
    '''
    if in_str == '':
        return ''

    i = 0
    chars = list(in_str)
    for j, ch in enumerate(chars):
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            chars[j] = ch.upper() if i % 2 == 0 else ch.lower()
            i += 1
    return ''.join(chars)

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
            print(convert_roller_case(test))

        test_cases.close()
