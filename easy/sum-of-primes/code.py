#!python3
import math

def is_prime(num_to_test):
    '''(int) -> boolean

    Returns True if num_to_test is a prime number
    False in other case
    
    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(23)
    True
    '''

    units_digit = num_to_test % 10
    if (num_to_test > 3 and units_digit == 2 or
        num_to_test > 10 and units_digit == 5):
        return False
        
    max_delimiter = int(math.sqrt(num_to_test))
    for d in range(2, max_delimiter + 1):
        if num_to_test % d == 0:
            return False
    return True
        
def sum_of_primes(n):
    '''(int) -> int

    Calculates sum of the first n prime numbers.

    >>> sum_of_primes(0)
    0
    >>> sum_of_primes(1)
    2
    >>> sum_of_primes(10)
    129
    >>> sum_of_primes(100)
    24133
    >>> sum_of_primes(1000)
    3682913
    '''
        
    result = 0
    primes_count = 0
    current_num = 2
    while (primes_count < n):
        if (is_prime(current_num)):
            primes_count += 1
            result += current_num
        current_num += 1
    return result

def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
    print(sum_of_primes(1000))
