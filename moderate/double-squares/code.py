#!python3
import math
def get_double_squares_count(num):
    ''' (int) -> int

    >>> get_double_squares_count(10)
    1

    >>> get_double_squares_count(25)
    2

    >>> get_double_squares_count(3)
    0

    >>> get_double_squares_count(0)
    1

    >>> get_double_squares_count(1)
    1
    '''
    if not num: return 1
    counter = 0
    for i in range(math.ceil(math.sqrt(num))):
        val = num - i ** 2
        s = math.sqrt(val)
        if s < i: break
        if int(s) == s:
            counter += 1
    return counter
    
if __name__ == '__main__':
    import sys
    if (len(sys.argv) <= 1):
        import doctest
        doctest.testmod()
    else:
        test_cases = open(sys.argv[1], 'r')
        row_num, row_count = 0, 0
        for test in test_cases:
            test = test.rstrip('\n')
            if row_num == 0:
                row_count = int(test)
            elif row_num > row_count:
                break
            else:
                print(get_double_squares_count(int(test)))
            row_num += 1

        test_cases.close()
