#!python3
def intersection(lst1, lst2):
    '''(list of interger, list of integer) -> list of integer

    Returns list contains intersection on lst1 and lst2 lists.
    
    >>> intersection([1,2,3,4],[4,5,6])
    [4]
    >>> intersection([20,21,22],[45,46,47])
    []
    >>> intersection([7,8,9],[8,9,10,11,12])
    [8, 9]
    '''

    result = list(set(lst1).intersection(set(lst2)))
    result.sort()
    return result

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
            result = intersection(*map(
                lambda s: list(map(int, s.split(','))),
                test.split(';',2)))
            print(','.join(map(str, result)))

        test_cases.close()