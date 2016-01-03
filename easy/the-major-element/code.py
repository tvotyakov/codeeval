#!python3
def get_major_element(nums):
    ''' (list of int) -> int or None

    Searches for and returns the major element of the given nums
    sequence of integers. If there is no the major element in nums,
    None will be return. The major element in a sequence with the
    length of L is the element which appears in a sequence more
    than L/2 times.

    >>> get_major_element([92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19])
    19

    >>> get_major_element([92,11,30,92,1,11,92,38,92,92,43,92,92,51,92,36,97,92,92,92,43,22,84,92,92])
    92

    >>> print(get_major_element([4,79,89,98,48,42,39,79,55,70,21,39,98,16,96,2,10,24,14,47,0,50,95,20,95,48,50,12,42]))
    None

    >>> print(get_major_element([2,2,1,1]))
    None
    '''
    nums_counts = {n: 0 for n in set(nums)}
    half_nums_len = len(nums) // 2
    for n in nums:
        c = nums_counts[n] = nums_counts[n] + 1
        if c > half_nums_len:
            return n    

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
            print(get_major_element(list(map(int, test.split(',')))))

        test_cases.close()
