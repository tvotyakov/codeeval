#!python3
def words_to_digits(words):
    '''(list of string) -> string

    >>> words_to_digits(['zero','two', 'five', 'seven', 'eight', 'four'])
    '025784'
    >>> words_to_digits(['three', 'seven', 'eight', 'nine', 'two'])
    '37892'
    '''
    word_to_num_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                       'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    result = ''
    for word in words:
        result += str(word_to_num_map[word])
    return result
    
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
            print(words_to_digits(test.split(';')))

        test_cases.close()
