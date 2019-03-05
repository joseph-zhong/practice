#!/usr/bin/env python3
""" Next Permutation.
https://leetcode.com/problems/next-permutation/
"""

def nextPermutation(nums):
  """ Modifies 'nums' in-place to represent the lexicographically next largest permutation of numbers.
  If 'nums' already represents the largest permutation possible, we will wrap, and modify 'nums' to be the smallest permutation.

  Approach: Greedy.
    1, 1, 1, 2, 3 => 1, 1, 1, 3, 2
    1, 1, 1, 3, 2 => 1, 1, 2, 1, 3
    1, 1, 1, 3, 2 => 1, 1, 2, 1, 3
    1, 1, 2, 1, 3 => 1, 1, 2, 3, 1
    5, 1, 5, 1, 5 => 5, 1, 5, 5, 1
    6, 4, 8, 7, 9 => 6, 4, 8, 9, 7
    6, 4, 8, 9, 9 => 6, 4, 9, 8, 9,
    6, 4, 1, 9, 9 => 6, 4, 9, 1, 9,
    3, 2, 1, 1, 1 => 1, 1, 1, 2, 3

    The key insight here is that if there exists a larger permutation, the left-most numbers aren't modified. Instead, the right-most number is
    inserted at the first position of a lesser value. The 'rightmost number' is the digit of least value, and consequently ...
    Note how this emulates the behavior of one iteration of bubble-sort.
  """
  if len(nums) <= 1:
    return nums

  l = len(nums)-2
  while 0 <= l and nums[l] >= nums[l+1]:
    l-=1

  def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

  def reverse(arr, i):
    j = len(arr) - 1
    while i < j:
      swap(arr, i, j)
      i+=1
      j-=1

  r = len(nums) - 1
  if 0 <= l:
    while 0 <= r and nums[r] <= nums[l]:
      r-=1
    swap(nums, l, r)
  reverse(nums, l+1)
  return nums

print(nextPermutation([1, 1, 1, 2, 3]))





