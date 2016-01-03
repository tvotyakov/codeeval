#!python3
def decode_writer(encoded_str, keys):
    '''(string, list of int) -> string

    Decodes and return writer's name of encoded_str based on keys.

    >>> decode_writer('osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg', [3, 35, 27, 62, 51, 27, 46, 57, 26, 10, 46, 63, 57, 45, 15, 43, 53])
    'Stephen King 1947'

    >>> decode_writer('3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA', [2, 26, 33, 55, 34, 50, 33, 61, 44, 28, 46, 32, 28, 30, 3, 50, 34, 61, 40, 7, 1, 31])
    'Kyotaro Nishimura 1930'
    '''
    return ''.join(encoded_str[key - 1] for key in keys)

def parse_string(in_str):
    '''(string) -> (string, list of integers)

    Parses in_str to a tuple of two elements: encoded string
    and list of keys.

    >>> parse_string('osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg| 3 35 27 62 51 27 46 57 26 10 46 63 57 45 15 43 53')
    ('osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg', [3, 35, 27, 62, 51, 27, 46, 57, 26, 10, 46, 63, 57, 45, 15, 43, 53])
    
    >>> parse_string('3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA| 2 26 33 55 34 50 33 61 44 28 46 32 28 30 3 50 34 61 40 7 1 31')
    ('3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA', [2, 26, 33, 55, 34, 50, 33, 61, 44, 28, 46, 32, 28, 30, 3, 50, 34, 61, 40, 7, 1, 31])
    '''
    encoded_str, key_str = in_str.split('| ');
    return encoded_str, list(map(int, key_str.split(' ')))

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
            print(decode_writer(*parse_string(test)))

        test_cases.close()
