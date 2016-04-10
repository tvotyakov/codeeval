#!python3
def check_cardnum(in_str):
    ''' string -> boolean

    Takes credit card number and returns true if the number is real, false else.

    >>> check_cardnum('9999 9999 9999 9999')
    False

    >>> check_cardnum('9999 9999 9999 9993')
    True

    >>> check_cardnum('1234 5678 9876 5432')
    True
    '''
    return sum(int(ch) * (2 if not i % 2 else 1)
        for i, ch in enumerate(in_str.replace(' ', ''))) % 10 == 0

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
            print('Real' if check_cardnum(test) else 'Fake')

        test_cases.close()
