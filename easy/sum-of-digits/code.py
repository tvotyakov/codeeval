#!python3
def sum_of_digits(n):
    '''(int) -> int
    
    >>> sum_of_digits(1)
    1
    >>> sum_of_digits(23)
    5
    >>> sum_of_digits(496)
    19
    '''

    def digits(num):
        while num > 0:
            yield num % 10
            num //= 10
        
    return sum(digits(n))
    
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
            print(sum_of_digits(int(test)))

        test_cases.close()
