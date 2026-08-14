class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # theSum = ((len(nums)) * ((len(nums)) + 1)) // 2
        #actualSum = sum(nums)
        #return theSum - actualSum


        # hash set - 0(n) space and time
        numsSet = set(nums) # set takes 0(n)

        for num in range(len(nums)+1):
            if num not in numsSet:
                return num

