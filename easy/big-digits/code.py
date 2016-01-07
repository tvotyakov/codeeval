#!python3
import re
FONT = [
    [0b01100, 0b10010, 0b10010, 0b10010, 0b01100],
    [0b00100, 0b01100, 0b00100, 0b00100, 0b01110],
    [0b11100, 0b00010, 0b01100, 0b10000, 0b11110],
    [0b11100, 0b00010, 0b01100, 0b00010, 0b11100],
    [0b01000, 0b10010, 0b11110, 0b00010, 0b00010],
    [0b11110, 0b10000, 0b11100, 0b00010, 0b11100],
    [0b01100, 0b10000, 0b11100, 0b10010, 0b01100],
    [0b11110, 0b00010, 0b00100, 0b01000, 0b01000],
    [0b01100, 0b10010, 0b01100, 0b10010, 0b01100],
    [0b01100, 0b10010, 0b01110, 0b00010, 0b01100],
];

def get_big_digit_line(num):
    ''' (int) -> string

    Returns string of "big digits" representation of one
    digit line according to its binary representation in
    the given integer num.

    >>> get_big_digit_line(1)
    '----*'

    >>> get_big_digit_line(0b11111)
    '*****'

    >>> get_big_digit_line(0b01010)
    '-*-*-'

    >>> get_big_digit_line(0b10101)
    '*-*-*'
    '''
    return '{0:05b}'.format(num).replace('0', '-').replace('1', '*')

def get_big_digits(in_str):
    ''' (string) -> string

    Returns string represented given in_str using special
    "big digits" ASCII font.

    >>> get_big_digits('')
    ''

    >>> get_big_digits('0')
    '-**--\\n*--*-\\n*--*-\\n*--*-\\n-**--\\n-----'

    >>> get_big_digits('0123456789')
    '-**----*--***--***---*---****--**--****--**---**--\\n*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-\\n*--*---*---**---**--****-***--***----*---**---***-\\n*--*---*--*-------*----*----*-*--*--*---*--*----*-\\n-**---***-****-***-----*-***---**---*----**---**--\\n--------------------------------------------------'

    >>> get_big_digits('3.1415926')
    '***----*---*-----*--****--**--***---**--\\n---*--**--*--*--**--*----*--*----*-*----\\n-**----*--****---*--***---***--**--***--\\n---*---*-----*---*-----*----*-*----*--*-\\n***---***----*--***-***---**--****--**--\\n----------------------------------------'

    >>> get_big_digits('01-01-1970')
    '-**----*---**----*----*---**--****--**--\\n*--*--**--*--*--**---**--*--*----*-*--*-\\n*--*---*--*--*---*----*---***---*--*--*-\\n*--*---*--*--*---*----*-----*--*---*--*-\\n-**---***--**---***--***--**---*----**--\\n----------------------------------------'

    >>> get_big_digits('4 8 15 16 23 42')
    '-*----**----*--****---*---**--***--***---*---***--\\n*--*-*--*--**--*-----**--*-------*----*-*--*----*-\\n****--**----*--***----*--***---**---**--****--**--\\n---*-*--*---*-----*---*--*--*-*-------*----*-*----\\n---*--**---***-***---***--**--****-***-----*-****-\\n--------------------------------------------------'
    '''
    pattern = re.compile('[^0-9]*')
    in_str = pattern.sub('', in_str)

    if len(in_str) == 0:
        return ''

    letter_lines = len(FONT[0])
    result = '\n'.join(
        ''.join(get_big_digit_line(FONT[int(n)][i]) for n in in_str)
        for i in range(letter_lines)) + '\n' + '-'*(len(in_str)*5)

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
            print(get_big_digits(test))

        test_cases.close()
