#!python3
def is_happy(n):
    '''(int) -> boolean

    Returns True if n is a 'happy number', False in other case.
    A 'happy number' is defined by the following process.
    Starting with any positive integer n, replace the number by
    the sum of the squares of its digits, and repeat the process
    until the number equals 1 (where it will stay), or it loops
    endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy numbers,
    while those that do not end in 1 are unhappy numbers.
    
    >>> is_happy(1)
    True
    >>> is_happy(7)
    True
    >>> is_happy(22)
    False
    '''

    def digits(num):
        while num > 0:
            yield num % 10
            num //= 10
        
    prev_nums = []
    current_num = n
    while True:
        if current_num == 1: return True
        if current_num in prev_nums: return False
        prev_nums.append(current_num)
        current_num = sum(d ** 2 for d in digits(current_num))
    
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
            print(1 if is_happy(int(test)) else 0)

        test_cases.close()
