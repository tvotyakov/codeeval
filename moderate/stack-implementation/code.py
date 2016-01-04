#!python3
stack = []
def clear():
    stack[:] = []
    
def push(val):
    ''' (int) -> None

    >>> clear();stack == []
    True

    >>> push(1); stack == [1]
    True

    >>> push(2); stack == [1, 2]
    True

    >>> push(3); stack == [1, 2, 3]
    True
    '''
    stack.append(val)

def pop():
    ''' () -> int

    >>> clear();stack == []
    True
    >>> push(1);push(2);push(3)
    >>> pop(), stack == [1, 2]
    (3, True)
    
    >>> pop(), stack == [1]
    (2, True)
    
    >>> pop(), stack == []
    (1, True)

    >>> pop()
    '''
    if len(stack) == 0: return None
    
    val = stack[-1]
    del stack[-1]
    return val

def parse_string(in_str):
    ''' (string) -> generator of list of integer

    Splits in_str string by spaces and returns every alternate element.

    >>> list(parse_string('1 2 3 4'))
    [1, 2, 3, 4]

    >>> list(parse_string('10 -2 3 4'))
    [10, -2, 3, 4]
    '''
    return map(int, in_str.split(' '))

def check_stack_implementation(in_str):
    ''' (string) -> string

    Returns string with every alternate integer (space delimited)
    from a given string in_str.
    
    >>> check_stack_implementation('1 2 3 4'), stack == []
    ('4 2', True)

    >>> check_stack_implementation('10 -2 3 4'), stack == []
    ('4 -2', True)
    '''
    
    clear()
    for el in parse_string(in_str):
        push(el)

    result, is_alt = '', True
    el = pop()
    while(el != None):
        if is_alt:
            result += ' ' + str(el)
        is_alt = not is_alt
        el = pop()
    return result.strip()
    
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
            print(check_stack_implementation(test))

        test_cases.close()
