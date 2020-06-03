#!/usr/bin/env python3
def canJumpBad(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    opt = [None for _ in range(len(nums))]
    opt[-1] = True

    for i in range(len(nums)-2, -1, -1):
        num = min(i + nums[i], len(nums)-1)
        for j in range(i+1, num+1):
            if opt[j]:
                opt[i] = True
                break
        if opt[i] is None:
            opt[i] = False
    return opt[0]

def canJump(nums):
    """

    Approach: Start from the far right. If the position plus it's greatest jump exceeds the far right, we can reach it.
    Greedily check this from right to left.
    """
    last_pos = len(nums)-1
    for curr_pos in range(len(nums)-1, -1, -1):
        if last_pos <= curr_pos + nums[last_pos]:
            last_pos = curr_pos
    return last_pos == 0

# print(canJump([0, 2, 3]))
print(canJump([2,3,1,1,4]))
