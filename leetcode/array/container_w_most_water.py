#!/usr/bin/env python3

def maxArea(height):
  res = 0
  l = 0
  r = len(height) - 1

  while l < r:
    res = max(res, (r-l)*min(height[l], height[r]))
    if height[l] < height[r]:
      l+=1
    else:
      r-=1
  return res


