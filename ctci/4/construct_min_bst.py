#!/usr/bin/env python3
""" 4.2 Minimal Tree """

from binary_tree import Node

def constructMinBst(vals):
    """ Given a sorted list of unique integers, this returns a binary search tree of minimum height. """

    def recurse(i, j):
        if j - i == 0:
            return None

        mid = j // 2 + i // 2
        root = Node(val=vals[mid])
        root.left = recurse(i, mid)
        root.right = recurse(mid+1, j)
        return root
    return recurse(0, len(vals))

Node.print(constructMinBst([1,2]))
Node.print(constructMinBst([1,2,3]))
Node.print(constructMinBst([1,2,3,4]))
Node.print(constructMinBst([1,2,3,4,5]))
Node.print(constructMinBst([1,2,3,4,5,6]))

