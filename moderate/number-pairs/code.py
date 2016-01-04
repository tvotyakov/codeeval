#!python3
def number_pairs(in_list, sum_val):
    ''' (list of integers, int) -> (list of tuples of integer)

    >>> number_pairs([1, 2, 3, 4, 6], 5)
    [(1, 4), (2, 3)]

    >>> number_pairs([2, 4, 5, 6, 9, 11, 15], 20)
    [(5, 15), (9, 11)]

    >>> number_pairs([1, 2, 3, 4], 50)
    []
    '''
    result = []
    for first_el in enumerate(in_list):
        if (first_el[1] > sum_val): break
        for second_el in in_list[first_el[0] + 1:]:
            sum_of_elements = first_el[1] + second_el
            if sum_of_elements == sum_val:
                result.append((first_el[1], second_el))
            elif sum_of_elements > sum_val:
                break
    return result
            
def parse_string(in_str):
    ''' (string) -> (list of integers, int)

    >>> parse_string('1,2,3,4,6;5')
    ([1, 2, 3, 4, 6], 5)

    >>> parse_string('2,4,5,6,9,11,15;20')
    ([2, 4, 5, 6, 9, 11, 15], 20)

    >>> parse_string('1,2,3,4;50')
    ([1, 2, 3, 4], 50)
    '''
    int_list, sum_val = in_str.split(';')
    return list(map(int, int_list.split(','))), int(sum_val)

def combine_string(in_list):
    '''(list of tuples of integer) -> string

    >>> combine_string([(1, 4), (2, 3)])
    '1,4;2,3'

    >>> combine_string([(5, 15), (9, 11)])
    '5,15;9,11'

    >>> combine_string([])
    'NULL'
    '''
    return (';'.join(map(lambda t: ','.join(map(str, t)), in_list))
            if in_list else 'NULL')

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
            print(combine_string(number_pairs(*parse_string(test))))

        test_cases.close()
