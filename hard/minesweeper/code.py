#!python3
def str_to_matrix(in_str):
    ''' (string) -> matrix

    Parses given in_str and fill M*N matrix. in_str
    contains M,N separated by comma, a simicolon and
    the M*N in row major form.

    >>> str_to_matrix('3,5;**.........*...')
    [['*', '*', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '*', '.', '.', '.']]

    >>> str_to_matrix('1,1;*')
    [['*']]
    >>> str_to_matrix('2,2;*.*.')
    [['*', '.'], ['*', '.']]
    '''
    matrix = []
    MN, line = in_str.split(';')
    M, N = map(int, MN.split(','))
    line = list(line)
    for i in range(M):
        matrix.append(line[N*i:N*(i+1)])
    return matrix

neighbours_pos = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]
def calc_mines(matrix, row, col):
    ''' (matrix, int, int) -> int

    Returns count of mines in the neighbour of a cell
    in the given row and column of the matrix. Returns '*'
    if the cell contains '*'.

    >>> calc_mines([['*', '*', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '*', '.', '.', '.']], 0, 0)
    '*'

    >>> calc_mines([['*', '*', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '*', '.', '.', '.']], 0, 2)
    1

    >>> calc_mines([['*', '*', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '*', '.', '.', '.']], 1, 0)
    3
    '''
    if (matrix[row][col] == '*'): return '*'
    s = sum(1
              for pos in neighbours_pos
                if (0 <= row + pos[0] < len(matrix) and
                    0 <= col + pos[1] < len(matrix[0]) and
                    matrix[row + pos[0]][col + pos[1]] == '*')
            )
    return s


def fill_matrix(str):
    ''' (string) -> matrix

    According to the given string representing source matrix
    in row major form returns matrix where each element
    contains either '*' which represents a mine in the
    corresponding sell, or a number which indicates the
    number of mines adjacent to it.

    >>> fill_matrix('5,3;**.........*...')
    [['*', '*', 1], [2, 2, 1], [0, 1, 1], [0, 1, '*'], [0, 1, 1]]

    >>> fill_matrix('3,5;**.........*...')
    [['*', '*', 1, 0, 0], [3, 3, 2, 0, 0], [1, '*', 1, 0, 0]]
    '''
    matrix = str_to_matrix(str)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = calc_mines(matrix, i, j)
    return matrix

def matrix_to_str(matrix):
    ''' (matrix) -> string

    Returns the given M*N matrix in row major form.

    >>> matrix_to_str([['*', '*', 1], [2, 2, 1], [0, 1, 1], [0, 1, '*'], [0, 1, 1]])
    '**122101101*011'

    >>> matrix_to_str([['*', '*', 1, 0, 0], [3, 3, 2, 0, 0], [1, '*', 1, 0, 0]])
    '**100332001*100'
    '''
    return ''.join(str(matrix[i][j])
                    for i in range(len(matrix))
                    for j in range(len(matrix[i])))

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
            print(matrix_to_str(fill_matrix(test)))

        test_cases.close()
