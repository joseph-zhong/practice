#!/usr/bin/env python3
"""
Word Search
https://leetcode.com/problems/word-search/
"""

from typing import List

def exist(board: List[List[str]], word: str):
  """
  :type board
  :type word: str
  :rtype: bool

  Approach: BFS or DFS.
    Iterate each letter which begins with word[0] -- O(n)
    Begin a DFS search, consuming one letter at a time -- O(k)
      We need to enable back-tracking with individual root-node paths
          Thus it will be simpler to use recursion rather than a stack.

  """
  height = len(board)
  length = len(board[0])

  # def dfs(r_s, c_s, idx):
  #   stack = [(r_s, c_s)]
  #   visited = []
  #
  #   while len(stack) > 0:
  #     # Expand.
  #     r, c = stack.pop()
  #     if (r, c) in visited: continue
  #     visited.append((r, c))
  #
  #     for r_i, c_i in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
  #       if (r_i, c_i) not in visited and (r_i, c_i) not in stack \
  #           and 0 <= r_i and 0 <= c_i and r_i < height and c_i < length \
  #           and board[r_i][c_i] == word[idx]:
  #         stack.append((r_i, c_i))
  #   return ''.join(visited)

  visited = set()
  def dfs2(r_s, c_s, idx):
    if board[r_s][c_s] != word[idx] or (r_s, c_s) in visited: return False
    if idx == len(word)-1: return True
    else:
      visited.add((r_s, c_s))
      for r_i, c_i in ((r_s - 1, c_s), (r_s + 1, c_s), (r_s, c_s - 1), (r_s, c_s + 1)):
        if 0 <= r_i < height and 0 <= c_i < length and dfs2(r_i, c_i, idx+1):
          return True
      visited.remove((r_s, c_s))

  for r in range(len(board)):
    for c in range(len(board[0])):
      if dfs2(r, c, 0):
        return True
  return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(exist(board, 'ABCCED'))
print(exist(board, 'SEE'))
print(exist(board, 'ABCB'))
print(exist(
  [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]], 'ABCEFSADEESE'))

