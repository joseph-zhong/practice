#!/usr/bin/env python3
""" 4.10: Check Subtree """

from binary_tree import Node

def equals(r1, r2):
    if r1 is None and r2 is None:
        return True
    elif r1 is None or r2 is None:
        return False
    elif r1.val != r2.val:
        return False
    return equals(r1.left, r2.left) and equals(r1.right, r2.right)

def isSubtree(s1, s2):
    """ Checks whether tree `s1` contains `s2`.

    Approach: To implement subtree checking, we simply need to recursively check for sub-tree equality.
    """

    if s1 is None:
        return False
    else:
        if s1.val == s2.val and equals(s1, s2):
            return True
        return isSubtree(s1.left, s2) or isSubtree(s1.right, s2)

print(isSubtree(Node(vals=[1,2,3]), Node(vals=[1,2,3])) == True)
print(isSubtree(Node(vals=[1,2,3]), Node(vals=[1,4,3])) == False)

