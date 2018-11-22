# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node.next == None:
            # do nothing
            return
        else:
            temp = node.next
            node.val = temp.val
            node.next = temp.next