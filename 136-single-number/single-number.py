class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(1) space
        # O(n) time
        numsMap = {} # creating a hash map 

        for num in nums:
            numsMap[num] = numsMap.get(num, 0) + 1
        
        for key, value in numsMap.items(): # looking at how many times a value appears
            if value == 1:
                return key