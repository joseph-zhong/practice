class Majority_Element:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        # sort the list
        nums.sort();
        
        # new hashmap to count numbers
        countDict = {}
        
        # now count the elements
        for num in nums:
            if countDict.has_key(num): # contains key 
                countDict[num] = countDict[num] + 1
            else:
                countDict.setdefault(num, 1)
            if countDict[num] > len(nums)/2:
                    return num 
                
m = Majority_Element()
m.majorityElement([3,3,4])