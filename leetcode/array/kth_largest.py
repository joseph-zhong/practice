#!/usr/bin/env python3
import heapq
def kth_largest(nums, k):
  return heapq.nlargest(k, nums)[-1]

