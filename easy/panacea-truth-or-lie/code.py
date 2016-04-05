#!python3
def check_componets(virus, antivirus):
    ''' (list of integer, list of integer) -> boolean

    Returns True if sum of virus components is greater or equal to sum of
    anitvirus components. Otherwise - False

    >>> check_componets([100, 110, 120], [300, 30])
    True

    >>> check_componets([94, 125, 89], [108, 149, 103])
    True

    >>> check_componets([147, 117], [71, 90, 98])
    False
    '''
    return sum(antivirus) >= sum(virus)

def parse_input(in_str):
    ''' string -> tuple of lists of integer

    Takes a string with virus components in the hexadecimal numeral system (HEX)
    separated by space and antivirus components in the binary number system (BIN)
    also separated by space. Virus and antivirus components are separated by a
    pipeline '|'. Returns tuple with two lists of integer. First list contains
    'virus' components, second - 'anitvirus' as integers.

    >>> parse_input('64 6e 78 | 100101100 11110')
    ([100, 110, 120], [300, 30])

    >>> parse_input('5e 7d 59 | 1101100 10010101 1100111')
    ([94, 125, 89], [108, 149, 103])

    >>> parse_input('93 75 | 1000111 1011010 1100010')
    ([147, 117], [71, 90, 98])
    '''
    def parse_ints(components, base):
        return list(map(lambda s: int(s, base), components.strip().split(' ')))

    viruses, antiviruses = in_str.split('|')
    return parse_ints(viruses, 16), parse_ints(antiviruses, 2)

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
            print(check_componets(*parse_input(test)))

        test_cases.close()
