#!python3
def calc_max_scores(in_data):
    ''' (iterator of lists of interger) -> list of integers

    Expects an iterator (generator or list) of lists of integers. Each list
    represents a row of 2D-matrix of integer scores. All lists should be of an
    equal length. Returns a list of integers with the highest score in each column
    of the matrix.

    >>> calc_max_scores([])
    []

    >>> calc_max_scores([[]])
    []

    >>> calc_max_scores([[1], [2]])
    [2]

    >>> calc_max_scores([[1, 2]])
    [1, 2]

    >>> calc_max_scores([[1, 2], [3, 4]])
    [3, 4]

    >>> calc_max_scores([[72, 64, 150], [100, 18, 33], [13, 250, -6]])
    [100, 250, 150]

    >>> calc_max_scores([[10, 25, -30, 44], [5, 16, 70, 8], [13, 1, 31, 12]])
    [13, 25, 70, 44]
    '''
    result = []
    for row in in_data:
        if not result:
            result = row[:]
            continue
        for col, val in enumerate(row):
            if val > result[col]:
                result[col] = val
    return result

def parse_in_str(in_str):
    ''' (string) -> generator of lists of integers

    Expects a string which representates a 2D-matrix of integer scores. Each row
    is separated by pipe (|). Each element in a row is separated by space.
    Parses and returns a generator of the matrix rows.

    >>> list(parse_in_str('1 | 2'))
    [[1], [2]]

    >>> list(parse_in_str('1'))
    [[1]]

    >>> list(parse_in_str('1 2 | 3 4'))
    [[1, 2], [3, 4]]

    >>> list(parse_in_str('1 2 | 3 4 | 5 6'))
    [[1, 2], [3, 4], [5, 6]]

    >>> list(parse_in_str('1 2 3 | 4 5 6 | 7 8 9'))
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    >>> list(parse_in_str('72 64 150 | 100 18 33 | 13 250 -6'))
    [[72, 64, 150], [100, 18, 33], [13, 250, -6]]

    >>> list(parse_in_str('10 25 -30 44 | 5 16 70 8 | 13 1 31 12'))
    [[10, 25, -30, 44], [5, 16, 70, 8], [13, 1, 31, 12]]

    >>> list(parse_in_str('100 6 300 20 10 | 5 200 6 9 500 | 1 10 3 400 143'))
    [[100, 6, 300, 20, 10], [5, 200, 6, 9, 500], [1, 10, 3, 400, 143]]
    '''
    return (list(map(int, row.split(' '))) for row in in_str.split(' | '))

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
            print(serialize_str(calc_max_scores(parse_in_str(test))))

        test_cases.close()
