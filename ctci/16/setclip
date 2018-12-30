#!/usr/bin/env python3
# 16.8 English Int.
# https://leetcode.com/problems/integer-to-english-words/solution/
#

specials = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ]

tens = ['', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]

specials = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tens = {
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

def english_int(num):
    """ Converts a given integer (e.g. 16) to the equivalent English (sixteen).
    """
    if num == 0:
        return 'zero'

    negative = "negative " if num < 0 else ""

    num = abs(num)
    num_billion = num // 1e9
    num_million = (num - num_billion * 1e9) // 1e6
    num_thousand = (num - num_billion * 1e9 - num_million * 1e6) // 1e3

    def helper(num):
        if num < 20:
            return specials.get(num)
        elif num < 100:
            ten = num // 10 * 10
            one = num - ten

            if one != 0:
                return tens.get(ten) + ' ' + specials.get(one)
            else:
                return tens.get(ten)
        else:
            num_hundred = num // 100

            rest = helper(num - num_hundred * 100)
            if rest:
                return specials.get(num_hundred) + " hundred, " + str(rest)
            else:
                return specials.get(num_hundred) + " hundred"

    res = ""
    if num_billion > 0:
        res += helper(num_billion) + " billion"
    if num_million > 0:
        mil = helper(num_million) + " million"
        if res == '':
            res += mil
        else:
            res += ', ' + mil
    if num_thousand > 0:
        thous = helper(num_thousand) + " thousand"
        if res == '':
            res += thous
        else:
            res += ', ' + thous

    rest = helper(num - num_billion * 1e9 - num_million * 1e6 - num_thousand * 1e3)
    if rest is not None:
        if res == '':
            res += rest
        else:
            res += ', ' + rest
    return negative + res

print(english_int(123e9))
print(english_int(123456789))
print(english_int(-1234567890))

