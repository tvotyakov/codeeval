#!python3
def split_input(input_string):
    ''' string -> generator of integer

    Splits input_string by a whitespace and returns generator of
    all elements as integer.

    >>> list(split_input('40 40 40 40 29 29 29 29 29 29 29 29 57 57 92 92 92 92 92 86 86 86 86 86 86 86 86 86 86'))
    [40, 40, 40, 40, 29, 29, 29, 29, 29, 29, 29, 29, 57, 57, 92, 92, 92, 92, 92, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86]

    >>> list(split_input('73 73 73 73 41 41 41 41 41 41 41 41 41 41'))
    [73, 73, 73, 73, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41]

    >>> list(split_input('1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2'))
    [1, 1, 3, 3, 3, 2, 2, 2, 2, 14, 14, 14, 11, 11, 11, 2]

    >>> list(split_input('7'))
    [7]
    '''
    
    return map(int, input_string.split(' '))

def compress(input_nums):
    ''' generator of integers -> generator of integers

    Assume that someone dictates you a sequence of numbers and you
    need to write it down. For brevity, he dictates it as follows:
    first says the number of consecutive identical numbers and then
    says the number itself. E.g. The sequence
      1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2
    will be dictated as "Two times one, three times three, four times
    two, three times fourteen, three times eleven, one time two",
    so you will write down the sequence 2 1 3 3 4 2 3 14 3 11 1 2
    This function compresses a sequence input_nums using described
    algorithm of compression and return generator of a compressed
    sequence.
    
    >>> list(compress(split_input('40 40 40 40 29 29 29 29 29 29 29 29 57 57 92 92 92 92 92 86 86 86 86 86 86 86 86 86 86')))
    [4, 40, 8, 29, 2, 57, 5, 92, 10, 86]

    >>> list(compress(split_input('73 73 73 73 41 41 41 41 41 41 41 41 41 41')))
    [4, 73, 10, 41]

    >>> list(compress(split_input('1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2')))
    [2, 1, 3, 3, 4, 2, 3, 14, 3, 11, 1, 2]
    
    >>> list(compress(split_input('7')))
    [1, 7]
    '''
    val, val_count = None, None
    for n in input_nums:
        if val == n:
            val_count += 1
        else:
            if val != None:
               yield val_count
               yield val
            val = n
            val_count = 1

    if val != None:
        yield val_count
        yield val

def join_output(compressed_sequence):
    '''

    >>> join_output(compress(split_input('1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2')))
    '2 1 3 3 4 2 3 14 3 11 1 2'

    >>> join_output(compress(split_input('73 73 73 73 41 41 41 41 41 41 41 41 41 41')))
    '4 73 10 41'

    >>> join_output(compress(split_input('1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2')))
    '2 1 3 3 4 2 3 14 3 11 1 2'
    
    >>> join_output(compress(split_input('7')))
    '1 7'
    '''
    return ' '.join(map(str, compressed_sequence))
    
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
            print(join_output(compress(split_input(test))))

        test_cases.close()
