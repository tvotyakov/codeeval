#!python3
def swap_elements(elements, positions):
    '''(list, list of tuples of integer) -> list

    >>> elements = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    >>> swap_elements(elements, [(0, 8)])
    >>> elements == ['9', '2', '3', '4', '5', '6', '7', '8', '1']
    True
    >>> elements = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    >>> swap_elements(elements, [(0, 1), (1, 3)])
    >>> elements == ['2', '4', '3', '1', '5', '6', '7', '8', '9', '10']
    True
    '''
    for pos in positions:
        elements[pos[0]], elements[pos[1]] = elements[pos[1]], elements[pos[0]]
    
def parse_str(in_str):
    '''(string) -> (list, list of tuples of integer)

    Parses given string in_str to tuple includes list of elements
    to swap and list of tuples with indexes of elements to swap.

    >>> parse_str('1 2 3 4 5 6 7 8 9 : 0-8')
    (['1', '2', '3', '4', '5', '6', '7', '8', '9'], [(0, 8)])
    >>> parse_str('1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3')
    (['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], [(0, 1), (1, 3)])
    '''
    num_list, positions = in_str.split(' : ')
    return (list(num_list.split(' ')),
            list(map(lambda s: tuple(map(int, s.split('-'))),
                     positions.split(', '))))

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
            elements, positions = parse_str(test)
            swap_elements(elements, positions)
            print(' '.join(elements))

        test_cases.close()