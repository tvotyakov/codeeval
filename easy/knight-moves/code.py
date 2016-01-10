#!python3
NEIGHBOURS_POS = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    ( 1, -2), ( 1, 2),
    ( 2, -1), (2,  1)
]

def get_knight_moves(current_pos):
    ''' (string) -> string

    Returns string with space separated positions of available
    knight moves from the given current position.

    >>> get_knight_moves('a1')
    'b3 c2'

    >>> get_knight_moves('a8')
    'b6 c7'

    >>> get_knight_moves('h8')
    'f7 g6'

    >>> get_knight_moves('g2')
    'e1 e3 f4 h4'

    >>> get_knight_moves('d6')
    'b5 b7 c4 c8 e4 e8 f5 f7'
    '''
    x, y = list(current_pos)
    x, y = ord(x) - ord('a') + 1, int(y)
    return ' '.join(chr(ord('a') + x + pos[0] - 1) + str(y + pos[1])
                        for pos in NEIGHBOURS_POS
                        if 0 < x + pos[0] < 9 and 0 < y + pos[1] < 9)

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
            print(get_knight_moves(test))

        test_cases.close()
