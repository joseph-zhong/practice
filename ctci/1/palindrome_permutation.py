#!/usr/bin/env python3
""" 1.4 Palindrome Permutation """

def isPermutationOfPalindrome(s1):
    """ Returns whether the string can be composed as a palindrome.

    Approach: A palindrome of even length must have character counts that are all even, and if a palindrome is of odd
    length, then only one character can be of odd count. We thus construct a character count by iterating through the
    string. """

    charCount = dict()
    for char in s1:
        if char not in charCount:
            charCount[char] = 0
        charCount[char] += 1

    count = 0
    for char in charCount:
        count += charCount[char] % 2
    return count <= 1

print(isPermutationOfPalindrome('aba') == True)
print(isPermutationOfPalindrome('aer') == False)
print(isPermutationOfPalindrome('aaabbbaaa') == True)
print(isPermutationOfPalindrome('aaabbbaa') == False)
print(isPermutationOfPalindrome('aaabbaa') == True)

