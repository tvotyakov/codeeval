#!python3
def calc_distances(road_points):
    '''(list of tuples) -> list of integers

    >>> calc_distances([('Rkbs', 5453), ('Wdqiz', 1245), ('Rwds', 3890), ('Ujma', 5589), ('Tbzmo', 1303)])
    [1245, 58, 2587, 1563, 136]

    >>> calc_distances([('Vgdfz', 70), ('Mgknxpi', 3958), ('Nsptghk', 2626), ('Wuzp', 2559), ('Jcdwi', 3761)])
    [70, 2489, 67, 1135, 197]
    
    >>> calc_distances([('Yvnzjwk', 5363), ('Pkabj', 5999), ('Xznvb', 3584), ('Jfksvx', 1240), ('Inwm', 5720)])
    [1240, 2344, 1779, 357, 279]
    
    >>> calc_distances([('Ramytdb', 2683), ('Voclqmb', 5236)])
    [2683, 2553]
    '''
    road_points.sort(key = lambda p: p[1])
    distances = [road_points[0][1]]
    distances.extend(el[1][1] - el[0][1]
                     for el in zip(road_points[:-1], road_points[1:]))
    return distances
    
def parse_string(in_str):
    '''(string) -> list of tuples

    Parses given in_str string and returns list of tuples with name of
    city and distance to this city.

    >>> parse_string('Rkbs,5453; Wdqiz,1245; Rwds,3890; Ujma,5589; Tbzmo,1303;')
    [('Rkbs', 5453), ('Wdqiz', 1245), ('Rwds', 3890), ('Ujma', 5589), ('Tbzmo', 1303)]
    
    >>> parse_string('Vgdfz,70; Mgknxpi,3958; Nsptghk,2626; Wuzp,2559; Jcdwi,3761;')
    [('Vgdfz', 70), ('Mgknxpi', 3958), ('Nsptghk', 2626), ('Wuzp', 2559), ('Jcdwi', 3761)]
    
    >>> parse_string('Yvnzjwk,5363; Pkabj,5999; Xznvb,3584; Jfksvx,1240; Inwm,5720;')
    [('Yvnzjwk', 5363), ('Pkabj', 5999), ('Xznvb', 3584), ('Jfksvx', 1240), ('Inwm', 5720)]

    >>> parse_string('Ramytdb,2683; Voclqmb,5236;')
    [('Ramytdb', 2683), ('Voclqmb', 5236)]
    '''
    def parse_element(el):
        t = el.strip().split(',')
        return t[0], int(t[1])
    
    g = map(parse_element, in_str.strip(';').split(';'))
    return list(g)

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
            print(','.join(map(str, calc_distances(parse_string(test)))))

        test_cases.close()
