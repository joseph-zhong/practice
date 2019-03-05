#!/usr/bin/env python3
""" 10.3: Search in Rotated Array """

def search(arr):
    """
    """

    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        mid = lo // 2 + hi // 2
        if arr[hi] < arr[mid]:
            lo = mid + 1
        else:
            hi = mid

    rot = lo
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = lo // 2 + hi // 2
        mid_rot = (mid + rot) % len(arr)

        if arr[mid_rot] == target:
            return mid_rot

        if a[mid_rot] < target:
            lo = mid+1
        else:
            hi = mid
    return -1



