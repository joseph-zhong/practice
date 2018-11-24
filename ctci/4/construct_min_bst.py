#!/usr/bin/env python3
""" 4.2 Minimal Tree """

from binary_tree import Node

def constructMinBst(vals):
    """ Given a sorted list of unique integers, this returns a binary search tree of minimum height. """

    if len(vals) == 0:
        return None

    mid = len(vals) // 2
    root = Node(val=vals[mid])
    root.left = constructMinBst(vals[:mid])
    root.right = constructMinBst(vals[mid+1:])
    return root

Node.print(constructMinBst([1,2]))
Node.print(constructMinBst([1,2,3]))
Node.print(constructMinBst([1,2,3,4]))
Node.print(constructMinBst([1,2,3,4,5]))
Node.print(constructMinBst([1,2,3,4,5,6]))

