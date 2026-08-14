class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        theSum = ((len(nums)) * ((len(nums)) + 1)) // 2
        actualSum = sum(nums)
        return theSum - actualSum