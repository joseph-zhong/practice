#!/usr/bin/env python3
"""
337. House Robber III
https://leetcode.com/problems/house-robber-iii/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def rob(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    opt = dict()

    def recurse(node, robbed):
      if node is None:
        return 0
      if (node, robbed) in opt:
        return opt[node, robbed]
      else:
        val = recurse(node.left, True) + recurse(node.right, True)
        if robbed:
          val = max(val, node.val + recurse(node.left, False) + recurse(node.right, False))
        opt[node, robbed] = val
        return opt[node, robbed]

    return recurse(root, True)


