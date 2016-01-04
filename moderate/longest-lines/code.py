#!python3
def get_longest_lines(n, in_list):
    '''(int, list of strings) -> (list of strings)

    Returns n longest lines in the given list of strings in_list.
    The returned list are sorted by string length in descending order.

    >>> get_longest_lines(2, ['Hello World', 'CodeEval', 'Quick Fox', 'A', 'San Francisco'])
    ['San Francisco', 'Hello World']
    '''
    in_list = in_list[:]
    in_list.sort(key = lambda s: (len(s), s), reverse = True)
    return in_list[:n]

def parse_file(in_list):
    '''(list of strings) -> (list of strings, int)

    >>> parse_file(['2\\n', 'Hello World\\n', 'CodeEval\\n', 'Quick Fox\\n', 'A\\n', 'San Francisco\\n'])
    (2, ['Hello World', 'CodeEval', 'Quick Fox', 'A', 'San Francisco'])

    >>> parse_file([' 2 \\n', 'Hello World \\n', '\\n', ' CodeEval\\n', 'Quick Fox\\n', '\\n', 'A\\n', 'San Francisco\\n'])
    (2, ['Hello World', 'CodeEval', 'Quick Fox', 'A', 'San Francisco'])
    '''
    normal_strings = list(s for s in (s.strip('\t\n ')
                                      for s in in_list)
                          if s)
    return int(normal_strings[0]), normal_strings[1:]

if __name__ == '__main__':
    import sys
    if (len(sys.argv) <= 1):
        import doctest
        doctest.testmod()
    else:
        test_cases = open(sys.argv[1], 'r')
        for s in get_longest_lines(*parse_file(test_cases.readlines())):
            print(s)

        test_cases.close()
