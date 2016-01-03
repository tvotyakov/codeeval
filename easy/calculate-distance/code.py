#!python3
import math
def distance(p1, p2):
    '''(tuple of two integers, tuple of two integers) -> integer

    Calculates distance between two points: p1 and p2.

    >>> distance((25, 4), (1, -6))
    26
    >>> distance((47, 43), (-25, -11))
    90
    '''
    d2 = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
    return int(math.sqrt(d2))

def str_to_points(in_str):
    '''(string) -> list of two tuples of two integers

    >>> str_to_points('(25, 4) (1, -6)')
    [(25, 4), (1, -6)]

    >>> str_to_points('(47, 43) (-25, -11)')
    [(47, 43), (-25, -11)]
    '''
    return list(map(
        lambda s: tuple(map(int, s.split(', '))),
        in_str.strip('()').split(') (')))

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
            
            print(distance(*str_to_points(test)))

        test_cases.close()
