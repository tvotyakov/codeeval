#!python3
def multiply_lists(list1, list2):
    '''(list of integers, list of integers) -> list of integers

    Multiplies corresponding elements in list1 and list2 and
    returns the list with the products.

    >>> multiply_lists([9, 0, 6], [15, 14, 9])
    [135, 0, 54]
    >>> multiply_lists([5], [8])
    [40]
    >>> multiply_lists([13, 4, 15, 1, 15, 5], [1, 4, 15, 14, 8, 2])
    [13, 16, 225, 14, 120, 10]
    '''
    return list(map(lambda t: t[0] * t[1], zip(list1, list2)))
    
def parse_input(in_str):
    '''(string) -> (list of integers, list of integers)

    Parses input string in_str and returns its representation
    as tuple of two lists of integers.

    >>> parse_input('9 0 6 | 15 14 9')
    ([9, 0, 6], [15, 14, 9])
    >>> parse_input('5 | 8')
    ([5], [8])
    >>> parse_input('13 4 15 1 15 5 | 1 4 15 14 8 2')
    ([13, 4, 15, 1, 15, 5], [1, 4, 15, 14, 8, 2])
    '''
    list1, list2 = map(lambda s: list(map(int, s.split(' '))),
                       in_str.split(' | '))
    return list1, list2
    
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
            print(' '.join(map(str, multiply_lists(*parse_input(test)))))

        test_cases.close()
