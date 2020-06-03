#!/usr/bin/env python3
"""
Unique Paths
https://leetcode.com/problems/unique-paths/
"""

def unique_paths(m, n):
  """ Returns the number of unique paths from the top-left corner to bottom-right, with no obstacles in a
  m x n sized grid. (columns x rows)

  Approach: DFS search.
    Enumerate each of the unique paths by traversing from right or down.

  """
  opt = dict()
  def dfs(r, c):
    if r == n-1 and c == m-1:
      return 1
    if (r, c) in opt:
      return opt[r, c]
    else:
      res = 0
      for r_i, c_i in ((r+1, c), (r, c+1)):
        if 0 <= r_i < n and 0 <= c_i < m:
          res += dfs(r_i, c_i)
      opt[r, c] = res
      return opt[r, c]

  return dfs(0, 0)

# print(unique_paths(3, 2))

def unique_paths2(m, n):
  """
  Approach: Bottom-up Dynamic Proramming.
  opt[r][c] = opt[r-1][c] + opt[r][c-1]
    Current num_paths is equal to the sum of paths from the top, and from the left.
  """
  opt = [[0] * m for _ in range(n)]

  for r in range(n):
    for c in range(m):
      if r == 0 or c == 0:
        opt[r][c] = 1
      else:
        opt[r][c] = opt[r-1][c] + opt[r][c-1]
  return opt[-1][-1]

# print(unique_paths2(3, 2))

def unique_paths3(m, n):
  """
  Approach: Combinatorics
  """
  import math
  return math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1)

# print(unique_paths3(3, 2))

def unique_paths4(m, n):
  p = m + n - 2
  # Taking the min of m and n minimizes the number of loops in the p choose k calculation
  k = min(m, n) - 1
  # p Choose k
  tot = 1
  for i in range(k):
    tot *= (p - i)
  for i in range(k):
    tot /= (k - i)
  return tot
print(unique_paths4(3, 2))