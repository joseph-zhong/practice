#!/usr/bin/env python3
""" Merge Intervals
https://leetcode.com/problems/merge-intervals/
"""
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
    """
    """
    sorted_intervals = sorted(intervals, key=lambda x: x.start)
    res = []

    for interval in sorted_intervals:
        if len(res) == 0 or res[-1].end < interval.start:
            res.append(interval)
        else:
            res[-1].end = max(res[-1].end, interval.end)
    return res


