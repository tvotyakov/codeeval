#!python3
cache = [0, 1]
def fibonacci(n):
    '''(int) -> int

    Returns n-th the Fibonacci number which defined as: F(0) = 0;
    F(1) = 1; F(n) = F(n-1) + F(n-2) when n > 1
    
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(12)
    144
    '''
    current_index = len(cache) - 1
    if n <= current_index:
        return cache[n]

    current_num = cache[current_index]
    while(current_index < n):
        current_index += 1
        current_num = (cache[current_index - 1] +
                       cache[current_index - 2])
        cache.append(current_num)
    return current_num

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
            print(fibonacci(int(test)))

        test_cases.close()
