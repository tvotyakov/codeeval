#!python3
def gen_triangle_line(prev_line):
    ''' (tuple of integer) -> generator of integer

    Returns generator of next line of Pascal's triangle
    for a given previous line prev_line.

    >>> tuple(gen_triangle_line((1,)))
    (1, 1)

    >>> tuple(gen_triangle_line((1, 1)))
    (1, 2, 1)
    
    >>> tuple(gen_triangle_line((1,2,1)))
    (1, 3, 3, 1)

    >>> tuple(gen_triangle_line((1, 3, 3, 1)))
    (1, 4, 6, 4, 1)

    >>> tuple(gen_triangle_line((1, 4, 6, 4, 1)))
    (1, 5, 10, 10, 5, 1)
    '''
    yield 1
    for i in range(len(prev_line) - 1):
        yield prev_line[i] + prev_line[i + 1]
    yield 1

triangle_cache = [(1,)]
def get_pascals_triangle(depth):
    '''(int) -> list of integer

    Returns Pascal's triangle of a given depth (1 based)
    in row major form.

    >>> get_pascals_triangle(0)
    ()

    >>> get_pascals_triangle(1)
    (1,)

    >>> get_pascals_triangle(2)
    (1, 1, 1)

    >>> get_pascals_triangle(6)
    (1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10, 10, 5, 1)

    >>> get_pascals_triangle(3)
    (1, 1, 1, 1, 2, 1)

    >>> get_pascals_triangle(4)
    (1, 1, 1, 1, 2, 1, 1, 3, 3, 1)

    >>> get_pascals_triangle(5)
    (1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1)
    '''
    if depth <= 0: return tuple()
    while(depth > len(triangle_cache)):
        triangle_cache.append(tuple(gen_triangle_line(triangle_cache[-1])))

    return tuple(i for line in triangle_cache[:depth] for i in line)

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
            print(' '.join(map(str, get_pascals_triangle(int(test)))))

        test_cases.close()
