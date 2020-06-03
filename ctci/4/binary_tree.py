#!/usr/bin/env python3

class Node:
    def __init__(self, val=None, left=None, right=None, vals=[]):
        if len(vals) > 0:
            root = Node.constructMinBst(vals)
            self.val = root.val
            self.left = root.left
            self.right = root.right
        else:
            self.val = val
            self.left = left
            self.right = right

    @staticmethod
    def constructMinBst(vals):
        def recurse(i, j):
            if j - i == 0:
                return None

            mid = j // 2 + i // 2
            root = Node(val=vals[mid])
            root.left = recurse(i, mid)
            root.right = recurse(mid+1, j)
            return root
        return recurse(0, len(vals))

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
            print(s.val, end='')

            curr = s.right
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            if len(stack) > 0:
                print(', ', end='')
            else:
                print('', end='')
        print("]")

if __name__ == '__main__':
    Node.print(Node(vals=[1,2,3]))
    Node.print(Node(vals=[1,2,3,4]))

