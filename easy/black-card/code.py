#!python3
def find_winner(in_list, num):
    ''' (list of string, integer) -> string

    Takes list and integer number. Starting with the first item, we start to
    count all items from one to the number circularly, and remove them until
    only one item will remain. This last item will be returned.

    >>> find_winner(['John'], 3)
    'John'

    >>> find_winner(['John', 'Sara', 'Tom', 'Susan'], 3)
    'Sara'

    >>> find_winner(['John', 'Tom', 'Mary'], 5)
    'Mary'
    '''
    list_ = in_list[:]
    while len(list_) > 1:
        del(list_[num%len(list_) - 1])
    return list_[0]

def parse_str(in_str):
    ''' string -> (list of string, integer)

    >>> parse_str('John Sara Tom Susan | 3')
    (['John', 'Sara', 'Tom', 'Susan'], 3)

    >>> parse_str('John Tom Mary | 5')
    (['John', 'Tom', 'Mary'], 5)
    '''
    list_, num = in_str.split(' | ')
    return list_.split(' '), int(num)

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
            print(find_winner(*parse_str(test)))

        test_cases.close()
