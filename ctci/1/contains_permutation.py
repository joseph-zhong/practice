#!/usr/bin/env python3
"""
1.2: Check Permutation
"""

def containsPermutation(s1, s2):
    """ Returns whether `s2` contains a substring that is a permutation of `s1`.

    Approach: keep a character count for `s1`. We will use a similar character count for a sliding window across `s2`.
    We will know whether a permutation is met if the character counts for `s1` and the window match since permutations have
    equal number of each character.
    """
    if len(s1) > len(s2):
        return False

    A = [ord(x) - ord('a') for x in s1]
    B = [ord(x) - ord('a') for x in s2]

    # Char count for s1.
    s1Count = [0] * 26
    for x in A:
        s1Count[x] += 1

    windowCount = [0] * 26
    for i, b in enumerate(B):
        windowCount[b] += 1
        if i >= len(s1):
            # Sliding window: must decrement the character we are leaving.
            windowCount[B[i - len(s1)]] -= 1
        if windowCount == s1Count:
            return True
    return False

print(containsPermutation('ab', 'eidbaooo') == True)
print(containsPermutation('ab', 'eidboaoo') == False)
print(containsPermutation('adc', 'dcda') == True)

