#!/usr/bin/env python3
""" 8.9 Parens """

def parens(n):
    """ Given `n` pairs of parentheses, this prints all valid combinations of parentheses possible to generate

    """

    res = []

    def recurse(s, l, r):
        if len(s) == 2 * n:
            res.append(s)
        else:
            if l < n:
                recurse(s + '(', l+1, r)
            if r < l:
                recurse(s + ')', l, r+1)

    recurse('', 0, 0)
    return res

parens1 = parens(2)
print(parens1)
print(all(x in ['()()', '(())'] for x in set(parens1)) and len(set(parens1)) == 2)

parens2 = parens(3)
print(parens2)
print(all(x in ['()()()', '()(())', '(())()', '(()())', '((()))'] for x in set(parens2)) and len(set(parens2)) == 5)

