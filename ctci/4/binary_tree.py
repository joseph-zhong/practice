#!/usr/bin/env python3

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def print(root):
        if root is None:
            print("[]")

        curr = root
        stack = []
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        print("[", end='')
        while len(stack) > 0:
            s = stack.pop()
            print(s.val, end=',')

            curr = s.right
            while curr is not None:
                stack.append(curr)
                curr = curr.left
        print("]")

if __name__ == '__main__':
    Node.print(Node(val=2, left=Node(val=1), right=Node(val=3)))

