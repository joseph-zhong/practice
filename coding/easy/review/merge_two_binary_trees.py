"""

merge_two_binary_trees.py
---

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None or t2 is None:
            if t1 is None and t2 is None:
                return None
            elif t1 is None:
                return t2
            else:
                return t1

        head = TreeNode(t1.val + t2.val)
        queue = deque()
        queue.append([t1, t2, head])
        while len(queue) > 0:
            t1_child, t2_child, curr = queue.popleft()

            if t1_child is not None and t1_child.left is not None \
                    or t2_child is not None and t2_child.left is not None:
                curr.left = TreeNode(0)
                if t1_child is not None and t1_child.left is not None:
                    curr.left.val += t1_child.left.val
                    left = t1_child.left
                else:
                    left = None
                if t2_child is not None and t2_child.left is not None:
                    curr.left.val += t2_child.left.val
                    left2 = t2_child.left
                else:
                    left2 = None
                queue.append([left, left2, curr.left])

            if t1_child is not None and t1_child.right is not None \
                    or (t2_child is not None and t2_child.right is not None):
                curr.right = TreeNode(0)
                if t1_child is not None and t1_child.right is not None:
                    curr.right.val += t1_child.right.val
                    right = t1_child.right
                else:
                    right = None
                if t2_child is not None and t2_child.right is not None:
                    curr.right.val += t2_child.right.val
                    right2 = t2_child.right
                else:
                    right2 = None
                queue.append([right, right2, curr.right])

        return head




