"""
two_sum_iv_input_is_bst.py
---

Leetcode: Easy
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/hints/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False

        queue = deque()
        queue.append(root)
        # Big assumption specific to problem: BST values are unique.
        numSet = set()

        while len(queue) > 0:
            curr = queue.popleft()
            target = k - curr.val
            if target in numSet:
                return True
            else:
                numSet.add(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
        return False



