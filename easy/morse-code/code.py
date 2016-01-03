#!python3
morse_code_map = {
    '.-':  'A',   '-...': 'B',  '-.-.': 'C',
    '-..': 'D',   '.': 'E',     '..-.': 'F',
    '--.': 'G',   '....': 'H',  '..': 'I',
    '.---': 'J',  '-.-': 'K',   '.-..': 'L',
    '--': 'M',    '-.': 'N',    '---': 'O',
    '.--.': 'P',  '--.-': 'Q',  '.-.': 'R',
    '...': 'S',   '-': 'T',     '..-': 'U',
    '...-': 'V',  '.--': 'W',   '-..-': 'X',
    '-.--': 'Y',  '--..': 'Z',  '-----': '0',
    '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9'}
def decode_morse(code_str):
    '''(string) -> string

    Decodes string code_str encoded with Morse code and return
    decoded result.

    >>> decode_morse('.- ...- ..--- .-- .... .. . -.-. -..-  ....- .....')
    'AV2WHIECX 45'

    >>> decode_morse('-... .... ...--')
    'BH3'
    '''
    return ' '.join(map(
        lambda w: ''.join(map(
            lambda ch: morse_code_map[ch], w.split(' '))),
        code_str.split('  ')))

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
            print(decode_morse(test))

        test_cases.close()
