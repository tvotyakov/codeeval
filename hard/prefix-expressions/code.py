#!python3
def find_operands_pos(expression_list):
    ''' (list of strings) -> integer

    Finds and returns index of first operand in the given list
    which representes a prefix expression parts.

    >>> find_operands_pos(['*', '+', '1', '2', '3'])
    2

    >>> find_operands_pos(['1'])
    0

    >>> find_operands_pos(['*', '1', '2'])
    1

    >>> find_operands_pos([])
    -1
    '''
    for i, x in enumerate(expression_list):
        if x not in '*+/':
            return i
    return -1

operations = {
    "*": lambda x, y: x * int(y),
    "+": lambda x, y: x + int(y),
    "/": lambda x, y: x / int(y)
}
def eval_expression(expression_str):
    ''' (string) -> integer

    Evals and returns result of the given prefix expression string.

    >>> eval_expression('* 1 2')
    2

    >>> eval_expression('+ 1 2')
    3

    >>> eval_expression('/ 2 2')
    1

    >>> eval_expression('1')
    1

    >>> eval_expression('* + 2 3 4')
    20

    >>> eval_expression('* / 1 2 4')
    2
    '''
    expression_list = expression_str.split(' ')
    start_operands_idx = find_operands_pos(expression_list)
    assert(start_operands_idx >= 0)

    val = int(expression_list[start_operands_idx])
    operand_idx = start_operands_idx + 1
    for operation_idx in range(start_operands_idx - 1, -1, -1):
        val = operations[expression_list[operation_idx]](val, expression_list[operand_idx])
        operand_idx += 1

    return round(val)

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
            print(eval_expression(test))

        test_cases.close()
