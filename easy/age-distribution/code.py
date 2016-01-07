#!python3
def get_age_category(age):
    ''' (int) -> string

    Returns category name based on the given age.

    >>> get_age_category(-1)
    'This program is for humans'

    >>> get_age_category(0)
    "Still in Mama's arms"

    >>> get_age_category(3)
    'Preschool Maniac'

    >>> get_age_category(5)
    'Elementary school'

    >>> get_age_category(11)
    'Elementary school'

    >>> get_age_category(12)
    'Middle school'

    >>> get_age_category(14)
    'Middle school'

    >>> get_age_category(15)
    'High school'

    >>> get_age_category(18)
    'High school'

    >>> get_age_category(19)
    'College'

    >>> get_age_category(22)
    'College'

    >>> get_age_category(23)
    'Working for the man'

    >>> get_age_category(65)
    'Working for the man'

    >>> get_age_category(66)
    'The Golden Years'

    >>> get_age_category(100)
    'The Golden Years'

    >>> get_age_category(101)
    'This program is for humans'
    '''
    message = "This program is for humans"

    if age < 0:
        pass
    elif age < 3:
        message = "Still in Mama's arms"
    elif age < 5:
        message = 'Preschool Maniac'
    elif age < 12:
        message = 'Elementary school'
    elif age < 15:
        message = 'Middle school'
    elif age < 19:
        message = 'High school'
    elif age < 23:
        message = 'College'
    elif age < 66:
        message = 'Working for the man'
    elif age <= 100:
        message = 'The Golden Years'

    return message

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
            print(get_age_category(int(test)))

        test_cases.close()
