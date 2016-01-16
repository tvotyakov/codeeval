#!python3
def sort_by_cocktail_algorithm(in_list, iter_count):
    ''' (list, int) -> None

    Applies iter_count iterations of "coctail sort" algorithm to the given
    input list in place (its mean that source in_list will be mutated).
    The resulting list will be also returned.

    >>> _list = [3, 2, 1]; print(sort_by_cocktail_algorithm(_list, 1), _list)
    [1, 2, 3] [1, 2, 3]

    >>> _list = [5, 4, 9, 10, 7, 3, 2, 1, 6]; print(sort_by_cocktail_algorithm(_list, 1), _list)
    [1, 4, 5, 9, 7, 3, 2, 6, 10] [1, 4, 5, 9, 7, 3, 2, 6, 10]

    >>> _list = [5, 4, 9, 10, 7, 3, 2, 1, 6]; print(sort_by_cocktail_algorithm(_list, 2), _list)
    [1, 2, 4, 5, 7, 3, 6, 9, 10] [1, 2, 4, 5, 7, 3, 6, 9, 10]

    >>> _list = [9, 8, 7, 6, 5, 4, 3, 2, 1]; print(sort_by_cocktail_algorithm(_list, 3), _list)
    [1, 2, 3, 6, 5, 4, 7, 8, 9] [1, 2, 3, 6, 5, 4, 7, 8, 9]
    '''
    def sort_pass(indeces):
        for i in indeces:
            if in_list[i] > in_list[i + 1]:
                in_list[i + 1], in_list[i] = in_list[i: i + 2]

    list_len = len(in_list)
    for iter_num in range(min(iter_count, list_len // 2)):
        # we will do iter_count iterations but not more than half of length of list
        # because doing more than half of length of list iterations is meaningless.

        # from the begining to the end
        sort_pass(range(iter_num, list_len - iter_num - 1))

        # from the end to the begining
        sort_pass(range(list_len - iter_num - 2, iter_num - 1, -1))

    return in_list

def parse_in_str(in_str):
    ''' (string) -> tuple(list, integer)

    Expects string with a list of integers separated by space followed by
    an integer separated by a pipeline '|'. Returns those list and the integer.

    >>> parse_in_str('1 2 3 4 | 1')
    ([1, 2, 3, 4], 1)

    >>> parse_in_str('1 | 2')
    ([1], 2)

    >>> parse_in_str('9 8 7 6 5 | 9')
    ([9, 8, 7, 6, 5], 9)
    '''
    _list, num = in_str.split('|')
    _list = list(map(int, (i for i in _list.split(' ') if i)))
    num = int(num)

    return _list, num

def serialize_str(in_list):
    ''' (list of integers) -> string

    Returns string with integers from the given list separated by space

    >>> serialize_str([1, 2, 3])
    '1 2 3'

    >>> serialize_str([])
    ''

    >>> serialize_str([1])
    '1'

    >>> serialize_str([99, 56, 100, 20, 33])
    '99 56 100 20 33'
    '''
    return ' '.join(map(str, in_list))

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
            print(serialize_str(sort_by_cocktail_algorithm(*parse_in_str(test))))

        test_cases.close()
