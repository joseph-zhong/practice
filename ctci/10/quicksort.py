#!/usr/bin/env python3
import random

def quicksort(arr):
  def partition(l, r):
    i = l - 1
    pivot = r

    for j in range(l, r):
      if arr[j] <= arr[pivot]:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i+1

  def qsort(l, r):
    if l >= r: return

    pivot = partition(l, r)
    qsort(l, pivot-1)
    qsort(pivot+1, r)
  return qsort(0, len(arr)-1)

arr = [3, 2, 1, -1, 0 ]
# arr = [3, 2, 1]
quicksort(arr)
print(arr)


arr.sort()