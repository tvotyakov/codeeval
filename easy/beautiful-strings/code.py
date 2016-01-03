#!python3
def max_beauty_of_string(in_str):
    '''(string) -> int

    Calculates maximum beauty of the in_str string.
    The beauty of the string is the sum of the beauty of the
    letters in it. The beauty of each letter is an integer
    between 1 and 26, inclusive, and no two letters have the
    same beauty.

    >>> max_beauty_of_string('ABbCcc')
    152

    >>> max_beauty_of_string('Good luck in the Facebook Hacker Cup this year!')
    754

    >>> max_beauty_of_string('Ignore punctuation, please :)')
    491

    >>> max_beauty_of_string('Sometimes test cases are hard to make up.')
    729

    >>> max_beauty_of_string('So I just go consult Professor Dalves')
    646
    '''
    normal_string = in_str.upper()
    letters = set(ch for ch in normal_string if ch.isalpha())
    letter_count_map = list((letter, normal_string.count(letter))
                            for letter in letters)
    letter_count_map.sort(key=lambda t: t[1], reverse = True)
    return sum(map(lambda t: t[0][1] * t[1],
                   zip(letter_count_map, range(26, 0, -1))))

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
            print(max_beauty_of_string(test))

        test_cases.close()
