class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        countDict = {} # num : count
        for num in nums:
            if not countDict.get(num):
                countDict[num] = 1
            else:
                countDict.pop(num)
        return countDict.keys()[0]