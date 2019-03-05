"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    queue = []
    if root is not None:
      queue.append(root)

    while len(queue) > 0:
      curr = []
      level_len = len(queue)
      for i in range(level_len):
        node = queue.pop(0)
        curr.append(node.val)
        if node.left is not None:
          queue.append(node.left)
        if node.right is not None:
          queue.append(node.right)
      res.append(curr)
    return res