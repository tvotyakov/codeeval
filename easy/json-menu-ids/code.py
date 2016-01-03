#!python3
import re

pattern = r'{"id": (\d*), "label":.*?}'
r = re.compile(pattern)
def sum_menu_ids(in_str):
    '''(string) -> int

    Calculates the sum of IDs of all "items" in the in_str
    in case a "label" exists for an item.

    >>> sum_menu_ids('{"menu": {"header": "menu", "items": [{"id": 27}, {"id": 0, "label": "Label 0"}, null, {"id": 93}, {"id": 85}, {"id": 54}, null, {"id": 46, "label": "Label 46"}]}}')
    46
    
    >>> sum_menu_ids('{"menu": {"header": "menu", "items": [{"id": 81}]}}')
    0
    
    >>> sum_menu_ids('{"menu": {"header": "menu", "items": [{"id": 70, "label": "Label 70"}, {"id": 85, "label": "Label 85"}, {"id": 93, "label": "Label 93"}, {"id": 2}]}}')
    248
    '''
    return sum(map(int, r.findall(in_str)))

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
            print(sum_menu_ids(test))

        test_cases.close()
