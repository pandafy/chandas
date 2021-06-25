CARDINALS = {
    0: 'शून्य',
    1: "एक",
    2: "द्वि",
    3: "त्रि",
    4: "चतुर्",
    5: "पञ्चन्",
    6: "षड्",
    7: "सप्त",
    8: "अष्ट",
    9: "नव",
    10: "दश",
    11: "एकादश",
    12: "द्वादश",
    13: "त्रयोदश",
    14: "चतुर्दशन्",
    15: "पञ्चदशन्",
    16: "षोडशन्",
    17: "सप्तदशन्",
    18: "अष्टादशन्",
    19: "नवदशन्",
    20: "विंशति",
    21: "द्वाविंशति",
    22: "एकविंशति",
    23: "त्रयोविंशति",
    28: "एकत्रिंशत्",
    30: "एकत्रिंशत्",
    31: "एकत्रिंशत्",
    32: "द्वात्रिंशत्",
    33: "त्रयस्त्रिंशत्",
    38: "अष्टात्रिंशत्",
    40: "चत्वारिंशत्",
    50: "पञ्चाशत्",
    60: "षष्टि",
    70: "सप्तति",
    80: "अशीति",
    90: "नवति",
    100: "शत",
    1000: "सहस्र",
    10000: "अयुत",
    100000: "लक्ष",
    1000000: "प्रयुत",
    10000000: "कोटि",
    100000000: "अर्बुद",
    1000000000: "अब्ज",
    10000000000: "खर्व",
    100000000000: "निखर्व",
    1000000000000: "महापद्म",
}

ORDINALS = {
    1: "प्रथम",
    2: "द्वितीय",
    3: "तृतीय",
    4: "चतुर्थ",
    5: "पञ्चम",
    6: "षष्ठ",
    7: "सप्तम",
    8: "अष्टम",
    9: "नवम",
    10: "दशम",
}


def ordinal_number(n):
    """Return the ordinal number for a given number n in Sanskrit"""
    if n == 0:
        return ''
    elif n in ORDINALS:
        return ORDINALS[n]
    else:
        ord = get_cardinal_number(n)
        if n >= 59:
            ord += 'tama'
        return ord


def get_cardinal_number(n):
    """Return the cardinal number for a given number n in Sanskrit"""
    PLUS = 'uttara'

    if n == 0:
        return ''

    if n in CARDINALS:
        return CARDINALS[n]

    if (n % 10) == 9 and (n % 100) != 9:
        return compose(('एकोन', get_cardinal_number(n + 1)))

    if n < 1000:
        if n <= 100:
            t = n // 10
            return compose((get_cardinal_number(n % 10), CARDINALS[t * 10]))
        else:
            h = n // 100
            if h == 1:
                return compose((get_cardinal_number(n % 100), PLUS, 'zata'))
            else:
                return compose((get_cardinal_number(n % 100), PLUS, CARDINALS[h], 'zata'))
    else:
        # More work needed
        raise ValueError('Number too big!')


def compose(pieces):
    """Fix sandhis etc. and return the correct text"""
    while pieces[0] == '':
        pieces = pieces[1:]

    SANDHIS = {
        ('अ', 'अ'): 'आ',
        ('अ', 'उ'): 'ओ',
        ('ह', 'अ'): 'र्',
        ('ह', 'च'): 'श',
        ('ह', 'न्'): 'र्न',
        ('ह', 'स'): 'स्स',
        ('ह', 'ट्'): 'स्ट',
        ('ह', 'उ'): 'रु',
        ('ह', 'व'): 'र्व',
        ('इ', 'अ'): 'य',
        ('इ', 'उ'): 'यु',
        ('ट', 'अ'): 'दा',
        ('ट', 'न्'): 'न्न',
        ('ट', 'उ'): 'दु',
        ('ट', 'व'): 'द्व',
    }

    print(pieces)
    result = pieces[0]

    for i in range(1, len(pieces)):
        suff = result[-1]
        pref = pieces[i][0]
        if (suff, pref) in SANDHIS:
            result = result[:-1] + SANDHIS[(suff, pref)] + pieces[i][1:]
        else:
            result = result + pieces[i]

    return result


if __name__ == '__main__':
    for i in range(1, 1001):
        print(i, ':', get_cardinal_number(i))
