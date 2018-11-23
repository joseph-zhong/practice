#!/usr/bin/env python3
class LinkedList():
    def __init__(self, val=None, next=None, vals=[]):
        self.next = next
        self.val = val

        if len(vals) > 0:
            self.val = vals[0]
        curr = self
        for v in vals[1:]:
            curr.next = LinkedList(val=v)
            curr = curr.next

    def count(self):
        res = 0
        curr = self
        while curr is not None:
            res += 1
            curr = curr.next
        return res

    @staticmethod
    def print(root):
        curr = root
        print("[", end='')
        while curr is not None:
            if curr.next is None:
                print(curr.val, end='')
            else:
                print(curr.val, end=', ')
            curr = curr.next
        print("]")

    @staticmethod
    def getMiddle(root):
        slow = root
        fast = root.next
        if fast.next is None:
          return slow
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        return slow

    @staticmethod
    def merge(left, right):
        res = LinkedList()
        if left is None or left.val is None: return right
        if right is None or right.val is None: return left

        if left.val <= right.val:
            res = left
            res.next = LinkedList.merge(left.next, right)
        else:
            res = right
            res.next = LinkedList.merge(left, right.next)
        return res

    @staticmethod
    def sorted(root):
        """ Returns a new list of the sorted self. """
        if root is None or root.next is None:
            return root

        mid = LinkedList.getMiddle(root)
        midNext = mid.next
        mid.next = None

        left = LinkedList.sorted(root)
        right = LinkedList.sorted(midNext)
        head = LinkedList.merge(left, right)
        return head

if __name__ == '__main__':
    a = LinkedList(vals=[11, 12, 12, 11, 11])
    LinkedList.print(a)
    b = LinkedList.sorted(a)
    LinkedList.print(b)


