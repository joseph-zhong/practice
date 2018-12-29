"""
hamming_dist.py
---

Leetcode: Easy problem
https://leetcode.com/problems/hamming-distance/description/

"""

def hammingDistance(self, x, y):
  """
  :type x: int
  :type y: int
  :rtype: int
  """
  return bin(x ^ y).count("1")

