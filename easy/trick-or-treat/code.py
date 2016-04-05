#!python3
COEFFS = (3, 4, 5)
KEYS_INDECES = {'Vampires': 0, 'Zombies': 1, 'Witches': 2, 'Houses': 3}

def parse_input(in_str):
    ''' in_str -> tuple(list of integers, integer)

    Takes an input string with number of Vampires, Zombies, Witches, and Houses.
    Returns tuple of list of integers and integer. List contains count of
    Vampires, Zombies, and Witches. Integer is a number of visited houses.

    >>> parse_input('Vampires: 1, Zombies: 1, Witches: 1, Houses: 1')
    ([1, 1, 1], 1)

    >>> parse_input('Vampires: 3, Zombies: 2, Witches: 1, Houses: 10')
    ([3, 2, 1], 10)

    >>> parse_input('Zombies: 2, Vampires: 3, Witches: 1, Houses: 10')
    ([3, 2, 1], 10)

    >>> parse_input('Houses: 1, Zombies: 2, Vampires: 3, Witches: 1, Houses: 1')
    ([3, 2, 1], 2)
    '''
    result = [0, 0, 0, 0]

    for data in in_str.split(', '):
        key, value = data.split(': ')
        value = int(value)
        result[KEYS_INDECES[key]] += value

    return result[:-1], result[-1]

def calc_candies(children, houses):
    ''' list of integer, integer -> int

    Expects list of integer with counts of Vampires, Zombies, Witches, and
    number of visited houses. Returns an integer number of candies each child
    will get, according to number of candies each costume gets in one house and
    number of visited houses.

    >>> calc_candies([1, 1, 1], 1)
    4

    >>> calc_candies([3, 2, 1], 10)
    36
    '''
    children_count = sum(children)
    total_candies = sum(COEFFS[i] * costumes_count * houses
                          for i, costumes_count in enumerate(children))
    return total_candies // children_count

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
            print(calc_candies(*parse_input(test)))

        test_cases.close()
