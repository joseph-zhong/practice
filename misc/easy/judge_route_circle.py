"""
judge_route_circle.py
---

Leetcode: Easy
https://leetcode.com/problems/judge-route-circle/description/

"""

def judgeCircle(self, moves):
  """
  :type moves: str
  :rtype: bool
  """
  return moves.count("R") == moves.count("L") and moves.count("D") == moves.count("U")

