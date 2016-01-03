#!python3
def gen_multiplication_table(n):
    '''(int) -> list of strings

    Returns list of strings represented grade school multiplication
    table upto nxn.

    >>> gen_multiplication_table(3)
    ['1   2   3', '2   4   6', '3   6   9']

    >>> gen_multiplication_table(4)
    ['1   2   3   4', '2   4   6   8', '3   6   9  12', '4   8  12  16']
    '''
    table = []
    for i in range(1, n + 1):
        line = ''
        for j in range(1, n + 1):
            line += repr(j * i).rjust(4)
        table.append(line.strip(' '))
    return table

for line in gen_multiplication_table(12):
    print(line)
