#!python3

DIGITS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
          'Eight', 'Nine']
TWO_DIGITS = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
              'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
TENS = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
        'Eighty', 'Ninety']
HUNDREDS = 'Hundred'
THREE_DIGITS = ['', 'Thousand', 'Million']

def get_text_dollar(amount):
    ''' (integer) -> string

    Returns text representation of a given amount of dollars.

    >>> get_text_dollar(2)
    'TwoDollars'

    >>> get_text_dollar(10)
    'TenDollars'

    >>> get_text_dollar(1000)
    'OneThousandDollars'

    >>> get_text_dollar(1000000)
    'OneMillionDollars'

    >>> [get_text_dollar(num) for num in [3, 4, 5, 6, 7, 8, 9]]
    ['ThreeDollars', 'FourDollars', 'FiveDollars', 'SixDollars', 'SevenDollars', 'EightDollars', 'NineDollars']

    >>> [get_text_dollar(num) for num in [11, 12, 13, 14, 15, 16, 17, 18, 19]]
    ['ElevenDollars', 'TwelveDollars', 'ThirteenDollars', 'FourteenDollars', 'FifteenDollars', 'SixteenDollars', 'SeventeenDollars', 'EighteenDollars', 'NineteenDollars']

    >>> [get_text_dollar(num) for num in [10, 20, 21, 30, 32, 40, 43, 50, 54, 60, 65, 70, 76, 80, 87, 90, 98]]
    ['TenDollars', 'TwentyDollars', 'TwentyOneDollars', 'ThirtyDollars', 'ThirtyTwoDollars', 'FortyDollars', 'FortyThreeDollars', 'FiftyDollars', 'FiftyFourDollars', 'SixtyDollars', 'SixtyFiveDollars', 'SeventyDollars', 'SeventySixDollars', 'EightyDollars', 'EightySevenDollars', 'NinetyDollars', 'NinetyEightDollars']

    >>> get_text_dollar(987654321)
    'NineHundredEightySevenMillionSixHundredFiftyFourThousandThreeHundredTwentyOneDollars'
    '''
    result = ['Dollars']

    def fill_tens_and_digits(amount):
        first_digit_amount = amount % 10
        two_digits_amount = amount % 100
        if 10 < two_digits_amount < 20:
            result.append(TWO_DIGITS[first_digit_amount - 1])
        else:
            if 0 < first_digit_amount < 10:
                result.append(DIGITS[first_digit_amount - 1])
            second_digit_amount = amount // 10 % 10
            if 0 < second_digit_amount < 10:
                result.append(TENS[second_digit_amount - 1])
        third_digit_amount = amount // 100 % 10
        if 0 < third_digit_amount < 10:
            result.append(HUNDREDS)
            result.append(DIGITS[third_digit_amount - 1])

    three_digits_block_idx = 0
    while amount > 0:
        three_digits_block = amount % 1000
        if three_digits_block:
            result.append(THREE_DIGITS[three_digits_block_idx])
            fill_tens_and_digits(three_digits_block)

        three_digits_block_idx += 1
        amount //= 1000

    result.reverse()
    return ''.join(result)

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
            print(get_text_dollar(int(test)))

        test_cases.close()
