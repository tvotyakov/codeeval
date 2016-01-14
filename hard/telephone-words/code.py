#!python3
import itertools

PHONE_CHARS = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
def get_string_gen(in_str):
    ''' (in_str) -> generator of strings

    Returns generator which generates all possible sequences of letters that
    can be represented by givent telephone number.

    >>> list(get_string_gen('0'))
    ['0']

    >>> list(get_string_gen('2'))
    ['a', 'b', 'c']

    >>> list(get_string_gen('23'))
    ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    >>> list(get_string_gen('456'))
    ['gjm', 'gjn', 'gjo', 'gkm', 'gkn', 'gko', 'glm', 'gln', 'glo', 'hjm', 'hjn', 'hjo', 'hkm', 'hkn', 'hko', 'hlm', 'hln', 'hlo', 'ijm', 'ijn', 'ijo', 'ikm', 'ikn', 'iko', 'ilm', 'iln', 'ilo']
    '''
    nums = map(int, list(in_str))
    chars = [PHONE_CHARS[num] for num in nums]
    return (''.join(prod) for prod in itertools.product(*chars))

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
            print(','.join(get_string_gen(test)))

        test_cases.close()
