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

    high_bound = int(math.sqrt(num_to_test)) + 1
    for d in range(2, high_bound):
        if num_to_test % d == 0:
            return False
    return True

def next_prime_palindrome():
    for n in range(1, 10):
        if is_prime(n):
            yield n
        else:
            pal = n * 10 + n
            if is_prime(pal):
                yield pal

            for j in range(0, 10):
                pal = n * 100 + j * 10 + n
                if is_prime(pal):
                    yield pal

print(max(next_prime_palindrome()))
