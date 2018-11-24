#!/usr/bin/env python3
""" 4.5 Validate BST

For more: https://leetcode.com/problems/validate-binary-search-tree/submissions/
"""

def isBst(root):
    """ Given a binary tree is a BST """
    if root is None: return True
    if root.left is None and root.right is None: return True

    def recurse(curr, lo, hi):
        if curr is None:
            return True

        if curr.left is None or lo < curr.left.val < curr.val:
            a = recurse(curr.left, lo, curr.val)
        else: return False
        if curr.right is None or hi > curr.right.val > curr.val:
            b = recurse(curr.right, curr.val, hi)
        else: return False
        return a and b
    return recurse(root, float('-inf'), float('inf'))

