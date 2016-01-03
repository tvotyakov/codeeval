#!python3
def digits(num):
    while num > 0:
        yield num % 10
        num //= 10

def is_armstrong_number(num):
    '''(int) -> boolean

    Determines if the input number num are Armstrong number.
    An Armstrong number is an n-digit number that is equal to
    the sum of the n'th powers of its digits.
    
    >>> is_armstrong_number(6)
    True
    >>> is_armstrong_number(153)
    True
    >>> is_armstrong_number(351)
    False
    '''
    
    num_digits = list(digits(num))
    digits_count = len(num_digits)
    return num == sum(map(lambda n: n ** digits_count, num_digits))

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
            print(is_armstrong_number(int(test)))

        test_cases.close()
