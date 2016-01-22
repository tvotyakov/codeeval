#!python3
COINS = [5, 3]
def get_minimum_coins(total):
    ''' (positive integer) -> positive integer

    Returns the minimum count of coins of value 1, 3, and 5 needed to arrive
    a given total integer.

    >>> get_minimum_coins(11)
    3

    >>> get_minimum_coins(20)
    4

    >>> get_minimum_coins(1)
    1

    >>> get_minimum_coins(3)
    1

    >>> get_minimum_coins(5)
    1

    >>> get_minimum_coins(107)
    23
    '''
    result = 0
    for coin in COINS:
        coin_count = total // coin
        total -= coin_count * coin
        result += coin_count

    return result + total

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
            print(get_minimum_coins(int(test)))

        test_cases.close()
