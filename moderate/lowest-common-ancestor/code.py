#!python3
ANCESTOR_INDEX = 0
DEPTH_INDEX = 1
tree = {30: (None, 0),
        8: (30, 1), 52: (30, 1),
        3: (8, 2), 20: (8, 2),
        10: (20, 3), 29: (20, 3)}

def get_ancestors(num):
    '''(num) -> set of tuples of integer

    Returns set of tuples represented num's ancestors and their
    depth in the tree.

    >>> set(get_ancestors(100)) == set()
    True
    
    >>> set(get_ancestors(8)) == {(30, 0),(8, 1)}
    True

    >>> set(get_ancestors(20)) == {(8, 1), (30, 0), (20, 2)}
    True

    >>> set(get_ancestors(30)) == {(30, 0)}
    True

    >>> set(get_ancestors(10)) == {(20, 2), (8, 1), (30, 0), (10, 3)}
    True
    '''
    if num not in tree: return

    ancestor = num
    while (ancestor != None):
        yield (ancestor, tree[ancestor][DEPTH_INDEX])
        ancestor = tree[ancestor][ANCESTOR_INDEX]

def get_lowest_common_ancestor(num1, num2):
    '''(int, int) -> int

    >>> get_lowest_common_ancestor(10, 29)
    20
    
    >>> get_lowest_common_ancestor(3, 29)
    8
    
    >>> get_lowest_common_ancestor(30, 29)
    30
    
    >>> get_lowest_common_ancestor(30, 30)
    30
    
    >>> get_lowest_common_ancestor(10, 52)
    30
    '''
    common_ancestors = set(get_ancestors(num1)) & set(get_ancestors(num2))
    if common_ancestors == set(): return None
    return max(common_ancestors, key = lambda a: a[DEPTH_INDEX])[ANCESTOR_INDEX]

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
            print(get_lowest_common_ancestor(*map(int, test.split(' ', 2))))

        test_cases.close()
