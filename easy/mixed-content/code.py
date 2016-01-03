#!python3
def split_content(in_str):
    '''(string) -> string

    Separates words with digits in the in_str string into two
    different list and combine them into one string separated
    by vertical bar ('|').

    >>> split_content('8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21')
    'melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17,21'
    >>> split_content('24,13,14,43,41')
    '24,13,14,43,41'
    '''
    words, numbers = [], []
    for elem in in_str.split(','):
        if elem.isdecimal():
            numbers.append(elem)
        else:
            words.append(elem)
            
    return '|'.join((','.join(words), ','.join(numbers))).strip('|')

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
            print(split_content(test))

        test_cases.close()
