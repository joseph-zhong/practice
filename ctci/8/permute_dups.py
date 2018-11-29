#!/usr/bin/env python3
""" 8.8 Permutations with Dups


"""

def permute(nums):
    """ Given a list of integers, print the permutations, accounting for duplicates.

    Approach: This problem can be reduced to the same algorithm as the 8.7, Permutations without Dups. In the previous
    problem, we computed the permutations for each character in the string. Here, because we have duplicate characters, we
    can instead consider only the unique characters, place them each at the beginning, and apply the same algorithm for the
    rest of the string.
    """

    n = len(nums)
    res = []

    def recurse(arr, l):
        if l == n-1:
            res.append(arr)
        else:
            for num in set(arr[l:]):
                # Take the set of unique numbers, and isolate them from the rest. Permute on the rest, while fixing the
                # unique element.
                aux = arr[l:]
                aux.remove(num)
                recurse(arr[:l] + [num] + aux, l+1)
    recurse(nums, 0)
    return res

perm1 = permute([1,1,3])
print(perm1)
print(all(x in perm1 for x in [[1,1,3], [1,3,1], [3,1,1], [3,1,1]]))

