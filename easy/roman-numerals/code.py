#!python3
def split_digits(num):
    ''' (int) -> list of int

    Splits the integer number num by digits. Returns
    list of digits in native order: most significant
    digit is at the first place, least is at the
    last place.

    >>> split_digits(0)
    [0]
    
    >>> split_digits(1)
    [1]

    >>> split_digits(12345)
    [1, 2, 3, 4, 5]
    '''
    result = [] if num > 0 else [0]
    while num > 0:
        result.append(num % 10)
        num //= 10
    return result[::-1]

cardinal_to_roman_map = {1: 'I', 2: 'II', 3: 'III',
                       4: 'IV', 5: 'V', 6: 'VI',
                       7: 'VII', 8: 'VIII', 9: 'IX',
                       10: 'X', 20: 'XX', 30: 'XXX',
                       40: 'XL', 50: 'L', 60: 'LX',
                       70: 'LXX', 80: 'LXXX', 90: 'XC',
                       100: 'C', 200: 'CC', 300: 'CCC',
                       400: 'CD', 500: 'D', 600: 'DC',
                       700: 'DCC', 800: 'DCCC', 900: 'CM',
                       1000: 'M', 2000: 'MM', 3000: 'MMM'}
def cardinal_to_roman(num):
    ''' (int) -> string

    Converts a cardinal integer number num to to a Roman numeral.

    Preconditions: 1 <= num <= 3999
    >>> cardinal_to_roman(1)
    'I'
    
    >>> cardinal_to_roman(4)
    'IV'

    >>> cardinal_to_roman(104)
    'CIV'
    
    >>> cardinal_to_roman(159)
    'CLIX'

    >>> cardinal_to_roman(296)
    'CCXCVI'

    >>> cardinal_to_roman(3992)
    'MMMCMXCII'

    >>> cardinal_to_roman(3999)
    'MMMCMXCIX'
    '''
    num_digits = split_digits(num)
    factor = 10 ** (len(num_digits) - 1)
    result = ''
    for digit in num_digits:
        if digit:
            result += cardinal_to_roman_map[digit * factor]
        factor //= 10
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
            print(cardinal_to_roman(int(test)))

        test_cases.close()
