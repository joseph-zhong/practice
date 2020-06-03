#!/usr/bin/env python3
""" 2.6 Palindrome """

from linkedlist import LinkedList

tail = None
def recursiveIsPalindrome(root):
    global tail
    if root is None or root.next is None: return True

    tail = root
    def recurse(head):
        global tail
        if head is None:
            return True
        if recurse(head.next):
            if head.val == tail.val:
                tail = tail.next
                return True
        return False
    return recurse(root)

def isPalindrome(root):
    """ Checks whether a linked list is a palindrome.

    Approach: We can find the middle of the list, reverse the list from that point and check the equality between the root
    and the reversed midpoint. """
    if root is None: return True
    if root.next is None: return True

    mid = getMid(root)
    revMid = reverse(mid)
    return isEqual(root, revMid)

def getMid(root):
    """ Sub-routine to get middle of linked list. """
    if root is None: return root
    slow = root
    fast = root
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(root):
    """ Reverses a linkedlist by prepending to a new head. """
    prev = None
    curr = root
    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev

def isEqual(s1, s2):
    """ Computes whether the two linked lists are equal by zipping each of them.
    If they are unequal in length or have any unequal values at the same position this will return false. """
    p1 = s1
    p2 = s2

    while p1 is not None and p2 is not None:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    # return p1 is None and p2 is None
    # REVIEW josephz: Special case for palindrome checker after reversal?
    return True


print("Iterative method")
print(1, isPalindrome(LinkedList(vals=[1, 1, 2, 2])) == False)
print(2, isPalindrome(LinkedList(vals=[1, 2, 1])) == True)
print(3, isPalindrome(LinkedList(vals=[1, 2, 2, 1])) == True)
print(4, isPalindrome(LinkedList(vals=[1])) == True)
print(5, isPalindrome(LinkedList(vals=[1, 1])) == True)
print(6, isPalindrome(LinkedList(vals=[1, 2])) == False)
print

print("Recursive method")
print(1, recursiveIsPalindrome(LinkedList(vals=[1, 1, 2, 2])) == False)
print(2, recursiveIsPalindrome(LinkedList(vals=[1, 2, 1])) == True)
print(3, recursiveIsPalindrome(LinkedList(vals=[1, 2, 2, 1])) == True)
print(4, recursiveIsPalindrome(LinkedList(vals=[1])) == True)
print(5, recursiveIsPalindrome(LinkedList(vals=[1, 1])) == True)
print(6, recursiveIsPalindrome(LinkedList(vals=[1, 2])) == False)


