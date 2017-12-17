"""
self_dividing_numbers.py
---

Leetcode: Easy
https://leetcode.com/problems/self-dividing-numbers/description/

"""
class Solution(object):
  def selfDividingNumbers(self, left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    return [num for num in range(left, right + 1) if isSelfDividing(num)]

def isSelfDividing(num):
  return "0" not in str(num) and all(num % int(c) == 0 for c in str(num))


