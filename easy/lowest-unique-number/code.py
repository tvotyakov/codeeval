#!python3
def lowest_unique_pos(in_list):
    '''(list of integers) -> int

    Returns a position of the lowest unique number in the given
    list in_list.

    >>> lowest_unique_pos([3, 3, 9, 1, 6, 5, 8, 1, 5, 3])
    5
    >>> lowest_unique_pos([9, 2, 9, 9, 1, 8, 8, 8, 2, 1, 1])
    0
    '''
    uniques = set(el for el in in_list if in_list.count(el) == 1)
    return in_list.index(min(uniques)) + 1 if uniques else 0

def parse_str(in_str):
    '''(string) -> list of integers

    >>> parse_str('3 3 9 1 6 5 8 1 5 3')
    [3, 3, 9, 1, 6, 5, 8, 1, 5, 3]
    >>> parse_str('9 2 9 9 1 8 8 8 2 1 1')
    [9, 2, 9, 9, 1, 8, 8, 8, 2, 1, 1]
    '''
    return list(map(int, in_str.split(' ')))

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
            print(lowest_unique_pos(parse_str(test)))

        test_cases.close()
