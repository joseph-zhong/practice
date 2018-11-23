#!/usr/bin/env python3
""" 2.1 Remove Dups """

from linkedlist import LinkedList

def removeDups(root):
    """ Given the head of a linked list, remove the nodes of duplicate value. The list is not necessarily sorted.

    Approach: We can keep track of a set of values used, and greedily remove nodes if necessary. """
    if root is None: return root

    vals = set()
    prev = None
    curr = root
    while curr is not None:
        if curr.val in vals:
            prev.next = curr.next
        else:
            vals.add(curr.val)
            prev = curr
        curr = curr.next
    return root

# TODO: Two other approaches are to preserve original ordering and use a O(n^2) nested scan to remove duplicates,
# Otherwise, if we don't wish to preserve original ordering we can sort the array and remove neighboring duplicates.

def removeDups2(root):
    """ Removes nodes of duplicate value by sorting the list first. Doesn't preserve original ordering. """
    head = LinkedList.sorted(root)

    prev = None
    curr = head
    while curr is not None:
        if curr.next is not None and curr.val == curr.next.val:
                curr.next = curr.next.next
        prev = curr
        curr = curr.next
    return head

LinkedList.print(removeDups2(LinkedList(vals=[13, 13, 12, 12, 11, 11])))



