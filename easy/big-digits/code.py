#!python3
import re
FONT = [
    ['-**--', '*--*-', '*--*-', '*--*-', '-**--'],
    ['--*--', '-**--', '--*--', '--*--', '-***-'],
    ['***--', '---*-', '-**--', '*----', '****-'],
    ['***--', '---*-', '-**--', '---*-', '***--'],
    ['-*---', '*--*-', '****-', '---*-', '---*-'],
    ['****-', '*----', '***--', '---*-', '***--'],
    ['-**--', '*----', '***--', '*--*-', '-**--'],
    ['****-', '---*-', '--*--', '-*---', '-*---'],
    ['-**--', '*--*-', '-**--', '*--*-', '-**--'],
    ['-**--', '*--*-', '-***-', '---*-', '-**--'],
];

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
    result = '\n'.join(''.join(FONT[int(n)][i] for n in in_str)
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
