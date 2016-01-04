#!python3
from decimal import *

bills_coins = (('ONE HUNDRED', Decimal('100.00')),
               ('FIFTY', Decimal('50.00')),
               ('TWENTY', Decimal('20.00')),
               ('TEN', Decimal('10.00')),
               ('FIVE', Decimal('5.00')),
               ('TWO', Decimal('2.00')),
               ('ONE', Decimal('1.00')),
               ('HALF DOLLAR', Decimal('.50')),
               ('QUARTER', Decimal('.25')),
               ('DIME', Decimal('.10')),
               ('NICKEL', Decimal('.05')),
               ('PENNY', Decimal('.01')))
                
def calc_change(purchase_price, cach):
    '''(Decimal, Decimal) -> string

    Returns string which represents a change what has to be
    returned to the customer based on the purchase price and
    the cash given by customer.

    >>> calc_change(Decimal('15.92'), Decimal('16.00'))
    'NICKEL,PENNY,PENNY,PENNY'
    
    >>> calc_change(Decimal('15.94'), Decimal('16.00'))
    'NICKEL,PENNY'

    >>> calc_change(Decimal('17'), Decimal('16'))
    'ERROR'

    >>> calc_change(Decimal('35'), Decimal('35'))
    'ZERO'

    >>> calc_change(Decimal('45'), Decimal('50'))
    'FIVE'
    '''
    bills_coins_counts = [0] * len(bills_coins)
    rest_sum = cach - purchase_price

    # special cases
    if rest_sum < 0: return 'ERROR'
    if rest_sum == 0: return 'ZERO'
    
    for elem in enumerate(bills_coins):
        bill_coin_count = int(rest_sum // elem[1][1])
        bills_coins_counts[elem[0]] = bill_coin_count
        rest_sum -= elem[1][1] * bill_coin_count

    result = []
    for elem in enumerate(bills_coins_counts):
        if elem[1] > 0:
            result += [bills_coins[elem[0]][0]] * elem[1]
            
    return ','.join(result)

def parse_string(in_str):
    '''(string) -> (Decimal, Decimal)

    >>> parse_string('15.94;16.00')
    (Decimal('15.94'), Decimal('16.00'))

    >>> parse_string('17;16')
    (Decimal('17'), Decimal('16'))

    >>> parse_string('35;35')
    (Decimal('35'), Decimal('35'))

    >>> parse_string('45;50')
    (Decimal('45'), Decimal('50'))
    '''
    return tuple(map(Decimal, in_str.split(';')))

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
            print(calc_change(*parse_string(test)))

        test_cases.close()
