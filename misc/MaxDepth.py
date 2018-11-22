# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

'''
Recursive solution involves depth-first traversal and counting +1 each traversal
but only returning the max from left or right sub-traversals
'''
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            
            
t = TreeNode(3)
tl = TreeNode(2)
tll = TreeNode(1)

t.left = tl
tl.left = tll

s = Solution()
print s.maxDepth(t)