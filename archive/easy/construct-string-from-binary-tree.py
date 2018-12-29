"""

construct-string-from-binary-tree.py
---

Leetcode: Easy
https://leetcode.com/problems/construct-string-from-binary-tree/description/
"""

def tree2str(self, t):
  """
  :type t: TreeNode
  :rtype: str
  """
  if t is None:
    return ""
  elif t.left is None and t.right is None:
    return str(t.val)
  elif t.left is None and t.right is not None:
    return str(t.val) + "()" + "(" + self.tree2str(t.right) + ")"
  elif t.left is not None and t.right is None:
    return str(t.val) + "(" + self.tree2str(t.left) + ")"
  else:
    return str(t.val) + "(" + self.tree2str(t.left) + ")" + "(" + self.tree2str(t.right) + ")"

