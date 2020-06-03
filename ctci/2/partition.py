#!/usr/bin/env python3
""" 2.4 Partition """

# def partition(root, x):
#     """ Partitions a linked list around value `x`, such that all nodes less than `x` come before nodes greater or equal to
#     `x`. Maintain the original relative order of the nodes less than and greater than `x`.
#
#     Approach: If we were instead given an ArrayList, we could simply concatenate each of the sublists between `x` that were
#     greater than `x` and append them at the end. However, with a LinkedList, we are only given access one pointer at a time.
#     Thus to implement this, we either want to append all the 'greater than `x`' values to the end, or prepend all the `'less
#     than `x`' values to the beginning.
#     """


def partition(self, head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """

    # New head for prepending.
    prev = ListNode(0)
    curr = ListNode(0)
    curr.next = head

    p_prev = prev
    p_curr = curr

    while p_curr is not None and p_curr.next is not None:
        if p_curr.next.val < x:
            p_prev.next = p_curr.next
            p_curr.next = p_curr.next.next
            p_prev.next.next = None
            p_prev = p_prev.next
        else:
            p_curr = p_curr.next
    p_prev.next = curr.next
    return prev.next

