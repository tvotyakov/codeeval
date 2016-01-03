#!python3
def split_input(s):
    ''' string -> (list of string, list of int)

    Splits input string s and return tuple of list of words and list of integers.
    List of word and list of integer should be separated by a semicolon.
    Each word and each integers should be separated by a single whitespace.

    >>> split_input('2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 2')
    (['2000', 'and', 'was', 'not', 'However,', 'implemented', '1998', 'it', 'until'], [9, 8, 3, 4, 1, 5, 7, 2])

    >>> split_input('programming first The language;3 2 1')
    (['programming', 'first', 'The', 'language'], [3, 2, 1])
    
    >>> split_input('programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9')
    (['programs', 'Manchester', 'The', 'written', 'ran', 'Mark', '1952', '1', 'in', 'Autocode', 'from'], [6, 2, 1, 7, 5, 3, 11, 4, 8, 9])

    >>> split_input('test;')
    (['test'], [])
    '''
    
    words, numbers = s.split(';')
    return (words.split(' '),
            list(map(int, numbers.split(' '))) if numbers else [])

def find_missed_num(nums):
    ''' (list of integers, int) -> int

    Looking for and returns first missed integer between 1 and len(nums) + 1
    (including) in the list of integer nums.

    >>> find_missed_num([9, 8, 3, 4, 1, 5, 7, 2])
    6

    >>> find_missed_num([3, 2, 1])
    4

    >>> find_missed_num([6, 2, 1, 7, 5, 3, 11, 4, 8, 9])
    10
    
    >>> find_missed_num([])
    1
    '''
    for n in range(1, len(nums) + 2):
        if n not in nums:
            return n

def recover_data(words, nums):
    '''(list of string, list of int) -> string

    >>> recover_data(*split_input('2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 2'))
    'However, it was not implemented until 1998 and 2000'

    >>> recover_data(*split_input('programming first The language;3 2 1'))
    'The first programming language'

    >>> recover_data(*split_input('programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9'))
    'The Manchester Mark 1 ran programs written in Autocode from 1952'

    >>> recover_data(*split_input('test;'))
    'test'
    '''
    nums.append(find_missed_num(nums))
    
    ordered_words = ['']*len(words)
    for i, w in enumerate(words):
        ordered_words[nums[i] - 1] = w
    
    return ' '.join(ordered_words)

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
            print(recover_data(*split_input(test)))

        test_cases.close()
