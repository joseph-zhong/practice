#!/usr/bin/env python3

def isSubstring(s1, s2):
    """ Checks if `s1` is a substring of `s2`. """
    return s1 in s2

def isStringRot(s1, s2):
    """ Checks if `s2` is a rotation of `s1` using only one call to `isSubstring`.
    Example: 'erbottlewat' is a rotation of 'waterbottle'.

    Approach: Notice that a string rotation has some beginning of the word at the end, and vice versa, with the end of the
    word at the beginning. Thus if we actually concatenate `s1` with itself, we will reconstruct the original word, with the
    beginning at end, or the end at the beginning. Thus the original word will always be a substring of the concatenated
    rotated string. """
    return isSubstring(s1, s2+s2)

print(isStringRot('waterbottle', 'erbottlewat') == True)

