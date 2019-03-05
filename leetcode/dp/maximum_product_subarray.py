#!/usr/bin/env python3
"""
Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/
"""

def maxProduct(nums):
  """
  Approach: Dynamic Programming.
    We keep two opt tables, 'mins' and 'maxs'. Because whenever we multiply the minimum (negative) product subseq, it becomes a candidate for the
    maximum product subseq. We store the running maximum product subseq into 'maxs'.

      mins[i] = mins( maxs[i-1] * nums[i], mins[i-1] * nums[i], nums[i] )
      maxs[i] = maxs( maxs[i-1] * nums[i], mins[i-1] * nums[i], nums[i] )
      res = max(maxs)
  """
  mins = [nums[0]]
  maxs = [nums[0]]

  for i in range(1, len(nums)):
    mins.append(min(maxs[i - 1] * nums[i], mins[i - 1] * nums[i], nums[i]))
    maxs.append(max(maxs[i - 1] * nums[i], mins[i - 1] * nums[i], nums[i]))
  return max(maxs)

def maxProduct2(nums):
  """ Returns the maximum product attainable via a product across a subarray from 'nums'.

  Approach: Dynamic Programming.
    We can remove our opt tables by keeping the running min and max subseqs. Following the previous strategy where multiplying the running subseq
    values by a negative value from 'nums' consequently switches the min and max subseq, we use that here.

    if nums[i] >= 0:
      maxSubseq = max(nums[i], maxSubseq * nums[i])
      minSubseq = min(nums[i], minSubseq * nums[i])
    else:
      maxSubseq = max(nums[i], minSubseq * nums[i])
      minSubseq = min(nums[i], maxSubseq * nums[i])
    res = max(res, maxSubseq)

  """

  maxSubseq = nums[0]
  minSubseq = nums[0]
  res = nums[0]
  for i in range(1, len(nums)):
    if nums[i] < 0:
      minSubseq, maxSubseq = maxSubseq, minSubseq
    maxSubseq = max(nums[i], maxSubseq*nums[i])
    minSubseq = min(nums[i], minSubseq*nums[i])
    res = max(res, maxSubseq)
  return res

print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 0, -1]))

print(maxProduct2([2, 3, -2, 4]))
print(maxProduct2([-2, 0, -1]))
