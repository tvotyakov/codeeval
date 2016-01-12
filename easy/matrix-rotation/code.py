#!python3
from math import sqrt
def get_rotated_matrix(matrix):
    '''

    Gets an array which represents a square matrix in row major form. Returns
    the generator to generate an array which represents clockwise rotated source
    matrix in row major form.

    >>> list(get_rotated_matrix([]))
    []

    >>> list(get_rotated_matrix(['a']))
    ['a']

    >>> list(get_rotated_matrix(['a', 'b', 'c', 'd']))
    ['c', 'a', 'd', 'b']

    >>> list(get_rotated_matrix(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']))
    ['g', 'd', 'a', 'h', 'e', 'b', 'i', 'f', 'c']
    '''
    matrix_size = round(sqrt(len(matrix)))

    return (matrix[row * matrix_size + col]
            for col in range(matrix_size)
            for row in range(matrix_size-1, -1, -1))

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
            print(' '.join(get_rotated_matrix(test.split(' '))))

        test_cases.close()
