#!/usr/bin/env python3
"""
Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""

class ListNode(object):
  def __init__(self, x, next=None):
    self.val = x
    self.next = next

  def __str__(self):
    curr = self
    res = ['[']
    while curr is not None:
      if curr.next is None:
        res.append(str(curr.val))
      else:
        res.append(str(curr.val) + ', ')
      curr = curr.next
    res.append(']')
    return ''.join(res)

  def __eq__(self, other):
    return self.__str__() == other.__str__()

def addTwoNumbers(l1, l2):
  """
  :type l1: ListNode
  :type l2: ListNode
  :rtype: ListNode

  Approach: Greedy.
    We simply zip through each of l1 and l2. We also need to keep track of a 'carry' value as the two value summation exceeds 9.
  """

  l1_i = l1
  l2_i = l2
  res = ListNode(None)
  curr = res
  carry = 0
  while l1_i is not None or l2_i is not None or carry > 0:
    if l1_i is not None and l2_i is not None:
      val = l1_i.val + l2_i.val
    elif l1_i is not None:
      val = l1_i.val
    elif l2_i is not None:
      val = l2_i.val
    else:
      val = 0
    val += carry

    tmp = val // 10
    val = val - tmp * 10
    assert 0 <= val < 10
    curr.val = val
    carry = tmp

    if l1_i is not None:
      l1_i = l1_i.next
    if l2_i is not None:
      l2_i = l2_i.next
    if l1_i is not None or l2_i is not None or carry > 0:
      curr.next = ListNode(None)
    curr = curr.next
  return res

# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
# print(addTwoNumbers(l1, l2) == [7, 0, 8])

l1 = ListNode(9, ListNode(9))
l2 = ListNode(1)
print(addTwoNumbers(l1, l2) == [0, 0, 1])




