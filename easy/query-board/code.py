#!python3
def get_matrix(size, *, row = None, col = None, num = None):
    '''(int, row = int, col = int, num = int) -> size*size matrix of integer

    Returns matrix of integer of given size filled with zeros.
    If row is set, then all elements in row with the given index will
    have value num instead of zero.
    If col is set, then all elements in column with the given index
    will have value num insetead of zero.

    >>> get_matrix(3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    >>> get_matrix(2)
    [[0, 0], [0, 0]]

    >>> get_matrix(3, row = 2, num = 1)
    [[0, 0, 0], [0, 0, 0], [1, 1, 1]]

    >>> get_matrix(3, col = 1, num = 2)
    [[0, 2, 0], [0, 2, 0], [0, 2, 0]]
    '''
    result = [[0] * size for _ in range(size)]
    if row != None:
        result[row] = [num] * size
    if col != None:
        for i in range(size):
            result[i][col] = num
    return result
    
def set_row(matrix, index, num):
    '''(matrix of integers, int, int) -> None

    Sets an integer value num of all elements in the matrix row
    with a given index.

    >>> m = get_matrix(256)
    >>> set_row(m, 15, 7)
    >>> m == get_matrix(256, row = 15, num = 7)
    True
    
    >>> m = get_matrix(256)
    >>> set_row(m, 16, 31)
    >>> m == get_matrix(256, row = 16, num = 31)
    True

    >>> m = get_matrix(256)
    >>> set_row(m, 0, 11)
    >>> m == get_matrix(256, row = 0, num = 11)
    True

    >>> m = get_matrix(256)
    >>> set_row(m, 255, 5)
    >>> m == get_matrix(256, row = 255, num = 5)
    True
    '''
    matrix[index] = [num] * len(matrix[index])

def set_col(matrix, index, num):
    '''(matrix of integers, int, int) -> None

    Sets an integer value num of all elements in the matrix
    column with a given index

    >>> m = get_matrix(256)
    >>> set_col(m, 32, 20)
    >>> m == get_matrix(256, col = 32, num = 20)
    True

    >>> m = get_matrix(256)
    >>> set_col(m, 2, 14)
    >>> m == get_matrix(256, col = 2, num = 14)
    True

    >>> m = get_matrix(256)
    >>> set_col(m, 0, -5)
    >>> m == get_matrix(256, col = 0, num = -5)
    True
    
    >>> m = get_matrix(256)
    >>> set_col(m, 255, 94)
    >>> m == get_matrix(256, col = 255, num = 94)
    True
    '''
    for i in range(len(matrix[0])):
        matrix[i][index] = num

def query_row(matrix, index):
    ''' (matrix of integers, int) -> int

    Returns a sum of all elements in a row with a given index
    in a matrix

    >>> m = get_matrix(256)
    >>> set_col(m, 32, 20)
    >>> set_row(m, 15, 7)
    >>> set_row(m, 16, 31)
    >>> set_col(m, 2, 14)
    >>> query_row(m, 10)
    34
    '''
    return sum(matrix[index])
    
def query_col(matrix, index):
    ''' (matrix of integers, int) -> int

    Returns a sum of all elements in a column with a given index
    in a matrix.

    >>> m = get_matrix(256)
    >>> set_col(m, 32, 20)
    >>> set_row(m, 15, 7)
    >>> set_row(m, 16, 31)
    >>> query_col(m, 32)
    5118
    '''
    return sum(matrix[i][index] for i in range(len(matrix[0])))

def query_board(commands):
    ''' generator of strings -> string

    >>> commands = ['SetCol 32 20', 'SetRow 15 7', 'SetRow 16 31', 'QueryCol 32']
    >>> [r for r in query_board(commands)]
    [5118]
    
    >>> commands = ['SetCol 32 20', 'SetRow 15 7', 'SetRow 16 31', 'QueryCol 32', 'SetCol 2 14', 'QueryRow 10']
    >>> [r for r in query_board(commands)]
    [5118, 34]
    
    >>> commands = ['SetCol 32 20', 'SetRow 15 7', 'SetRow 16 31', 'QueryCol 32', 'SetCol 2 14', 'QueryRow 10', 'SetCol 14 0', 'QueryRow 15']
    >>> [r for r in query_board(commands)]
    [5118, 34, 1792]

    >>> commands = ['SetCol 32 20', 'SetRow 15 7', 'SetRow 16 31', 'QueryCol 32', 'SetCol 2 14', 'QueryRow 10', 'SetCol 14 0', 'QueryRow 15', 'SetRow 10 1', 'QueryCol 2']
    >>> [r for r in query_board(commands)]
    [5118, 34, 1792, 3571]
    '''
    query_board_commands = {
        'SetCol': set_col,
        'SetRow': set_row,
        'QueryCol': query_col,
        'QueryRow': query_row,
        }
    m = get_matrix(256)
    for command in commands:
        command_name, *params = command.split(' ')
        params = list(map(int, params))
        result = query_board_commands[command_name](m, *params)
        if result:
            yield result

if __name__ == '__main__':
    import sys
    if (len(sys.argv) <= 1):
        import doctest
        doctest.testmod()
    else:
        test_cases = (test.rstrip('\n') for test in open(sys.argv[1], 'r'))
        for r in query_board(s for s in test_cases if s):
            print(r)

        test_cases.close()
