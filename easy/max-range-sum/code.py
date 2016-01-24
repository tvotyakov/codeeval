#!python3
def get_max_range_sum(in_list, range_len):
    ''' (list of integers, integer) -> integer

    Expects a list of integers and the number of contiguous integers (range_len).
    Returns the maximum sum of the given number of contiguous integers from the
    list, if it is positive, or 0 else.

    >>> get_max_range_sum([1,2, 3], 0)
    0

    >> get_max_range_sum([], 2)
    0

    >>> get_max_range_sum([1], 2)
    0

    >>> get_max_range_sum([1, 2], 2)
    3

    >>> get_max_range_sum([1, 2, 3, 4, 5], 2)
    9

    >>> get_max_range_sum([-2, 1, -3, 2, -4, 3], 2)
    0

    >>> get_max_range_sum([-2, 1, -3, 2, -4, 3], 3)
    1

    >>> get_max_range_sum([7, -3, -10, 4, 2, 8, -2, 4, -5, -2], 5)
    16

    >>> get_max_range_sum([-4, 3, -10, 5, 3, -7, -3, 7, -6, 3], 6)
    0

    >>> get_max_range_sum([-7, 0, -45, 34, -24, 7], 3)
    17
    '''
    if not range_len or range_len > len(in_list):
        return 0
    max_sum = cur_sum = sum(in_list[:range_len])
    for i, next_num in enumerate(in_list[range_len:]):
        cur_sum += -in_list[i] + next_num
        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum if max_sum >= 0 else 0

def parse_in_str(in_str):
    ''' (string) -> tuple of list of integer and integer

    Expects an input string contains an integer number followed by (separated by
    a semicolon) a list of integers separated by space. Returns a tuple with the
    list and the integer number.

    >>> parse_in_str('')
    ([], 0)

    >>> parse_in_str('5;7 -3 -10 4 2 8 -2 4 -5 -2')
    ([7, -3, -10, 4, 2, 8, -2, 4, -5, -2], 5)

    >>> parse_in_str(';-4 3 -10 5 3 -7 -3 7 -6 3')
    ([-4, 3, -10, 5, 3, -7, -3, 7, -6, 3], 0)

    >>> parse_in_str('6;-4 3 -10 5 3 -7 -3 7 -6 3')
    ([-4, 3, -10, 5, 3, -7, -3, 7, -6, 3], 6)

    >>> parse_in_str('3;-7 0 -45 34 -24 7')
    ([-7, 0, -45, 34, -24, 7], 3)
    '''
    if not in_str: return [], 0

    num, out_list = in_str.split(';')
    num = int(num) if num else 0
    out_list = list(map(int, out_list.split(' ')))
    return out_list, num

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
            print(get_max_range_sum(*parse_in_str(test)))

        test_cases.close()
