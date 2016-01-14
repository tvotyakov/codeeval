#!python3
import re

cleaning_pattern = re.compile(r'[\W\d_]+')

def get_cleaned_str(in_str):
    ''' (string) -> string

    Takes a string with mixed words and extra numbers and symbols. Returns
    a new string with cleaned up words (without extra numbers and symbols)
    separated by spaces in lowercase letters.

    >>> get_cleaned_str('test')
    'test'

    >>> get_cleaned_str('Test')
    'test'

    >>> get_cleaned_str('test012Test---test@@@test')
    'test test test test'

    >>> get_cleaned_str('(--9Hello----World...--)')
    'hello world'

    >>> get_cleaned_str('Can 0$9 ---you~')
    'can you'

    >>> get_cleaned_str('13What213are;11you-123+138doing7')
    'what are you doing'
    '''
    return ' '.join(s for s in cleaning_pattern.split(in_str) if s).lower()

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
            print(get_cleaned_str(test))

        test_cases.close()
