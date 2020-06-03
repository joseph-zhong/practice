#!/usr/bin/env python3
""" 4.8 First Common Ancestor """

def first_common_ancestor(root, s1, s2):
    if root is None:
        return None
   if root.val == s1 or root.val == s2:
       return root

   left = first_common_ancestor(root.left, s1, s2)
   right = first_common_ancestor(root.right, s1, s2)
   if left is not None and right is not None:
       return root
   if left is not None:
       return left
   return right

