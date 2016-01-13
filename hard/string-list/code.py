#!python3
import itertools
def get_string_gen(str_len, characters):
    ''' (int, list of characters) -> list of strings

    Returns all of the possible ways to write a string of length str_len from
    the given list of characters in alphabetical order. Expects that the given
    list of characters sorted alphabetically.

    >>> list(get_string_gen(1, ['a']))
    ['a']

    >>> list(get_string_gen(2, ['a', 'b']))
    ['aa', 'ab', 'ba', 'bb']

    >>> list(get_string_gen(3, ['o', 'p']))
    ['ooo', 'oop', 'opo', 'opp', 'poo', 'pop', 'ppo', 'ppp']
    '''
    return (''.join(p) for p in itertools.product(characters, repeat = str_len))

def parse_string(in_str):
    ''' (string) -> tuple of an integer and list of letters

    Expects a string with a positive integer N, followed by a string S
    (comma-delimited). Extracts these values from the in_str, and returns
    the integer N, and a list of unique characters from S sorted alphabetically.

    >>> parse_string('1,aa')
    (1, ['a'])

    >>> parse_string('2,ab')
    (2, ['a', 'b'])

    >>> parse_string('2,ba')
    (2, ['a', 'b'])

    >>> parse_string('3,pop')
    (3, ['o', 'p'])
    '''
    num, s = in_str.split(',')[:2]
    return int(num), sorted(set(s))

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
            print(','.join(get_string_gen(*parse_string(test))))

        test_cases.close()
