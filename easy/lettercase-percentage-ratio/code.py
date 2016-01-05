#!python3
from decimal import *

def get_lettercase_ratio(in_str):
    ''' (string) -> tuple of decimals

    Returns percentage ratios of lowercase and uppercase
    letters in the in_str relative to the length of in_str.

    >>> get_lettercase_ratio('')
    (Decimal('0'), Decimal('0'))

    >>> get_lettercase_ratio('UPPER')
    (Decimal('0'), Decimal('100'))

    >>> get_lettercase_ratio('lower')
    (Decimal('100'), Decimal('0'))

    >>> get_lettercase_ratio('UPPERlower')
    (Decimal('50.0'), Decimal('50.0'))

    >>> get_lettercase_ratio('thisTHIS')
    (Decimal('50.0'), Decimal('50.0'))

    >>> get_lettercase_ratio('AAbbCCDDEE')
    (Decimal('20.0'), Decimal('80.0'))

    >>> print('(%.2f, %.2f)' % get_lettercase_ratio('UkJ'))
    (33.33, 66.67)
    '''
    if (len(in_str) == 0):
        return Decimal(0), Decimal(0)

    lower_count = len([l for l in in_str if l.islower()])

    lower_percent = Decimal(lower_count) / len(in_str) * 100
    upper_percent = 100 - lower_percent
    return (lower_percent, upper_percent)

def get_lettercase_ratio_str(in_str):
    ''' (string) -> string

    Returns formatted string of percentage ratios of lowercase and
    uppercase letters in the in_str relative to the length of in_str
    according to template: 'lowercase: LCR, uppercase: UCR', where
    LCR - lowercase letters percentage ratio rounded to the second
    digit after the point, and UCR - uppercase letters percentage
    ratio rounded to the second digit after the point.

    >>> get_lettercase_ratio_str('')
    'lowercase: 0.00 uppercase: 0.00'

    >>> get_lettercase_ratio_str('UPPER')
    'lowercase: 0.00 uppercase: 100.00'

    >>> get_lettercase_ratio_str('lower')
    'lowercase: 100.00 uppercase: 0.00'

    >>> get_lettercase_ratio_str('UPPERlower')
    'lowercase: 50.00 uppercase: 50.00'

    >>> get_lettercase_ratio_str('thisTHIS')
    'lowercase: 50.00 uppercase: 50.00'

    >>> get_lettercase_ratio_str('AAbbCCDDEE')
    'lowercase: 20.00 uppercase: 80.00'

    >>> get_lettercase_ratio_str('UkJ')
    'lowercase: 33.33 uppercase: 66.67'
    '''
    return 'lowercase: %.2f uppercase: %.2f' % (get_lettercase_ratio(in_str))

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
            print(get_lettercase_ratio_str(test))

        test_cases.close()
