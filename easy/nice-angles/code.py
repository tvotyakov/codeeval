#!python3
def get_nice_angle(angle):
    ''' (float) -> string

    Returns string value represented the given float angle
    with fractional	part reduced to minutes and seconds. The
    whole and fractional parts are separated by period, minutes
    are separated by apostrophe, seconds by double quotes. The
    values of minutes and seconds are returned as two numbers
    (with leading zeros if needed).


    >>> get_nice_angle(0)
    '0.00\\'00"'

    >>> get_nice_angle(0.0001)
    '0.00\\'00"'

    >>> get_nice_angle(-10)
    '-10.00\\'00"'

    >>> get_nice_angle(10)
    '10.00\\'00"'

    >>> get_nice_angle(.25)
    '0.15\\'00"'

    >>> get_nice_angle(1.1)
    '1.06\\'00"'

    >>> get_nice_angle(1.01)
    '1.00\\'36"'

    >>> get_nice_angle(330.39991833)
    '330.23\\'59"'

    >>> get_nice_angle(0.001)
    '0.00\\'03"'

    >>> get_nice_angle(14.64530319)
    '14.38\\'43"'

    >>> get_nice_angle(254.16991217)
    '254.10\\'11"'
    '''
    whole = int(angle)
    fract = (angle - whole) * 60
    minutes = int(fract)
    fract = (fract - minutes) * 60
    seconds = int(fract)
    return '{0:d}.{1:02d}\'{2:02d}"'.format(whole, minutes, seconds)

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
            print(get_nice_angle(float(test)))

        test_cases.close()
