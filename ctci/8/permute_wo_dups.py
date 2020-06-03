#!/usr/bin/env python3
""" 8.7 Permutations Without Dups.

https://leetcode.com/problems/permutations/submissions/
"""

def permute(nums):
    """ Given an array of unique integers, compute the list of all permutations.

    Approach: We will be able to compute all permutations using recursive backtracking. A permutation of a string can easily
    be achieved by swapping any of the characters, and by swapping each of the characters with one another, we compute all
    permutations. This is an expensive O(n!) algorithm.
    """

    def recurse(arr, l, r, aux):
        if r - l == 0:
            aux.append([x for x in arr])
        else:
            for i in range(len(arr)):
                # Iterate through the characters, swapping it with a pivot to create a new permutation.
                arr[i], arr[l] = arr[l], arr[i]
                recurse(arr, l+1, r, aux)

                # Backtrack the modification.
                arr[l], arr[i] = arr[i], arr[l]
    res = []
    recurse(nums, 0, len(nums)-1, res)
    return res

perm1 = permute([1,2,3])
print(all(x in perm1 for x in [[1,2,3], [1,3,2], [2,1,3],[2,3,1], [3,1,2], [3,2,1]]))

