#!python3
PARENTHESES_PAIRS = {'(': ')', '[': ']', '{': '}'}
def check_parentheses(in_str):
    ''' (string) -> boolean

    Returns True, if the input string has a valid parentheses order.

    >>> [check_parentheses(val) for val in ['()', '[]', '{}']]
    [True, True, True]

    >>> [check_parentheses(val) for val in ['([{}])', '()[]{}']]
    [True, True]

    >>> [check_parentheses(val) for val in ['[', '(', '{', ']', ')', '}']]
    [False, False, False, False, False, False]

    >>> [check_parentheses(val) for val in ['][', ')(', '}{']]
    [False, False, False]

    >>> [check_parentheses(val) for val in ['[(])', '[{]}', '([)]', '({)}', '{[}]', '{(})']]
    [False, False, False, False, False, False]
    '''
    is_valid, parentheses = True, []
    for char in in_str:
        if char in '([{':
            parentheses.append(char)
        else:
            is_valid = (bool(parentheses) and
                        PARENTHESES_PAIRS[parentheses.pop()] == char)
        if not is_valid: break

    return is_valid and not parentheses

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
            print(check_parentheses(test))

        test_cases.close()
