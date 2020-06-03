class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None

  def push(self, val):
    if self.head is None:
      self.head = Node(val=val)
      self.tail = self.head
    else:
      self.tail.next = Node(val=val)
      self.tail = self.tail.next

  def pop(self):
    res = None
    if self.head is not None:
      res = self.head
      self.head = self.head.next

    if self.head is None:
      self.tail = None

    if res is not None:
      return res.val
    return None

  def peek(self):
    return self.head.val
